import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/foundation.dart';
import '../models/user_model.dart';

class AuthService {
  static final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL:
        'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  // In-memory reference to the currently logged in user session
  static UserModel? currentUser;
  static final ValueNotifier<UserModel?> currentUserNotifier = ValueNotifier<UserModel?>(null);
  static StreamSubscription<DatabaseEvent>? _userSubscription;

  /// Helper to get the correct ImageProvider depending on whether it's a URL or Base64 string
  static ImageProvider? getAvatarProvider(String? avatarUrl) {
    if (avatarUrl == null || avatarUrl.isEmpty) {
      return null;
    }
    if (avatarUrl.startsWith('data:image') || avatarUrl.contains('base64,')) {
      try {
        final base64String = avatarUrl.contains(',') ? avatarUrl.split(',')[1] : avatarUrl;
        return MemoryImage(base64Decode(base64String.trim()));
      } catch (e) {
        debugPrint("Error parsing base64 avatar: $e");
      }
    }
    return NetworkImage(avatarUrl);
  }

  static void startUserListener(String email) {
    _userSubscription?.cancel();
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    // Set presence status
    _dbRef.child('Users/$sanitizedEmail/presence').set('online');
    _dbRef.child('Users/$sanitizedEmail/presence').onDisconnect().set('offline');

    _userSubscription = _dbRef.child(userPath).onValue.listen((event) {
      if (event.snapshot.exists && event.snapshot.value != null) {
        final data = event.snapshot.value as Map<dynamic, dynamic>;
        final user = UserModel.fromMap(sanitizedEmail, data);
        currentUser = user;
        currentUserNotifier.value = user;
        debugPrint('AuthService: Real-time user update received: ${user.xp} XP, ${user.coins} Coins');

        // Automatically check and reset streak if expired
        final lastActive = user.lastActiveDate;
        final currentStreak = user.streakCount;

        if (currentStreak > 0 && lastActive != null) {
          final now = DateTime.now();
          final todayStr = now.toIso8601String().split('T')[0];
          final yesterday = now.subtract(const Duration(days: 1));
          final yesterdayStr = yesterday.toIso8601String().split('T')[0];

          if (lastActive != todayStr && lastActive != yesterdayStr) {
            // Streak is broken! Reset to 0 in database and save it as previousStreak
            _dbRef.child(userPath).update({
              'streakCount': 0,
              'previousStreak': currentStreak,
            });
            debugPrint('AuthService: Streak expired. Reset to 0 in database. Previous streak saved: $currentStreak');
          }
        }
      }
    });
  }

  // Helper to sanitize emails for database keys
  static String sanitizeEmail(String email) {
    return email
        .trim()
        .toLowerCase()
        .replaceAll(r'.', '_')
        .replaceAll(r'@', '_')
        .replaceAll(r'#', '_')
        .replaceAll(r'$', '_')
        .replaceAll(r'[', '_')
        .replaceAll(r']', '_');
  }

  static String getLevel(int xp) {
    if (xp >= 2000) return 'Master';
    if (xp >= 1000) return 'Expert';
    if (xp >= 500) return 'Advanced';
    if (xp >= 200) return 'Intermediate';
    return 'Beginner';
  }

  static int getLevelIndex(String level) {
    final levels = ['Beginner', 'Intermediate', 'Advanced', 'Expert', 'Master'];
    return levels.indexOf(level);
  }

  static String? getBadgeName(int coins) {
    if (coins >= 5000) return 'Diamond';
    if (coins >= 2500) return 'Platinum';
    if (coins >= 1000) return 'Gold';
    if (coins >= 500) return 'Silver';
    if (coins >= 100) return 'Bronze';
    return null;
  }

