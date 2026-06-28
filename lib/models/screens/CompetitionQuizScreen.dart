import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/firebase_service.dart';
import '../../services/auth_service.dart';
import '../question.dart';
import 'CompetitionResultsScreen.dart';

class CompetitionQuizScreen extends StatefulWidget {
  final String competitionId;
  final String competitionTitle;
  final List<Question> questions;
  final int durationMinutes;
  final String subjectName;

  const CompetitionQuizScreen({
    super.key,
    required this.competitionId,
    required this.competitionTitle,
    required this.questions,
    required this.durationMinutes,
    required this.subjectName,
  });

  @override
  State<CompetitionQuizScreen> createState() => _CompetitionQuizScreenState();
}

class _CompetitionQuizScreenState extends State<CompetitionQuizScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  int _currentQuestionIndex = 0;
  String? _selectedOptionKey;
  final Map<int, String> _userAnswers = {};

  late Timer _timer;
  late int _secondsRemaining;
  bool _isSubmitting = false;

  @override
  void initState() {
    super.initState();
    _secondsRemaining = widget.durationMinutes * 60;
    _startTimer();
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_secondsRemaining > 0) {
        setState(() {
          _secondsRemaining--;
        });
      } else {
        _timer.cancel();
        _finishQuiz();
      }
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  String _formatTime(int seconds) {
    int mins = seconds ~/ 60;
    int secs = seconds % 60;
    return "${mins.toString().padLeft(2, '0')}:${secs.toString().padLeft(2, '0')}";
  }

  int get _totalQuestions => widget.questions.length;

  void _nextQuestion() {
    if (_selectedOptionKey != null) {
      _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
    }

    if (_currentQuestionIndex < _totalQuestions - 1) {
      setState(() {
        _currentQuestionIndex++;
        _selectedOptionKey = _userAnswers[_currentQuestionIndex];
      });
    } else {
      _finishQuiz();
    }
  }

  void _finishQuiz() async {
    if (_isSubmitting) return;
    setState(() => _isSubmitting = true);

    _timer.cancel();

    // Save final answer if selected
    if (_selectedOptionKey != null) {
      _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
    }

    int correctCount = 0;
    for (int i = 0; i < widget.questions.length; i++) {
      if (_userAnswers[i] == widget.questions[i].correctAnswer) {
        correctCount++;
      }
    }

    // Reward Logic:
    // 1. 20 XP and 20 Coins per correct answer
    int xpEarned = correctCount * 20;
    int coinsEarned = correctCount * 20;

    // 2. Passing bonus (+50 XP / +50 Coins) if score >= 60%
    double percentage = _totalQuestions > 0 ? (correctCount / _totalQuestions) * 100 : 0.0;
    if (percentage >= 60) {
      xpEarned += 50;
      coinsEarned += 50;
    }

    try {
      int oldXp = AuthService.currentUser?.xp ?? 0;
      final int timeTaken = (widget.durationMinutes * 60) - _secondsRemaining;

      // Submit score to the Competition leaderboard
      await _firebaseService.submitCompetitionScore(
        competitionId: widget.competitionId,
        score: correctCount,
        timeTakenSeconds: timeTaken,
      );

      // Save rewards to User Profile
      await AuthService.updateUserXp(xpEarned);
      await AuthService.updateUserCoins(coinsEarned);

      int newXp = oldXp + xpEarned;

      if (!mounted) return;

      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => CompetitionResultsScreen(
            competitionId: widget.competitionId,
            competitionTitle: widget.competitionTitle,
            subjectName: widget.subjectName,
            totalQuestions: _totalQuestions,
            correctAnswers: correctCount,
            oldXp: oldXp,
            newXp: newXp,
            xpEarned: xpEarned,
          ),
        ),
      );
    } catch (e) {
      debugPrint("Error submitting competition quiz: $e");
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Error saving score: $e"), backgroundColor: Colors.redAccent),
        );
        setState(() => _isSubmitting = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    if (widget.questions.isEmpty) {
      return Scaffold(
        backgroundColor: const Color(0xFF1E1B4B),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("No questions found for this quiz.", style: GoogleFonts.outfit(color: Colors.white70)),
              const SizedBox(height: 20),
              ElevatedButton(onPressed: () => Navigator.pop(context), child: const Text("Go Back")),
            ],
          ),
        ),
      );
    }

    final currentQuestion = widget.questions[_currentQuestionIndex];

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
          child: _isSubmitting
              ? const Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CircularProgressIndicator(color: Colors.cyanAccent),
                      SizedBox(height: 20),
                      Text("Submitting your score...", style: TextStyle(color: Colors.white70)),
                    ],
                  ),
                )
              : Column(
                  children: [
                    _buildAppBar(context),
                    Expanded(
                      child: SingleChildScrollView(
                        padding: const EdgeInsets.symmetric(horizontal: 25.0),
                        child: Column(
                          children: [
                            _buildHeaderInfo(),
                            const SizedBox(height: 30),
                            _buildQuestionBox(currentQuestion.questionText),
                            const SizedBox(height: 30),
                            _buildOptionsList(currentQuestion.options),
                            const SizedBox(height: 40),
                          ],
                        ),
                      ),
                    ),
                    _buildBottomControls(),
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
              // Confirm quit dialog
              showDialog(
                context: context,
                builder: (context) => AlertDialog(
                  backgroundColor: const Color(0xFF312E81),
                  title: Text("Quit Quiz?", style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold)),
                  content: Text(
                    "Are you sure you want to quit? This will submit your current progress.",
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
                        _finishQuiz();
                      },
                      child: const Text("Quit"),
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
          Column(
            children: [
              Text(
                "Competition Quiz",
                style: GoogleFonts.outfit(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                widget.competitionTitle,
                style: GoogleFonts.outfit(color: Colors.white60, fontSize: 12),
              ),
            ],
          ),
          ElevatedButton(
            onPressed: _finishQuiz,
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.redAccent.withOpacity(0.2),
              foregroundColor: Colors.redAccent,
              side: const BorderSide(color: Colors.redAccent, width: 1.5),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(15),
              ),
            ),
            child: const Text("Finish", style: TextStyle(fontWeight: FontWeight.bold)),
          ),
        ],
      ),
    ).animate().slideY(begin: -1);
  }

  Widget _buildHeaderInfo() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              "Question ${_currentQuestionIndex + 1}/$_totalQuestions",
              style: GoogleFonts.outfit(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 5),
            Container(
              width: 150,
              height: 6,
              decoration: BoxDecoration(
                color: Colors.white10,
                borderRadius: BorderRadius.circular(10),
              ),
              child: FractionallySizedBox(
                alignment: Alignment.centerLeft,
                widthFactor: (_currentQuestionIndex + 1) / _totalQuestions,
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.cyanAccent,
                    borderRadius: BorderRadius.circular(10),
                  ),
                ),
              ),
            ),
          ],
        ),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 10),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.05),
            borderRadius: BorderRadius.circular(15),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
          ),
          child: Row(
            children: [
              const Icon(Icons.timer_rounded, color: Colors.orangeAccent, size: 20),
              const SizedBox(width: 8),
              Text(
                _formatTime(_secondsRemaining),
                style: GoogleFonts.outfit(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
            ],
          ),
        ),
      ],
    ).animate().fadeIn(delay: 150.ms);
  }

  Widget _buildQuestionBox(String text) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 35),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: Text(
        text,
        textAlign: TextAlign.center,
        style: GoogleFonts.outfit(
          color: Colors.white,
          fontSize: 20,
          fontWeight: FontWeight.bold,
          height: 1.4,
        ),
      ),
    ).animate().fadeIn().scale(curve: Curves.easeOutBack);
  }

  Widget _buildOptionsList(Map<String, String> options) {
    final keys = options.keys.toList();
    return Column(
      children: List.generate(keys.length, (index) {
        final key = keys[index];
        final value = options[key]!;
        bool isSelected = _selectedOptionKey == key;
        return Padding(
          padding: const EdgeInsets.only(bottom: 15),
          child: GestureDetector(
            onTap: () => setState(() => _selectedOptionKey = key),
            child: Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: isSelected ? Colors.cyanAccent.withOpacity(0.1) : Colors.white.withOpacity(0.05),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: isSelected ? Colors.cyanAccent : Colors.white.withOpacity(0.1),
                  width: 2,
                ),
              ),
              child: Row(
                children: [
                  Container(
                    width: 30,
                    height: 30,
                    decoration: BoxDecoration(
                      color: isSelected ? Colors.cyanAccent : Colors.white10,
                      shape: BoxShape.circle,
                    ),
                    child: Center(
                      child: Text(
                        key.toUpperCase(),
                        style: TextStyle(
                          color: isSelected ? Colors.black : Colors.white70,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 20),
                  Expanded(
                    child: Text(
                      value,
                      style: GoogleFonts.outfit(
                        color: isSelected ? Colors.white : Colors.white70,
                        fontSize: 16,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ).animate().fadeIn(delay: (index * 80).ms),
        );
      }),
    );
  }

  Widget _buildBottomControls() {
    return Container(
      padding: const EdgeInsets.all(25),
      child: Row(
        children: [
          Expanded(
            child: OutlinedButton(
              onPressed: _currentQuestionIndex > 0
                  ? () {
                      if (_selectedOptionKey != null) {
                        _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
                      }
                      setState(() {
                        _currentQuestionIndex--;
                        _selectedOptionKey = _userAnswers[_currentQuestionIndex];
                      });
                    }
                  : null,
              style: OutlinedButton.styleFrom(
                side: BorderSide(
                  color: _currentQuestionIndex > 0 ? Colors.white30 : Colors.white12,
                ),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                padding: const EdgeInsets.symmetric(vertical: 18),
              ),
              child: Text(
                "Previous",
                style: GoogleFonts.outfit(
                  color: _currentQuestionIndex > 0 ? Colors.white : Colors.white24,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
          const SizedBox(width: 20),
          Expanded(
            child: ElevatedButton(
              onPressed: _selectedOptionKey != null ? _nextQuestion : null,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.cyanAccent,
                foregroundColor: Colors.black,
                disabledBackgroundColor: Colors.cyanAccent.withOpacity(0.3),
                disabledForegroundColor: Colors.black.withOpacity(0.3),
                padding: const EdgeInsets.symmetric(vertical: 18),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              ),
              child: Text(
                _currentQuestionIndex == _totalQuestions - 1 ? "Finish Quiz" : "Next Question",
                style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
    ).animate().slideY(begin: 1);
  }
}
