import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'QuizResultsScreen.dart';
import '../../services/firebase_service.dart';
import '../../services/auth_service.dart';
import '../question.dart';

class QuizQuestionScreen extends StatefulWidget {
  final String subjectId;
  final String chapterId;
  final String difficulty;

  const QuizQuestionScreen({
    super.key,
    required this.subjectId,
    required this.chapterId,
    required this.difficulty,
  });

  @override
  State<QuizQuestionScreen> createState() => _QuizQuestionScreenState();
}

class _QuizQuestionScreenState extends State<QuizQuestionScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  List<Question> _questions = [];
  int _currentQuestionIndex = 0;
  String? _selectedOptionKey;
  int _score = 0;
  bool _isLoading = true;
  final Map<int, String> _userAnswers = {};

  @override
  void initState() {
    super.initState();
    _loadQuestions();
  }

  Future<void> _loadQuestions() async {
    debugPrint('Loading questions for: Subject=${widget.subjectId}, Chapter=${widget.chapterId}, Difficulty=${widget.difficulty}');
    final questions = await _firebaseService.getQuestions(
      widget.subjectId,
      widget.chapterId,
      widget.difficulty,
    );
    debugPrint('Found ${questions.length} questions');
    
    // Shuffle questions to ensure variety on each attempt
    questions.shuffle();
    
    if (mounted) {
      setState(() {
        _questions = questions;
        _isLoading = false;
      });
    }
  }

  void _nextQuestion() {
    if (_selectedOptionKey == null) return;

    _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;

    if (_selectedOptionKey == _questions[_currentQuestionIndex].correctAnswer) {
      _score++;
    }

    if (_currentQuestionIndex < _questions.length - 1) {
      setState(() {
        _currentQuestionIndex++;
        _selectedOptionKey = null;
      });
    } else {
      _finishQuiz();
    }
  }

  void _finishQuiz() async {
    if (_selectedOptionKey != null) {
      _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
    }

    int xpEarned = _score * 2;

    int oldXp = AuthService.currentUser?.xp ?? 0;
    int currentCoins = AuthService.currentUser?.coins ?? 0;

    // Save to database (XP and Streak)
    await AuthService.updateUserXp(xpEarned);
    await AuthService.updateUserStreak();

    String friendlySubjectName = widget.subjectId;
    if (widget.subjectId.toLowerCase() == 'his') {
      friendlySubjectName = 'Taariikh';
    } else if (widget.subjectId.toLowerCase() == 'geo') {
      friendlySubjectName = 'Juqraafi';
    } else if (widget.subjectId.toLowerCase() == 'bio') {
      friendlySubjectName = 'Biology';
    } else if (widget.subjectId.toLowerCase() == 'somali') {
      friendlySubjectName = 'Somali';
    } else if (widget.subjectId.toLowerCase() == 'tech') {
      friendlySubjectName = 'Technology';
    }

    await _firebaseService.logExamQuizAttempt(
      type: 'quiz',
      subjectId: widget.subjectId,
      subjectName: friendlySubjectName,
      score: _score,
      totalQuestions: _questions.length,
    );

    int newXp = oldXp + xpEarned;

    if (!mounted) return;

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => QuizResultsScreen(
          totalQuestions: _questions.length,
          correctAnswers: _score,
          subjectName: widget.subjectId,
          oldXp: oldXp,
          newXp: newXp,
          oldCoins: currentCoins,
          newCoins: currentCoins,
          questions: _questions,
          userAnswers: _userAnswers,
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
        appBar: AppBar(backgroundColor: Colors.transparent, elevation: 0, iconTheme: const IconThemeData(color: Colors.white)),
        body: Center(child: Text("No questions found for this selection.", style: GoogleFonts.outfit(color: Colors.white70))),
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
                      _buildDifficultyTag(),
                      const SizedBox(height: 20),
                      _buildProgressIndicator(),
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

  Widget _buildDifficultyTag() {
    Color tagColor = widget.difficulty.toLowerCase() == "easy"
        ? Colors.cyanAccent
        : widget.difficulty.toLowerCase() == "medium"
            ? Colors.amberAccent
            : Colors.redAccent;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: BoxDecoration(
        color: tagColor.withOpacity(0.1),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: tagColor.withOpacity(0.3)),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.bolt_rounded, color: tagColor, size: 16),
          const SizedBox(width: 8),
          Text(
            widget.difficulty.toUpperCase(),
            style: GoogleFonts.outfit(
              color: tagColor,
              fontWeight: FontWeight.bold,
              fontSize: 12,
              letterSpacing: 1.2,
            ),
          ),
        ],
      ),
    ).animate().fadeIn().scale();
  }

  Widget _buildProgressIndicator() {
    return Column(
      children: [
        Row(
          children: [
            Text(
              "${_currentQuestionIndex + 1}/${_questions.length}",
              style: GoogleFonts.outfit(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        const SizedBox(height: 15),
        ClipRRect(
          borderRadius: BorderRadius.circular(10),
          child: LinearProgressIndicator(
            value: (_currentQuestionIndex + 1) / _questions.length,
            minHeight: 8,
            backgroundColor: Colors.white.withOpacity(0.1),
            valueColor: const AlwaysStoppedAnimation<Color>(Colors.orangeAccent),
          ),
        ).animate().fadeIn(delay: 300.ms),
      ],
    );
  }

  Widget _buildQuestionBox(String text) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 40),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            blurRadius: 20,
            offset: const Offset(0, 10),
          ),
        ],
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
    ).animate().fadeIn().scale(duration: 600.ms, curve: Curves.easeOutBack);
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
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 300),
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: isSelected ? Colors.cyanAccent.withOpacity(0.2) : Colors.white.withOpacity(0.05),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: isSelected ? Colors.cyanAccent : Colors.white.withOpacity(0.1),
                  width: 2,
                ),
                boxShadow: isSelected
                    ? [BoxShadow(color: Colors.cyanAccent.withOpacity(0.2), blurRadius: 10, spreadRadius: 2)]
                    : [],
              ),
              child: Row(
                children: [
                  Container(
                    width: 35,
                    height: 35,
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
                        fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
                      ),
                    ),
                  ),
                  if (isSelected)
                    const Icon(Icons.check_circle_rounded, color: Colors.cyanAccent),
                ],
              ),
            ).animate().fadeIn(delay: (index * 100).ms, duration: 400.ms).slideX(begin: 0.1),
          ),
        );
      }),
    );
  }

  Widget _buildBottomControls() {
    return Container(
      padding: const EdgeInsets.all(25),
      decoration: BoxDecoration(
        color: const Color(0xFF1E1B4B).withOpacity(0.95),
        border: Border(top: BorderSide(color: Colors.white.withOpacity(0.05))),
      ),
      child: Row(
        children: [
          Expanded(
            child: OutlinedButton(
              onPressed: _currentQuestionIndex > 0 ? () => setState(() => _currentQuestionIndex--) : null,
              style: OutlinedButton.styleFrom(
                side: const BorderSide(color: Colors.white24),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                padding: const EdgeInsets.symmetric(vertical: 18),
              ),
              child: const Text("Previous", style: TextStyle(color: Colors.white70)),
            ),
          ),
          const SizedBox(width: 20),
          Expanded(
            child: ElevatedButton(
              onPressed: _selectedOptionKey != null ? _nextQuestion : null,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.cyanAccent,
                foregroundColor: Colors.black,
                disabledBackgroundColor: Colors.white10,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                padding: const EdgeInsets.symmetric(vertical: 18),
                elevation: 10,
                shadowColor: Colors.cyanAccent.withOpacity(0.5),
              ),
              child: Text(
                _currentQuestionIndex < _questions.length - 1 ? "Next" : "Finish",
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
    ).animate().slideY(begin: 1, duration: 600.ms);
  }
}
