import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import '../question.dart';
import 'CreateCompetitionScreen.dart';
import 'CompetitionQuizScreen.dart';
import 'CompetitionResultsScreen.dart';
import 'CompetitionLobbyScreen.dart';

class CompetitionsListScreen extends StatefulWidget {
  const CompetitionsListScreen({super.key});

  @override
  State<CompetitionsListScreen> createState() => _CompetitionsListScreenState();
}

class _CompetitionsListScreenState extends State<CompetitionsListScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final FirebaseService _firebaseService = FirebaseService();
  final String _currentUserEmail = AuthService.currentUser?.email ?? '';
  final String _currentUserSanitized = AuthService.sanitizeEmail(AuthService.currentUser?.email ?? '');

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging) {
        setState(() {});
      }
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
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
              _buildAppBar(context),
              _buildTabs(),
              Expanded(
                child: StreamBuilder<List<Map<String, dynamic>>>(
                  stream: _firebaseService.streamCompetitions(),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return const Center(child: CircularProgressIndicator(color: Colors.cyanAccent));
                    }

                    if (snapshot.hasError) {
                      return Center(
                        child: Text(
                          "Error loading competitions: ${snapshot.error}",
                          style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 16),
                        ),
                      );
                    }

                    final allComps = snapshot.data ?? [];
                    if (allComps.isEmpty) {
                      return _buildEmptyState();
                    }

                    // Separate active and completed competitions based on current user's completion status
                    // or overall competition status.
                    // An active competition is one where the current user hasn't finished yet.
                    // A completed competition is one where the current user HAS finished.
                    final activeComps = allComps.where((comp) {
                      final String status = comp['status'] ?? '';
                      if (status == 'expired') return false;

                      final scores = comp['scores'] as Map<dynamic, dynamic>? ?? {};
                      final myScoreData = scores[_currentUserSanitized] as Map<dynamic, dynamic>?;
                      final bool isMyCompleted = myScoreData?['completed'] ?? false;

                      // Double check client side expiration
                      final bool quizStarted = comp['quizStarted'] ?? false;
                      final int createdAt = comp['createdAt'] ?? 0;
                      if (!quizStarted && createdAt > 0) {
                        final int now = DateTime.now().millisecondsSinceEpoch;
                        if (now - createdAt > 120000) {
                          // Check if any friend accepted
                          final String creatorEmail = comp['creatorEmail'] ?? '';
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
                            return false;
                          }
                        }
                      }

                      return !isMyCompleted;
                    }).toList();

                    final completedComps = allComps.where((comp) {
                      final scores = comp['scores'] as Map<dynamic, dynamic>? ?? {};
                      final myScoreData = scores[_currentUserSanitized] as Map<dynamic, dynamic>?;
                      final bool isMyCompleted = myScoreData?['completed'] ?? false;
                      return isMyCompleted;
                    }).toList();

                    final currentList = _tabController.index == 0 ? activeComps : completedComps;

                    if (currentList.isEmpty) {
                      return _buildEmptyState();
                    }

                    return ListView.builder(
                      physics: const BouncingScrollPhysics(),
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      itemCount: currentList.length,
                      itemBuilder: (context, index) {
                        return _buildCompetitionCard(currentList[index], index);
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const CreateCompetitionScreen()),
          );
        },
        backgroundColor: Colors.cyanAccent,
        foregroundColor: Colors.black,
        icon: const Icon(Icons.add_rounded, size: 24),
        label: Text(
          "Create Competition",
          style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
        ),
        elevation: 8,
      ).animate().scale(delay: 500.ms, curve: Curves.easeOutBack),
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
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Text(
            "Quiz Competitions",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48), // Spacer to balance back button
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildTabs() {
    return TabBar(
      controller: _tabController,
      dividerColor: Colors.transparent,
      indicatorColor: Colors.cyanAccent,
      indicatorWeight: 3,
      labelColor: Colors.cyanAccent,
      unselectedLabelColor: Colors.white38,
      labelStyle: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 16),
      tabs: const [
        Tab(text: "Active"),
        Tab(text: "Completed"),
      ],
    ).animate().fadeIn(delay: 200.ms);
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.emoji_events_outlined,
            size: 80,
            color: Colors.white.withOpacity(0.15),
          ),
          const SizedBox(height: 20),
          Text(
            _tabController.index == 0
                ? "No active competitions.\nCreate one and challenge your friends!"
                : "You haven't completed any competitions yet.",
            textAlign: TextAlign.center,
            style: GoogleFonts.outfit(color: Colors.white38, fontSize: 16, height: 1.5),
          ),
        ],
      ).animate().fadeIn(),
    );
  }

  Widget _buildCompetitionCard(Map<String, dynamic> comp, int index) {
    final String compId = comp['id'] ?? '';
    final String title = comp['title'] ?? 'Competition';
    final String description = comp['description'] ?? 'No description';
    final String subjectName = comp['subjectName'] ?? 'General';
    final int duration = comp['duration'] ?? 15;
    final int questionCount = comp['questionCount'] ?? 10;
    final String creatorEmail = comp['creatorEmail'] ?? '';
    final Map<dynamic, dynamic> scores = comp['scores'] as Map<dynamic, dynamic>? ?? {};

    final myScoreData = scores[_currentUserSanitized] as Map<dynamic, dynamic>?;
    final bool hasCompleted = myScoreData?['completed'] ?? false;

    // Build lists of participants
    final List<Widget> participantWidgets = [];
    scores.forEach((key, val) {
      final pMap = val as Map<dynamic, dynamic>;
      final String name = pMap['fullName'] ?? 'Participant';
      final bool done = pMap['completed'] ?? false;
      final int score = pMap['score'] ?? 0;
      final String email = pMap['email'] ?? '';

      final bool isCreator = email.toLowerCase() == creatorEmail.toLowerCase();
      final bool isCurrent = email.toLowerCase() == _currentUserEmail.toLowerCase();

      participantWidgets.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: Row(
            children: [
              CircleAvatar(
                radius: 14,
                backgroundColor: done ? Colors.greenAccent.withOpacity(0.2) : Colors.amberAccent.withOpacity(0.1),
                child: Text(
                  name.isNotEmpty ? name[0].toUpperCase() : 'P',
                  style: GoogleFonts.outfit(
                    color: done ? Colors.greenAccent : Colors.amberAccent,
                    fontSize: 10,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Row(
                  children: [
                    Flexible(
                      child: Text(
                        isCurrent ? "You" : name,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: GoogleFonts.outfit(
                          color: isCurrent ? Colors.white : Colors.white70,
                          fontWeight: isCurrent ? FontWeight.bold : FontWeight.normal,
                          fontSize: 13,
                        ),
                      ),
                    ),
                    if (isCreator) ...[
                      const SizedBox(width: 5),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 1),
                        decoration: BoxDecoration(
                          color: Colors.cyanAccent.withOpacity(0.15),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: Text(
                          "Host",
                          style: GoogleFonts.outfit(color: Colors.cyanAccent, fontSize: 8, fontWeight: FontWeight.bold),
                        ),
                      ),
                    ],
                  ],
                ),
              ),
              Text(
                done ? "$score/$questionCount" : "Pending",
                style: GoogleFonts.outfit(
                  color: done ? Colors.greenAccent : Colors.orangeAccent,
                  fontWeight: FontWeight.bold,
                  fontSize: 12,
                ),
              ),
            ],
          ),
        ),
      );
    });

    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(25),
        border: Border.all(
          color: hasCompleted ? Colors.cyanAccent.withOpacity(0.3) : Colors.white.withOpacity(0.1),
          width: hasCompleted ? 1.5 : 1.0,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.15),
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
              Expanded(
                child: Text(
                  title,
                  style: GoogleFonts.outfit(
                    color: Colors.white,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.cyanAccent.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Text(
                  subjectName,
                  style: GoogleFonts.outfit(
                    color: Colors.cyanAccent,
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
          if (description.isNotEmpty) ...[
            const SizedBox(height: 8),
            Text(
              description,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: GoogleFonts.outfit(color: Colors.white54, fontSize: 13),
            ),
          ],
          const SizedBox(height: 15),
          Row(
            children: [
              const Icon(Icons.help_outline_rounded, color: Colors.white38, size: 16),
              const SizedBox(width: 6),
              Text(
                "$questionCount Questions",
                style: GoogleFonts.outfit(color: Colors.white60, fontSize: 12),
              ),
              const SizedBox(width: 20),
              const Icon(Icons.timer_outlined, color: Colors.white38, size: 16),
              const SizedBox(width: 6),
              Text(
                "$duration min",
                style: GoogleFonts.outfit(color: Colors.white60, fontSize: 12),
              ),
            ],
          ),
          const Divider(color: Colors.white10, height: 30),
          Text(
            "Leaderboard",
            style: GoogleFonts.outfit(
              color: Colors.white70,
              fontSize: 14,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 10),
          ...participantWidgets,
          const SizedBox(height: 15),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              if (!hasCompleted)
                Builder(
                  builder: (context) {
                    final bool quizStarted = comp['quizStarted'] ?? false;
                    return ElevatedButton(
                      onPressed: () {
                        if (!quizStarted) {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => CompetitionLobbyScreen(
                                competitionId: compId,
                              ),
                            ),
                          );
                        } else {
                          // Navigate to CompetitionQuizScreen
                          final List<dynamic> rawQuestions = comp['questions'] ?? [];
                          final List<Question> questions = rawQuestions.asMap().entries.map((entry) {
                            return Question.fromMap(entry.key.toString(), entry.value as Map);
                          }).toList();

                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => CompetitionQuizScreen(
                                competitionId: compId,
                                competitionTitle: title,
                                questions: questions,
                                durationMinutes: duration,
                                subjectName: subjectName,
                              ),
                            ),
                          );
                        }
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.cyanAccent,
                        foregroundColor: Colors.black,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                        elevation: 0,
                      ),
                      child: Text(
                        quizStarted ? "Start Quiz" : "Join Lobby",
                        style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
                      ),
                    );
                  }
                )
              else
                ElevatedButton(
                  onPressed: () {
                    // Navigate to CompetitionResultsScreen to see final scores
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => CompetitionResultsScreen(
                          competitionId: compId,
                          competitionTitle: title,
                          subjectName: subjectName,
                          totalQuestions: questionCount,
                        ),
                      ),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white.withOpacity(0.1),
                    foregroundColor: Colors.cyanAccent,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                      side: BorderSide(color: Colors.cyanAccent.withOpacity(0.5)),
                    ),
                    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                    elevation: 0,
                  ),
                  child: Text(
                    "Leaderboard",
                    style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
                  ),
                ),
            ],
          ),
        ],
      ),
    ).animate().fadeIn(delay: (index * 100).ms).slideY(begin: 0.05);
  }
}