  /// Register a new user in the database
  static Future<UserModel> registerUser({
    required String fullName,
    required String email,
    required String phoneNumber,
    required String password,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      final snapshot = await _dbRef.child(userPath).get();
      if (snapshot.exists) {
        throw Exception('This email is already registered.');
      }

      // Check if phone number is already taken
      try {
        final phoneSnapshot = await _dbRef
            .child('Users')
            .orderByChild('phoneNumber')
            .equalTo(phoneNumber.trim())
            .get();
        if (phoneSnapshot.exists && phoneSnapshot.value != null) {
          throw Exception('This number is already registered.');
        }
      } catch (e) {
        if (e.toString().contains('This number is already registered.')) {
          rethrow;
        }
        try {
          final DatabaseEvent event = await _dbRef.child('Users').once();
          final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
          if (data != null) {
            for (final val in data.values) {
              if (val is Map && val['phoneNumber']?.toString().trim() == phoneNumber.trim()) {
                throw Exception('This number is already registered.');
              }
            }
          }
        } catch (innerErr) {
          if (innerErr.toString().contains('This number is already registered.')) {
            rethrow;
          }
          throw Exception('This number is already registered.');
        }
      }

      // Generate a push key or use sanitized email as key
      final newUser = UserModel(
        id: sanitizedEmail,
        fullName: fullName.trim(),
        email: email.trim().toLowerCase(),
        phoneNumber: phoneNumber.trim(),
        password: password,
        coins: 0, // Users start with 0 coins — earned through quizzes!
        xp: 0, // Initial XP is 0
      );

      await _dbRef.child(userPath).set(newUser.toMap());

      // Seed a welcome system update notification
      final welcomeId = DateTime.now().millisecondsSinceEpoch.toString();
      await _dbRef.child('Users/$sanitizedEmail/notifications/$welcomeId').set({
        'id': welcomeId,
        'type': 'system',
        'title': 'Welcome to Aqoon Bile!',
        'message': 'Welcome to the platform! Challenge friends, take quizzes, and track your streaks in real time.',
        'timestamp': DateTime.now().millisecondsSinceEpoch,
        'isRead': false,
      });

      currentUser = newUser;
      currentUserNotifier.value = newUser;
      startUserListener(email);
      debugPrint('AuthService: User registered successfully: ${newUser.email}');
      return newUser;
    } catch (e) {
      debugPrint('AuthService: Registration error: $e');
      rethrow;
    }
  }

  /// Update the current user's XP in the database and local session
  static Future<void> updateUserXp(int additionalXp) async {
    if (currentUser == null) return;

    final oldXp = currentUser!.xp;
    final updatedXp = oldXp + additionalXp;
    final sanitizedEmail = sanitizeEmail(currentUser!.email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      await _dbRef.child(userPath).update({'xp': updatedXp});
      
      // Also increment daily XP in history log for charts
      final dateStr = DateTime.now().toIso8601String().split('T')[0]; // YYYY-MM-DD
      await _dbRef.child('Users/$sanitizedEmail/xp_history/$dateStr').set(ServerValue.increment(additionalXp));

      // Level Promotion Check
      final oldLevel = getLevel(oldXp);
      final newLevel = getLevel(updatedXp);
      if (getLevelIndex(newLevel) > getLevelIndex(oldLevel)) {
        final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
        await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'level_up',
          'title': 'Level Up Promotion',
          'message': 'Congratulations! You have been promoted to $newLevel!',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
        });
      }

