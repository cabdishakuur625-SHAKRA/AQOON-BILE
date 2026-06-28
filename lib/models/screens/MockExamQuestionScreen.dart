import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'QuizResultsScreen.dart';
import '../../services/firebase_service.dart';
import '../../services/auth_service.dart';
import '../question.dart';

class MockExamQuestionScreen extends StatefulWidget {
  final String subjectId;
  final String subjectName;
  final Map<String, int> distribution;
  final int durationMinutes;

  const MockExamQuestionScreen({
    super.key,
    required this.subjectId,
    required this.subjectName,
    required this.distribution,
    required this.durationMinutes,
  });

  @override
  State<MockExamQuestionScreen> createState() => _MockExamQuestionScreenState();
}

class _MockExamQuestionScreenState extends State<MockExamQuestionScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  List<Question> _questions = [];
  int _currentQuestionIndex = 0;
  String? _selectedOptionKey;
  Map<int, String> _userAnswers = {};
  bool _isLoading = true;

  late Timer _timer;
  late int _secondsRemaining;

  @override
  void initState() {
    super.initState();
    _secondsRemaining = widget.durationMinutes * 60;
    _loadQuestions();
    _startTimer();
  }

  Future<void> _loadQuestions() async {
    final questions = await _firebaseService.getMockExamQuestions(widget.subjectId, widget.distribution);
    if (mounted) {
      setState(() {
        _questions = questions;
        _isLoading = false;
      });
    }
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_secondsRemaining > 0) {
        setState(() {
          _secondsRemaining--;
        });
      } else {
        _timer.cancel();
        _finishExam();
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

  int get _totalQuestions => _questions.length;

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
      _finishExam();
    }
  }

  void _finishExam() async {
    if (_selectedOptionKey != null) {
      _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
    }

    int correctCount = 0;
    for (int i = 0; i < _questions.length; i++) {
      if (_userAnswers[i] == _questions[i].correctAnswer) {
        correctCount++;
      }
    }

    int oldXp = AuthService.currentUser?.xp ?? 0;
    int oldCoins = AuthService.currentUser?.coins ?? 0;
    int coinsEarned = correctCount * 4;

    // Save to database (Coins and Streak)
    if (coinsEarned > 0) {
      await AuthService.updateUserCoins(coinsEarned);
    }
    await AuthService.updateUserStreak();

    await _firebaseService.logExamQuizAttempt(
      type: 'mock_exam',
      subjectId: widget.subjectId,
      subjectName: widget.subjectName,
      score: correctCount,
      totalQuestions: _totalQuestions,
    );

    final int timeTaken = (widget.durationMinutes * 60) - _secondsRemaining;

    if (!mounted) return;

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => QuizResultsScreen(
          totalQuestions: _totalQuestions,
          correctAnswers: correctCount,
          subjectName: widget.subjectName,
          oldXp: oldXp,
          newXp: oldXp,
          oldCoins: oldCoins,
          newCoins: oldCoins + coinsEarned,
          questions: _questions,
          userAnswers: _userAnswers,
          isMockExam: true,
          timeTakenSeconds: timeTaken,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        backgroundColor: Color(0xFF1E1B4B),
        body: Center(child: CircularProgressIndicator(color: Colors.cyanAccent)),
      );
    }

    if (_questions.isEmpty) {
      return Scaffold(
        backgroundColor: const Color(0xFF1E1B4B),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("No questions found.", style: GoogleFonts.outfit(color: Colors.white70)),
              const SizedBox(height: 20),
              ElevatedButton(onPressed: () => Navigator.pop(context), child: const Text("Go Back")),
            ],
          ),
        ),
      );
    }

    final currentQuestion = _questions[_currentQuestionIndex];

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
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.close_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Column(
            children: [
              Text(
                "Mock Exam",
                style: GoogleFonts.outfit(
                  color: Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                widget.subjectName,
                style: GoogleFonts.outfit(color: Colors.white60, fontSize: 12),
              ),
            ],
          ),
          ElevatedButton(
            onPressed: () => _finishExam(),
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
    ).animate().fadeIn(delay: 200.ms);
  }

  Widget _buildQuestionBox(String text) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 40),
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
          fontSize: 22,
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
          ).animate().fadeIn(delay: (index * 100).ms),
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
              onPressed: _currentQuestionIndex > 0 ? () {
                if (_selectedOptionKey != null) {
                  _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
                }
                setState(() {
                  _currentQuestionIndex--;
                  _selectedOptionKey = _userAnswers[_currentQuestionIndex];
                });
              } : null,
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
                _currentQuestionIndex == _totalQuestions - 1 ? "Finish Exam" : "Next Question",
                style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
    ).animate().slideY(begin: 1);
  }
}
