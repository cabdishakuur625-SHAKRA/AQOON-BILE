import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:file_picker/file_picker.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'ChatScreen.dart';
import 'Sign-in.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';

class ProfilePreviewScreen extends StatefulWidget {
  final String name;
  final String? avatarUrl;
  final String? email;
  final String? phone;
  final int? coins;
  final int? xp;

  const ProfilePreviewScreen({
    super.key,
    required this.name,
    this.avatarUrl,
    this.email,
    this.phone,
    this.coins,
    this.xp,
  });

  @override
  State<ProfilePreviewScreen> createState() => _ProfilePreviewScreenState();
}

class _ProfilePreviewScreenState extends State<ProfilePreviewScreen> {
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  List<Map<String, dynamic>> targetFriends = [];
  List<Map<String, dynamic>> mutualFriends = [];
  int myFriendsCount = 0;
  bool _isLoading = true;
  String _selectedTimeRange = 'all';

  @override
  void initState() {
    super.initState();
    _loadProfileData();
    
    final currentEmail = AuthService.currentUser?.email;
    final isOwnProfile = AuthService.currentUser != null &&
        (widget.email == null ||
         widget.email!.toLowerCase() == currentEmail!.toLowerCase() ||
         widget.name.toLowerCase() == AuthService.currentUser!.fullName.toLowerCase());
         
    if (isOwnProfile) {
      AuthService.currentUserNotifier.addListener(_onCurrentUserChanged);
      final targetEmail = currentEmail ?? widget.email ?? '';
      if (targetEmail == 'cabdishakuur625@gmail.com') {
        FirebaseService().seedDemoProgressDataIfEmpty(targetEmail);
      }
    }
  }

  @override
  void dispose() {
    AuthService.currentUserNotifier.removeListener(_onCurrentUserChanged);
    super.dispose();
  }

  @override
  void didUpdateWidget(covariant ProfilePreviewScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    
    final currentEmail = AuthService.currentUser?.email;
    final wasOwnProfile = AuthService.currentUser != null &&
        (oldWidget.email == null ||
         oldWidget.email!.toLowerCase() == currentEmail!.toLowerCase() ||
         oldWidget.name.toLowerCase() == AuthService.currentUser!.fullName.toLowerCase());
         
    final isOwnProfile = AuthService.currentUser != null &&
        (widget.email == null ||
         widget.email!.toLowerCase() == currentEmail!.toLowerCase() ||
         widget.name.toLowerCase() == AuthService.currentUser!.fullName.toLowerCase());
         
    if (wasOwnProfile != isOwnProfile) {
      if (isOwnProfile) {
        AuthService.currentUserNotifier.addListener(_onCurrentUserChanged);
      } else {
        AuthService.currentUserNotifier.removeListener(_onCurrentUserChanged);
      }
    }
    _loadProfileData();
  }

  void _onCurrentUserChanged() {
    if (mounted) {
      _loadProfileData();
    }
  }

