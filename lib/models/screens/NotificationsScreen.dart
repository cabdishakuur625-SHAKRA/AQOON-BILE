import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import 'ProfilePreviewScreen.dart';
import 'CompetitionLobbyScreen.dart';
import 'ChatScreen.dart';

class NotificationsScreen extends StatefulWidget {
  const NotificationsScreen({super.key});

  @override
  State<NotificationsScreen> createState() => _NotificationsScreenState();
}

class _NotificationsScreenState extends State<NotificationsScreen> {
  final FirebaseService _firebaseService = FirebaseService();

  String _getSectionHeader(int timestamp) {
    final date = DateTime.fromMillisecondsSinceEpoch(timestamp);
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final yesterday = today.subtract(const Duration(days: 1));
    final checkDate = DateTime(date.year, date.month, date.day);

    if (checkDate == today) {
      return "Today";
    } else if (checkDate == yesterday) {
      return "Yesterday";
    } else {
      return "Older";
    }
  }

  String _formatTime(int timestamp) {
    final date = DateTime.fromMillisecondsSinceEpoch(timestamp);
    final hour = date.hour > 12 ? date.hour - 12 : (date.hour == 0 ? 12 : date.hour);
    final min = date.minute.toString().padLeft(2, '0');
    final period = date.hour >= 12 ? "PM" : "AM";
    return "$hour:$min $period";
  }

