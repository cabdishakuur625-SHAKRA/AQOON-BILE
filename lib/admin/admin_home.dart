import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../services/auth_service.dart';

import 'manage_user_points.dart';
import 'add_subject.dart';
import 'add_chapter.dart';
import 'add_question.dart';
import 'manage_papers.dart';
import '../services/firebase_service.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import '../services/seed_data.dart';
import 'dart:convert';

class AdminHome extends StatelessWidget {
  const AdminHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: const Text('Admin Dashboard', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF1A237E), Color(0xFF311B92), Color(0xFF4A148C)],
          ),
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Manage Content',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                  ),
                ).animate().fadeIn(duration: 600.ms).slideX(begin: -0.2),
                const SizedBox(height: 8),
                Text(
                  'Add and organize subjects, chapters, and questions.',
                  style: TextStyle(
                    color: Colors.white.withOpacity(0.7),
                    fontSize: 16,
                  ),
                ).animate().fadeIn(delay: 200.ms, duration: 600.ms),
                const SizedBox(height: 40),
                Expanded(
                  child: GridView.count(
                    crossAxisCount: 2,
                    crossAxisSpacing: 16,
                    mainAxisSpacing: 16,
                    children: [
                      _buildAdminCard(
                        context,
                        'Add Subject',
                        Icons.book_rounded,
                        const AddSubjectScreen(),
                        const Color(0xFF64B5F6),
                      ),
                      _buildAdminCard(
                        context,
                        'Add Chapter',
                        Icons.collections_bookmark_rounded,
                        const AddChapterScreen(),
                        const Color(0xFF81C784),
                      ),
                      _buildAdminCard(
                        context,
                        'Add Question',
                        Icons.quiz_rounded,
                        const AddQuestionScreen(),
                        const Color(0xFFFFB74D),
                      ),
                      _buildAdminCard(
                        context,
                        'Seed Database',
                        Icons.cloud_upload_rounded,
                        null,
                        const Color(0xFFBA68C8),
                        onTap: () => _seedDatabase(context),
                      ),
                       _buildAdminCard(
                         context,
                         'Manage Papers',
                         Icons.picture_as_pdf_rounded,
                         const ManagePapersScreen(),
                         Colors.redAccent,
                       ),
                        // New card for managing users, XP & coins
                        _buildAdminCard(
                          context,
                          'Manage Users',
                          Icons.manage_accounts_rounded,
                          const ManageUserPointsScreen(),
                          const Color(0xFF90CAF9),
                        ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  void _seedDatabase(BuildContext context) async {
    try {
      await FirebaseService().seedDatabase();
      if (!context.mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('All subjects fully seeded with MCQ questions! 🎉')));
    } catch (e) {
      if (!context.mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error: $e')));
    }
  }

  Widget _buildAdminCard(BuildContext context, String title, IconData icon, Widget? screen, Color color, {VoidCallback? onTap}) {
    return GestureDetector(
      onTap: onTap ?? () {
        if (screen != null) {
          Navigator.push(context, MaterialPageRoute(builder: (context) => screen));
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Coming soon!')),
          );
        }
      },
      child: Container(
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.1),
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: Colors.white.withOpacity(0.2)),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: color.withOpacity(0.2),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: color, size: 32),
            ),
            const SizedBox(height: 16),
            Text(
              title,
              textAlign: TextAlign.center,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 16,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ).animate().scale(delay: 400.ms, duration: 400.ms, curve: Curves.easeOutBack),
    );
  }
}
