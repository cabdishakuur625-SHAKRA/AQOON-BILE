import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'QuizResultsScreen.dart';
import '../../services/auth_service.dart';
import '../question.dart';

class ChallengeQuizScreen extends StatefulWidget {
  final String challengeId;
  final String title;
  final List<Question> questions;
  final int initialIndex;
  final int initialScore;
  final int xpReward;
  final int coinsReward;

  const ChallengeQuizScreen({
    super.key,
    required this.challengeId,
    required this.title,
    required this.questions,
    required this.initialIndex,
    required this.initialScore,
    required this.xpReward,
    required this.coinsReward,
  });

  @override
  State<ChallengeQuizScreen> createState() => _ChallengeQuizScreenState();
}

class _ChallengeQuizScreenState extends State<ChallengeQuizScreen> {
  int _currentQuestionIndex = 0;
  String? _selectedOptionKey;
  int _score = 0;
  bool _saving = false;
  final Map<int, String> _userAnswers = {};

  @override
  void initState() {
    super.initState();
    _currentQuestionIndex = widget.initialIndex;
    if (_currentQuestionIndex >= widget.questions.length) {
      _currentQuestionIndex = 0;
    }
    _score = widget.initialScore;
  }

  Future<void> _saveCurrentProgress() async {
    if (widget.questions.isEmpty) return;
    setState(() => _saving = true);
    try {
      await AuthService.saveChallengeProgress(
        challengeId: widget.challengeId,
        status: 'in_progress',
        currentIndex: _currentQuestionIndex,
        score: _score,
        questions: widget.questions.map((q) => q.toMap()).toList(),
      );
    } catch (e) {
      debugPrint('Error saving challenge progress: $e');
    }
    if (mounted) {
      setState(() => _saving = false);
    }
  }

  void _nextQuestion() async {
    if (_selectedOptionKey == null) return;

    _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;

    // Evaluate answer
    if (_selectedOptionKey == widget.questions[_currentQuestionIndex].correctAnswer) {
      _score++;
    }

    if (_currentQuestionIndex < widget.questions.length - 1) {
      setState(() {
        _currentQuestionIndex++;
        _selectedOptionKey = null;
      });
      await _saveCurrentProgress();
    } else {
      _finishChallenge();
    }
  }

  void _finishChallenge() async {
    if (_selectedOptionKey != null) {
      _userAnswers[_currentQuestionIndex] = _selectedOptionKey!;
    }

    setState(() => _saving = true);
    int oldXp = AuthService.currentUser?.xp ?? 0;
    int oldCoins = AuthService.currentUser?.coins ?? 0;

    try {
      // 1. Mark as completed in the database
      await AuthService.saveChallengeProgress(
        challengeId: widget.challengeId,
        status: 'completed',
        currentIndex: widget.questions.length,
        score: _score,
        questions: widget.questions.map((q) => q.toMap()).toList(),
      );

      // 2. Award Coins and update Streak
      await AuthService.updateUserCoins(widget.coinsReward);
      await AuthService.updateUserStreak();
    } catch (e) {
      debugPrint('Error finalizing challenge: $e');
    }

    if (mounted) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => QuizResultsScreen(
            totalQuestions: widget.questions.length,
            correctAnswers: _score,
            subjectName: widget.title,
            oldXp: oldXp,
            newXp: oldXp,
            oldCoins: oldCoins,
            newCoins: oldCoins + widget.coinsReward,
            questions: widget.questions,
            userAnswers: _userAnswers,
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (widget.questions.isEmpty) {
      return Scaffold(
        backgroundColor: const Color(0xFF1E1B4B),
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          iconTheme: const IconThemeData(color: Colors.white),
        ),
        body: Center(
          child: Text(
            "No questions found for this challenge.",
            style: GoogleFonts.outfit(color: Colors.white60, fontSize: 18),
          ),
        ),
      );
    }

    final currentQuestion = widget.questions[_currentQuestionIndex];

    return PopScope(
      canPop: true,
      onPopInvokedWithResult: (didPop, result) async {
        if (didPop) {
          // Auto-save current progress in the background when popping
          AuthService.saveChallengeProgress(
            challengeId: widget.challengeId,
            status: 'in_progress',
            currentIndex: _currentQuestionIndex,
            score: _score,
            questions: widget.questions.map((q) => q.toMap()).toList(),
          );
        }
      },
      child: Scaffold(
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
                _buildHeaderBar(),
                Expanded(
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.symmetric(horizontal: 25.0),
                    child: Column(
                      children: [
                        const SizedBox(height: 10),
                        _buildDifficultyTag(currentQuestion.difficultyLevel),
                        const SizedBox(height: 20),
                        _buildProgressIndicator(),
                        const SizedBox(height: 30),
                        _buildQuestionBox(currentQuestion.questionText),
                        const SizedBox(height: 30),
                        _buildOptionsList(currentQuestion.options),
                        const SizedBox(height: 20),
                      ],
                    ),
                  ),
                ),
                _buildBottomControls(),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildHeaderBar() {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          IconButton(
            onPressed: () => Navigator.maybePop(context),
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Expanded(
            child: Text(
              widget.title,
              textAlign: TextAlign.center,
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: GoogleFonts.outfit(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          _saving
              ? const SizedBox(
                  width: 20,
                  height: 20,
                  child: CircularProgressIndicator(color: Colors.cyanAccent, strokeWidth: 2),
                )
              : const Icon(Icons.cloud_done_rounded, color: Colors.cyanAccent, size: 20),
        ],
      ),
    ).animate().slideY(begin: -1);
  }

  Widget _buildDifficultyTag(String difficulty) {
    Color tagColor = difficulty.toLowerCase() == "easy"
        ? Colors.cyanAccent
        : difficulty.toLowerCase() == "medium"
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
            difficulty.toUpperCase(),
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
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "${_currentQuestionIndex + 1}/${widget.questions.length}",
              style: GoogleFonts.outfit(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
            Row(
              children: [
                const Icon(Icons.monetization_on_rounded, color: Colors.cyanAccent, size: 20),
                const SizedBox(width: 6),
                Text(
                  "+${widget.coinsReward} Coins",
                  style: GoogleFonts.outfit(
                    color: Colors.cyanAccent,
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ],
        ),
        const SizedBox(height: 15),
        ClipRRect(
          borderRadius: BorderRadius.circular(10),
          child: LinearProgressIndicator(
            value: (_currentQuestionIndex + 1) / widget.questions.length,
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
              onPressed: _currentQuestionIndex > 0
                  ? () => setState(() {
                        _currentQuestionIndex--;
                        _selectedOptionKey = null;
                      })
                  : null,
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
                _currentQuestionIndex < widget.questions.length - 1 ? "Next" : "Finish",
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
    ).animate().slideY(begin: 1, duration: 600.ms);
  }
}
