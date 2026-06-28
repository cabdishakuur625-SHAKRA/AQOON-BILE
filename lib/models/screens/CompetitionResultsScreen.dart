import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:confetti/confetti.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import '../../services/auth_service.dart';
import 'HomeScreen.dart';

class CompetitionResultsScreen extends StatefulWidget {
  final String competitionId;
  final String competitionTitle;
  final String subjectName;
  final int totalQuestions;
  
  // Optional parameters when navigated directly after completing a quiz
  final int? correctAnswers;
  final int? oldXp;
  final int? newXp;
  final int? xpEarned;

  const CompetitionResultsScreen({
    super.key,
    required this.competitionId,
    required this.competitionTitle,
    required this.subjectName,
    required this.totalQuestions,
    this.correctAnswers,
    this.oldXp,
    this.newXp,
    this.xpEarned,
  });

  @override
  State<CompetitionResultsScreen> createState() => _CompetitionResultsScreenState();
}

class _CompetitionResultsScreenState extends State<CompetitionResultsScreen> {
  late ConfettiController _confettiController;
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  @override
  void initState() {
    super.initState();
    _confettiController = ConfettiController(duration: const Duration(seconds: 4));
    
    // Play confetti if they just finished and scored some questions
    if (widget.correctAnswers != null && widget.correctAnswers! > 0) {
      _confettiController.play();
    }
  }

  @override
  void dispose() {
    _confettiController.dispose();
    super.dispose();
  }

  String _formatTimeTaken(int? seconds) {
    if (seconds == null || seconds <= 0) return "0:00";
    final int mins = seconds ~/ 60;
    final int secs = seconds % 60;
    return "$mins:${secs.toString().padLeft(2, '0')}";
  }