  /// Query target user's friends list and match against current user's friends to calculate mutual friends dynamically
  Future<void> _loadProfileData() async {
    final currentEmail = AuthService.currentUser?.email;
    final isOwnProfile = AuthService.currentUser != null &&
        (widget.email == null ||
         widget.email!.toLowerCase() == currentEmail!.toLowerCase() ||
         widget.name.toLowerCase() == AuthService.currentUser!.fullName.toLowerCase());
         
    final targetEmail = isOwnProfile ? (currentEmail ?? widget.email ?? '') : (widget.email ?? "${widget.name.toLowerCase().replaceAll(' ', '')}@gmail.com");
    final targetKey = AuthService.sanitizeEmail(targetEmail);

    try {
      final myEmail = AuthService.currentUser?.email;
      final myKey = myEmail != null ? AuthService.sanitizeEmail(myEmail) : null;

      final snapshot = await _dbRef.child('Users').get();
      if (!snapshot.exists || snapshot.value == null) {
        if (mounted) {
          setState(() {
            _isLoading = false;
          });
        }
        return;
      }

      final Map<dynamic, dynamic> allUsersMap = snapshot.value as Map<dynamic, dynamic>;

      // Get my friends keys to check mutuals and own count
      Map<dynamic, dynamic> myFriendsKeysMap = {};
      if (myKey != null) {
        final myUserMap = allUsersMap[myKey] as Map<dynamic, dynamic>? ?? {};
        myFriendsKeysMap = myUserMap['friends'] as Map<dynamic, dynamic>? ?? {};
      }

      final List<Map<String, dynamic>> loadedTargetFriends = [];
      final List<Map<String, dynamic>> loadedMutualFriends = [];

      if (!isOwnProfile) {
        // Get target user's friends keys
        final targetUserMap = allUsersMap[targetKey] as Map<dynamic, dynamic>? ?? {};
        final Map<dynamic, dynamic> targetFriendsKeysMap = targetUserMap['friends'] as Map<dynamic, dynamic>? ?? {};

        targetFriendsKeysMap.forEach((friendKey, _) {
          final friendMap = allUsersMap[friendKey] as Map<dynamic, dynamic>?;
          if (friendMap != null) {
            final String fName = friendMap['fullName'] ?? 'User';
            final String fEmail = friendMap['email'] ?? '';
            final Map<String, dynamic> fData = {
              'name': fName,
              'email': fEmail,
            };

            loadedTargetFriends.add(fData);

            // If friend is also in my friends, they are a mutual friend
            if (myFriendsKeysMap.containsKey(friendKey)) {
              loadedMutualFriends.add(fData);
            }
          }
        });
      }

      if (mounted) {
        setState(() {
          targetFriends = loadedTargetFriends;
          mutualFriends = loadedMutualFriends;
          myFriendsCount = myFriendsKeysMap.length;
          _isLoading = false;
        });
      }
    } catch (e) {
      debugPrint("Error loading profile preview data: $e");
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final currentEmail = AuthService.currentUser?.email;
    final isOwnProfile = AuthService.currentUser != null &&
        (widget.email == null ||
         widget.email!.toLowerCase() == currentEmail!.toLowerCase() ||
         widget.name.toLowerCase() == AuthService.currentUser!.fullName.toLowerCase());
         
    final targetEmail = isOwnProfile ? (currentEmail ?? widget.email ?? '') : (widget.email ?? "${widget.name.toLowerCase().replaceAll(' ', '')}@gmail.com");

    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E1B4B), Color(0xFF312E81)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              _buildAppBar(context),
              Expanded(
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                    : SingleChildScrollView(
                        padding: const EdgeInsets.symmetric(horizontal: 25.0),
                        child: Column(
                          children: [
                            const SizedBox(height: 10),
                            _buildProfileHeader(targetEmail, isOwnProfile),
                            const SizedBox(height: 30),
                            _buildStatsCard(isOwnProfile),
                            const SizedBox(height: 30),
                            _buildActionButtons(context, isOwnProfile, targetEmail),
                            if (isOwnProfile || (AuthService.currentUser?.isAdmin ?? false)) ...[
                              const SizedBox(height: 35),
                              _buildProgressSection(targetEmail),
                            ],
                            if (!isOwnProfile) ...[
                              const SizedBox(height: 35),
                              _buildMutualFriendsSection(),
                            ],
                            const SizedBox(height: 35),
                            isOwnProfile
                                ? Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Row(
                                        children: [
                                          const Icon(Icons.group_rounded, color: Colors.cyanAccent, size: 20),
                                          const SizedBox(width: 10),
                                          Text(
                                            "Friends",
                                            style: GoogleFonts.outfit(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
                                          ),
                                        ],
                                      ),
                                      const SizedBox(height: 15),
                                      Container(
                                        width: double.infinity,
                                        padding: const EdgeInsets.all(20),
                                        decoration: BoxDecoration(
                                          color: Colors.white.withOpacity(0.03),
                                          borderRadius: BorderRadius.circular(20),
                                          border: Border.all(color: Colors.white.withOpacity(0.05)),
                                        ),
                                        child: Text(
                                          myFriendsCount == 0
                                              ? "No friends added yet. Go to Find Friends to search and add friends!"
                                              : "You have $myFriendsCount friends. Manage them in Find Friends.",
                                          textAlign: TextAlign.center,
                                          style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14, height: 1.4),
                                        ),
                                      ),
                                    ],
                                  )
                                : _buildFriendsGrid(),
                            const SizedBox(height: 40),
                          ],
                        ),
                      ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildAppBar(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          IconButton(
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Text(
            "Preview Profile",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48),
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildProfileHeader(String targetEmail, bool isOwnProfile) {
    final displayName = isOwnProfile ? (AuthService.currentUser?.fullName ?? widget.name) : widget.name;
    final displayEmail = isOwnProfile ? (AuthService.currentUser?.email ?? targetEmail) : targetEmail;
    final displayCoins = isOwnProfile ? (AuthService.currentUser?.coins ?? widget.coins ?? 0) : (widget.coins ?? 0);
    final displayAvatar = isOwnProfile ? (AuthService.currentUser?.avatarUrl ?? widget.avatarUrl) : widget.avatarUrl;

    return Column(
      children: [
        GestureDetector(
          onTap: isOwnProfile ? _changeProfilePicture : null,
          child: Container(
            padding: const EdgeInsets.all(4),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(color: Colors.cyanAccent.withOpacity(0.3), width: 2),
            ),
            child: Stack(
              children: [
                CircleAvatar(
                  radius: 65,
                  backgroundColor: Colors.white.withOpacity(0.1),
                  backgroundImage: AuthService.getAvatarProvider(displayAvatar),
                  child: (displayAvatar == null || displayAvatar.isEmpty)
                      ? Text(
                          displayName.split(' ').map((e) => e[0]).join(),
                          style: GoogleFonts.outfit(color: Colors.cyanAccent, fontSize: 32, fontWeight: FontWeight.bold),
                        )
                      : null,
                ),
                if (isOwnProfile)
                  Positioned(
                    bottom: 0,
                    right: 0,
                    child: CircleAvatar(
                      radius: 18,
                      backgroundColor: Colors.cyanAccent,
                      child: const Icon(Icons.camera_alt_rounded, size: 16, color: Colors.black),
                    ),
                  ),
              ],
            ),
          ).animate().scale(duration: 600.ms, curve: Curves.easeOutBack),
        ),
        const SizedBox(height: 20),
        Text(
          displayName,
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 26, fontWeight: FontWeight.bold),
        ).animate().fadeIn(delay: 200.ms),
        Text(
          displayEmail,
          style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
        ).animate().fadeIn(delay: 300.ms),
        _buildBadgesRow(displayCoins).animate().fadeIn(delay: 400.ms).slideY(begin: 0.1),
      ],
    );
  }

  Future<void> _changeProfilePicture() async {
    try {
      final result = await FilePicker.platform.pickFiles(
        type: FileType.image,
        allowMultiple: false,
      );

      if (result == null || result.files.isEmpty) return;

      final file = result.files.first;
      
      // Show loading indicator dialog
      if (!mounted) return;
      showDialog(
        context: context,
        barrierDismissible: false,
        builder: (context) => const Center(
          child: CircularProgressIndicator(color: Colors.cyanAccent),
        ),
      );

      final String sanitizedEmail = AuthService.sanitizeEmail(AuthService.currentUser!.email);
      
      // Try default storage bucket first
      Reference ref = FirebaseStorage.instance.ref().child('profile_pictures/$sanitizedEmail.jpg');
      UploadTask uploadTask;
      if (kIsWeb) {
        uploadTask = ref.putData(file.bytes!);
      } else {
        uploadTask = ref.putFile(File(file.path!));
      }

      String downloadUrl;
      bool isStorageUpload = true;

      try {
        TaskSnapshot snapshot;
        try {
          snapshot = await uploadTask;
        } catch (e) {
          debugPrint("Default storage bucket failed ($e), trying fallback appspot.com bucket...");
          // Fallback to traditional appspot.com bucket
          final fallbackRef = FirebaseStorage.instanceFor(bucket: 'gs://aqoonbile-3389f.appspot.com')
              .ref()
              .child('profile_pictures/$sanitizedEmail.jpg');
          if (kIsWeb) {
            uploadTask = fallbackRef.putData(file.bytes!);
          } else {
            uploadTask = fallbackRef.putFile(File(file.path!));
          }
          snapshot = await uploadTask;
        }
        downloadUrl = await snapshot.ref.getDownloadURL();
      } catch (e) {
        debugPrint("Firebase Storage upload failed ($e). Falling back to Base64 Database storage...");
        isStorageUpload = false;
        
        // Fallback: Read file bytes and encode to base64
        final fileBytes = await File(file.path!).readAsBytes();
        downloadUrl = 'data:image/jpeg;base64,' + base64Encode(fileBytes);
      }

      // Update database Users/$sanitizedEmail/avatarUrl
      await _dbRef.child('Users/$sanitizedEmail').update({
        'avatarUrl': downloadUrl,
      });

      // Update local currentUser state
      if (AuthService.currentUser != null) {
        AuthService.currentUser = AuthService.currentUser!.copyWith(avatarUrl: downloadUrl);
        AuthService.currentUserNotifier.value = AuthService.currentUser;
      }

      if (mounted) {
        Navigator.pop(context); // Dismiss loading dialog
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text("Profile picture updated successfully!"),
            backgroundColor: Colors.green,
          ),
        );
        setState(() {}); // Force rebuild of profile preview
      }
    } catch (e) {
      if (mounted) {
        Navigator.pop(context); // Dismiss loading if open
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text("Failed to update profile picture: $e"),
            backgroundColor: Colors.redAccent,
          ),
        );
      }
    }
  }

  void _showEditProfileDialog(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const EditProfileScreen()),
    );
  }

  Widget _buildBadgesRow(int coins) {
    final List<Map<String, dynamic>> badgeConfig = [
      {
        'name': 'Bronze',
        'icon': Icons.military_tech_rounded,
        'color': const Color(0xFFCD7F32),
        'threshold': 100,
      },
      {
        'name': 'Silver',
        'icon': Icons.shield_rounded,
        'color': const Color(0xFFC0C0C0),
        'threshold': 500,
      },
      {
        'name': 'Gold',
        'icon': Icons.emoji_events_rounded,
        'color': const Color(0xFFFFD700),
        'threshold': 1000,
      },
      {
        'name': 'Platinum',
        'icon': Icons.workspace_premium_rounded,
        'color': const Color(0xFF00F2FE),
        'threshold': 2500,
      },
      {
        'name': 'Diamond',
        'icon': Icons.diamond_rounded,
        'color': const Color(0xFFB9F2FF),
        'threshold': 5000,
      },
    ];

    return Container(
      margin: const EdgeInsets.only(top: 20),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.03),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.05)),
      ),
      child: Column(
        children: [
          Text(
            "BADGES & ACHIEVEMENTS",
            style: GoogleFonts.outfit(
              color: Colors.white38,
              fontSize: 11,
              fontWeight: FontWeight.w900,
              letterSpacing: 1.5,
            ),
          ),
          const SizedBox(height: 12),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: badgeConfig.map((badge) {
              final isUnlocked = coins >= (badge['threshold'] as int);
              final Color color = badge['color'] as Color;
              final IconData icon = badge['icon'] as IconData;
              final String name = badge['name'] as String;

              return Tooltip(
                message: isUnlocked
                    ? "$name Badge unlocked!"
                    : "Unlock at ${badge['threshold']} coins",
                child: Column(
                  children: [
                    Stack(
                      alignment: Alignment.center,
                      children: [
                        Container(
                          padding: const EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: isUnlocked
                                ? color.withOpacity(0.1)
                                : Colors.white.withOpacity(0.02),
                            border: Border.all(
                              color: isUnlocked ? color : Colors.white10,
                              width: 1.5,
                            ),
                            boxShadow: isUnlocked
                                ? [
                                    BoxShadow(
                                      color: color.withOpacity(0.2),
                                      blurRadius: 8,
                                      spreadRadius: 1,
                                    )
                                  ]
                                : [],
                          ),
                          child: Icon(
                            icon,
                            size: 24,
                            color: isUnlocked ? color : Colors.white24,
                          ),
                        ),
                        if (!isUnlocked)
                          Positioned(
                            bottom: 0,
                            right: 0,
                            child: Container(
                              padding: const EdgeInsets.all(2),
                              decoration: const BoxDecoration(
                                color: Color(0xFF1E1B4B),
                                shape: BoxShape.circle,
                              ),
                              child: const Icon(
                                Icons.lock_rounded,
                                size: 10,
                                color: Colors.white38,
                              ),
                            ),
                          ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Text(
                      name,
                      style: GoogleFonts.outfit(
                        color: isUnlocked ? Colors.white70 : Colors.white24,
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _buildStatsCard(bool isOwnProfile) {
    final displayPhone = isOwnProfile ? (AuthService.currentUser?.phoneNumber ?? widget.phone ?? "614353583") : (widget.phone ?? "614353583");
    final displayXp = isOwnProfile ? (AuthService.currentUser?.xp ?? widget.xp ?? 0) : (widget.xp ?? 0);
    final displayCoins = isOwnProfile ? (AuthService.currentUser?.coins ?? widget.coins ?? 0) : (widget.coins ?? 0);

    String level = "Beginner";
    if (displayXp >= 2000) {
      level = "Master";
    } else if (displayXp >= 1000) {
      level = "Expert";
    } else if (displayXp >= 500) {
      level = "Advanced";
    } else if (displayXp >= 200) {
      level = "Intermediate";
    }

    String badge = "None";
    if (displayCoins >= 5000) {
      badge = "Diamond";
    } else if (displayCoins >= 2500) {
      badge = "Platinum";
    } else if (displayCoins >= 1000) {
      badge = "Gold";
    } else if (displayCoins >= 500) {
      badge = "Silver";
    } else if (displayCoins >= 100) {
      badge = "Bronze";
    }

    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: Column(
        children: [
          _buildStatRow(Icons.phone_rounded, "Phone", displayPhone),
          _buildStatRow(Icons.star_rounded, "XP", displayXp.toString()),
          _buildStatRow(Icons.monetization_on_rounded, "Coins", displayCoins.toString()),
          _buildStatRow(Icons.bar_chart_rounded, "Level", level),
          _buildStatRow(Icons.workspace_premium_rounded, "Badge", badge),
          isOwnProfile
              ? _buildStatRow(Icons.group_rounded, "Friends", myFriendsCount.toString(), isLast: true)
              : _buildStatRow(Icons.group_rounded, "Friends", targetFriends.length.toString()),
          if (!isOwnProfile)
            _buildStatRow(Icons.people_alt_rounded, "Mutual Friends", mutualFriends.length.toString(), isLast: true),
        ],
      ),
    ).animate().fadeIn(delay: 400.ms).slideX(begin: 0.1);
  }

  Widget _buildStatRow(IconData icon, String label, String value, {bool isLast = false}) {
    return Padding(
      padding: EdgeInsets.only(bottom: isLast ? 0 : 20),
      child: Row(
        children: [
          Icon(icon, color: Colors.cyanAccent, size: 20),
          const SizedBox(width: 15),
          Text(label, style: GoogleFonts.outfit(color: Colors.white60, fontSize: 15)),
          const Spacer(),
          Text(value, style: GoogleFonts.outfit(color: Colors.white, fontSize: 15, fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }

  Widget _buildActionButtons(BuildContext context, bool isOwnProfile, String targetEmail) {
    if (isOwnProfile) {
      return Row(
        children: [
          Expanded(
            child: ElevatedButton(
              onPressed: () {
                _showEditProfileDialog(context);
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.cyanAccent.withOpacity(0.2),
                foregroundColor: Colors.cyanAccent,
                padding: const EdgeInsets.symmetric(vertical: 18),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                side: const BorderSide(color: Colors.cyanAccent, width: 1.5),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.edit_rounded, size: 20),
                  const SizedBox(width: 8),
                  Text("Edit Profile", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
                ],
              ),
            ),
          ),
          const SizedBox(width: 20),
          Expanded(
            child: ElevatedButton(
              onPressed: () {
                AuthService.logout();
                Navigator.of(context).pushAndRemoveUntil(
                  MaterialPageRoute(builder: (context) => const SignInScreen()),
                  (route) => false,
                );
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("Logged out successfully"),
                    backgroundColor: Colors.redAccent,
                  ),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.redAccent.withOpacity(0.2),
                foregroundColor: Colors.redAccent,
                padding: const EdgeInsets.symmetric(vertical: 18),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                side: const BorderSide(color: Colors.redAccent, width: 1.5),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.power_settings_new_rounded, size: 20),
                  const SizedBox(width: 8),
                  Text("Logout", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
                ],
              ),
            ),
          ),
        ],
      );
    }

    return Row(
      children: [
        Expanded(
          child: ElevatedButton(
            onPressed: () {
              Navigator.pop(context, 'unfriend');
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.redAccent.withOpacity(0.2),
              foregroundColor: Colors.redAccent,
              padding: const EdgeInsets.symmetric(vertical: 18),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              side: const BorderSide(color: Colors.redAccent, width: 1.5),
            ),
            child: Text("Unfriend", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
          ),
        ),
        const SizedBox(width: 20),
        Expanded(
          child: ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ChatScreen(
                    userName: widget.name,
                    avatarUrl: widget.avatarUrl,
                    userEmail: widget.email ?? "${widget.name.toLowerCase().replaceAll(' ', '')}@gmail.com",
                  ),
                ),
              );
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.cyanAccent,
              foregroundColor: Colors.black,
              padding: const EdgeInsets.symmetric(vertical: 18),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              elevation: 8,
              shadowColor: Colors.cyanAccent.withOpacity(0.5),
            ),
            child: Text("Message", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
          ),
        ),
      ],
    ).animate().fadeIn(delay: 600.ms).slideY(begin: 0.2);
  }

  Widget _buildMutualFriendsSection() {
    if (mutualFriends.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "Mutual Friends",
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 15),
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          child: Row(
            children: mutualFriends.map((friend) {
              return Padding(
                padding: const EdgeInsets.only(right: 20.0),
                child: _buildMutualFriendAvatar(friend['name'] ?? 'User'),
              );
            }).toList(),
          ),
        ),
      ],
    ).animate().fadeIn(delay: 800.ms);
  }

  Widget _buildMutualFriendAvatar(String name) {
    return Column(
      children: [
        CircleAvatar(
          radius: 25,
          backgroundColor: Colors.cyanAccent.withOpacity(0.2),
          child: Text(
            name.split(' ').map((e) => e[0]).join(),
            style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold, fontSize: 14),
          ),
        ),
        const SizedBox(height: 8),
        Text(
          name.split(' ')[0],
          style: GoogleFonts.outfit(color: Colors.white60, fontSize: 12),
        ),
      ],
    );
  }

  Widget _buildFriendsGrid() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "Friends",
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 15),
        targetFriends.isEmpty
            ? Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.03),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white.withOpacity(0.05)),
                ),
                child: Text(
                  "No friends added yet.",
                  textAlign: TextAlign.center,
                  style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
                ),
              )
            : GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 3,
                  crossAxisSpacing: 10,
                  mainAxisSpacing: 10,
                  childAspectRatio: 0.8,
                ),
                itemCount: targetFriends.length,
                itemBuilder: (context, index) {
                  final friend = targetFriends[index];
                  return _buildFriendCard(friend['name'] ?? 'User');
                },
              ),
      ],
    ).animate().fadeIn(delay: 1.seconds);
  }

  Widget _buildFriendCard(String name) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 15),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.05)),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          CircleAvatar(
            radius: 22,
            backgroundColor: Colors.cyanAccent.withOpacity(0.2),
            child: Text(
              name.split(' ').map((e) => e[0]).join(),
              style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold, fontSize: 12),
            ),
          ),
          const SizedBox(height: 10),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4.0),
            child: Text(
              name.split(' ')[0],
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: GoogleFonts.outfit(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w500),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTimeRangeSelector() {
    final List<Map<String, String>> ranges = [
      {'key': 'all', 'label': 'All Time'},
      {'key': 'today', 'label': 'Today'},
      {'key': 'yesterday', 'label': 'Yesterday'},
      {'key': 'week', 'label': '7 Days'},
      {'key': 'month', 'label': 'Month'},
    ];

    return Container(
      margin: const EdgeInsets.only(bottom: 25),
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.04),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.08)),
      ),
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        child: Row(
          children: ranges.map((range) {
            final isSelected = _selectedTimeRange == range['key'];
            return GestureDetector(
              onTap: () {
                setState(() {
                  _selectedTimeRange = range['key']!;
                });
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                decoration: BoxDecoration(
                  color: isSelected ? Colors.cyanAccent : Colors.transparent,
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: isSelected
                      ? [
                          BoxShadow(
                            color: Colors.cyanAccent.withOpacity(0.3),
                            blurRadius: 10,
                            spreadRadius: 1,
                          )
                        ]
                      : [],
                ),
                child: Text(
                  range['label']!,
                  style: GoogleFonts.outfit(
                    color: isSelected ? Colors.black : Colors.white60,
                    fontSize: 13,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            );
          }).toList(),
        ),
      ),
    );
  }

  Widget _buildProgressSection(String email) {
    final firebaseService = FirebaseService();
    return StreamBuilder<Map<String, int>>(
      stream: firebaseService.streamWeeklyXp(email),
      builder: (context, xpSnapshot) {
        return StreamBuilder<List<Map<String, dynamic>>>(
          stream: firebaseService.streamExamQuizHistory(email),
          builder: (context, historySnapshot) {
            final xpData = xpSnapshot.data ?? {};
            final historyData = historySnapshot.data ?? [];

            // Calculate current week's XP values
            final Map<String, int> weeklyXpValues = _getWeeklyXpValues(xpData);
            final List<int> chartXpValues = [
              weeklyXpValues["Mon"] ?? 0,
              weeklyXpValues["Tue"] ?? 0,
              weeklyXpValues["Wed"] ?? 0,
              weeklyXpValues["Thu"] ?? 0,
              weeklyXpValues["Fri"] ?? 0,
              weeklyXpValues["Sat"] ?? 0,
              weeklyXpValues["Sun"] ?? 0,
            ];

            // Calculate category progress stats for mock exams
            final mockStats = _calculateCategoryStats(historyData, 'mock_exam', _selectedTimeRange);

            // Calculate category progress stats for quizzes
            final quizStats = _calculateCategoryStats(historyData, 'quiz', _selectedTimeRange);

            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                _buildTimeRangeSelector(),
                // 1. XP Weekly Chart Card
                _buildProgressCard(
                  title: "XP This Week",
                  child: Container(
                    height: 180,
                    width: double.infinity,
                    padding: const EdgeInsets.only(top: 10),
                    child: CustomPaint(
                      painter: WeeklyXpPainter(
                        values: chartXpValues,
                        days: const ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 25),
                // 2. Mock Exam Category Performance Card
                _buildProgressCard(
                  title: "Mock exam performance by category",
                  child: CategoryBarChart(
                    stats: mockStats,
                  ),
                ),
                const SizedBox(height: 25),
                // 3. Quiz Category Performance Card
                _buildProgressCard(
                  title: "Quiz performance by category",
                  child: CategoryBarChart(
                    stats: quizStats,
                  ),
                ),
              ],
            );
          },
        );
      },
    );
  }

  Widget _buildProgressCard({
    required String title,
    Widget? subtitle,
    required Widget child,
  }) {
    IconData? cardIcon;
    if (title.toLowerCase().contains("mock")) {
      cardIcon = Icons.bar_chart_rounded;
    } else if (title.toLowerCase().contains("quiz")) {
      cardIcon = Icons.assignment_turned_in_rounded;
    } else if (title.toLowerCase().contains("xp")) {
      cardIcon = Icons.trending_up_rounded;
    }

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(25),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.04),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.08)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.15),
            blurRadius: 15,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  title,
                  style: GoogleFonts.outfit(
                    color: Colors.white,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
              if (cardIcon != null) ...[
                const SizedBox(width: 8),
                Icon(
                  cardIcon,
                  color: Colors.white60,
                  size: 24,
                ),
              ],
            ],
          ),
          if (subtitle != null) ...[
            const SizedBox(height: 15),
            subtitle,
          ],
          const SizedBox(height: 20),
          child,
        ],
      ),
    ).animate().fadeIn(duration: 500.ms).slideY(begin: 0.05);
  }

  Widget _buildLegendItem(String label, Color color) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
          width: 8,
          height: 8,
          decoration: BoxDecoration(
            color: color,
            shape: BoxShape.circle,
            boxShadow: [
              BoxShadow(
                color: color.withOpacity(0.4),
                blurRadius: 4,
                spreadRadius: 1,
              ),
            ],
          ),
        ),
        const SizedBox(width: 6),
        Text(
          label,
          style: GoogleFonts.outfit(color: Colors.white60, fontSize: 11),
        ),
      ],
    );
  }

  Map<String, int> _getWeeklyXpValues(Map<String, int> xpHistory) {
    final now = DateTime.now();
    // Monday of the current week (weekday: 1 = Mon, 7 = Sun)
    final monday = now.subtract(Duration(days: now.weekday - 1));

    final Map<String, int> result = {};
    final daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

    for (int i = 0; i < 7; i++) {
      final dateKey = monday.add(Duration(days: i)).toIso8601String().split('T')[0];
      final xp = xpHistory[dateKey] ?? 0;
      result[daysOfWeek[i]] = xp;
    }
    return result;
  }

  Map<String, Map<String, int>> _calculateCategoryStats(List<Map<String, dynamic>> history, String targetType, String timeRange) {
    // Initialize everything to 0/0
    final Map<String, Map<String, int>> stats = {};
    for (var key in CategoryBarChart.subjectMetadata.keys) {
      stats[key] = {'correct': 0, 'total': 0};
    }

    final now = DateTime.now();
    final todayStart = DateTime(now.year, now.month, now.day).millisecondsSinceEpoch;
    final yesterdayStart = todayStart - 86400000;
    final sevenDaysAgo = now.subtract(const Duration(days: 7)).millisecondsSinceEpoch;
    final thirtyDaysAgo = now.subtract(const Duration(days: 30)).millisecondsSinceEpoch;

    // Filter history to matches of targetType and selected timeRange
    final filteredHistory = history.where((item) {
      if ((item['type'] ?? '') != targetType) return false;
      final int timestamp = int.tryParse(item['timestamp']?.toString() ?? '0') ?? 0;
      if (timestamp == 0) return false;

      switch (timeRange) {
        case 'today':
          return timestamp >= todayStart;
        case 'yesterday':
          return timestamp >= yesterdayStart && timestamp < todayStart;
        case 'week':
          return timestamp >= sevenDaysAgo;
        case 'month':
          return timestamp >= thirtyDaysAgo;
        case 'all':
        default:
          return true;
      }
    }).toList();

    for (var item in filteredHistory) {
      final String subjectId = (item['subjectId'] ?? '').toString().toLowerCase();
      final int score = int.tryParse(item['score']?.toString() ?? '0') ?? 0;
      final int total = int.tryParse(item['totalQuestions']?.toString() ?? '0') ?? 0;

      String mappedKey = '';
      if (subjectId == 'geo' || subjectId == 'geography' || subjectId == 'juqraafi') {
        mappedKey = 'geo';
      } else if (subjectId == 'tech' || subjectId == 'technology') {
        mappedKey = 'tech';
      } else if (subjectId == 'his' || subjectId == 'history' || subjectId == 'taariikh') {
        mappedKey = 'his';
      } else if (subjectId == 'bio' || subjectId == 'biology') {
        mappedKey = 'bio';
      } else if (subjectId == 'somali' || subjectId == 'af-somali') {
        mappedKey = 'somali';
      } else if (subjectId == 'eng' || subjectId == 'english') {
        mappedKey = 'eng';
      } else if (subjectId == 'math' || subjectId == 'maths' || subjectId == 'xisaab') {
        mappedKey = 'math';
      } else if (subjectId == 'arabic' || subjectId == 'carabi') {
        mappedKey = 'arabic';
      } else if (subjectId == 'phy' || subjectId == 'physics' || subjectId == 'fiisigis') {
        mappedKey = 'phy';
      } else if (subjectId == 'chem' || subjectId == 'chemistry' || subjectId == 'kimistari') {
        mappedKey = 'chem';
      } else if (subjectId == 'bus' || subjectId == 'business' || subjectId == 'ganacsi') {
        mappedKey = 'bus';
      } else if (subjectId == 'tarbiyo' || subjectId == 'tarbiyada') {
        mappedKey = 'tarbiyo';
      }

      if (mappedKey.isNotEmpty) {
        stats[mappedKey]!['correct'] = stats[mappedKey]!['correct']! + score;
        stats[mappedKey]!['total'] = stats[mappedKey]!['total']! + total;
      }
    }

    return stats;
  }
}