      currentUser = currentUser!.copyWith(xp: updatedXp);
      currentUserNotifier.value = currentUser;
      debugPrint(
        'AuthService: Updated user XP in DB by +$additionalXp to $updatedXp and logged history',
      );
    } catch (e) {
      debugPrint('AuthService: Error updating XP in DB: $e');
    }
  }

  /// Update the current user's coins in the database and local session
  static Future<void> updateUserCoins(int additionalCoins) async {
    if (currentUser == null) return;

    final oldCoins = currentUser!.coins;
    final updatedCoins = oldCoins + additionalCoins;
    final sanitizedEmail = sanitizeEmail(currentUser!.email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      await _dbRef.child(userPath).update({'coins': updatedCoins});

      // Badge Earned Check
      final oldBadge = getBadgeName(oldCoins);
      final newBadge = getBadgeName(updatedCoins);
      if (newBadge != oldBadge && newBadge != null) {
        final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
        await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'badge_earned',
          'title': 'New Badge Earned',
          'message': 'Congratulations! You have unlocked the $newBadge Badge!',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
        });
      }

      currentUser = currentUser!.copyWith(coins: updatedCoins);
      currentUserNotifier.value = currentUser;
      debugPrint(
        'AuthService: Updated user coins in DB by +$additionalCoins to $updatedCoins',
      );
    } catch (e) {
      debugPrint('AuthService: Error updating coins in DB: $e');
    }
  }

  /// Authenticate a user by matching email and password
  static Future<UserModel> loginUser({
    required String email,
    required String password,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      final snapshot = await _dbRef.child(userPath).get();
      if (!snapshot.exists) {
        throw Exception('No account found with this email. Please sign up.');
      }

      final data = snapshot.value as Map<dynamic, dynamic>;
      final user = UserModel.fromMap(sanitizedEmail, data);

      if (user.password != password) {
        throw Exception('Incorrect password. Please try again.');
      }

      currentUser = user;
      currentUserNotifier.value = user;
      startUserListener(email);
      debugPrint('AuthService: User logged in successfully: ${user.email}');
      return user;
    } catch (e) {
      debugPrint('AuthService: Login error: $e');
      rethrow;
    }
  }

  /// Password recovery: retrieves and returns password for simulation
  static Future<String> recoverPassword(String email) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      final snapshot = await _dbRef.child(userPath).get();
      if (!snapshot.exists) {
        throw Exception('No registered account was found with this email.');
      }

      final data = snapshot.value as Map<dynamic, dynamic>;
      final password = data['password'] as String? ?? '';

      debugPrint(
        'AuthService: Recovered password successfully for email: $email',
      );
      return password;
    } catch (e) {
      debugPrint('AuthService: Password recovery error: $e');
      rethrow;
    }
  }

  /// Logout clean session
  static void logout() {
    if (currentUser != null) {
      final sanitizedEmail = sanitizeEmail(currentUser!.email);
      _dbRef.child('Users/$sanitizedEmail/presence').set('offline');
    }
    _userSubscription?.cancel();
    _userSubscription = null;
    currentUser = null;
    currentUserNotifier.value = null;
    debugPrint('AuthService: User logged out.');
  }

  // ─── Friend Request System ─────────────────────────────────

  /// Send a friend request from the current user to [targetEmail]
  static Future<void> sendFriendRequest(String targetEmail) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final targetKey = sanitizeEmail(targetEmail);

    await _dbRef.child('Users/$myKey/sentRequests/$targetKey').set(true);
    await _dbRef.child('Users/$targetKey/friendRequests/$myKey').set(true);

    // Add real-time notification to the target user
    final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
    await _dbRef.child('Users/$targetKey/notifications/$notificationId').set({
      'id': notificationId,
      'type': 'friend_request',
      'title': 'New Friend Request',
      'message': '${currentUser!.fullName} sent you a friend request.',
      'timestamp': DateTime.now().millisecondsSinceEpoch,
      'isRead': false,
      'senderEmail': currentUser!.email,
      'senderName': currentUser!.fullName,
    });

    debugPrint('AuthService: Sent friend request to $targetEmail');
  }

  /// Cancel a pending friend request the current user sent to [targetEmail]
  static Future<void> cancelFriendRequest(String targetEmail) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final targetKey = sanitizeEmail(targetEmail);

    await _dbRef.child('Users/$myKey/sentRequests/$targetKey').remove();
    await _dbRef.child('Users/$targetKey/friendRequests/$myKey').remove();
    debugPrint('AuthService: Cancelled friend request to $targetEmail');
  }

  /// Accept a friend request from [senderEmail]
  static Future<void> acceptFriendRequest(String senderEmail) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final senderKey = sanitizeEmail(senderEmail);

    // Add each other as friends with creation timestamp
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    await _dbRef.child('Users/$myKey/friends/$senderKey').set(timestamp);
    await _dbRef.child('Users/$senderKey/friends/$myKey').set(timestamp);

    // Clean up the request entries
    await _dbRef.child('Users/$myKey/friendRequests/$senderKey').remove();
    await _dbRef.child('Users/$senderKey/sentRequests/$myKey').remove();

    // Add real-time notification to the sender (who initiated the request)
    final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
    await _dbRef.child('Users/$senderKey/notifications/$notificationId').set({
      'id': notificationId,
      'type': 'friend_accepted',
      'title': 'Friend Request Accepted',
      'message': '${currentUser!.fullName} accepted your friend request.',
      'timestamp': timestamp,
      'isRead': false,
      'senderEmail': currentUser!.email,
      'senderName': currentUser!.fullName,
    });

    debugPrint(
      'AuthService: Accepted friend request from $senderEmail at timestamp $timestamp',
    );
  }

  /// Decline a friend request from [senderEmail]
  static Future<void> declineFriendRequest(String senderEmail) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final senderKey = sanitizeEmail(senderEmail);

    await _dbRef.child('Users/$myKey/friendRequests/$senderKey').remove();
    await _dbRef.child('Users/$senderKey/sentRequests/$myKey').remove();

    // Add real-time notification to the sender (who initiated the request)
    final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
    await _dbRef.child('Users/$senderKey/notifications/$notificationId').set({
      'id': notificationId,
      'type': 'friend_rejected',
      'title': 'Friend Request Rejected',
      'message': '${currentUser!.fullName} rejected your friend request.',
      'timestamp': DateTime.now().millisecondsSinceEpoch,
      'isRead': false,
      'senderEmail': currentUser!.email,
      'senderName': currentUser!.fullName,
    });

    debugPrint('AuthService: Declined friend request from $senderEmail');
  }

  /// Unfriend a user
  static Future<void> unfriend(String friendEmail) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final friendKey = sanitizeEmail(friendEmail);

    await _dbRef.child('Users/$myKey/friends/$friendKey').remove();
    await _dbRef.child('Users/$friendKey/friends/$myKey').remove();
    debugPrint('AuthService: Unfriended $friendEmail');
  }

  /// Get a set of sanitized email keys from a sub-node (friendRequests, sentRequests, friends)
  static Future<Set<String>> _getKeySet(String subNode) async {
    if (currentUser == null) return {};
    final myKey = sanitizeEmail(currentUser!.email);
    final snapshot = await _dbRef.child('Users/$myKey/$subNode').get();
    if (!snapshot.exists || snapshot.value == null) return {};
    final data = snapshot.value as Map<dynamic, dynamic>;
    return data.keys.cast<String>().toSet();
  }

  static Future<Set<String>> getFriendRequestKeys() =>
      _getKeySet('friendRequests');
  static Future<Set<String>> getSentRequestKeys() => _getKeySet('sentRequests');
  static Future<Set<String>> getFriendKeys() => _getKeySet('friends');

  /// Fetch user data for a given sanitized email key
  static Future<Map<String, dynamic>?> getUserDataByKey(
    String sanitizedKey,
  ) async {
    final snapshot = await _dbRef.child('Users/$sanitizedKey').get();
    if (!snapshot.exists || snapshot.value == null) return null;
    final data = snapshot.value as Map<dynamic, dynamic>;
    return Map<String, dynamic>.from(data);
  }

  /// Set admin status for a user
  static Future<void> setUserAdmin({
    required String email,
    required bool isAdmin,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';
    try {
      await _dbRef.child(userPath).update({'isAdmin': isAdmin});
      // If current user is the same, update local copy
      if (currentUser != null && currentUser!.email == email) {
        currentUser = currentUser!.copyWith(isAdmin: isAdmin);
        currentUserNotifier.value = currentUser;
      }
      debugPrint('AuthService: Updated admin status for $email to $isAdmin');
    } catch (e) {
      debugPrint('AuthService: Error updating admin status: $e');
      rethrow;
    }
  }

  /// Retrieve all users from the database
  static Future<List<UserModel>> getAllUsers() async {
    try {
      final DatabaseEvent event = await _dbRef.child('Users').once();
      final Map<dynamic, dynamic>? data =
          event.snapshot.value as Map<dynamic, dynamic>?;
      if (data == null) return [];
      return data.entries
          .map(
            (e) => UserModel.fromMap(
              e.key as String,
              Map<String, dynamic>.from(e.value as Map),
            ),
          )
          .toList();
    } catch (e) {
      debugPrint('AuthService: Error fetching all users: $e');
      rethrow;
    }
  }

  /// Set XP for a user
  static Future<void> setUserXp({
    required String email,
    required int xp,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';
    
    int oldXp = 0;
    final snapshot = await _dbRef.child('$userPath/xp').get();
    if (snapshot.exists && snapshot.value != null) {
      oldXp = (snapshot.value as num).toInt();
    }

    await _dbRef.child(userPath).update({'xp': xp});

    // Update daily XP history by the difference so that the chart updates in real-time
    if (xp == 0) {
      await _dbRef.child('Users/$sanitizedEmail/xp_history').remove();
    } else {
      final diff = xp - oldXp;
      if (diff != 0) {
        final dateStr = DateTime.now().toIso8601String().split('T')[0];
        await _dbRef.child('Users/$sanitizedEmail/xp_history/$dateStr').set(ServerValue.increment(diff));
      }
    }

    final oldLevel = getLevel(oldXp);
    final newLevel = getLevel(xp);
    if (getLevelIndex(newLevel) > getLevelIndex(oldLevel)) {
      final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
      await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
        'id': notificationId,
        'type': 'level_up',
        'title': 'Level Up Promotion',
        'message': 'Congratulations! You have been promoted to $newLevel!',
        'timestamp': DateTime.now().millisecondsSinceEpoch,
        'isRead': false,
      });
    }

    if (currentUser != null && currentUser!.email == email) {
      currentUser = currentUser!.copyWith(xp: xp);
      currentUserNotifier.value = currentUser;
    }
    debugPrint('AuthService: Updated XP for $email to $xp and checked promotions');
  }

  /// Set coins for a user
  static Future<void> setUserCoins({
    required String email,
    required int coins,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';
    
    int oldCoins = 0;
    final snapshot = await _dbRef.child('$userPath/coins').get();
    if (snapshot.exists && snapshot.value != null) {
      oldCoins = (snapshot.value as num).toInt();
    }

    await _dbRef.child(userPath).update({'coins': coins});

    final oldBadge = getBadgeName(oldCoins);
    final newBadge = getBadgeName(coins);
    if (newBadge != oldBadge && newBadge != null) {
      final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
      await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
        'id': notificationId,
        'type': 'badge_earned',
        'title': 'New Badge Earned',
        'message': 'Congratulations! You have unlocked the $newBadge Badge!',
        'timestamp': DateTime.now().millisecondsSinceEpoch,
        'isRead': false,
      });
    }

    if (currentUser != null && currentUser!.email == email) {
      currentUser = currentUser!.copyWith(coins: coins);
      currentUserNotifier.value = currentUser;
    }
    debugPrint('AuthService: Updated coins for $email to $coins and checked badges');
  }

  /// Get progress of a specific challenge
  static Future<Map<dynamic, dynamic>?> getChallengeProgress(String challengeId) async {
    if (currentUser == null) return null;
    final myKey = sanitizeEmail(currentUser!.email);
    final snapshot = await _dbRef.child('Users/$myKey/challenges/$challengeId').get();
    if (!snapshot.exists || snapshot.value == null) return null;
    return snapshot.value as Map<dynamic, dynamic>;
  }

  /// Update/save challenge progress
  static Future<void> saveChallengeProgress({
    required String challengeId,
    required String status,
    required int currentIndex,
    required int score,
    required List<dynamic> questions,
  }) async {
    if (currentUser == null) return;
    final myKey = sanitizeEmail(currentUser!.email);
    final challengePath = 'Users/$myKey/challenges/$challengeId';

    await _dbRef.child(challengePath).set({
      'status': status,
      'currentIndex': currentIndex,
      'score': score,
      'questions': questions,
    });
  }

  /// Get all challenges progress for current user
  static Future<Map<dynamic, dynamic>> getAllChallengesProgress() async {
    if (currentUser == null) return {};
    final myKey = sanitizeEmail(currentUser!.email);
    final snapshot = await _dbRef.child('Users/$myKey/challenges').get();
    if (!snapshot.exists || snapshot.value == null) return {};
    return snapshot.value as Map<dynamic, dynamic>;
  }

  /// Get challenges progress and reset if period changed (every 7 weeks / 49 days)
  static Future<Map<dynamic, dynamic>> getChallengesProgressWithReset() async {
    if (currentUser == null) return {};
    final myKey = sanitizeEmail(currentUser!.email);
    final now = DateTime.now();
    final int currentPeriod = now.millisecondsSinceEpoch ~/ 4233600000; // 7 weeks (49 days) in ms

    try {
      final clearedSnapshot = await _dbRef.child('Users/$myKey/challenges_last_cleared_period').get();
      int lastClearedPeriod = -1;
      if (clearedSnapshot.exists && clearedSnapshot.value != null) {
        lastClearedPeriod = clearedSnapshot.value as int;
      }

      if (lastClearedPeriod != currentPeriod) {
        // Clear challenge progress node
        await _dbRef.child('Users/$myKey/challenges').remove();
        // Update cleared period index in DB
        await _dbRef.child('Users/$myKey/challenges_last_cleared_period').set(currentPeriod);
        debugPrint('AuthService: Cleared all challenges progress for 7-week cycle reset. Period: $currentPeriod');
        return {};
      }

      final progressSnapshot = await _dbRef.child('Users/$myKey/challenges').get();
      if (!progressSnapshot.exists || progressSnapshot.value == null) return {};
      return progressSnapshot.value as Map<dynamic, dynamic>;
    } catch (e) {
      debugPrint('AuthService: Error getting challenges progress with reset: $e');
      return getAllChallengesProgress();
    }
  }

  /// Update the current user's streak in the database and local session
  static Future<void> updateUserStreak() async {
    if (currentUser == null) return;

    final sanitizedEmail = sanitizeEmail(currentUser!.email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      final now = DateTime.now();
      final todayStr = now.toIso8601String().split('T')[0]; // YYYY-MM-DD
      
      final lastActive = currentUser!.lastActiveDate;
      final currentStreak = currentUser!.streakCount;

      if (lastActive == todayStr) {
        // Already active today, nothing to change
        debugPrint('AuthService: Streak already updated today ($todayStr)');
        return;
      }

      int newStreak = 1;
      int newPrevStreak = currentUser!.previousStreak;

      if (lastActive != null) {
        final yesterday = now.subtract(const Duration(days: 1));
        final yesterdayStr = yesterday.toIso8601String().split('T')[0];

        if (lastActive == yesterdayStr) {
          // Consecutiveness maintained!
          newStreak = currentStreak + 1;
          debugPrint('AuthService: Streak incremented consecutive day! New streak: $newStreak');
        } else {
          // Streak broken
          newStreak = 1;
          newPrevStreak = currentStreak; // Save previous streak before resetting
          debugPrint('AuthService: Streak broken! Saved previous streak: $newPrevStreak');
        }
      } else {
        debugPrint('AuthService: First day of activity. Streak set to 1');
      }

      await _dbRef.child(userPath).update({
        'lastActiveDate': todayStr,
        'streakCount': newStreak,
        'previousStreak': newPrevStreak,
      });

      // Send real-time notifications for streak changes
      if (newStreak == 3) {
        final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
        await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'streak_start',
          'title': 'New Streak Started',
          'message': 'Keep it up! You have started a 3-day activity streak!',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
        });
      } else if (newPrevStreak >= 3 && newStreak == 1) {
        final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
        await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'streak_lost',
          'title': 'Streak Lost',
          'message': 'Oh no! You lost your $newPrevStreak-day activity streak. You can restore it using a Restore point!',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
        });
      }

      currentUser = currentUser!.copyWith(
        lastActiveDate: todayStr,
        streakCount: newStreak,
        previousStreak: newPrevStreak,
      );
      currentUserNotifier.value = currentUser;
    } catch (e) {
      debugPrint('AuthService: Error updating user streak: $e');
    }
  }

  /// Restore a lost streak using a monthly restore point
  static Future<void> restoreUserStreak() async {
    if (currentUser == null) return;

    final sanitizedEmail = sanitizeEmail(currentUser!.email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      final now = DateTime.now();
      final todayStr = now.toIso8601String().split('T')[0]; // YYYY-MM-DD
      final currentMonthStr = "${now.year}-${now.month.toString().padLeft(2, '0')}";

      final int prevRestores = currentUser!.availableRestores;
      if (prevRestores <= 0) {
        debugPrint('AuthService: No restores left this month!');
        return;
      }

      final int targetStreak = currentUser!.previousStreak;
      if (targetStreak < 3) {
        debugPrint('AuthService: Previous streak was not active, cannot restore!');
        return;
      }

      final int remainingRestores = prevRestores - 1;

      await _dbRef.child(userPath).update({
        'streakCount': targetStreak,
        'previousStreak': 0,
        'streakRestoresLeft': remainingRestores,
        'lastRestoreMonth': currentMonthStr,
        'lastActiveDate': todayStr,
      });

      // Send real-time notification for streak restoration
      final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
      await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
        'id': notificationId,
        'type': 'streak_start',
        'title': 'Streak Restored!',
        'message': 'Awesome! Your streak of $targetStreak days has been successfully restored.',
        'timestamp': DateTime.now().millisecondsSinceEpoch,
        'isRead': false,
      });

      currentUser = currentUser!.copyWith(
        streakCount: targetStreak,
        previousStreak: 0,
        streakRestoresLeft: remainingRestores,
        lastRestoreMonth: currentMonthStr,
        lastActiveDate: todayStr,
      );
      currentUserNotifier.value = currentUser;
      debugPrint('AuthService: Streak restored successfully to $targetStreak. Restores left: $remainingRestores');
    } catch (e) {
      debugPrint('AuthService: Error restoring streak: $e');
    }
  }

  /// Set streak count for a user (admin override)
  static Future<void> setUserStreakAdmin({
    required String email,
    required int streakCount,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    try {
      await _dbRef.child(userPath).update({'streakCount': streakCount});
      if (currentUser != null && currentUser!.email == email) {
        currentUser = currentUser!.copyWith(streakCount: streakCount);
        currentUserNotifier.value = currentUser;
      }
      debugPrint('AuthService: Updated streak count for $email to $streakCount (Admin)');
    } catch (e) {
      debugPrint('AuthService: Error updating streak count for admin: $e');
    }
  }

  /// Update the current user's profile information
  static Future<void> updateUserProfile({
    required String fullName,
    String? newPhoneNumber,
    String? newEmail,
    String? newPassword,
  }) async {
    if (currentUser == null) return;
    final oldEmail = currentUser!.email;
    final oldSanitized = sanitizeEmail(oldEmail);
    final newEmailVal = newEmail != null && newEmail.trim().isNotEmpty ? newEmail.trim() : oldEmail;
    final newSanitized = sanitizeEmail(newEmailVal);
    final newPhoneVal = newPhoneNumber != null && newPhoneNumber.trim().isNotEmpty ? newPhoneNumber.trim() : currentUser!.phoneNumber;

    // Check if new phone number is already taken by any user in the database
    if (newPhoneNumber != null && newPhoneNumber.trim().isNotEmpty) {
      try {
        final phoneSnapshot = await _dbRef
            .child('Users')
            .orderByChild('phoneNumber')
            .equalTo(newPhoneVal)
            .get();
        if (phoneSnapshot.exists && phoneSnapshot.value != null) {
          throw Exception('This number is already registered.');
        }
      } catch (e) {
        if (e.toString().contains('This number is already registered.')) {
          rethrow;
        }
        try {
          final DatabaseEvent event = await _dbRef.child('Users').once();
          final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
          if (data != null) {
            for (final val in data.values) {
              if (val is Map && val['phoneNumber']?.toString().trim() == newPhoneVal.trim()) {
                throw Exception('This number is already registered.');
              }
            }
          }
        } catch (innerErr) {
          if (innerErr.toString().contains('This number is already registered.')) {
            rethrow;
          }
          throw Exception('This number is already registered.');
        }
      }
    }

    // Check if new email is already taken by any user in the database
    if (newEmail != null && newEmail.trim().isNotEmpty) {
      final checkSnapshot = await _dbRef.child('Users/$newSanitized').get();
      if (checkSnapshot.exists) {
        throw Exception('This email is already registered.');
      }
    }

    final Map<String, dynamic> updates = {
      'fullName': fullName.trim(),
      'phoneNumber': newPhoneVal,
    };

    if (newPassword != null && newPassword.isNotEmpty) {
      updates['password'] = newPassword;
    }

    if (newEmailVal.trim().toLowerCase() != oldEmail.trim().toLowerCase()) {
      updates['email'] = newEmailVal.trim();
    }

    if (newSanitized != oldSanitized) {
      // Check if new email is already taken by another user
      final checkSnapshot = await _dbRef.child('Users/$newSanitized').get();
      if (checkSnapshot.exists) {
        throw Exception('This email is already registered.');
      }

      // Get old user data
      final snapshot = await _dbRef.child('Users/$oldSanitized').get();
      if (snapshot.exists && snapshot.value != null) {
        final Map<dynamic, dynamic> oldData = snapshot.value as Map<dynamic, dynamic>;
        final Map<String, dynamic> newData = Map<String, dynamic>.from(oldData);
        newData.addAll(updates);

        // 1. Write to new sanitized path
        await _dbRef.child('Users/$newSanitized').set(newData);

        // 2. Remove old path
        await _dbRef.child('Users/$oldSanitized').remove();

        // 3. Update all friend references in the database
        final friendsKeys = (oldData['friends'] as Map<dynamic, dynamic>?)?.keys.cast<String>() ?? [];
        for (final friendKey in friendsKeys) {
          final friendNode = _dbRef.child('Users/$friendKey');
          final friendValSnapshot = await friendNode.child('friends/$oldSanitized').get();
          if (friendValSnapshot.exists) {
            await friendNode.child('friends/$newSanitized').set(friendValSnapshot.value);
            await friendNode.child('friends/$oldSanitized').remove();
          }
        }

        // Clean up requests as well if any
        final requestKeys = (oldData['friendRequests'] as Map<dynamic, dynamic>?)?.keys.cast<String>() ?? [];
        for (final rKey in requestKeys) {
          final rNode = _dbRef.child('Users/$rKey');
          final rValSnapshot = await rNode.child('sentRequests/$oldSanitized').get();
          if (rValSnapshot.exists) {
            await rNode.child('sentRequests/$newSanitized').set(rValSnapshot.value);
            await rNode.child('sentRequests/$oldSanitized').remove();
          }
        }

        final sentKeys = (oldData['sentRequests'] as Map<dynamic, dynamic>?)?.keys.cast<String>() ?? [];
        for (final sKey in sentKeys) {
          final sNode = _dbRef.child('Users/$sKey');
          final sValSnapshot = await sNode.child('friendRequests/$oldSanitized').get();
          if (sValSnapshot.exists) {
            await sNode.child('friendRequests/$newSanitized').set(sValSnapshot.value);
            await sNode.child('friendRequests/$oldSanitized').remove();
          }
        }
      } else {
        await _dbRef.child('Users/$newSanitized').update(updates);
      }
    } else {
      await _dbRef.child('Users/$oldSanitized').update(updates);
    }

    // Update local session
    currentUser = currentUser!.copyWith(
      fullName: fullName.trim(),
      phoneNumber: newPhoneVal,
      email: newEmailVal,
      password: newPassword != null && newPassword.isNotEmpty ? newPassword : currentUser!.password,
    );
    currentUserNotifier.value = currentUser;
  }

  /// Generate and store a recovery code for password reset
  static Future<void> sendRecoveryCode(String email, String code) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    final snapshot = await _dbRef.child(userPath).get();
    if (!snapshot.exists) {
      throw Exception('No registered account was found with this email.');
    }

    // Store recovery code and timestamp
    await _dbRef.child(userPath).update({
      'recoveryCode': code,
      'recoveryCodeTimestamp': DateTime.now().millisecondsSinceEpoch,
    });
  }

  /// Reset the password using a verification code
  static Future<void> resetPasswordWithCode({
    required String email,
    required String code,
    required String newPassword,
  }) async {
    final sanitizedEmail = sanitizeEmail(email);
    final userPath = 'Users/$sanitizedEmail';

    final snapshot = await _dbRef.child(userPath).get();
    if (!snapshot.exists) {
      throw Exception('No registered account was found with this email.');
    }

    final data = snapshot.value as Map<dynamic, dynamic>;
    final storedCode = data['recoveryCode'] as String? ?? '';
    final storedTimestamp = data['recoveryCodeTimestamp'] as int? ?? 0;

    if (storedCode.isEmpty || storedCode != code) {
      throw Exception('Invalid verification code.');
    }

    // Code is valid for 10 minutes (600,000 milliseconds)
    final int now = DateTime.now().millisecondsSinceEpoch;
    if (now - storedTimestamp > 600000) {
      throw Exception('Verification code has expired. Please request a new one.');
    }

    // Code matches and is valid, update password and clear recovery code
    await _dbRef.child(userPath).update({
      'password': newPassword,
      'recoveryCode': null,
      'recoveryCodeTimestamp': null,
    });

    // Send a system notification for password reset success
    final notificationId = DateTime.now().millisecondsSinceEpoch.toString();
    await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
      'id': notificationId,
      'type': 'system',
      'title': 'Password Reset Success',
      'message': 'Your account password has been successfully reset using verification code.',
      'timestamp': DateTime.now().millisecondsSinceEpoch,
      'isRead': false,
    });

    // Update local session if logged in as this user
    if (currentUser != null && currentUser!.email.toLowerCase() == email.toLowerCase()) {
      currentUser = currentUser!.copyWith(password: newPassword);
      currentUserNotifier.value = currentUser;
    }
  }
}
