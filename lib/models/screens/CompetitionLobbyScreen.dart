import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import '../question.dart';
import 'CompetitionQuizScreen.dart';

class CompetitionLobbyScreen extends StatefulWidget {
  final String competitionId;

  const CompetitionLobbyScreen({
    super.key,
    required this.competitionId,
  });

  @override
  State<CompetitionLobbyScreen> createState() => _CompetitionLobbyScreenState();
}

class _CompetitionLobbyScreenState extends State<CompetitionLobbyScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  final String _currentUserEmail = AuthService.currentUser?.email ?? '';
  final String _currentUserSanitized = AuthService.sanitizeEmail(AuthService.currentUser?.email ?? '');

  StreamSubscription<Map<String, dynamic>?>? _compSubscription;
  Map<String, dynamic>? _compData;
  bool _isLoading = true;

  Timer? _countdownTimer;
  int _secondsRemaining = 120; // 2 minutes lobby limit

  @override
  void initState() {
    super.initState();
    _startLobbyListener();
    _startLocalTimer();
  }

  @override
  void dispose() {
    _compSubscription?.cancel();
    _countdownTimer?.cancel();
    super.dispose();
  }

  void _startLobbyListener() {
    _compSubscription = _firebaseService.streamCompetition(widget.competitionId).listen((comp) {
      if (!mounted) return;

      if (comp == null) {
        setState(() => _isLoading = false);
        return;
      }

      final String status = comp['status'] ?? '';
      if (status == 'expired') {
        _compSubscription?.cancel();
        _compSubscription = null;
        _countdownTimer?.cancel();
        if (mounted) {
          showDialog(
            context: context,
            barrierDismissible: false,
            builder: (context) => AlertDialog(
              backgroundColor: const Color(0xFF312E81),
              title: Text("Lobby Expired", style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold)),
              content: Text(
                "This competition lobby has expired because no invited participants joined in time.",
                style: GoogleFonts.outfit(color: Colors.white70),
              ),
              actions: [
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.cyanAccent,
                    foregroundColor: Colors.black,
                  ),
                  onPressed: () {
                    Navigator.pop(context); // Close dialog
                    Navigator.pop(context); // Exit lobby
                  },
                  child: const Text("OK"),
                ),
              ],
            ),
          );
        }
        return;
      }

      setState(() {
        _compData = comp;
        _isLoading = false;
        
        // Sync the countdown timer using the server-side lobbyTimerStart timestamp
        final int? timerStart = comp['lobbyTimerStart'] as int?;
        if (timerStart != null) {
          final int now = DateTime.now().millisecondsSinceEpoch;
          final int elapsedSeconds = (now - timerStart) ~/ 1000;
          final int remaining = 120 - elapsedSeconds;
          _secondsRemaining = remaining > 0 ? remaining : 0;
        }
      });

      // Auto start the quiz if quizStarted is set to true by the creator
      final bool quizStarted = comp['quizStarted'] ?? false;
      if (quizStarted) {
        _navigateToQuiz();
      }
    });
  }

  void _startLocalTimer() {
    _countdownTimer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_secondsRemaining > 0) {
        setState(() {
          _secondsRemaining--;
        });
      } else {
        _countdownTimer?.cancel();
        _checkLobbyExpiration();
      }
    });
  }

  void _checkLobbyExpiration() {
    if (_compData == null) return;
    final String creatorEmail = _compData!['creatorEmail'] ?? '';
    final bool isCreator = creatorEmail.toLowerCase() == _currentUserEmail.toLowerCase();

    if (isCreator) {
      // Check if any friend joined/ready
      final Map<dynamic, dynamic> scores = _compData!['scores'] as Map<dynamic, dynamic>? ?? {};
      bool hasAnyFriendAccepted = false;
      scores.forEach((key, val) {
        final pMap = val as Map<dynamic, dynamic>;
        final String email = pMap['email'] ?? '';
        final String status = pMap['status'] ?? 'waiting';
        if (email.toLowerCase() != creatorEmail.toLowerCase() && (status == 'ready' || status == 'completed')) {
          hasAnyFriendAccepted = true;
        }
      });

      if (!hasAnyFriendAccepted) {
        // Mark as expired in firebase
        _firebaseService.markCompetitionExpired(widget.competitionId);
      }
    }
  }

  void _navigateToQuiz() {
    if (!mounted || _compData == null) return;

    // Stop listening to avoid double triggers
    _compSubscription?.cancel();
    _compSubscription = null;
    _countdownTimer?.cancel();

    final String title = _compData!['title'] ?? 'Competition';
    final String subjectName = _compData!['subjectName'] ?? 'General';
    final int duration = _compData!['duration'] ?? 15;
    final List<dynamic> rawQuestions = _compData!['questions'] ?? [];

    final List<Question> questions = rawQuestions.asMap().entries.map((entry) {
      return Question.fromMap(entry.key.toString(), entry.value as Map);
    }).toList();

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => CompetitionQuizScreen(
          competitionId: widget.competitionId,
          competitionTitle: title,
          questions: questions,
          durationMinutes: duration,
          subjectName: subjectName,
        ),
      ),
    );
  }

  Future<void> _toggleReady(bool currentReady) async {
    try {
      final newReady = !currentReady;
      await _firebaseService.setParticipantReady(widget.competitionId, ready: newReady);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(newReady ? "You are marked as ready!" : "You are marked as not ready."),
            backgroundColor: newReady ? Colors.green : Colors.orange,
          ),
        );
      }
    } catch (e) {
      debugPrint("Error toggling ready status: $e");
    }
  }

  Future<void> _startQuiz() async {
    try {
      await _firebaseService.startCompetitionQuiz(widget.competitionId);
    } catch (e) {
      debugPrint("Error starting quiz: $e");
    }
  }

  String _formatTimer(int seconds) {
    final int mins = seconds ~/ 60;
    final int secs = seconds % 60;
    return "${mins.toString().padLeft(2, '0')}:${secs.toString().padLeft(2, '0')}";
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        backgroundColor: Color(0xFF1E1B4B),
        body: Center(child: CircularProgressIndicator(color: Colors.cyanAccent)),
      );
    }

    if (_compData == null) {
      return Scaffold(
        backgroundColor: const Color(0xFF1E1B4B),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Competition not found.", style: GoogleFonts.outfit(color: Colors.white70)),
              const SizedBox(height: 20),
              ElevatedButton(onPressed: () => Navigator.pop(context), child: const Text("Go Back")),
            ],
          ),
        ),
      );
    }

    final String creatorEmail = _compData!['creatorEmail'] ?? '';
    final Map<dynamic, dynamic> scores = _compData!['scores'] as Map<dynamic, dynamic>? ?? {};

    final bool isCreator = creatorEmail.toLowerCase() == _currentUserEmail.toLowerCase();

    // Check my ready status
    final myScoreData = scores[_currentUserSanitized] as Map<dynamic, dynamic>?;
    final String myStatus = myScoreData?['status'] ?? 'waiting';
    final bool isIReady = myStatus == 'ready' || myStatus == 'creator';

    // Check if at least one friend is ready
    bool isAnyFriendReady = false;
    scores.forEach((key, val) {
      final pMap = val as Map<dynamic, dynamic>;
      final String email = pMap['email'] ?? '';
      final String status = pMap['status'] ?? 'waiting';
      if (email.toLowerCase() != creatorEmail.toLowerCase() && status == 'ready') {
        isAnyFriendReady = true;
      }
    });

    // Extract player list to render in order (Creator first, then Ready, then Waiting)
    final List<LobbyPlayer> players = [];
    scores.forEach((key, val) {
      final pMap = val as Map<dynamic, dynamic>;
      players.add(LobbyPlayer(
        name: pMap['fullName'] ?? 'Participant',
        email: pMap['email'] ?? '',
        status: pMap['status'] ?? 'waiting',
      ));
    });

    players.sort((a, b) {
      if (a.status == 'creator') return -1;
      if (b.status == 'creator') return 1;
      if (a.status == 'ready' && b.status == 'waiting') return -1;
      if (a.status == 'waiting' && b.status == 'ready') return 1;
      return a.name.compareTo(b.name);
    });

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
          child: Column(
            children: [
              _buildAppBar(context),
              Expanded(
                child: SingleChildScrollView(
                  physics: const BouncingScrollPhysics(),
                  padding: const EdgeInsets.symmetric(horizontal: 25.0),
                  child: Column(
                    children: [
                      const SizedBox(height: 10),
                      // Mockup Icon
                      const Icon(
                        Icons.people_rounded,
                        size: 90,
                        color: Colors.white,
                      ).animate().scale(duration: 600.ms, curve: Curves.easeOutBack),
                      const SizedBox(height: 15),
                      Text(
                        "Waiting for Friends",
                        style: GoogleFonts.outfit(
                          color: Colors.white,
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ).animate().fadeIn(delay: 200.ms),
                      const SizedBox(height: 8),
                      Text(
                        "Your competition invitation has been sent",
                        style: GoogleFonts.outfit(
                          color: Colors.white70,
                          fontSize: 13,
                        ),
                      ).animate().fadeIn(delay: 300.ms),
                      const SizedBox(height: 25),
                      // Countdown timer pill
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 10),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.08),
                          borderRadius: BorderRadius.circular(25),
                          border: Border.all(color: Colors.white.withOpacity(0.15), width: 1.5),
                        ),
                        child: Text(
                          _formatTimer(_secondsRemaining),
                          style: GoogleFonts.outfit(
                            color: Colors.white,
                            fontSize: 22,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ).animate().scale(delay: 400.ms, curve: Curves.easeOutBack),
                      const SizedBox(height: 35),
                      // Participants Status header
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          "Participants Status",
                          style: GoogleFonts.outfit(
                            color: Colors.white70,
                            fontSize: 15,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ).animate().fadeIn(delay: 500.ms),
                      const SizedBox(height: 15),
                      // Render list
                      _buildParticipantsList(players),
                      const SizedBox(height: 40),
                      // Control actions
                      _buildControlAction(isCreator, isIReady, isAnyFriendReady),
                      const SizedBox(height: 30),
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
            onPressed: () {
              showDialog(
                context: context,
                builder: (context) => AlertDialog(
                  backgroundColor: const Color(0xFF312E81),
                  title: Text("Leave Lobby?", style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold)),
                  content: Text(
                    "Are you sure you want to leave the competition lobby?",
                    style: GoogleFonts.outfit(color: Colors.white70),
                  ),
                  actions: [
                    TextButton(
                      onPressed: () => Navigator.pop(context),
                      child: Text("Cancel", style: TextStyle(color: Colors.cyanAccent)),
                    ),
                    ElevatedButton(
                      style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent),
                      onPressed: () {
                        Navigator.pop(context); // Close dialog
                        Navigator.pop(context); // Exit screen
                      },
                      child: const Text("Leave"),
                    ),
                  ],
                ),
              );
            },
            icon: const Icon(Icons.close_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Text(
            "Competition Lobby",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48), // Spacer to balance close button
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildParticipantsList(List<LobbyPlayer> players) {
    return Column(
      children: List.generate(players.length, (index) {
        final player = players[index];
        final bool isMe = player.email.toLowerCase() == _currentUserEmail.toLowerCase();
        
        Color badgeColor;
        String badgeText;
        final bool isTimedOut = player.status == 'waiting' && _secondsRemaining <= 80;
        
        if (player.status == 'creator') {
          badgeColor = Colors.pinkAccent;
          badgeText = "Creator";
        } else if (player.status == 'ready') {
          badgeColor = Colors.greenAccent;
          badgeText = "Ready";
        } else if (player.status == 'declined') {
          badgeColor = Colors.redAccent;
          badgeText = "Declined";
        } else if (isTimedOut) {
          badgeColor = Colors.redAccent;
          badgeText = "Timed Out";
        } else {
          badgeColor = Colors.amberAccent;
          badgeText = "Waiting";
        }

        return Container(
          margin: const EdgeInsets.only(bottom: 12),
          padding: const EdgeInsets.all(18),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.06),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: Colors.white.withOpacity(0.08)),
          ),
          child: Row(
            children: [
              CircleAvatar(
                radius: 20,
                backgroundColor: badgeColor.withOpacity(0.2),
                child: Text(
                  player.name.isNotEmpty ? player.name[0].toUpperCase() : 'P',
                  style: GoogleFonts.outfit(color: badgeColor, fontWeight: FontWeight.bold),
                ),
              ),
              const SizedBox(width: 15),
              Expanded(
                child: Text(
                  isMe ? "You" : player.name,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: GoogleFonts.outfit(
                    color: Colors.white,
                    fontSize: 15,
                    fontWeight: isMe ? FontWeight.bold : FontWeight.normal,
                  ),
                ),
              ),
              const SizedBox(width: 10),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
                decoration: BoxDecoration(
                  color: badgeColor.withOpacity(0.12),
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: badgeColor.withOpacity(0.3), width: 1.2),
                ),
                child: Text(
                  badgeText,
                  style: GoogleFonts.outfit(
                    color: badgeColor,
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
        ).animate().fadeIn(delay: (600 + index * 100).ms).slideY(begin: 0.1);
      }),
    );
  }

  Widget _buildControlAction(bool isCreator, bool isIReady, bool isAnyFriendReady) {
    if (isCreator) {
      // Creator starts the quiz. Enabled when any friend is ready or timer runs out
      final bool startEnabled = isAnyFriendReady || _secondsRemaining <= 0;
      
      final List<String> declineMessages = [];
      if (_compData != null) {
        final Map<dynamic, dynamic> scores = _compData!['scores'] as Map<dynamic, dynamic>? ?? {};
        final String creatorEmail = _compData!['creatorEmail'] ?? '';
        scores.forEach((key, val) {
          final pMap = val as Map<dynamic, dynamic>;
          final String email = pMap['email'] ?? '';
          final String name = pMap['fullName'] ?? 'Participant';
          final String status = pMap['status'] ?? 'waiting';

          if (email.toLowerCase() != creatorEmail.toLowerCase()) {
            bool isDeclined = status == 'declined';
            bool isTimedOut = status == 'waiting' && _secondsRemaining <= 80;
            if (isDeclined || isTimedOut) {
              declineMessages.add("your invite has declined and $name");
            }
          }
        });
      }

      return Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: startEnabled ? _startQuiz : null,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.cyanAccent,
                foregroundColor: Colors.black,
                disabledBackgroundColor: Colors.white10,
                disabledForegroundColor: Colors.white24,
                padding: const EdgeInsets.symmetric(vertical: 20),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                elevation: 8,
              ),
              child: Text(
                "Start Quiz",
                style: GoogleFonts.outfit(fontSize: 16, fontWeight: FontWeight.bold),
              ),
            ),
          ).animate().fadeIn(delay: 800.ms),
          if (declineMessages.isNotEmpty) ...[
            const SizedBox(height: 15),
            ...declineMessages.map((msg) => Padding(
              padding: const EdgeInsets.only(top: 4.0),
              child: Text(
                msg,
                textAlign: TextAlign.center,
                style: GoogleFonts.outfit(
                  color: Colors.redAccent,
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                ),
              ),
            )),
          ],
        ],
      );
    } else {
      // Invited friend marks ready
      return SizedBox(
        width: double.infinity,
        child: ElevatedButton(
          onPressed: () => _toggleReady(isIReady),
          style: ElevatedButton.styleFrom(
            backgroundColor: isIReady ? Colors.green : Colors.cyanAccent,
            foregroundColor: isIReady ? Colors.white : Colors.black,
            padding: const EdgeInsets.symmetric(vertical: 20),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
            elevation: 8,
          ),
          child: Text(
            isIReady ? "Change to Not Ready" : "I'm Ready",
            style: GoogleFonts.outfit(fontSize: 16, fontWeight: FontWeight.bold),
          ),
        ),
      ).animate().fadeIn(delay: 800.ms);
    }
  }
}

class LobbyPlayer {
  final String name;
  final String email;
  final String status;

  LobbyPlayer({
    required this.name,
    required this.email,
    required this.status,
  });
}