  Future<void> _handleNotificationTap(Map<String, dynamic> notif) async {
    final String notifId = notif['id'] ?? '';
    final String type = notif['type'] ?? '';
    final String senderEmail = notif['senderEmail'] ?? '';
    final String senderName = notif['senderName'] ?? '';
    final String compId = notif['competitionId'] ?? '';

    // Mark as read in database
    if (notifId.isNotEmpty) {
      await _firebaseService.markNotificationRead(notifId);
    }

    if (!mounted) return;

    // Redirections based on notification type
    if (type == 'friend_request' || type == 'friend_accepted' || type == 'friend_rejected') {
      if (senderEmail.isNotEmpty) {
        _navigateToProfile(senderEmail, senderName);
      }
    } else if (type == 'competition_invite') {
      if (compId.isNotEmpty) {
        // Show loading indicator
        showDialog(
          context: context,
          barrierDismissible: false,
          builder: (c) => const Center(child: CircularProgressIndicator(color: Colors.cyanAccent)),
        );
        try {
          final compData = await _firebaseService.streamCompetition(compId).first;
          if (mounted) Navigator.pop(context); // Close loading indicator
          if (compData == null) {
            if (mounted) {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text("Competition not found."), backgroundColor: Colors.redAccent),
              );
            }
            return;
          }

          final String status = compData['status'] ?? '';
          final bool quizStarted = compData['quizStarted'] ?? false;
          final int createdAt = compData['createdAt'] ?? 0;
          final String creatorEmail = compData['creatorEmail'] ?? '';
          final String currentUserEmail = AuthService.currentUser?.email ?? '';
          final String currentUserSanitized = AuthService.sanitizeEmail(currentUserEmail);

          bool isExpired = status == 'expired';
          if (!isExpired && !quizStarted && createdAt > 0) {
            final int now = DateTime.now().millisecondsSinceEpoch;
            if (now - createdAt > 120000) {
              final scores = compData['scores'] as Map<dynamic, dynamic>? ?? {};
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
                await _firebaseService.markCompetitionExpired(compId);
              }
            }
          }

          if (!mounted) return;

          if (isExpired) {
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text("This competition lobby has expired."), backgroundColor: Colors.orangeAccent),
            );
            return;
          }

          final scores = compData['scores'] as Map<dynamic, dynamic>? ?? {};
          final myScoreData = scores[currentUserSanitized] as Map<dynamic, dynamic>?;
          final String myStatus = myScoreData?['status'] ?? 'waiting';
          final bool isCreator = creatorEmail.toLowerCase() == currentUserEmail.toLowerCase();

          if (quizStarted) {
            if (myStatus == 'ready' || isCreator) {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => CompetitionLobbyScreen(competitionId: compId),
                ),
              );
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text("This competition has already started."), backgroundColor: Colors.orangeAccent),
              );
            }
            return;
          }

          if (isCreator || myStatus == 'ready') {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => CompetitionLobbyScreen(competitionId: compId),
              ),
            );
          } else if (myStatus == 'waiting' || myStatus == 'declined') {
            _showInviteDialog(compData);
          } else {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text("You have already completed this competition."), backgroundColor: Colors.orangeAccent),
            );
          }
        } catch (e) {
          if (mounted) Navigator.pop(context);
          debugPrint("Error handling competition invite tap: $e");
        }
      }
    } else if (type == 'competition_started') {
      if (compId.isNotEmpty) {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => CompetitionLobbyScreen(competitionId: compId),
          ),
        );
      }
    } else if (type == 'new_message') {
      if (senderEmail.isNotEmpty) {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ChatScreen(
              userName: senderName,
              userEmail: senderEmail,
              avatarUrl: 'https://i.pravatar.cc/150?u=${AuthService.sanitizeEmail(senderEmail)}',
            ),
          ),
        );
      }
    }
  }

  Future<void> _navigateToProfile(String email, String defaultName) async {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (c) => const Center(child: CircularProgressIndicator(color: Colors.cyanAccent)),
    );

    try {
      final sanitized = AuthService.sanitizeEmail(email);
      final data = await AuthService.getUserDataByKey(sanitized);
      if (mounted) {
        Navigator.pop(context); // Close loading indicator
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ProfilePreviewScreen(
              name: data?['fullName'] ?? defaultName,
              email: email,
              phone: data?['phoneNumber'],
              coins: data?['coins'],
              xp: data?['xp'],
            ),
          ),
        );
      }
    } catch (e) {
      if (mounted) Navigator.pop(context);
      debugPrint("Error loading profile: $e");
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
                          await _firebaseService.declineCompetition(compId);
                          if (mounted) {
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(content: Text("Invitation declined"), backgroundColor: Colors.redAccent),
                            );
                          }
                        },
                        style: TextButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 14),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15),
                            side: BorderSide(color: Colors.white.withOpacity(0.15)),
                          ),
                        ),
                        child: Text(
                          "Decline",
                          style: GoogleFonts.outfit(color: Colors.white70, fontWeight: FontWeight.bold),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: ElevatedButton(
                        onPressed: () async {
                          Navigator.pop(context);
                          await _firebaseService.setParticipantReady(compId, ready: false);
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

  Future<void> _markAllRead() async {
    try {
      await _firebaseService.markAllNotificationsRead();
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text("All notifications marked as read!"),
            backgroundColor: Colors.green,
          ),
        );
      }
    } catch (e) {
      debugPrint("Error marking all read: $e");
    }
  }

  IconData _getIconData(String type) {
    switch (type) {
      case 'friend_request':
      case 'friend_accepted':
      case 'friend_rejected':
        return Icons.notifications_rounded;
      case 'competition_invite':
        return Icons.star_rounded;
      case 'competition_started':
        return Icons.play_circle_filled_rounded;
      case 'competition_declined':
        return Icons.cancel_rounded;
      case 'level_up':
        return Icons.emoji_events_rounded;
      case 'badge_earned':
        return Icons.workspace_premium_rounded;
      case 'streak_lost':
      case 'streak_start':
        return Icons.local_fire_department_rounded;
      case 'new_message':
        return Icons.chat_bubble_rounded;
      default:
        return Icons.info_rounded;
    }
  }

  Color _getIconColor(String type) {
    switch (type) {
      case 'friend_request':
      case 'friend_accepted':
      case 'friend_rejected':
        return Colors.blueAccent;
      case 'competition_invite':
        return Colors.amberAccent;
      case 'competition_started':
        return Colors.greenAccent;
      case 'competition_declined':
        return Colors.redAccent;
      case 'level_up':
        return Colors.cyanAccent;
      case 'badge_earned':
        return Colors.orangeAccent;
      case 'streak_lost':
        return Colors.redAccent;
      case 'streak_start':
        return Colors.orangeAccent;
      case 'new_message':
        return Colors.greenAccent;
      default:
        return Colors.tealAccent;
    }
  }

  @override
  Widget build(BuildContext context) {
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
              _buildAppBar(),
              Expanded(
                child: StreamBuilder<List<Map<String, dynamic>>>(
                  stream: _firebaseService.streamNotifications(
                    AuthService.sanitizeEmail(AuthService.currentUser?.email ?? ''),
                  ),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return const Center(child: CircularProgressIndicator(color: Colors.cyanAccent));
                    }

                    final list = snapshot.data ?? [];
                    if (list.isEmpty) {
                      return Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              Icons.notifications_off_outlined,
                              size: 72,
                              color: Colors.white.withOpacity(0.15),
                            ),
                            const SizedBox(height: 16),
                            Text(
                              "No notifications yet",
                              style: GoogleFonts.outfit(color: Colors.white38, fontSize: 16),
                            ),
                          ],
                        ),
                      );
                    }

                    // Group notifications by section (Today, Yesterday, Older)
                    final Map<String, List<Map<String, dynamic>>> grouped = {
                      "Today": [],
                      "Yesterday": [],
                      "Older": [],
                    };

                    for (var notif in list) {
                      final int timestamp = notif['timestamp'] ?? 0;
                      final header = _getSectionHeader(timestamp);
                      grouped[header]?.add(notif);
                    }

                    final List<Widget> listItems = [];
                    grouped.forEach((sectionTitle, sectionList) {
                      if (sectionList.isNotEmpty) {
                        listItems.add(
                          Padding(
                            padding: const EdgeInsets.only(left: 20, top: 20, bottom: 10),
                            child: Text(
                              sectionTitle,
                              style: GoogleFonts.outfit(
                                color: Colors.white60,
                                fontSize: 15,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        );

                        for (var i = 0; i < sectionList.length; i++) {
                          listItems.add(_buildNotificationCard(sectionList[i], i));
                        }
                      }
                    });

                    return ListView(
                      physics: const BouncingScrollPhysics(),
                      children: listItems,
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildAppBar() {
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
            "Notifications",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          IconButton(
            onPressed: _markAllRead,
            icon: const Icon(Icons.check_circle_outline_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
        ],
      ),
    ).animate().slideY(begin: -1, duration: 600.ms);
  }

  Widget _buildNotificationCard(Map<String, dynamic> notif, int index) {
    final String title = notif['title'] ?? 'Alert';
    final String message = notif['message'] ?? '';
    final int timestamp = notif['timestamp'] ?? 0;
    final String type = notif['type'] ?? 'system';
    final bool isRead = notif['isRead'] ?? false;

    final IconData icon = _getIconData(type);
    final Color iconColor = _getIconColor(type);

    return GestureDetector(
      onTap: () => _handleNotificationTap(notif),
      child: Container(
        margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isRead ? Colors.transparent : Colors.cyanAccent.withOpacity(0.2),
            width: isRead ? 1.0 : 1.5,
          ),
        ),
        child: Row(
          children: [
            // Left Status Icon
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: iconColor.withOpacity(0.1),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: iconColor, size: 24),
            ),
            const SizedBox(width: 16),

            // Center details
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: GoogleFonts.outfit(
                      color: Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    message,
                    style: GoogleFonts.outfit(
                      color: Colors.white70,
                      fontSize: 13,
                      height: 1.3,
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    _formatTime(timestamp),
                    style: GoogleFonts.outfit(
                      color: Colors.white38,
                      fontSize: 11,
                    ),
                  ),
                ],
              ),
            ),

            // Right unread indicator
            if (!isRead)
              Padding(
                padding: const EdgeInsets.only(left: 8.0),
                child: Container(
                  width: 8,
                  height: 8,
                  decoration: const BoxDecoration(
                    color: Colors.greenAccent,
                    shape: BoxShape.circle,
                  ),
                ),
              ),
          ],
        ),
      ),
    ).animate().fadeIn(delay: (index * 50).ms, duration: 400.ms).slideY(begin: 0.1);
  }
}
