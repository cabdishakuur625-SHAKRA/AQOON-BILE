import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:confetti/confetti.dart';
import 'QuizSubjectsScreen.dart';
import 'ChallengesScreen.dart';
import 'CompetitionsListScreen.dart';
import 'CreateMockExamScreen.dart';
import 'FindFriendsScreen.dart';
import 'ProfilePreviewScreen.dart';
import 'PapersListScreen.dart';
import 'NotificationsScreen.dart';
import 'CompetitionLobbyScreen.dart';
import '../../admin/admin_home.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import '../user_model.dart';
import 'dart:async';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;
  late ConfettiController _confettiController;
  String? _currentLevel;

  List<Map<String, dynamic>> _notifications = [];
  StreamSubscription<List<Map<String, dynamic>>>? _notificationsSubscription;
  final Set<String> _seenInviteIds = {};
  final Set<String> _processedMsgIds = {};

  @override
  void initState() {
    super.initState();
    _confettiController = ConfettiController(duration: const Duration(seconds: 4));

    final user = AuthService.currentUser;
    if (user != null) {
      _currentLevel = _getLevel(user.xp);
      _listenForNotifications();
    }
    AuthService.currentUserNotifier.addListener(_onUserChanged);
  }

  @override
  void dispose() {
    _notificationsSubscription?.cancel();
    AuthService.currentUserNotifier.removeListener(_onUserChanged);
    _confettiController.dispose();
    super.dispose();
  }

  void _listenForNotifications() {
    _notificationsSubscription?.cancel();
    final FirebaseService firebaseService = FirebaseService();
    final currentUser = AuthService.currentUser;
    if (currentUser == null) return;
    final sanitizedEmail = AuthService.sanitizeEmail(currentUser.email);

    _notificationsSubscription = firebaseService.streamNotifications(sanitizedEmail).listen((list) {
      if (!mounted) return;
      setState(() {
        _notifications = list;
      });

      for (var notif in list) {
        final String type = notif['type'] ?? '';
        final String notifId = notif['id'] ?? '';
        final String compId = notif['competitionId'] ?? '';
        final bool isRead = notif['isRead'] ?? false;

        if (!isRead && notifId.isNotEmpty) {
          if (type == 'new_message') {
            final roomId = notif['roomId'] as String?;
            final msgId = notif['msgId'] as String?;
            if (roomId != null && msgId != null && !_processedMsgIds.contains(msgId)) {
              _processedMsgIds.add(msgId);
              final db = FirebaseDatabase.instanceFor(
                app: Firebase.app(),
                databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
              );
              db.ref('Chats/$roomId/messages/$msgId/delivered').set(true);
            }
          } else if (type == 'competition_invite' && compId.isNotEmpty) {
            if (!_seenInviteIds.contains(compId)) {
              _seenInviteIds.add(compId);
              _fetchAndShowInviteDialog(compId);
            }
          } else if (type == 'competition_started' && compId.isNotEmpty) {
            if (!_seenInviteIds.contains(notifId)) {
              _seenInviteIds.add(notifId);
              firebaseService.markNotificationRead(notifId);
              if (mounted) {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => CompetitionLobbyScreen(
                      competitionId: compId,
                    ),
                  ),
                );
              }
            }
          } else if (type == 'level_up') {
            if (!_seenInviteIds.contains(notifId)) {
              _seenInviteIds.add(notifId);
              firebaseService.markNotificationRead(notifId);
              final message = notif['message'] ?? '';
              final newLevel = message.split('to ').last.replaceAll('!', '').trim();
              _showLevelUpDialog(newLevel);
            }
          } else if (type == 'badge_earned') {
            if (!_seenInviteIds.contains(notifId)) {
              _seenInviteIds.add(notifId);
              firebaseService.markNotificationRead(notifId);
              final message = notif['message'] ?? '';
              final badgeName = message.split('the ').last.replaceAll(' Badge!', '').trim();
              _showBadgePromotionDialog(badgeName);
            }
          }
        }
      }
    });
  }

  Future<void> _fetchAndShowInviteDialog(String compId) async {
    try {
      final FirebaseService firebaseService = FirebaseService();
      final compData = await firebaseService.streamCompetition(compId).first;
      if (compData == null || !mounted) return;

      final String status = compData['status'] ?? '';
      final bool quizStarted = compData['quizStarted'] ?? false;
      final int createdAt = compData['createdAt'] ?? 0;

      bool isExpired = status == 'expired';
      if (!isExpired && !quizStarted && createdAt > 0) {
        final int now = DateTime.now().millisecondsSinceEpoch;
        if (now - createdAt > 120000) {
          // Check if any friend accepted
          final scores = compData['scores'] as Map<dynamic, dynamic>? ?? {};
          final String creatorEmail = compData['creatorEmail'] ?? '';
          bool hasAnyFriendAccepted = false;
          scores.forEach((sKey, sVal) {
            final pMap = sVal as Map<dynamic, dynamic>;
            final String email = pMap['email'] ?? '';
            final String pStatus = pMap['status'] ?? 'waiting';
            if (email.toLowerCase() != creatorEmail.toLowerCase() &&
                (pStatus == 'ready' || pStatus == 'completed')) {
              hasAnyFriendAccepted = true;
            }
          });
          if (!hasAnyFriendAccepted) {
            isExpired = true;
            firebaseService.markCompetitionExpired(compId);
          }
        }
      }

      final currentUser = AuthService.currentUser;
      if (currentUser == null) return;
      final sanitizedEmail = AuthService.sanitizeEmail(currentUser.email);
      final scores = compData['scores'] as Map<dynamic, dynamic>? ?? {};
      final myScoreData = scores[sanitizedEmail] as Map<dynamic, dynamic>?;
      final String myStatus = myScoreData?['status'] ?? 'waiting';

      if (status == 'active' && !quizStarted && myStatus == 'waiting' && !isExpired) {
        _showInviteDialog(compData);
      }
    } catch (e) {
      debugPrint("Error fetching invite details: $e");
    }
  }

  void _showInviteDialog(Map<String, dynamic> comp) {
    final String compId = comp['id'] ?? '';
    final String title = comp['title'] ?? 'Competition';
    final String creatorName = comp['creatorName'] ?? 'A friend';
    final String subjectName = comp['subjectName'] ?? 'General';
    final int questionCount = comp['questionCount'] ?? 10;
    final int duration = comp['duration'] ?? 15;

    showDialog(
      context: context,
      barrierDismissible: false,
      barrierColor: Colors.black.withOpacity(0.7),
      builder: (BuildContext context) {
        return ClipRRect(
          borderRadius: BorderRadius.circular(30),
          child: BackdropFilter(
            filter: ImageFilter.blur(sigmaX: 15, sigmaY: 15),
            child: AlertDialog(
              backgroundColor: const Color(0xFF1E1B4B).withOpacity(0.8),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30),
                side: BorderSide(color: Colors.cyanAccent.withOpacity(0.2), width: 1.5),
              ),
              title: Row(
                children: [
                  Icon(Icons.emoji_events_rounded, color: Colors.cyanAccent, size: 28)
                      .animate(onPlay: (c) => c.repeat())
                      .shake(hz: 4, curve: Curves.easeInOut),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      "Competition Invite!",
                      style: GoogleFonts.outfit(
                        color: Colors.white,
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  RichText(
                    text: TextSpan(
                      style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16, height: 1.4),
                      children: [
                        TextSpan(
                          text: creatorName,
                          style: const TextStyle(color: Colors.cyanAccent, fontWeight: FontWeight.bold),
                        ),
                        const TextSpan(text: " has invited you to join a quiz competition: "),
                        TextSpan(
                          text: title,
                          style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 20),
                  Container(
                    padding: const EdgeInsets.all(15),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.05),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: Colors.white.withOpacity(0.1)),
                    ),
                    child: Column(
                      children: [
                        Row(
                          children: [
                            const Icon(Icons.menu_book_rounded, color: Colors.purpleAccent, size: 18),
                            const SizedBox(width: 8),
                            Text(
                              "Subject: $subjectName",
                              style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Row(
                          children: [
                            const Icon(Icons.help_outline_rounded, color: Colors.orangeAccent, size: 18),
                            const SizedBox(width: 8),
                            Text(
                              "Questions: $questionCount Qs",
                              style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Row(
                          children: [
                            const Icon(Icons.timer_outlined, color: Colors.greenAccent, size: 18),
                            const SizedBox(width: 8),
                            Text(
                              "Duration: $duration minutes",
                              style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              actionsPadding: const EdgeInsets.only(bottom: 20, left: 20, right: 20),
              actions: [
                Row(
                  children: [
                    Expanded(
                      child: TextButton(
                        onPressed: () async {
                          Navigator.pop(context);
                          final FirebaseService firebaseService = FirebaseService();
                          await firebaseService.declineCompetition(compId);
                        },
                        style: TextButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 14),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15),
                            side: BorderSide(color: Colors.white.withOpacity(0.15)),
                          ),
                        ),
                        child: Text(
                          "Cancel",
                          style: GoogleFonts.outfit(color: Colors.white70, fontWeight: FontWeight.bold),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: ElevatedButton(
                        onPressed: () async {
                          Navigator.pop(context);
                          final FirebaseService firebaseService = FirebaseService();
                          await firebaseService.setParticipantReady(compId, ready: false);
                          if (mounted) {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => CompetitionLobbyScreen(
                                  competitionId: compId,
                                ),
                              ),
                            );
                          }
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.cyanAccent,
                          foregroundColor: Colors.black,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15),
                          ),
                          elevation: 0,
                        ),
                        child: Text(
                          "Join",
                          style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  void _onUserChanged() {
    if (!mounted) return;
    setState(() {}); // Rebuild home screen components dynamically

    final user = AuthService.currentUserNotifier.value;
    if (user != null) {
      if (_notificationsSubscription == null) {
        _listenForNotifications();
      }
      _currentLevel = _getLevel(user.xp);
    } else {
      _notificationsSubscription?.cancel();
      _notificationsSubscription = null;
      _notifications = [];
    }
  }

  bool _isPromotion(String oldLvl, String newLvl) {
    final levels = ['Beginner', 'Intermediate', 'Advanced', 'Expert', 'Master'];
    return levels.indexOf(newLvl) > levels.indexOf(oldLvl);
  }

  String _getLevel(int xp) {
    if (xp >= 2000) return 'Master';
    if (xp >= 1000) return 'Expert';
    if (xp >= 500) return 'Advanced';
    if (xp >= 200) return 'Intermediate';
    return 'Beginner';
  }

  void _showLevelUpDialog(String newLevel) {
    IconData levelIcon = Icons.star_rounded;
    Color levelColor = Colors.cyanAccent;

    switch (newLevel) {
      case 'Intermediate':
        levelIcon = Icons.emoji_events_rounded;
        levelColor = Colors.cyanAccent;
        break;
      case 'Advanced':
        levelIcon = Icons.shield_rounded;
        levelColor = Colors.purpleAccent;
        break;
      case 'Expert':
        levelIcon = Icons.military_tech_rounded;
        levelColor = Colors.amberAccent;
        break;
      case 'Master':
        levelIcon = Icons.workspace_premium_rounded;
        levelColor = Colors.redAccent;
        break;
      default:
        levelIcon = Icons.star_rounded;
        levelColor = Colors.greenAccent;
    }

    final String firstName = AuthService.currentUser?.fullName.split(' ')[0].toUpperCase() ?? "LEARNER";

    _confettiController.play();
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) {
        return BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
          child: Dialog(
            backgroundColor: Colors.transparent,
            insetPadding: const EdgeInsets.symmetric(horizontal: 20),
            child: Stack(
              clipBehavior: Clip.none,
              alignment: Alignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 30),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [
                        const Color(0xFF1E1B4B).withOpacity(0.95),
                        const Color(0xFF312E81).withOpacity(0.95),
                      ],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(30),
                    border: Border.all(color: levelColor.withOpacity(0.3), width: 2),
                    boxShadow: [
                      BoxShadow(
                        color: levelColor.withOpacity(0.15),
                        blurRadius: 30,
                        spreadRadius: 5,
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Align(
                        alignment: Alignment.topRight,
                        child: IconButton(
                          onPressed: () => Navigator.pop(context),
                          icon: const Icon(Icons.close_rounded, color: Colors.white60),
                          style: IconButton.styleFrom(
                            backgroundColor: Colors.white.withOpacity(0.05),
                            padding: const EdgeInsets.all(8),
                          ),
                        ),
                      ),
                      const SizedBox(height: 10),
                      // Glowing Avatar & Badge Stack
                      Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
                          Container(
                            padding: const EdgeInsets.all(4),
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              border: Border.all(color: levelColor, width: 3),
                              boxShadow: [
                                BoxShadow(
                                  color: levelColor.withOpacity(0.4),
                                  blurRadius: 20,
                                  spreadRadius: 4,
                                ),
                              ],
                            ),
                            child: CircleAvatar(
                              radius: 50,
                              backgroundImage: AuthService.getAvatarProvider(AuthService.currentUser?.avatarUrl),
                              child: (AuthService.currentUser?.avatarUrl == null || AuthService.currentUser!.avatarUrl!.isEmpty)
                                  ? Text(
                                      AuthService.currentUser?.fullName.split(' ').map((e) => e[0]).join() ?? '',
                                      style: GoogleFonts.outfit(color: levelColor, fontSize: 24, fontWeight: FontWeight.bold),
                                    )
                                  : null,
                            ),
                          ),
                          Positioned(
                            bottom: -5,
                            right: -5,
                            child: Container(
                              padding: const EdgeInsets.all(8),
                              decoration: BoxDecoration(
                                color: const Color(0xFF1E1B4B),
                                shape: BoxShape.circle,
                                border: Border.all(color: levelColor, width: 2),
                                boxShadow: [
                                  BoxShadow(
                                    color: Colors.black.withOpacity(0.3),
                                    blurRadius: 5,
                                    offset: const Offset(0, 3),
                                  ),
                                ],
                              ),
                              child: Icon(levelIcon, size: 24, color: levelColor),
                            ),
                          ),
                        ],
                      ).animate()
                       .scale(duration: 800.ms, curve: Curves.elasticOut)
                       .then()
                       .shake(hz: 2, duration: 600.ms),
                      const SizedBox(height: 25),
                      Text(
                        "CONGRATULATIONS, $firstName!",
                        textAlign: TextAlign.center,
                        style: GoogleFonts.outfit(
                          color: levelColor,
                          fontSize: 24,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 1.2,
                        ),
                      ).animate().fadeIn().slideY(begin: -0.3),
                      const SizedBox(height: 8),
                      Text(
                        "You've been promoted!",
                        style: GoogleFonts.outfit(
                          color: Colors.white70,
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      const SizedBox(height: 15),
                      // Level badge pill
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.05),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(color: Colors.white10),
                        ),
                        child: Text(
                          newLevel.toUpperCase(),
                          style: GoogleFonts.outfit(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 1,
                          ),
                        ),
                      ).animate().scale(delay: 300.ms, duration: 500.ms, curve: Curves.easeOutBack),
                      const SizedBox(height: 35),
                      ElevatedButton(
                        onPressed: () => Navigator.pop(context),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: levelColor,
                          foregroundColor: Colors.black,
                          elevation: 8,
                          shadowColor: levelColor.withOpacity(0.3),
                          padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 16),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                        ),
                        child: Text(
                          "Awesome!",
                          style: GoogleFonts.outfit(
                            fontWeight: FontWeight.bold,
                            fontSize: 18,
                          ),
                        ),
                      ).animate().fadeIn(delay: 700.ms).scale(),
                    ],
                  ),
                ),
                // Confetti overlay on top!
                Positioned(
                  top: -50,
                  child: ConfettiWidget(
                    confettiController: _confettiController,
                    blastDirectionality: BlastDirectionality.explosive,
                    shouldLoop: false,
                    numberOfParticles: 40,
                    emissionFrequency: 0.05,
                    colors: const [
                      Colors.cyanAccent,
                      Colors.purpleAccent,
                      Colors.amberAccent,
                      Colors.redAccent,
                      Colors.greenAccent,
                      Colors.orangeAccent,
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  void _showBadgePromotionDialog(String badgeName) {
    IconData badgeIcon = Icons.military_tech_rounded;
    Color badgeColor = const Color(0xFFCD7F32);

    switch (badgeName) {
      case 'Bronze':
        badgeIcon = Icons.military_tech_rounded;
        badgeColor = const Color(0xFFCD7F32);
        break;
      case 'Silver':
        badgeIcon = Icons.shield_rounded;
        badgeColor = const Color(0xFFC0C0C0);
        break;
      case 'Gold':
        badgeIcon = Icons.emoji_events_rounded;
        badgeColor = const Color(0xFFFFD700);
        break;
      case 'Platinum':
        badgeIcon = Icons.workspace_premium_rounded;
        badgeColor = const Color(0xFF00F2FE);
        break;
      case 'Diamond':
        badgeIcon = Icons.diamond_rounded;
        badgeColor = const Color(0xFFB9F2FF);
        break;
    }

    final String firstName = AuthService.currentUser?.fullName.split(' ')[0].toUpperCase() ?? "LEARNER";

    _confettiController.play();
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) {
        return BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
          child: Dialog(
            backgroundColor: Colors.transparent,
            insetPadding: const EdgeInsets.symmetric(horizontal: 20),
            child: Stack(
              clipBehavior: Clip.none,
              alignment: Alignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 30),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [
                        const Color(0xFF1E1B4B).withOpacity(0.95),
                        const Color(0xFF312E81).withOpacity(0.95),
                      ],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(30),
                    border: Border.all(color: badgeColor.withOpacity(0.3), width: 2),
                    boxShadow: [
                      BoxShadow(
                        color: badgeColor.withOpacity(0.15),
                        blurRadius: 30,
                        spreadRadius: 5,
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Align(
                        alignment: Alignment.topRight,
                        child: IconButton(
                          onPressed: () => Navigator.pop(context),
                          icon: const Icon(Icons.close_rounded, color: Colors.white60),
                          style: IconButton.styleFrom(
                            backgroundColor: Colors.white.withOpacity(0.05),
                            padding: const EdgeInsets.all(8),
                          ),
                        ),
                      ),
                      const SizedBox(height: 10),
                      // Glowing Avatar & Badge Stack
                      Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
                          Container(
                            padding: const EdgeInsets.all(4),
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              border: Border.all(color: badgeColor, width: 3),
                              boxShadow: [
                                BoxShadow(
                                  color: badgeColor.withOpacity(0.4),
                                  blurRadius: 20,
                                  spreadRadius: 4,
                                ),
                              ],
                            ),
                            child: CircleAvatar(
                              radius: 50,
                              backgroundImage: AuthService.getAvatarProvider(AuthService.currentUser?.avatarUrl),
                              child: (AuthService.currentUser?.avatarUrl == null || AuthService.currentUser!.avatarUrl!.isEmpty)
                                  ? Text(
                                      AuthService.currentUser?.fullName.split(' ').map((e) => e[0]).join() ?? '',
                                      style: GoogleFonts.outfit(color: badgeColor, fontSize: 24, fontWeight: FontWeight.bold),
                                    )
                                  : null,
                            ),
                          ),
                          Positioned(
                            bottom: -5,
                            right: -5,
                            child: Container(
                              padding: const EdgeInsets.all(8),
                              decoration: BoxDecoration(
                                color: const Color(0xFF1E1B4B),
                                shape: BoxShape.circle,
                                border: Border.all(color: badgeColor, width: 2),
                                boxShadow: [
                                  BoxShadow(
                                    color: Colors.black.withOpacity(0.3),
                                    blurRadius: 5,
                                    offset: const Offset(0, 3),
                                  ),
                                ],
                              ),
                              child: Icon(badgeIcon, size: 24, color: badgeColor),
                            ),
                          ),
                        ],
                      ).animate()
                       .scale(duration: 800.ms, curve: Curves.elasticOut)
                       .then()
                       .shake(hz: 2, duration: 600.ms),
                      const SizedBox(height: 25),
                      Text(
                        "CONGRATULATIONS, $firstName!",
                        textAlign: TextAlign.center,
                        style: GoogleFonts.outfit(
                          color: badgeColor,
                          fontSize: 24,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 1.2,
                        ),
                      ).animate().fadeIn().slideY(begin: -0.3),
                      const SizedBox(height: 8),
                      Text(
                        "You promoted this badge!",
                        style: GoogleFonts.outfit(
                          color: Colors.white70,
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      const SizedBox(height: 15),
                      // Badge pill
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.05),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(color: Colors.white10),
                        ),
                        child: Text(
                          badgeName.toUpperCase(),
                          style: GoogleFonts.outfit(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 1,
                          ),
                        ),
                      ).animate().scale(delay: 300.ms, duration: 500.ms, curve: Curves.easeOutBack),
                      const SizedBox(height: 35),
                      ElevatedButton(
                        onPressed: () => Navigator.pop(context),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: badgeColor,
                          foregroundColor: Colors.black,
                          elevation: 8,
                          shadowColor: badgeColor.withOpacity(0.3),
                          padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 16),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                        ),
                        child: Text(
                          "Awesome!",
                          style: GoogleFonts.outfit(
                            fontWeight: FontWeight.bold,
                            fontSize: 18,
                          ),
                        ),
                      ).animate().fadeIn(delay: 700.ms).scale(),
                    ],
                  ),
                ),
                // Confetti overlay on top!
                Positioned(
                  top: -50,
                  child: ConfettiWidget(
                    confettiController: _confettiController,
                    blastDirectionality: BlastDirectionality.explosive,
                    shouldLoop: false,
                    numberOfParticles: 40,
                    emissionFrequency: 0.05,
                    colors: const [
                      Colors.cyanAccent,
                      Colors.purpleAccent,
                      Colors.amberAccent,
                      Colors.redAccent,
                      Colors.greenAccent,
                      Colors.orangeAccent,
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B), // Deep Indigo
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E1B4B), Color(0xFF312E81), Color(0xFF4338CA)],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            physics: const BouncingScrollPhysics(),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SizedBox(height: 20),
                  _buildHeader(),
                  const SizedBox(height: 10),
                  _buildGreeting(),
                  const SizedBox(height: 15),
                  _buildPromoBanner(),
                  const SizedBox(height: 20),
                  _buildSectionTitle("Featured Categories"),
                  const SizedBox(height: 20),
                  _buildCategoriesGrid(),
                  const SizedBox(height: 30),
                ],
              ),
            ),
          ),
        ),
      ),
      bottomNavigationBar: _buildBottomNav(),
    );
  }

  Widget _buildHeader() {
    final user = AuthService.currentUser;
    final userName = user?.fullName ?? "ABDI SHAKUUR";
    final userCoins = user?.coins ?? 1236;
    final userEmail = user?.email;
    final userPhone = user?.phoneNumber;
    final userXp = user?.xp;

    return Row(
      children: [
        GestureDetector(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => ProfilePreviewScreen(
                  name: userName,
                  avatarUrl: user?.avatarUrl,
                  email: userEmail,
                  phone: userPhone,
                  coins: userCoins,
                  xp: userXp,
                ),
              ),
            );
          },
          child: Container(
            padding: const EdgeInsets.all(3),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: const LinearGradient(
                colors: [Colors.cyanAccent, Colors.purpleAccent],
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.cyanAccent.withOpacity(0.5),
                  blurRadius: 10,
                  spreadRadius: 2,
                ),
              ],
            ),
             child: ValueListenableBuilder<UserModel?>(
              valueListenable: AuthService.currentUserNotifier,
              builder: (context, user, _) {
                final displayAvatar = user?.avatarUrl;
                final displayName = user?.fullName ?? userName;
                return CircleAvatar(
                  radius: 20,
                  backgroundImage: AuthService.getAvatarProvider(displayAvatar),
                  child: (displayAvatar == null || displayAvatar.isEmpty)
                      ? Text(
                          displayName.isNotEmpty ? displayName[0].toUpperCase() : '',
                          style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold, fontSize: 14),
                        )
                      : null,
                );
              },
            ),
          ),
        ).animate().scale(duration: 600.ms, curve: Curves.easeOutBack),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                userName,
                style: GoogleFonts.outfit(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 4),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white24),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(Icons.stars, color: Colors.amber, size: 14),
                    const SizedBox(width: 4),
                    Text(
                      "$userCoins COINS",
                      style: GoogleFonts.outfit(
                        color: Colors.amber,
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ).animate().fadeIn(delay: 200.ms, duration: 600.ms).slideX(begin: -0.2),
        const SizedBox(width: 8),
        if (AuthService.currentUser?.isAdmin == true) ...[
          _buildAdminIconButton(),
          const SizedBox(width: 6),
        ],
        _buildNotificationIconButton(),
        const SizedBox(width: 6),
        _buildStreakIconButton(),
      ],
    );
  }

  Widget _buildNotificationIconButton() {
    final int unreadCount = _notifications.where((n) => !(n['isRead'] ?? false)).length;

    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const NotificationsScreen()),
          );
        },
        borderRadius: BorderRadius.circular(30),
        child: Stack(
          clipBehavior: Clip.none,
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.1),
                shape: BoxShape.circle,
                border: Border.all(color: Colors.white10),
              ),
              child: const Icon(
                Icons.notifications_rounded,
                color: Colors.white,
                size: 26,
              ),
            ),
            if (unreadCount > 0)
              Positioned(
                top: -2,
                right: -2,
                child: Container(
                  padding: const EdgeInsets.all(4),
                  decoration: const BoxDecoration(
                    color: Colors.redAccent,
                    shape: BoxShape.circle,
                  ),
                  constraints: const BoxConstraints(
                    minWidth: 16,
                    minHeight: 16,
                  ),
                  child: Center(
                    child: Text(
                      "$unreadCount",
                      style: GoogleFonts.outfit(
                        color: Colors.white,
                        fontSize: 8,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ).animate(onPlay: (c) => c.repeat(reverse: true)).scale(duration: 1.seconds, begin: const Offset(0.9, 0.9), end: const Offset(1.1, 1.1)),
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildAdminIconButton() {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const AdminHome()),
          );
        },
        borderRadius: BorderRadius.circular(30),
        child: Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.1),
            shape: BoxShape.circle,
            border: Border.all(color: Colors.white10),
          ),
          child: const Icon(
            Icons.admin_panel_settings_rounded,
            color: Colors.cyanAccent,
            size: 26,
          ),
        ),
      ),
    );
  }


  Widget _buildStreakIconButton() {
    final user = AuthService.currentUser;
    final streakCount = user?.streakCount ?? 0;
    final isStreakActive = streakCount > 0;
    final Color themeColor = isStreakActive ? Colors.orangeAccent : Colors.white30;
    final IconData streakIcon = isStreakActive ? Icons.local_fire_department_rounded : Icons.local_fire_department_outlined;

    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: () => _showStreakDialog(),
        borderRadius: BorderRadius.circular(30),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.1),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: isStreakActive ? Colors.orangeAccent.withOpacity(0.3) : Colors.white10),
            boxShadow: isStreakActive
                ? [
                    BoxShadow(
                      color: Colors.orangeAccent.withOpacity(0.15),
                      blurRadius: 8,
                      spreadRadius: 1,
                    )
                  ]
                : [],
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                streakIcon,
                color: themeColor,
                size: 20,
              ).animate(target: isStreakActive ? 1 : 0).shake(hz: 3, curve: Curves.easeInOut),
              if (isStreakActive) ...[
                const SizedBox(width: 4),
                Text(
                  "$streakCount",
                  style: GoogleFonts.outfit(
                    color: Colors.orangeAccent,
                    fontWeight: FontWeight.bold,
                    fontSize: 14,
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }

  void _showStreakDialog() {
    _confettiController.stop();

    showDialog(
      context: context,
      barrierDismissible: true,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setStateDialog) {
            final user = AuthService.currentUser;
            final streakCount = user?.streakCount ?? 0;
            final isStreakActive = streakCount > 0;
            final previousStreak = user?.previousStreak ?? 0;
            final restoresLeft = user?.availableRestores ?? 5;
            
            // Check if streak can be restored:
            final canRestore = previousStreak >= 3 && streakCount < previousStreak && restoresLeft > 0;

            return Dialog.fullscreen(
              backgroundColor: Colors.transparent,
              child: Stack(
                children: [
                  Container(
                    width: double.infinity,
                    height: double.infinity,
                    padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 30),
                    decoration: const BoxDecoration(
                      gradient: LinearGradient(
                        colors: [
                          Color(0xFF1E1B4B),
                          Color(0xFF312E81),
                        ],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ),
                    ),
                    child: SafeArea(
                      child: Column(
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                "Activity Streak",
                                style: GoogleFonts.outfit(
                                  color: Colors.white,
                                  fontSize: 24,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                              IconButton(
                                onPressed: () => Navigator.pop(context),
                                icon: const Icon(Icons.close_rounded, color: Colors.white60),
                                style: IconButton.styleFrom(
                                  backgroundColor: Colors.white.withOpacity(0.05),
                                  padding: const EdgeInsets.all(8),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 30),
                          
                          // Flame icon state
                          Stack(
                            alignment: Alignment.center,
                            children: [
                              Container(
                                padding: const EdgeInsets.all(24),
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: isStreakActive ? Colors.orangeAccent.withOpacity(0.1) : Colors.white.withOpacity(0.02),
                                  boxShadow: isStreakActive
                                      ? [
                                          BoxShadow(
                                            color: Colors.orangeAccent.withOpacity(0.3),
                                            blurRadius: 35,
                                            spreadRadius: 6,
                                          )
                                        ]
                                      : [],
                                ),
                                child: Icon(
                                  isStreakActive ? Icons.local_fire_department_rounded : Icons.local_fire_department_outlined,
                                  size: 80,
                                  color: isStreakActive ? Colors.orangeAccent : Colors.white30,
                                ),
                              ).animate(target: isStreakActive ? 1 : 0).scale(duration: 500.ms, curve: Curves.easeOutBack),
                            ],
                          ),
                          const SizedBox(height: 20),
                          Text(
                            isStreakActive
                                ? "$streakCount Day Streak!"
                                : "Start your streak!",
                            style: GoogleFonts.outfit(
                              color: Colors.white,
                              fontSize: 26,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 10),
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 20),
                            child: Text(
                              isStreakActive
                                  ? "You're on fire! Keep completing quizzes or mock exams daily to keep it burning."
                                  : "Complete a general quiz or mock exam today to begin your streak progress.",
                              textAlign: TextAlign.center,
                              style: GoogleFonts.outfit(
                                color: Colors.white70,
                                fontSize: 15,
                              ),
                            ),
                          ),
                          const SizedBox(height: 30),

                          // Streak checklist
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: List.generate(3, (index) {
                              final step = index + 1;
                              final isDone = streakCount >= step;
                              final Color stepColor = isDone ? Colors.orangeAccent : Colors.white24;
                              return Row(
                                children: [
                                  Column(
                                    children: [
                                      Container(
                                        width: 44,
                                        height: 44,
                                        decoration: BoxDecoration(
                                          shape: BoxShape.circle,
                                          color: isDone ? Colors.orangeAccent.withOpacity(0.1) : Colors.transparent,
                                          border: Border.all(color: stepColor, width: 2),
                                        ),
                                        child: Center(
                                          child: isDone
                                              ? const Icon(Icons.check_rounded, color: Colors.orangeAccent, size: 24)
                                              : Text(
                                                  "$step",
                                                  style: GoogleFonts.outfit(
                                                    color: Colors.white38,
                                                    fontSize: 16,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                        ),
                                      ),
                                      const SizedBox(height: 6),
                                      Text(
                                        "Day $step",
                                        style: GoogleFonts.outfit(
                                          color: isDone ? Colors.white70 : Colors.white38,
                                          fontSize: 12,
                                          fontWeight: FontWeight.bold,
                                        ),
                                      ),
                                    ],
                                  ),
                                  if (index < 2)
                                    Container(
                                      width: 35,
                                      height: 2.5,
                                      margin: const EdgeInsets.only(bottom: 18),
                                      color: streakCount >= (step + 1) ? Colors.orangeAccent : Colors.white10,
                                    ),
                                ],
                              );
                            }),
                          ),
                          const SizedBox(height: 30),

                          // Restore Section
                          if (canRestore) ...[
                            ElevatedButton(
                              onPressed: () async {
                                showDialog(
                                  context: context,
                                  barrierDismissible: false,
                                  builder: (context) => const Center(child: CircularProgressIndicator(color: Colors.orangeAccent)),
                                );
                                await AuthService.restoreUserStreak();
                                if (context.mounted) {
                                  Navigator.pop(context); // Pop loading dialog
                                  setStateDialog(() {}); // Update local dialog state
                                  setState(() {}); // Update home screen state
                                  _confettiController.play();
                                  
                                  final remaining = AuthService.currentUser?.availableRestores ?? 0;
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    SnackBar(
                                      content: Text("Streak restored successfully! $remaining restores left this month."),
                                      backgroundColor: Colors.orange,
                                    ),
                                  );
                                }
                              },
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Colors.orangeAccent,
                                foregroundColor: Colors.black,
                                elevation: 8,
                                shadowColor: Colors.orangeAccent.withOpacity(0.3),
                                padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 16),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                              ),
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  const Icon(Icons.restore_rounded, size: 22),
                                  const SizedBox(width: 8),
                                  Text(
                                    "Restore Streak (Recover $previousStreak Days)",
                                    style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 15),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 8),
                            Text(
                              "5 restores reset monthly. Remaining: $restoresLeft",
                              style: GoogleFonts.outfit(
                                color: Colors.orangeAccent.withOpacity(0.8),
                                fontSize: 12,
                                fontWeight: FontWeight.w500,
                              ),
                            ),
                            const SizedBox(height: 20),
                          ],

                          const Divider(color: Colors.white10, height: 20),
                          const SizedBox(height: 10),
                          
                          // Leaders Title
                          Text(
                            "FRIENDS & LEADERBOARD",
                            style: GoogleFonts.outfit(
                              color: Colors.orangeAccent,
                              fontSize: 14,
                              fontWeight: FontWeight.w900,
                              letterSpacing: 1.2,
                            ),
                          ),
                          const SizedBox(height: 15),

                          // FutureBuilder for streaks list
                          Expanded(
                            child: FutureBuilder<List<UserModel>>(
                              future: AuthService.getAllUsers(),
                              builder: (context, snapshot) {
                                if (snapshot.connectionState == ConnectionState.waiting) {
                                  return const Center(child: CircularProgressIndicator(color: Colors.orangeAccent));
                                }
                                if (snapshot.hasError || !snapshot.hasData || snapshot.data!.isEmpty) {
                                  return Center(
                                    child: Text(
                                      "No other users found.",
                                      style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
                                    ),
                                  );
                                }

                                final usersList = snapshot.data!;
                                final filteredList = usersList.where((u) => u.streakCount > 0).toList();
                                filteredList.sort((a, b) => b.streakCount.compareTo(a.streakCount));

                                if (filteredList.isEmpty) {
                                  return Center(
                                    child: Text(
                                      "No active streaks in your network yet. Be the first!",
                                      style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
                                    ),
                                  );
                                }

                                return ListView.builder(
                                  physics: const BouncingScrollPhysics(),
                                  itemCount: filteredList.length,
                                  itemBuilder: (context, index) {
                                    final userRow = filteredList[index];
                                    final bool isMe = userRow.email.toLowerCase() == AuthService.currentUser?.email.toLowerCase();
                                    final rank = index + 1;
                                    
                                    IconData rankIcon;
                                    Color rankColor;
                                    bool showMedal = rank <= 3;
                                    
                                    if (rank == 1) {
                                      rankIcon = Icons.emoji_events_rounded;
                                      rankColor = const Color(0xFFFFD700);
                                    } else if (rank == 2) {
                                      rankIcon = Icons.emoji_events_rounded;
                                      rankColor = const Color(0xFFC0C0C0);
                                    } else if (rank == 3) {
                                      rankIcon = Icons.emoji_events_rounded;
                                      rankColor = const Color(0xFFCD7F32);
                                    } else {
                                      rankIcon = Icons.circle;
                                      rankColor = Colors.transparent;
                                    }

                                    final isRowStreakActive = userRow.streakCount > 0;

                                    return Container(
                                      margin: const EdgeInsets.only(bottom: 10),
                                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                                      decoration: BoxDecoration(
                                        color: isMe ? Colors.orangeAccent.withOpacity(0.08) : Colors.white.withOpacity(0.02),
                                        borderRadius: BorderRadius.circular(16),
                                        border: Border.all(
                                          color: isMe ? Colors.orangeAccent.withOpacity(0.3) : Colors.transparent,
                                        ),
                                      ),
                                      child: Row(
                                        children: [
                                          SizedBox(
                                            width: 35,
                                            child: showMedal
                                                ? Icon(rankIcon, color: rankColor, size: 22)
                                                : Text(
                                                    "#$rank",
                                                    style: GoogleFonts.outfit(
                                                      color: Colors.white38,
                                                      fontSize: 14,
                                                      fontWeight: FontWeight.bold,
                                                    ),
                                                  ),
                                          ),
                                          const SizedBox(width: 8),
                                          Expanded(
                                            child: Text(
                                              userRow.fullName,
                                              maxLines: 1,
                                              overflow: TextOverflow.ellipsis,
                                              style: GoogleFonts.outfit(
                                                color: isMe ? Colors.orangeAccent : Colors.white,
                                                fontWeight: isMe ? FontWeight.bold : FontWeight.w500,
                                                fontSize: 15,
                                              ),
                                            ),
                                          ),
                                          const SizedBox(width: 10),
                                          Icon(
                                            isRowStreakActive ? Icons.local_fire_department_rounded : Icons.local_fire_department_outlined,
                                            size: 18,
                                            color: isRowStreakActive ? Colors.orangeAccent : Colors.white24,
                                          ),
                                          const SizedBox(width: 4),
                                          Text(
                                            "${userRow.streakCount}d",
                                            style: GoogleFonts.outfit(
                                              color: isRowStreakActive ? Colors.orangeAccent : Colors.white38,
                                              fontWeight: FontWeight.bold,
                                              fontSize: 14,
                                            ),
                                          ),
                                        ],
                                      ),
                                    );
                                  },
                                );
                              },
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  
                  // Confetti Widget overlay!
                  Align(
                    alignment: Alignment.topCenter,
                    child: ConfettiWidget(
                      confettiController: _confettiController,
                      blastDirectionality: BlastDirectionality.explosive,
                      shouldLoop: false,
                      numberOfParticles: 35,
                      colors: const [
                        Colors.orangeAccent,
                        Colors.amberAccent,
                        Colors.redAccent,
                        Colors.yellowAccent,
                      ],
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }

  Widget _buildGreeting() {
    final user = AuthService.currentUser;
    final displayFirstName = user != null ? user.fullName.split(' ')[0] : "Back!";
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "Welcome $displayFirstName 👋",
          style: GoogleFonts.outfit(
            color: Colors.white,
            fontSize: 28,
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(height: 8),
        Text(
          "Let's test your knowledge today.",
          style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16),
        ),
      ],
    ).animate().fadeIn(duration: 800.ms).slideY(begin: 0.1);
  }

  Widget _buildPromoBanner() {
    return Container(
      width: double.infinity,
      height: 185,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(30),
        gradient: const LinearGradient(
          colors: [Color(0xFFFACC15), Color(0xFFEAB308)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.yellow.withOpacity(0.3),
            blurRadius: 20,
            offset: const Offset(0, 10),
          ),
        ],
      ),
      child: Stack(
        children: [
          // Background patterns
          Positioned(
            right: -20,
            top: -20,
            child: CircleAvatar(
              radius: 60,
              backgroundColor: Colors.white.withOpacity(0.1),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Flexible(
                  child: SizedBox(
                    width: 180,
                    child: Text(
                      "Do you want to Challenge with friends?",
                      style: GoogleFonts.outfit(
                        color: Colors.black87,
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                        height: 1.2,
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 15),
                ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const FindFriendsScreen(),
                          ),
                        );
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.black,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15),
                        ),
                        padding: const EdgeInsets.symmetric(
                          horizontal: 20,
                          vertical: 12,
                        ),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.person_add_alt_1_rounded, size: 18),
                          const SizedBox(width: 8),
                          Text(
                            "Find Friends",
                            style: GoogleFonts.outfit(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    )
                    .animate(
                      onPlay: (controller) => controller.repeat(reverse: true),
                    )
                    .scale(
                      duration: 1.seconds,
                      begin: const Offset(1, 1),
                      end: const Offset(1.05, 1.05),
                    ),
              ],
            ),
          ),
          Positioned(
            right: 0,
            bottom: 0,
            child:
                Image.asset(
                  'assets/images/character.png',
                  height: 180, // Allow character to be slightly larger
                  fit: BoxFit.contain,
                  errorBuilder: (context, error, stackTrace) =>
                      const SizedBox(),
                ).animate().slideX(
                  begin: 1,
                  duration: 800.ms,
                  curve: Curves.easeOutCubic,
                ),
          ),
        ],
      ),
    ).animate().scale(duration: 600.ms, curve: Curves.easeOutBack);
  }

  Widget _buildSectionTitle(String title) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(
          title,
          style: GoogleFonts.outfit(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          ),
        ),
        TextButton(
          onPressed: () {},
          child: Text(
            "See All",
            style: GoogleFonts.outfit(color: Colors.cyanAccent),
          ),
        ),
      ],
    );
  }

  Widget _buildCategoriesGrid() {
    final categories = [
      _CategoryData("Quizzes", Icons.quiz_rounded, [
        const Color(0xFF3B82F6),
        const Color(0xFF2563EB),
      ]),
      _CategoryData("Your Exams", Icons.assignment_rounded, [
        const Color(0xFF10B981),
        const Color(0xFF059669),
      ]),
      _CategoryData("Mock Exams", Icons.library_add_rounded, [
        const Color(0xFFF43F5E),
        const Color(0xFFE11D48),
      ]),
      _CategoryData("Competition", Icons.emoji_events_rounded, [
        const Color(0xFFF59E0B),
        const Color(0xFFD97706),
      ]),
    ];

    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        crossAxisSpacing: 15,
        mainAxisSpacing: 15,
        childAspectRatio: 1.3,
      ),
      itemCount: categories.length,
      itemBuilder: (context, index) {
        final cat = categories[index];
        return _buildCategoryCard(cat, index);
      },
    );
  }

  Widget _buildCategoryCard(_CategoryData cat, int index) {
    return GestureDetector(
      onTap: () {
        if (cat.title == "Quizzes") {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const QuizSubjectsScreen()),
          );
        } else if (cat.title == "Competition") {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const CompetitionsListScreen()),
          );
        } else if (cat.title == "Mock Exams") {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const CreateMockExamScreen()),
          );
        } else if (cat.title == "Your Exams") {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const PapersListScreen()),
          );
        }
      },
      child:
          Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(25),
                  gradient: LinearGradient(
                    colors: cat.colors,
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: cat.colors[0].withOpacity(0.3),
                      blurRadius: 15,
                      offset: const Offset(0, 8),
                    ),
                  ],
                ),
                child: Stack(
                  children: [
                    Positioned(
                      right: -10,
                      bottom: -10,
                      child: Icon(
                        cat.icon,
                        size: 80,
                        color: Colors.white.withOpacity(0.15),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(20.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            padding: const EdgeInsets.all(8),
                            decoration: BoxDecoration(
                              color: Colors.white.withOpacity(0.2),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Icon(
                              cat.icon,
                              color: Colors.white,
                              size: 24,
                            ),
                          ),
                          const Spacer(),
                          Text(
                            cat.title,
                            style: GoogleFonts.outfit(
                              color: Colors.white,
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              )
              .animate()
              .fadeIn(delay: (index * 100).ms, duration: 500.ms)
              .scale(curve: Curves.easeOutBack),
    );
  }

  Widget _buildBottomNav() {
    return Container(
      margin: const EdgeInsets.all(20),
      height: 80,
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.08),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            blurRadius: 30,
            offset: const Offset(0, 10),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _buildNavItem(0, Icons.home_rounded, "Home"),
          _buildNavItem(
            1,
            Icons.explore_rounded,
            "Quiz",
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const QuizSubjectsScreen(),
                ),
              );
            },
          ),
          _buildNavItem(2, Icons.flag_rounded, "Challenges", onTap: () {
            Navigator.push(context, MaterialPageRoute(builder: (context) => const ChallengesScreen()));
          }),
          _buildNavItem(3, Icons.emoji_events_rounded, "Competition", onTap: () {
            Navigator.push(context, MaterialPageRoute(builder: (context) => const CompetitionsListScreen()));
          }),
          _buildNavItem(4, Icons.person_rounded, "Profile", onTap: () {
            final user = AuthService.currentUser;
            final userName = user?.fullName ?? "ABDI SHAKUUR";
            final userCoins = user?.coins ?? 1236;
            final userEmail = user?.email;
            final userPhone = user?.phoneNumber;
            final userXp = user?.xp;

            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => ProfilePreviewScreen(
                  name: userName,
                  avatarUrl: user?.avatarUrl,
                  email: userEmail,
                  phone: userPhone,
                  coins: userCoins,
                  xp: userXp,
                ),
              ),
            );
          }),
        ],
      ),
    ).animate().slideY(begin: 1, duration: 600.ms, curve: Curves.easeOutCubic);
  }

  Widget _buildNavItem(
    int index,
    IconData icon,
    String label, {
    VoidCallback? onTap,
  }) {
    bool isSelected = _selectedIndex == index;
    return GestureDetector(
      onTap: () {
        setState(() => _selectedIndex = index);
        if (onTap != null) onTap();
      },
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          AnimatedContainer(
            duration: const Duration(milliseconds: 300),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: isSelected
                  ? Colors.cyanAccent.withOpacity(0.1)
                  : Colors.transparent,
              shape: BoxShape.circle,
            ),
            child: Icon(
              icon,
              color: isSelected ? Colors.cyanAccent : Colors.white38,
              size: 28,
            ),
          ),
          const SizedBox(height: 2),
          Text(
            label,
            style: GoogleFonts.outfit(
              color: isSelected ? Colors.cyanAccent : Colors.white38,
              fontSize: 10,
              fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
            ),
          ),
        ],
      ),
    );
  }
}

class _CategoryData {
  final String title;
  final IconData icon;
  final List<Color> colors;

  _CategoryData(this.title, this.icon, this.colors);
}
