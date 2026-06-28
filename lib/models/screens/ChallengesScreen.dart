import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import '../question.dart';
import 'ChallengeQuizScreen.dart';

class ChallengesScreen extends StatefulWidget {
  const ChallengesScreen({super.key});

  @override
  State<ChallengesScreen> createState() => _ChallengesScreenState();
}

class _ChallengesScreenState extends State<ChallengesScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final TextEditingController _searchController = TextEditingController();
  bool _isLoading = true;
  Map<dynamic, dynamic> _userChallengesProgress = {};

  final List<ChallengeData> _challenges = [];

  static final List<ChallengeData> _allChallenges = [
    ChallengeData(
      id: "challenge_his_ch1",
      title: "History - Cutubka 1aad: Dawladda Cusmaaniyiinta Challenge",
      subjectId: "his",
      chapterId: "his_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_geo_ch1",
      title: "Geography - Cutubka 1aad: Hordhaca Jiyooloojiga Challenge",
      subjectId: "geo",
      chapterId: "geo_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_bio_ch1",
      title: "Biology - Chapter 1: The Nervous System Challenge",
      subjectId: "bio",
      chapterId: "bio_ch1",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_tarbiyo_ch1",
      title: "Tarbiyo - الوحدة الأولى Challenge",
      subjectId: "tarbiyo",
      chapterId: "tarbiyo_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_somali_ch1",
      title: "Somali - Cutubka 1 & 2: Qoraal Sharraxeed iyo Beeraha Challenge",
      subjectId: "somali",
      chapterId: "somali_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_tech_ch1",
      title: "Technology - Unit 1: Introduction to System Analysis and Design Challenge",
      subjectId: "tech",
      chapterId: "tech_ch1",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_eng_ch1",
      title: "English - Unit 1 & 2: Never Forget & Oral Presentation Challenge",
      subjectId: "eng",
      chapterId: "eng_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_math_ch1",
      title: "Mathematics - Chapter 1: Circular Functions and Trigonometry Challenge",
      subjectId: "math",
      chapterId: "math_ch1",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_arabic_ch1",
      title: "Arabic - الوحدة الأولى: حروف الجر والنداء Challenge",
      subjectId: "arabic",
      chapterId: "arabic_ch1",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_phy_ch1",
      title: "Physics - Oscillatory Motion Challenge",
      subjectId: "phy",
      chapterId: "phy_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_chem_ch1",
      title: "Chemistry - Hydrocarbons Challenge",
      subjectId: "chem",
      chapterId: "chem_ch1",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_bus_ch1",
      title: "Business - Business Plan Challenge",
      subjectId: "bus",
      chapterId: "bus_ch1",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_his_ch2",
      title: "History - Cutubka 2aad: Dunida Islaamka iyo Qadiyadaha Casriga ah Challenge",
      subjectId: "his",
      chapterId: "his_ch2",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_math_ch2",
      title: "Mathematics - Chapter 2: Coordinate Geometry (Analytic Geometry) Challenge",
      subjectId: "math",
      chapterId: "math_ch2",
      difficulty: "hard",
      xpReward: 0,
      coinsReward: 60,
    ),
    ChallengeData(
      id: "challenge_phy_ch2",
      title: "Physics - Wave Motion Challenge",
      subjectId: "phy",
      chapterId: "phy_ch2",
      difficulty: "medium",
      xpReward: 0,
      coinsReward: 60,
    ),
  ];

  void _initializeDailyChallenges() {
    final now = DateTime.now();
    // Calculate day index since epoch: 1000 * 60 * 60 * 24 = 86400000 ms
    final int dayIndex = (now.millisecondsSinceEpoch / 86400000).floor();
    
    _challenges.clear();
    const int activeCount = 5;
    const int totalCount = 15;
    final int startIndex = (dayIndex * activeCount) % totalCount;
    
    final Set<String> activeIds = {};
    for (int i = 0; i < activeCount; i++) {
      activeIds.add(_allChallenges[(startIndex + i) % totalCount].id);
    }

    for (var baseChallenge in _allChallenges) {
      final bool active = activeIds.contains(baseChallenge.id);
      _challenges.add(ChallengeData(
        id: baseChallenge.id,
        title: baseChallenge.title,
        subjectId: baseChallenge.subjectId,
        chapterId: baseChallenge.chapterId,
        difficulty: baseChallenge.difficulty,
        xpReward: baseChallenge.xpReward,
        coinsReward: baseChallenge.coinsReward,
        isActive: active,
      ));
    }
  }

  @override
  void initState() {
    super.initState();
    _initializeDailyChallenges();
    _tabController = TabController(length: 4, vsync: this);
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging) {
        setState(() {});
      }
    });
    _searchController.addListener(() {
      setState(() {});
    });
    _loadUserChallenges();
  }

  @override
  void dispose() {
    _tabController.dispose();
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadUserChallenges() async {
    if (mounted) setState(() => _isLoading = true);
    try {
      final progress = await AuthService.getChallengesProgressWithReset();
      _userChallengesProgress = progress;

      // Update local challenge objects status and indices
      for (var challenge in _challenges) {
        if (progress.containsKey(challenge.id)) {
          final progMap = progress[challenge.id] as Map<dynamic, dynamic>;
          challenge.status = progMap['status'] ?? 'pending';
          challenge.currentIndex = progMap['currentIndex'] ?? 0;
          challenge.score = progMap['score'] ?? 0;
        } else {
          challenge.status = 'pending';
          challenge.currentIndex = 0;
          challenge.score = 0;
        }
      }
    } catch (e) {
      debugPrint("Error loading user challenges: $e");
    }
    if (mounted) setState(() => _isLoading = false);
  }

  List<ChallengeData> getFilteredChallenges() {
    final query = _searchController.text.toLowerCase().trim();
    List<ChallengeData> list = List.from(_challenges);

    if (query.isNotEmpty) {
      list = list.where((c) => c.title.toLowerCase().contains(query)).toList();
    }

    final tabIndex = _tabController.index;
    if (tabIndex == 0) {
      // Sort active ones first
      list.sort((a, b) {
        if (a.isActive && !b.isActive) return -1;
        if (!a.isActive && b.isActive) return 1;
        return 0;
      });
      return list;
    }
    if (tabIndex == 1) {
      return list.where((c) => c.status == 'pending' && c.isActive).toList();
    }
    if (tabIndex == 2) {
      return list.where((c) => c.status == 'in_progress').toList();
    }
    return list.where((c) => c.status == 'completed').toList();
  }

  Future<void> _startChallenge(ChallengeData challenge) async {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => const Center(child: CircularProgressIndicator(color: Colors.cyanAccent)),
    );

    try {
      final questions = await FirebaseService().getChallengeQuestions(
        challenge.subjectId,
        challenge.chapterId,
      );

      if (mounted) Navigator.pop(context); // Close loading dialog

      if (questions.isEmpty) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text("Could not load questions for this challenge. Try again later.")),
          );
        }
        return;
      }

      // Take first 22 questions
      questions.shuffle();
      final selectedQuestions = questions.take(22).toList();

      // Save to database
      await AuthService.saveChallengeProgress(
        challengeId: challenge.id,
        status: 'in_progress',
        currentIndex: 0,
        score: 0,
        questions: selectedQuestions.map((q) => q.toMap()).toList(),
      );

      // Navigate
      if (mounted) {
        await Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ChallengeQuizScreen(
              challengeId: challenge.id,
              title: challenge.title,
              questions: selectedQuestions,
              initialIndex: 0,
              initialScore: 0,
              xpReward: challenge.xpReward,
              coinsReward: challenge.coinsReward,
            ),
          ),
        );
        _loadUserChallenges(); // Reload when returning
      }
    } catch (e) {
      if (mounted) {
        Navigator.pop(context); // Close loading dialog
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Error launching challenge: $e")),
        );
      }
    }
  }

  Future<void> _resumeChallenge(ChallengeData challenge) async {
    final progress = _userChallengesProgress[challenge.id] as Map<dynamic, dynamic>?;
    if (progress == null) return;

    final int index = progress['currentIndex'] ?? 0;
    final int score = progress['score'] ?? 0;
    final List<dynamic> rawQuestions = progress['questions'] ?? [];

    final List<Question> loadedQuestions = rawQuestions.asMap().entries.map((entry) {
      return Question.fromMap(entry.key.toString(), entry.value as Map);
    }).toList();

    if (mounted) {
      await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ChallengeQuizScreen(
            challengeId: challenge.id,
            title: challenge.title,
            questions: loadedQuestions,
            initialIndex: index,
            initialScore: score,
            xpReward: challenge.xpReward,
            coinsReward: challenge.coinsReward,
          ),
        ),
      );
      _loadUserChallenges(); // Reload when returning
    }
  }

  @override
  Widget build(BuildContext context) {
    final displayChallenges = getFilteredChallenges();

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
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: Column(
                    children: [
                      _buildSearchBar(),
                      const SizedBox(height: 20),
                      _buildTabs(),
                      const SizedBox(height: 20),
                      _buildSortingHeader(displayChallenges.length),
                      Expanded(
                        child: _isLoading
                            ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                            : displayChallenges.isEmpty
                                ? Center(
                                    child: Text(
                                      "No challenges found in this section.",
                                      style: GoogleFonts.outfit(color: Colors.white38, fontSize: 16),
                                    ),
                                  )
                                : ListView.builder(
                                    physics: const BouncingScrollPhysics(),
                                    itemCount: displayChallenges.length,
                                    itemBuilder: (context, index) {
                                      return _buildChallengeCard(displayChallenges[index], index);
                                    },
                                  ),
                      ),
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
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Text(
            "Daily Challenges",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48),
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildSearchBar() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.08),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: TextField(
        controller: _searchController,
        style: const TextStyle(color: Colors.white),
        decoration: InputDecoration(
          icon: const Icon(Icons.search_rounded, color: Colors.white54),
          hintText: "Search challenges...",
          hintStyle: GoogleFonts.outfit(color: Colors.white38),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 18),
        ),
      ),
    ).animate().fadeIn(delay: 200.ms).slideX(begin: 0.1);
  }

  Widget _buildTabs() {
    return TabBar(
      controller: _tabController,
      isScrollable: true,
      dividerColor: Colors.transparent,
      indicatorColor: Colors.cyanAccent,
      indicatorWeight: 3,
      labelColor: Colors.cyanAccent,
      unselectedLabelColor: Colors.white38,
      labelStyle: GoogleFonts.outfit(fontWeight: FontWeight.bold),
      tabs: const [
        Tab(text: "All"),
        Tab(text: "Pending"),
        Tab(text: "In Process"),
        Tab(text: "Completed"),
      ],
    ).animate().fadeIn(delay: 400.ms);
  }

  Widget _buildSortingHeader(int count) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 10),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            "$count Available",
            style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16),
          ),
          Row(
            children: [
              const Icon(Icons.star_rounded, color: Colors.amberAccent, size: 20),
              const SizedBox(width: 6),
              Text(
                "Earn Rewards",
                style: GoogleFonts.outfit(color: Colors.amberAccent, fontSize: 14, fontWeight: FontWeight.bold),
              ),
            ],
          ),
        ],
      ),
    ).animate().fadeIn(delay: 500.ms);
  }

  Widget _buildChallengeCard(ChallengeData challenge, int index) {
    bool isCompleted = challenge.status == 'completed';
    bool isInProgress = challenge.status == 'in_progress';
    bool isLocked = !challenge.isActive;

    String actionText = "Start now";
    if (isInProgress) actionText = "Resume";
    if (isCompleted) actionText = "Done";
    if (isLocked) actionText = "Locked";

    String statusDetailText = "Not Started yet";
    if (isInProgress) statusDetailText = "In Progress (${challenge.currentIndex}/22)";
    if (isCompleted) statusDetailText = "Completed";
    if (isLocked) statusDetailText = "Locked: Cycles weekly";

    Color tagColor = challenge.difficulty.toLowerCase() == "easy"
        ? Colors.cyanAccent
        : challenge.difficulty.toLowerCase() == "medium"
            ? Colors.amberAccent
            : Colors.redAccent;
    if (isLocked) tagColor = Colors.white38;

    return Container(
      margin: const EdgeInsets.only(bottom: 15),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(25),
        border: Border.all(
          color: isCompleted
              ? Colors.cyanAccent.withOpacity(0.3)
              : isLocked
                  ? Colors.white.withOpacity(0.02)
                  : Colors.white.withOpacity(0.1),
          width: isCompleted ? 1.5 : 1.0,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 10,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: isLocked
                  ? Colors.white.withOpacity(0.02)
                  : isCompleted
                      ? Colors.cyanAccent.withOpacity(0.1)
                      : isInProgress
                          ? Colors.orangeAccent.withOpacity(0.1)
                          : Colors.white10,
              shape: BoxShape.circle,
            ),
            child: Icon(
              isLocked
                  ? Icons.lock_rounded
                  : isCompleted
                      ? Icons.check_circle_rounded
                      : isInProgress
                          ? Icons.play_circle_fill_rounded
                          : Icons.lock_open_rounded,
              color: isLocked
                  ? Colors.white24
                  : isCompleted
                      ? Colors.cyanAccent
                      : isInProgress
                          ? Colors.orangeAccent
                          : Colors.white38,
              size: 30,
            ),
          ),
          const SizedBox(width: 15),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  challenge.title,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: GoogleFonts.outfit(
                    color: isLocked ? Colors.white38 : Colors.white,
                    fontSize: 17,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: tagColor.withOpacity(0.15),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        challenge.difficulty.toUpperCase(),
                        style: GoogleFonts.outfit(color: tagColor, fontSize: 10, fontWeight: FontWeight.bold),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        statusDetailText,
                        style: GoogleFonts.outfit(
                          color: isCompleted
                              ? Colors.cyanAccent
                              : isInProgress
                                  ? Colors.orangeAccent
                                  : Colors.white38,
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(width: 10),
          ElevatedButton(
            onPressed: isLocked
                ? () {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text("This challenge is locked. Active challenges change every 7 days!"),
                        backgroundColor: Colors.indigo,
                      ),
                    );
                  }
                : isCompleted
                    ? () {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text("You have already completed this challenge today!"),
                            backgroundColor: Colors.cyan,
                          ),
                        );
                      }
                    : () {
                        if (isInProgress) {
                          _resumeChallenge(challenge);
                        } else {
                          _startChallenge(challenge);
                        }
                      },
            style: ElevatedButton.styleFrom(
              backgroundColor: isLocked
                  ? Colors.white.withOpacity(0.05)
                  : isCompleted
                      ? Colors.cyanAccent.withOpacity(0.2)
                      : isInProgress
                          ? Colors.orangeAccent
                          : Colors.cyanAccent,
              foregroundColor: isLocked
                  ? Colors.white24
                  : isCompleted
                      ? Colors.cyanAccent
                      : Colors.black,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              elevation: 0,
            ),
            child: Text(
              actionText,
              style: GoogleFonts.outfit(
                fontWeight: FontWeight.bold,
                fontSize: 13,
                color: isLocked ? Colors.white38 : null,
              ),
            ),
          ),
        ],
      ),
    ).animate().fadeIn(delay: (300 + index * 100).ms).slideY(begin: 0.1);
  }
}

class ChallengeData {
  final String id;
  final String title;
  final String subjectId;
  final String chapterId;
  final String difficulty;
  final int xpReward;
  final int coinsReward;
  String status; // 'pending', 'in_progress', 'completed'
  int currentIndex;
  int score;
  final bool isActive;

  ChallengeData({
    required this.id,
    required this.title,
    required this.subjectId,
    required this.chapterId,
    required this.difficulty,
    required this.xpReward,
    required this.coinsReward,
    this.status = 'pending',
    this.currentIndex = 0,
    this.score = 0,
    this.isActive = true,
  });
}
