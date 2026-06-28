import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../question.dart';

class ReviewAnswersScreen extends StatelessWidget {
  final List<Question> questions;
  final Map<int, String> userAnswers;

  const ReviewAnswersScreen({
    super.key,
    required this.questions,
    required this.userAnswers,
  });

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
              _buildAppBar(context),
              Expanded(
                child: questions.isEmpty
                    ? Center(
                        child: Text(
                          "No questions to review.",
                          style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16),
                        ),
                      )
                    : ListView.builder(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                        itemCount: questions.length,
                        itemBuilder: (context, index) {
                          final question = questions[index];
                          final chosenAnswer = userAnswers[index];
                          return _buildQuestionCard(question, index, chosenAnswer)
                              .animate()
                              .fadeIn(delay: (index * 100).ms, duration: 400.ms)
                              .slideY(begin: 0.1);
                        },
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
        children: [
          IconButton(
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          const SizedBox(width: 15),
          Text(
            "Review Answers",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildQuestionCard(Question question, int index, String? chosenAnswer) {
    return Container(
      margin: const EdgeInsets.only(bottom: 25),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(25),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 10,
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
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: Colors.cyanAccent.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(color: Colors.cyanAccent.withOpacity(0.2)),
                ),
                child: Text(
                  "Question ${index + 1}",
                  style: GoogleFonts.outfit(
                    color: Colors.cyanAccent,
                    fontWeight: FontWeight.bold,
                    fontSize: 12,
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.05),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Text(
                  question.difficultyLevel.toUpperCase(),
                  style: GoogleFonts.outfit(
                    color: Colors.white54,
                    fontSize: 10,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 15),
          Text(
            question.questionText,
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 17,
              fontWeight: FontWeight.bold,
              height: 1.4,
            ),
          ),
          const SizedBox(height: 20),
          ...question.options.entries.map((entry) {
            final optionKey = entry.key;
            final optionValue = entry.value;
            final isUserChoice = chosenAnswer == optionKey;
            final isCorrect = question.correctAnswer == optionKey;

            Color itemBgColor = Colors.white.withOpacity(0.03);
            Color itemBorderColor = Colors.white.withOpacity(0.08);
            Color circleBgColor = Colors.white10;
            Color circleTextColor = Colors.white70;
            Widget? trailingIcon;

            if (isCorrect) {
              itemBgColor = Colors.greenAccent.withOpacity(0.15);
              itemBorderColor = Colors.greenAccent;
              circleBgColor = Colors.greenAccent;
              circleTextColor = Colors.black;
              trailingIcon = Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    isUserChoice ? "Your Answer (Correct)" : "Correct Answer",
                    style: GoogleFonts.outfit(
                      color: Colors.greenAccent,
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(width: 6),
                  const Icon(Icons.check_circle_rounded, color: Colors.greenAccent, size: 20),
                ],
              );
            } else if (isUserChoice) {
              itemBgColor = Colors.redAccent.withOpacity(0.15);
              itemBorderColor = Colors.redAccent;
              circleBgColor = Colors.redAccent;
              circleTextColor = Colors.white;
              trailingIcon = Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    "Your Answer (Incorrect)",
                    style: GoogleFonts.outfit(
                      color: Colors.redAccent,
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(width: 6),
                  const Icon(Icons.cancel_rounded, color: Colors.redAccent, size: 20),
                ],
              );
            }

            return Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Container(
                padding: const EdgeInsets.all(15),
                decoration: BoxDecoration(
                  color: itemBgColor,
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(color: itemBorderColor, width: 1.5),
                ),
                child: Row(
                  children: [
                    Container(
                      width: 28,
                      height: 28,
                      decoration: BoxDecoration(
                        color: circleBgColor,
                        shape: BoxShape.circle,
                      ),
                      child: Center(
                        child: Text(
                          optionKey.toUpperCase(),
                          style: TextStyle(
                            color: circleTextColor,
                            fontWeight: FontWeight.bold,
                            fontSize: 13,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 15),
                    Expanded(
                      child: Text(
                        optionValue,
                        style: GoogleFonts.outfit(
                          color: isCorrect || isUserChoice ? Colors.white : Colors.white70,
                          fontSize: 15,
                          fontWeight: isCorrect || isUserChoice ? FontWeight.w600 : FontWeight.normal,
                        ),
                      ),
                    ),
                    if (trailingIcon != null) trailingIcon,
                  ],
                ),
              ),
            );
          }),
        ],
      ),
    );
  }
}