// ─── Progress Tracking Custom Painter & Widgets ─────────────

class WeeklyXpPainter extends CustomPainter {
  final List<int> values;
  final List<String> days;

  WeeklyXpPainter({required this.values, required this.days});

  @override
  void paint(Canvas canvas, Size size) {
    const double paddingLeft = 35.0;
    const double paddingBottom = 25.0;
    const double paddingTop = 10.0;
    const double paddingRight = 10.0;

    final double chartWidth = size.width - paddingLeft - paddingRight;
    final double chartHeight = size.height - paddingTop - paddingBottom;

    final Paint gridPaint = Paint()
      ..color = Colors.white.withOpacity(0.05)
      ..strokeWidth = 1.0;

    final TextPainter textPainter = TextPainter(
      textDirection: TextDirection.ltr,
    );

    // Draw horizontal grid lines and labels
    const int maxVal = 400;
    const int steps = 4; // 0, 100, 200, 300, 400
    for (int i = 0; i <= steps; i++) {
      final double y = paddingTop + chartHeight - (i * chartHeight / steps);
      canvas.drawLine(
        Offset(paddingLeft, y),
        Offset(size.width - paddingRight, y),
        gridPaint,
      );

      final String label = (i * 100).toString();
      textPainter.text = TextSpan(
        text: label,
        style: GoogleFonts.outfit(color: Colors.white38, fontSize: 10),
      );
      textPainter.layout();
      textPainter.paint(
        canvas,
        Offset(paddingLeft - textPainter.width - 8, y - textPainter.height / 2),
      );
    }

    if (values.length < 7) return;

    // Calculate points coordinates
    final List<Offset> points = [];
    final double stepX = chartWidth / 6;
    for (int i = 0; i < 7; i++) {
      final double x = paddingLeft + (i * stepX);
      final double val = values[i].clamp(0, maxVal).toDouble();
      final double y = paddingTop + chartHeight - (val * chartHeight / maxVal);
      points.add(Offset(x, y));
    }

    // Draw area gradient under the curve
    if (points.isNotEmpty) {
      final Path fillPath = Path();
      fillPath.moveTo(points[0].dx, paddingTop + chartHeight);

      // Draw smooth curve using Cubic Beziers
      for (int i = 0; i < points.length - 1; i++) {
        final Offset p0 = points[i];
        final Offset p1 = points[i + 1];
        final double controlX = (p0.dx + p1.dx) / 2;
        fillPath.cubicTo(controlX, p0.dy, controlX, p1.dy, p1.dx, p1.dy);
      }

      fillPath.lineTo(points[points.length - 1].dx, paddingTop + chartHeight);
      fillPath.close();

      final Paint fillPaint = Paint()
        ..shader = LinearGradient(
          colors: [
            Colors.orangeAccent.withOpacity(0.35),
            Colors.purpleAccent.withOpacity(0.08),
            Colors.transparent,
          ],
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
        ).createShader(Rect.fromLTRB(paddingLeft, paddingTop, size.width, size.height - paddingBottom));

      canvas.drawPath(fillPath, fillPaint);
    }

    // Draw the curved line itself
    final Path linePath = Path();
    linePath.moveTo(points[0].dx, points[0].dy);
    for (int i = 0; i < points.length - 1; i++) {
      final Offset p0 = points[i];
      final Offset p1 = points[i + 1];
      final double controlX = (p0.dx + p1.dx) / 2;
      linePath.cubicTo(controlX, p0.dy, controlX, p1.dy, p1.dx, p1.dy);
    }

    final Paint linePaint = Paint()
      ..shader = const LinearGradient(
        colors: [
          Colors.redAccent,
          Colors.orangeAccent,
          Colors.yellowAccent,
          Colors.greenAccent,
          Colors.cyanAccent,
        ],
      ).createShader(Rect.fromPoints(points[0], points[points.length - 1]))
      ..strokeWidth = 3.0
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;

    canvas.drawPath(linePath, linePaint);

    // Draw points/dots and weekday labels
    for (int i = 0; i < 7; i++) {
      final Offset pt = points[i];

      Color dotColor = Colors.greenAccent;
      if (i == 0 || i == 1) {
        dotColor = Colors.redAccent;
      } else if (i == 2) {
        dotColor = Colors.orangeAccent;
      } else if (i == 3) {
        dotColor = Colors.yellowAccent;
      }

      final Paint dotPaint = Paint()
        ..color = dotColor
        ..style = PaintingStyle.fill;

      final Paint shadowPaint = Paint()
        ..color = dotColor.withOpacity(0.4)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 4.0);

      // Draw shadow and dot
      canvas.drawCircle(pt, 6.0, shadowPaint);
      canvas.drawCircle(pt, 4.0, dotPaint);

      // Draw day label
      textPainter.text = TextSpan(
        text: days[i],
        style: GoogleFonts.outfit(color: Colors.white38, fontSize: 10),
      );
      textPainter.layout();
      textPainter.paint(
        canvas,
        Offset(pt.dx - textPainter.width / 2, size.height - paddingBottom + 5),
      );
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}

class CategoryBarChart extends StatelessWidget {
  final Map<String, Map<String, int>> stats;

