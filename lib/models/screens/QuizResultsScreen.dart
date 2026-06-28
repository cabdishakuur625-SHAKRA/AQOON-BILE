import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../question.dart';
import 'HomeScreen.dart';
import 'ReviewAnswersScreen.dart';

class QuizResultsScreen extends StatefulWidget {
  final int totalQuestions;
  final int correctAnswers;
  final String subjectName;
  final int oldXp;
  final int newXp;
  final int oldCoins;
  final int newCoins;
  final List<Question> questions;
  final Map<int, String> userAnswers;
  final bool isMockExam;
  final int? timeTakenSeconds;

  const QuizResultsScreen({
    super.key,
    required this.totalQuestions,
    required this.correctAnswers,
    required this.subjectName,
    required this.oldXp,
    required this.newXp,
    required this.oldCoins,
    required this.newCoins,
    required this.questions,
    required this.userAnswers,
    this.isMockExam = false,
    this.timeTakenSeconds,
  });

  @override
  State<QuizResultsScreen> createState() => _QuizResultsScreenState();
}

class _QuizResultsScreenState extends State<QuizResultsScreen> {
  String _formatTimeTaken(int totalSeconds) {
    int minutes = totalSeconds ~/ 60;
    int seconds = totalSeconds % 60;
    if (minutes > 0) {
      return "${minutes}m ${seconds}s";
    } else {
      return "${seconds}s";
    }
  }

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double percentage = widget.totalQuestions > 0 ? (widget.correctAnswers / widget.totalQuestions) * 100 : 0.0;
    bool isSuccess = percentage >= 60;
    int xpEarned = widget.newXp - widget.oldXp;

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
                      const SizedBox(height: 20),
                      _buildResultsCard(isSuccess, percentage),
                      const SizedBox(height: 30),
                      _buildStatsRow(xpEarned),
                      const SizedBox(height: 40),
                      _buildActionButtons(context),
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
      child: Text(
        widget.isMockExam ? "Mock Exam Results" : "Quiz Results",
        style: GoogleFonts.outfit(
          color: Colors.white,
          fontSize: 22,
          fontWeight: FontWeight.bold,
        ),
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildResultsCard(bool isSuccess, double percentage) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(30),
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
      child: Column(
        children: [
          Stack(
            alignment: Alignment.center,
            children: [
              SizedBox(
                width: 150,
                height: 150,
                child: CircularProgressIndicator(
                  value: percentage / 100,
                  strokeWidth: 12,
                  backgroundColor: Colors.white10,
                  valueColor: AlwaysStoppedAnimation<Color>(
                    isSuccess ? Colors.cyanAccent : Colors.orangeAccent,
                  ),
                ),
              ),
              Column(
                children: [
                  Text(
                    "${percentage.toInt()}%",
                    style: GoogleFonts.outfit(
                      color: Colors.white,
                      fontSize: 36,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Text(
                    "Score",
                    style: GoogleFonts.outfit(color: Colors.white60, fontSize: 14),
                  ),
                ],
              ),
            ],
          ).animate().scale(duration: 800.ms, curve: Curves.easeOutBack),
          const SizedBox(height: 30),
          Text(
            isSuccess ? "Congratulations!" : "Try Again!",
            style: GoogleFonts.outfit(
              color: isSuccess ? Colors.cyanAccent : Colors.orangeAccent,
              fontSize: 28,
              fontWeight: FontWeight.bold,
            ),
          ).animate().fadeIn(delay: 400.ms),
          const SizedBox(height: 10),
          Text(
            "You scored ${widget.correctAnswers} out of ${widget.totalQuestions}",
            style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16),
          ).animate().fadeIn(delay: 600.ms),
          if (widget.isMockExam && widget.timeTakenSeconds != null) ...[
            const SizedBox(height: 12),
            Text(
              "Time Taken: ${_formatTimeTaken(widget.timeTakenSeconds!)}",
              style: GoogleFonts.outfit(
                color: Colors.cyanAccent,
                fontSize: 15,
                fontWeight: FontWeight.w600,
              ),
            ).animate().fadeIn(delay: 700.ms),
          ],
        ],
      ),
    );
  }

  Widget _buildStatsRow(int xpEarned) {
    final int coinsEarned = widget.newCoins - widget.oldCoins;
    final bool showCoins = coinsEarned > 0 || (widget.newXp == widget.oldXp);

    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        _buildStatItem("Correct", widget.correctAnswers.toString(), Colors.cyanAccent),
        _buildStatItem("Wrong", (widget.totalQuestions - widget.correctAnswers).toString(), Colors.redAccent),
        if (showCoins)
          _buildStatItem("Coins Earned", "+$coinsEarned", Colors.cyanAccent)
        else
          _buildStatItem("XP Earned", "+$xpEarned", Colors.amberAccent),
      ],
    ).animate().fadeIn(delay: 800.ms).slideY(begin: 0.2);
  }

  Widget _buildStatItem(String label, String value, Color color) {
    IconData icon;
    if (label == "Correct") {
      icon = Icons.check_rounded;
    } else if (label == "Wrong") {
      icon = Icons.close_rounded;
    } else if (label == "Coins Earned") {
      icon = Icons.monetization_on_rounded;
    } else {
      icon = Icons.stars_rounded;
    }

    return Column(
      children: [
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            shape: BoxShape.circle,
          ),
          child: Icon(
            icon,
            color: color,
            size: 24,
          ),
        ),
        const SizedBox(height: 10),
        Text(
          value,
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
        ),
        Text(
          label,
          style: GoogleFonts.outfit(color: Colors.white38, fontSize: 12),
        ),
      ],
    );
  }



  Widget _buildActionButtons(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: ElevatedButton(
            onPressed: () {
              Navigator.of(context).pushAndRemoveUntil(
                MaterialPageRoute(builder: (context) => const HomeScreen()),
                (route) => false,
              );
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
                const Icon(Icons.home_rounded, size: 20),
                const SizedBox(width: 8),
                Text("Home", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
              ],
            ),
          ),
        ),
        const SizedBox(width: 20),
        Expanded(
          child: ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ReviewAnswersScreen(
                    questions: widget.questions,
                    userAnswers: widget.userAnswers,
                  ),
                ),
              );
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.purpleAccent,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 18),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              elevation: 8,
              shadowColor: Colors.purpleAccent.withOpacity(0.4),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.refresh_rounded, size: 20),
                const SizedBox(width: 8),
                Text("Review", style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
              ],
            ),
          ),
        ),
      ],
    ).animate().fadeIn(delay: 1.2.seconds).slideY(begin: 0.2);
  }
}