  void _showMyResultsBottomSheet() {
    final int score = widget.correctAnswers ?? 0;
    final int total = widget.totalQuestions;
    final double percentage = total > 0 ? (score / total) * 100 : 0.0;
    final int xp = widget.xpEarned ?? 0;
    final int wrong = total - score;

    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return Container(
          decoration: const BoxDecoration(
            color: Color(0xFF1E1B4B),
            borderRadius: BorderRadius.vertical(top: Radius.circular(30)),
            gradient: LinearGradient(
              colors: [Color(0xFF2E1065), Color(0xFF1E1B4B)],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
            ),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 30),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                width: 50,
                height: 5,
                decoration: BoxDecoration(
                  color: Colors.white24,
                  borderRadius: BorderRadius.circular(10),
                ),
              ),
              const SizedBox(height: 20),
              Text(
                "My Performance Details",
                style: GoogleFonts.outfit(
                  color: Colors.white,
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 30),
              Stack(
                alignment: Alignment.center,
                children: [
                  SizedBox(
                    width: 120,
                    height: 120,
                    child: CircularProgressIndicator(
                      value: percentage / 100,
                      strokeWidth: 8,
                      backgroundColor: Colors.white10,
                      valueColor: const AlwaysStoppedAnimation<Color>(Colors.cyanAccent),
                    ),
                  ),
                  Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        "${percentage.toInt()}%",
                        style: GoogleFonts.outfit(
                          color: Colors.white,
                          fontSize: 28,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        "Accuracy",
                        style: GoogleFonts.outfit(color: Colors.white60, fontSize: 11),
                      ),
                    ],
                  ),
                ],
              ),
              const SizedBox(height: 30),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _buildStatItem("Correct", score.toString(), Colors.greenAccent, Icons.check_circle_rounded),
                  _buildStatItem("Wrong", wrong.toString(), Colors.redAccent, Icons.cancel_rounded),
                  _buildStatItem("XP", "+$xp", Colors.amberAccent, Icons.stars_rounded),
                ],
              ),
              const SizedBox(height: 35),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: () => Navigator.pop(context),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.cyanAccent,
                    foregroundColor: Colors.black,
                    padding: const EdgeInsets.symmetric(vertical: 18),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                  ),
                  child: Text(
                    "Close",
                    style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 16),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildStatItem(String label, String value, Color color, IconData icon) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            shape: BoxShape.circle,
          ),
          child: Icon(icon, color: color, size: 22),
        ),
        const SizedBox(height: 8),
        Text(
          value,
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
        ),
        Text(
          label,
          style: GoogleFonts.outfit(color: Colors.white38, fontSize: 11),
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF3B1E87), Color(0xFF1E1B4B)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Stack(
            children: [
              Column(
                children: [
                  const SizedBox(height: 25),
                  _buildLeaderboardHeader(),
                  const SizedBox(height: 10),
                  Text(
                    "See how you ranked against other participants!",
                    style: GoogleFonts.outfit(
                      color: Colors.white70,
                      fontSize: 14,
                    ),
                  ).animate().fadeIn(delay: 200.ms),
                  const SizedBox(height: 25),
                  Expanded(
                    child: _buildLeaderboardStream(),
                  ),
                  _buildBottomControls(context),
                  const SizedBox(height: 20),
                ],
              ),
              Align(
                alignment: Alignment.topCenter,
                child: ConfettiWidget(
                  confettiController: _confettiController,
                  blastDirectionality: BlastDirectionality.explosive,
                  shouldLoop: false,
                  numberOfParticles: 45,
                  colors: const [
                    Colors.cyanAccent,
                    Colors.purpleAccent,
                    Colors.amberAccent,
                    Colors.greenAccent,
                    Colors.redAccent,
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildLeaderboardHeader() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 12),
      decoration: BoxDecoration(
        color: const Color(0xFFDBEAFE),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.2), width: 1.5),
      ),
      child: Text(
        "Leaderboard",
        style: GoogleFonts.outfit(
          color: const Color(0xFF1E3A8A),
          fontSize: 24,
          fontWeight: FontWeight.bold,
        ),
      ),
    ).animate().scale(duration: 600.ms, curve: Curves.easeOutBack);
  }

  Widget _buildLeaderboardStream() {
    return StreamBuilder<DatabaseEvent>(
      stream: _dbRef.child('Competitions/${widget.competitionId}/scores').onValue,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Center(child: CircularProgressIndicator(color: Colors.cyanAccent));
        }

        if (snapshot.hasError) {
          return Center(
            child: Text(
              "Error loading standings: ${snapshot.error}",
              style: const TextStyle(color: Colors.redAccent),
            ),
          );
        }

        final snapshotVal = snapshot.data?.snapshot.value;
        if (snapshotVal == null) {
          return Center(
            child: Text(
              "No scores submitted yet.",
              style: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
            ),
          );
        }

        final Map<dynamic, dynamic> scoresMap = snapshotVal as Map<dynamic, dynamic>;
        final List<LeaderboardPlayer> players = [];

        scoresMap.forEach((key, val) {
          final pMap = val as Map<dynamic, dynamic>;
          players.add(LeaderboardPlayer(
            name: pMap['fullName'] ?? 'Participant',
            email: pMap['email'] ?? '',
            score: pMap['score'] ?? 0,
            completed: pMap['completed'] ?? false,
            timeTaken: pMap['timeTaken'] as int?,
          ));
        });

        // Sorting: completed players first.
        // Ranked by higher score accuracy, then lower time taken.
        players.sort((a, b) {
          if (a.completed && !b.completed) return -1;
          if (!a.completed && b.completed) return 1;
          if (!a.completed && !b.completed) return a.name.compareTo(b.name);

          // Both completed: compare score accuracy
          final scoreCompare = b.score.compareTo(a.score);
          if (scoreCompare != 0) return scoreCompare;

          // Same score: compare time taken (lower is better)
          final timeA = a.timeTaken ?? 999999;
          final timeB = b.timeTaken ?? 999999;
          return timeA.compareTo(timeB);
        });

        return ListView.builder(
          physics: const BouncingScrollPhysics(),
          padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 10),
          itemCount: players.length,
          itemBuilder: (context, index) {
            final player = players[index];
            final bool isMe = player.email.toLowerCase() == (AuthService.currentUser?.email ?? '').toLowerCase();
            
            // Format time taken
            final String formattedTime = _formatTimeTaken(player.timeTaken);
            // Calculate accuracy percentage
            final int accuracy = widget.totalQuestions > 0 
                ? ((player.score / widget.totalQuestions) * 100).round() 
                : 0;

            // Mockup Colors: white card for others, light blue card for "You"
            final Color cardColor = isMe ? const Color(0xFFEFF6FF) : Colors.white;
            final Color textColor = isMe ? const Color(0xFF1E3A8A) : Colors.black87;

            // Rank medal widgets
            Widget medalWidget;
            if (index == 0 && player.completed) {
              medalWidget = _buildMedalBadge(Colors.amber, "1");
            } else if (index == 1 && player.completed) {
              medalWidget = _buildMedalBadge(Colors.grey.shade400, "2");
            } else if (index == 2 && player.completed) {
              medalWidget = _buildMedalBadge(Colors.brown.shade400, "3");
            } else {
              medalWidget = Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  color: Colors.white12,
                  shape: BoxShape.circle,
                  border: Border.all(color: Colors.white30),
                ),
                child: Center(
                  child: Text(
                    "${index + 1}",
                    style: GoogleFonts.outfit(color: Colors.white70, fontWeight: FontWeight.bold, fontSize: 13),
                  ),
                ),
              );
            }

            return Container(
              margin: const EdgeInsets.only(bottom: 15),
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: cardColor,
                borderRadius: BorderRadius.circular(20),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.1),
                    blurRadius: 8,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Row(
                children: [
                  medalWidget,
                  const SizedBox(width: 18),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          isMe ? "${player.name} (You)" : player.name,
                          style: GoogleFonts.outfit(
                            color: textColor,
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        const SizedBox(height: 8),
                        Row(
                          children: [
                            // Time taken pill
                            _buildInfoPill(
                              Icons.access_time_rounded,
                              formattedTime,
                              isMe,
                            ),
                            const SizedBox(width: 10),
                            // Accuracy pill
                            _buildInfoPill(
                              Icons.percent,
                              "$accuracy %",
                              isMe,
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ).animate().fadeIn(delay: (300 + index * 100).ms).slideY(begin: 0.08);
          },
        );
      },
    );
  }

  Widget _buildMedalBadge(Color color, String rank) {
    return Container(
      width: 36,
      height: 36,
      decoration: BoxDecoration(
        color: color.withOpacity(0.2),
        shape: BoxShape.circle,
        border: Border.all(color: color, width: 2),
      ),
      child: Stack(
        alignment: Alignment.center,
        children: [
          Icon(Icons.workspace_premium, color: color, size: 20),
          Positioned(
            bottom: 2,
            child: Text(
              rank,
              style: GoogleFonts.outfit(
                color: color,
                fontWeight: FontWeight.w900,
                fontSize: 10,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInfoPill(IconData icon, String text, bool isMe) {
    final Color pillBg = isMe ? const Color(0xFFDBEAFE) : Colors.black.withOpacity(0.04);
    final Color iconColor = isMe ? const Color(0xFF2563EB) : Colors.black45;
    final Color textColor = isMe ? const Color(0xFF1E3A8A) : Colors.black54;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      decoration: BoxDecoration(
        color: pillBg,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 12, color: iconColor),
          const SizedBox(width: 5),
          Text(
            text,
            style: GoogleFonts.outfit(
              color: textColor,
              fontSize: 11,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildBottomControls(BuildContext context) {
    final bool hasResultsData = widget.correctAnswers != null;

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25.0, vertical: 10),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: () {
                Navigator.of(context).pushAndRemoveUntil(
                  MaterialPageRoute(builder: (context) => const HomeScreen()),
                  (route) => false,
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF0EA5E9),
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 18),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                elevation: 6,
              ),
              child: Text(
                "Back to Home",
                style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 16),
              ),
            ),
          ).animate().fadeIn(delay: 600.ms).slideY(begin: 0.1),
          if (hasResultsData) ...[
            const SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton(
                onPressed: _showMyResultsBottomSheet,
                style: OutlinedButton.styleFrom(
                  foregroundColor: Colors.white,
                  side: const BorderSide(color: Colors.white30, width: 1.5),
                  padding: const EdgeInsets.symmetric(vertical: 18),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                ),
                child: Text(
                  "View My Results",
                  style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 16),
                ),
              ),
            ).animate().fadeIn(delay: 700.ms).slideY(begin: 0.1),
          ],
        ],
      ),
    );
  }
}

class LeaderboardPlayer {
  final String name;
  final String email;
  final int score;
  final bool completed;
  final int? timeTaken;

  LeaderboardPlayer({
    required this.name,
    required this.email,
    required this.score,
    required this.completed,
    this.timeTaken,
  });
}