  const CategoryBarChart({
    super.key,
    required this.stats,
  });

  static const Map<String, Map<String, dynamic>> subjectMetadata = {
    'geo': {'name': 'Juqraafi', 'color': Colors.redAccent},
    'tech': {'name': 'Tech', 'color': Colors.cyanAccent},
    'his': {'name': 'Taariikh', 'color': Colors.purpleAccent},
    'bio': {'name': 'Biology', 'color': Colors.blueAccent},
    'somali': {'name': 'Somali', 'color': Colors.orangeAccent},
    'eng': {'name': 'English', 'color': Colors.pinkAccent},
    'math': {'name': 'Maths', 'color': Colors.tealAccent},
    'arabic': {'name': 'Arabic', 'color': Colors.lightGreenAccent},
    'phy': {'name': 'Physics', 'color': Colors.deepOrangeAccent},
    'chem': {'name': 'Chemistry', 'color': Colors.amberAccent},
    'bus': {'name': 'Business', 'color': Colors.indigoAccent},
    'tarbiyo': {'name': 'Tarbiyo', 'color': Colors.greenAccent},
  };

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 220,
      padding: const EdgeInsets.only(top: 10),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Left vertical labels (100% to 0%)
          Padding(
            padding: const EdgeInsets.only(bottom: 35.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: List.generate(6, (index) {
                final pct = 100 - (index * 20);
                return Text(
                  "$pct%",
                  style: GoogleFonts.outfit(color: Colors.white38, fontSize: 9),
                );
              }),
            ),
          ),
          const SizedBox(width: 10),
          // Horizontal scrollable area for the bars
          Expanded(
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              physics: const BouncingScrollPhysics(),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: subjectMetadata.entries.map((entry) {
                  final key = entry.key;
                  final name = entry.value['name'] as String;
                  final color = entry.value['color'] as Color;

                  final item = stats[key] ?? {'correct': 0, 'total': 0};
                  final int correct = item['correct'] ?? 0;
                  final int total = item['total'] ?? 0;
                  final double percent = total > 0 ? (correct / total) : 0.0;

                  return Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 10),
                    child: _buildBarColumn(name, correct, total, percent, color),
                  );
                }).toList(),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildBarColumn(String label, int correct, int total, double percent, Color barColor) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Expanded(
          child: Container(
            width: 28,
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.05),
              borderRadius: BorderRadius.circular(15),
            ),
            clipBehavior: Clip.antiAlias,
            alignment: Alignment.bottomCenter,
            child: LayoutBuilder(
              builder: (context, constraints) {
                final fillHeight = constraints.maxHeight * percent;
                return AnimatedContainer(
                  duration: const Duration(milliseconds: 800),
                  curve: Curves.easeOutCubic,
                  width: 28,
                  height: fillHeight > 0 ? fillHeight : 0,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [
                        barColor.withOpacity(0.5),
                        barColor,
                      ],
                      begin: Alignment.bottomCenter,
                      end: Alignment.topCenter,
                    ),
                    borderRadius: BorderRadius.circular(15),
                    boxShadow: [
                      BoxShadow(
                        color: barColor.withOpacity(0.4),
                        blurRadius: 8,
                        spreadRadius: 1,
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
        ),
        const SizedBox(height: 10),
        Text(
          "$correct/$total",
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold),
        ),
        Text(
          label,
          style: GoogleFonts.outfit(color: Colors.white38, fontSize: 9),
        ),
      ],
    );
  }
}

class EditProfileScreen extends StatefulWidget {
  const EditProfileScreen({super.key});

  @override
  State<EditProfileScreen> createState() => _EditProfileScreenState();
}

class _EditProfileScreenState extends State<EditProfileScreen> {
  final nameController = TextEditingController(); // Starts empty
  final emailController = TextEditingController(); // Starts empty
  final phoneController = TextEditingController(); // Starts empty
  
  final currentPasswordController = TextEditingController();
  final newPasswordController = TextEditingController();
  final confirmPasswordController = TextEditingController();

  final formKey = GlobalKey<FormState>();
  bool changePassword = false;
  bool obscureCurrent = true;
  bool obscureNew = true;
  bool obscureConfirm = true;
  bool isSaving = false;
  String errorMessage = '';

  @override
  void initState() {
    super.initState();
    nameController.addListener(_updateState);
    emailController.addListener(_updateState);
    phoneController.addListener(_updateState);
  }

  void _updateState() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    nameController.removeListener(_updateState);
    emailController.removeListener(_updateState);
    phoneController.removeListener(_updateState);
    nameController.dispose();
    emailController.dispose();
    phoneController.dispose();
    currentPasswordController.dispose();
    newPasswordController.dispose();
    confirmPasswordController.dispose();
    super.dispose();
  }

  // Verification code recovery flow inside Edit Profile
  void _handleForgotPasswordInsideProfile(String email) async {
    setState(() {
      isSaving = true;
      errorMessage = '';
    });

    try {
      final int randomCodeNum = (DateTime.now().millisecondsSinceEpoch % 900000) + 100000;
      final codeStr = randomCodeNum.toString();

      await AuthService.sendRecoveryCode(email, codeStr);

      if (!mounted) return;
      
      // Show simulated code toast
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            "Simulation Code: $codeStr",
            style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.orangeAccent,
          duration: const Duration(seconds: 10),
        ),
      );

      // Show dialog to enter code
      _showVerifyCodeDialog(email, codeStr);
    } catch (e) {
      setState(() {
        errorMessage = e.toString().replaceAll('Exception: ', '');
      });
    } finally {
      setState(() {
        isSaving = false;
      });
    }
  }

  void _showVerifyCodeDialog(String email, String generatedCode) {
    final codeVerificationController = TextEditingController();
    final verifyFormKey = GlobalKey<FormState>();
    String verifyError = '';

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setDialogState) {
            return AlertDialog(
              backgroundColor: const Color(0xFF1E1B4B),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
                side: const BorderSide(color: Colors.cyanAccent, width: 1),
              ),
              title: Text(
                "Verify Code",
                style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold),
              ),
              content: Form(
                key: verifyFormKey,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "A verification code has been generated. Enter the code below to verify.",
                      style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13),
                    ),
                    const SizedBox(height: 15),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: codeVerificationController,
                        keyboardType: TextInputType.number,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (value == null || value.trim().isEmpty) {
                            return 'Please enter verification code';
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          prefixIcon: const Icon(Icons.security_rounded, color: Colors.white54, size: 22),
                          hintText: "Enter 6-digit Code",
                          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                          border: InputBorder.none,
                          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        ),
                      ),
                    ),
                    if (verifyError.isNotEmpty) ...[
                      const SizedBox(height: 10),
                      Text(
                        verifyError,
                        style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                      ),
                    ],
                  ],
                ),
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: Text("CANCEL", style: GoogleFonts.outfit(color: Colors.white54)),
                ),
                ElevatedButton(
                  onPressed: () {
                    if (!verifyFormKey.currentState!.validate()) return;
                    if (codeVerificationController.text.trim() != generatedCode) {
                      setDialogState(() {
                        verifyError = "Invalid verification code.";
                      });
                      return;
                    }
                    Navigator.pop(context); // close verify dialog
                    _showResetPasswordDialog(email, generatedCode);
                  },
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.cyanAccent),
                  child: Text("VERIFY", style: GoogleFonts.outfit(color: Colors.black, fontWeight: FontWeight.bold)),
                ),
              ],
            );
          },
        );
      },
    );
  }

  void _showResetPasswordDialog(String email, String code) {
    final resetNewPasswordController = TextEditingController();
    final resetConfirmPasswordController = TextEditingController();
    final resetFormKey = GlobalKey<FormState>();
    String resetError = '';
    bool isResetting = false;

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setDialogState) {
            return AlertDialog(
              backgroundColor: const Color(0xFF1E1B4B),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
                side: const BorderSide(color: Colors.cyanAccent, width: 1),
              ),
              title: Text(
                "Reset Password",
                style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold),
              ),
              content: Form(
                key: resetFormKey,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text("New Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 8),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: resetNewPasswordController,
                        obscureText: true,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter a new password';
                          }
                          if (value.length < 6) {
                            return 'Password must be at least 6 characters';
                          }
                          if (!RegExp(r'[a-zA-Z]').hasMatch(value) || !RegExp(r'[0-9]').hasMatch(value)) {
                            return 'Password must contain both letters and numbers';
                          }
                          return null;
                        },
                        decoration: const InputDecoration(
                          prefixIcon: Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                          border: InputBorder.none,
                          contentPadding: EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        ),
                      ),
                    ),
                    const SizedBox(height: 15),
                    Text("Confirm Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 8),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: resetConfirmPasswordController,
                        obscureText: true,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please confirm password';
                          }
                          if (value != resetNewPasswordController.text) {
                            return 'Passwords do not match';
                          }
                          return null;
                        },
                        decoration: const InputDecoration(
                          prefixIcon: Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                          border: InputBorder.none,
                          contentPadding: EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        ),
                      ),
                    ),
                    if (resetError.isNotEmpty) ...[
                      const SizedBox(height: 10),
                      Text(
                        resetError,
                        style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                      ),
                    ],
                  ],
                ),
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: Text("CANCEL", style: GoogleFonts.outfit(color: Colors.white54)),
                ),
                ElevatedButton(
                  onPressed: isResetting ? null : () async {
                    if (!resetFormKey.currentState!.validate()) return;
                    setDialogState(() {
                      isResetting = true;
                      resetError = '';
                    });
                    try {
                      await AuthService.resetPasswordWithCode(
                        email: email,
                        code: code,
                        newPassword: resetNewPasswordController.text,
                      );
                      if (context.mounted) {
                        Navigator.pop(context); // close reset dialog
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text("Password successfully reset!"),
                            backgroundColor: Colors.green,
                          ),
                        );
                      }
                    } catch (e) {
                      setDialogState(() {
                        resetError = e.toString().replaceAll('Exception: ', '');
                      });
                    } finally {
                      setDialogState(() {
                        isResetting = false;
                      });
                    }
                  },
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.cyanAccent),
                  child: isResetting
                      ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.black))
                      : Text("RESET PASSWORD", style: GoogleFonts.outfit(color: Colors.black, fontWeight: FontWeight.bold)),
                ),
              ],
            );
          },
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final user = AuthService.currentUser;
    if (user == null) {
      return const Scaffold(
        body: Center(child: Text("User not logged in")),
      );
    }

    final newEmailVal = emailController.text.trim();
    final newPhoneVal = phoneController.text.trim();
    final isEmailEntered = newEmailVal.isNotEmpty;
    final isPhoneEntered = newPhoneVal.isNotEmpty;
    final showCurrentPassword = changePassword || isEmailEntered || isPhoneEntered;
    
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          onPressed: () => Navigator.pop(context),
          icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
        ),
        title: Text(
          "Edit Profile",
          style: GoogleFonts.outfit(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E1B4B), Color(0xFF312E81)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(25),
            physics: const BouncingScrollPhysics(),
            child: Form(
              key: formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Update your account name, email, phone number, and password below.",
                    style: GoogleFonts.outfit(color: Colors.white60, fontSize: 14),
                  ),
                  const SizedBox(height: 25),

                  // Name Field
                  Text("Name", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 8),
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.06),
                      borderRadius: BorderRadius.circular(15),
                      border: Border.all(color: Colors.white.withOpacity(0.12)),
                    ),
                    child: TextFormField(
                      controller: nameController,
                      style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                      validator: (value) {
                        if (value != null && value.trim().isNotEmpty && value.trim().length < 3) {
                          return 'Name must be at least 3 letters';
                        }
                        return null;
                      },
                      decoration: InputDecoration(
                        prefixIcon: const Icon(Icons.person_outline_rounded, color: Colors.white54, size: 22),
                        hintText: "Enter your full name",
                        hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),

                  // Email Field
                  Text("Email", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 8),
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.06),
                      borderRadius: BorderRadius.circular(15),
                      border: Border.all(color: Colors.white.withOpacity(0.12)),
                    ),
                    child: TextFormField(
                      controller: emailController,
                      keyboardType: TextInputType.emailAddress,
                      style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                      validator: (value) {
                        if (value != null && value.trim().isNotEmpty) {
                          final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
                          if (!emailRegex.hasMatch(value.trim())) {
                            return 'Please enter a valid email address';
                          }
                        }
                        return null;
                      },
                      decoration: InputDecoration(
                        prefixIcon: const Icon(Icons.email_outlined, color: Colors.white54, size: 22),
                        hintText: "Enter new email address",
                        hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),

                  // Phone Field
                  Text("Number", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 8),
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.06),
                      borderRadius: BorderRadius.circular(15),
                      border: Border.all(color: Colors.white.withOpacity(0.12)),
                    ),
                    child: TextFormField(
                      controller: phoneController,
                      keyboardType: TextInputType.phone,
                      style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                      validator: (value) {
                        if (value != null && value.trim().isNotEmpty) {
                          final phoneVal = value.trim();
                          final phoneRegex = RegExp(r'^\+?[0-9]{9,12}$');
                          if (!phoneRegex.hasMatch(phoneVal)) {
                            return 'Number must be between 9 and 12 digits';
                          }
                        }
                        return null;
                      },
                      decoration: InputDecoration(
                        prefixIcon: const Icon(Icons.phone_outlined, color: Colors.white54, size: 22),
                        hintText: "Enter your phone number",
                        hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                        errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),

                  // Change Password Toggle
                  Row(
                    children: [
                      Checkbox(
                        value: changePassword,
                        activeColor: Colors.cyanAccent,
                        checkColor: Colors.black,
                        onChanged: (val) {
                          setState(() {
                            changePassword = val ?? false;
                          });
                        },
                      ),
                      Text(
                        "Change Account Password",
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 14, fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                  
                  if (showCurrentPassword) ...[
                    const SizedBox(height: 15),
                    // Current Password
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text("Current Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                        TextButton(
                          onPressed: () {
                            final targetEmail = emailController.text.trim().isNotEmpty
                                ? emailController.text.trim()
                                : user.email;
                            _handleForgotPasswordInsideProfile(targetEmail);
                          },
                          style: TextButton.styleFrom(padding: EdgeInsets.zero, minimumSize: Size.zero, tapTargetSize: MaterialTapTargetSize.shrinkWrap),
                          child: Text(
                            "Forgot password?",
                            style: GoogleFonts.outfit(color: Colors.cyanAccent, fontSize: 12, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: currentPasswordController,
                        obscureText: obscureCurrent,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (showCurrentPassword && (value == null || value.isEmpty)) {
                            return 'Please enter your current password';
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          prefixIcon: const Icon(Icons.lock_outline_rounded, color: Colors.white54, size: 22),
                          hintText: "Enter current password",
                          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                          suffixIcon: IconButton(
                            icon: Icon(obscureCurrent ? Icons.visibility_off_outlined : Icons.visibility_outlined, color: Colors.white54),
                            onPressed: () => setState(() => obscureCurrent = !obscureCurrent),
                          ),
                          border: InputBorder.none,
                          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                          errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                        ),
                      ),
                    ),
                  ],

                  if (changePassword) ...[
                    const SizedBox(height: 15),
                    // New Password
                    Text("New Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 8),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: newPasswordController,
                        obscureText: obscureNew,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (changePassword) {
                            if (value == null || value.isEmpty) {
                              return 'Please enter a new password';
                            }
                            if (value.length < 6) {
                              return 'Password must be at least 6 characters';
                            }
                            if (!RegExp(r'[a-zA-Z]').hasMatch(value) || !RegExp(r'[0-9]').hasMatch(value)) {
                              return 'Password must contain both letters and numbers';
                            }
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          prefixIcon: const Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                          hintText: "Enter new password",
                          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                          suffixIcon: IconButton(
                            icon: Icon(obscureNew ? Icons.visibility_off_outlined : Icons.visibility_outlined, color: Colors.white54),
                            onPressed: () => setState(() => obscureNew = !obscureNew),
                          ),
                          border: InputBorder.none,
                          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                          errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                        ),
                      ),
                    ),
                    const SizedBox(height: 15),

                    // Confirm New Password
                    Text("Confirm New Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 8),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.06),
                        borderRadius: BorderRadius.circular(15),
                        border: Border.all(color: Colors.white.withOpacity(0.12)),
                      ),
                      child: TextFormField(
                        controller: confirmPasswordController,
                        obscureText: obscureConfirm,
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                        validator: (value) {
                          if (changePassword) {
                            if (value == null || value.isEmpty) {
                              return 'Please confirm your new password';
                            }
                            if (value != newPasswordController.text) {
                              return 'Passwords do not match';
                            }
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          prefixIcon: const Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                          hintText: "Confirm new password",
                          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                          suffixIcon: IconButton(
                            icon: Icon(obscureConfirm ? Icons.visibility_off_outlined : Icons.visibility_outlined, color: Colors.white54),
                            onPressed: () => setState(() => obscureConfirm = !obscureConfirm),
                          ),
                          border: InputBorder.none,
                          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                          errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
                        ),
                      ),
                    ),
                  ],

                  if (errorMessage.isNotEmpty) ...[
                    const SizedBox(height: 15),
                    Row(
                      children: [
                        const Icon(Icons.error_outline_rounded, color: Colors.redAccent, size: 16),
                        const SizedBox(width: 6),
                        Expanded(
                          child: Text(
                            errorMessage,
                            style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 13),
                          ),
                        ),
                      ],
                    ).animate().shake(),
                  ],
                  const SizedBox(height: 30),

                  // Submit Button
                  SizedBox(
                    width: double.infinity,
                    height: 55,
                    child: ElevatedButton(
                      onPressed: isSaving ? null : () async {
                        if (!formKey.currentState!.validate()) return;

                        final newEmailValLocal = emailController.text.trim();
                        final newPhoneValLocal = phoneController.text.trim();
                        final isEmailEnteredLocal = newEmailValLocal.isNotEmpty;
                        final isPhoneEnteredLocal = newPhoneValLocal.isNotEmpty;
                        final showCurrentPasswordLocal = changePassword || isEmailEnteredLocal || isPhoneEnteredLocal;

                        if (showCurrentPasswordLocal) {
                          // Validate current password
                          if (currentPasswordController.text != user.password) {
                            setState(() {
                              errorMessage = "Incorrect current password.";
                            });
                            return;
                          }
                        }

                        setState(() {
                          isSaving = true;
                          errorMessage = '';
                        });

                        try {
                          await AuthService.updateUserProfile(
                            fullName: nameController.text.trim().isNotEmpty ? nameController.text.trim() : user.fullName,
                            newPhoneNumber: phoneController.text.trim().isNotEmpty ? phoneController.text.trim() : null,
                            newEmail: emailController.text.trim().isNotEmpty ? emailController.text.trim() : null,
                            newPassword: changePassword ? newPasswordController.text : null,
                          );

                          if (mounted) {
                            Navigator.pop(context); // Go back
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                content: Row(
                                  children: [
                                    const Icon(Icons.check_circle_rounded, color: Colors.greenAccent),
                                    const SizedBox(width: 10),
                                    Text(
                                      "Profile updated successfully!",
                                      style: GoogleFonts.outfit(color: Colors.white),
                                    ),
                                  ],
                                ),
                                backgroundColor: const Color(0xFF1E1B4B),
                                behavior: SnackBarBehavior.floating,
                              ),
                            );
                          }
                        } catch (e) {
                          setState(() {
                            errorMessage = e.toString().replaceAll("Exception: ", "");
                          });
                        } finally {
                          setState(() {
                            isSaving = false;
                          });
                        }
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.cyanAccent,
                        foregroundColor: Colors.black,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15),
                        ),
                      ),
                      child: isSaving
                          ? const SizedBox(
                              width: 24,
                              height: 24,
                              child: CircularProgressIndicator(color: Colors.black, strokeWidth: 2),
                            )
                          : Text(
                              "SAVE CHANGES",
                              style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 15),
                            ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
