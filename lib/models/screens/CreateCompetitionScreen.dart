import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import '../../services/auth_service.dart';
import '../../services/firebase_service.dart';
import '../subject.dart';
import 'CompetitionLobbyScreen.dart';

class CreateCompetitionScreen extends StatefulWidget {
  const CreateCompetitionScreen({super.key});

  @override
  State<CreateCompetitionScreen> createState() => _CreateCompetitionScreenState();
}

class _CreateCompetitionScreenState extends State<CreateCompetitionScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  final _formKey = GlobalKey<FormState>();
  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _descriptionController = TextEditingController();
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = "";

  List<Subject> _subjects = [];
  String? _selectedSubjectId;
  String _selectedSubjectName = "";
  
  int _questionCount = 10;
  int _duration = 15;

  List<FriendData> _friendsList = [];
  List<FriendData> _allUsersList = [];
  final List<String> _selectedFriendEmails = [];
  
  bool _isLoadingSubjects = true;
  bool _isLoadingFriends = true;
  bool _isCreating = false;

  @override
  void initState() {
    super.initState();
    _loadSubjects();
    _loadFriends();
  }

  @override
  void dispose() {
    _titleController.dispose();
    _descriptionController.dispose();
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadSubjects() async {
    _firebaseService.getSubjects().listen((subjects) {
      if (mounted) {
        setState(() {
          _subjects = subjects;
          if (_subjects.isNotEmpty && _selectedSubjectId == null) {
            _selectedSubjectId = _subjects[0].id;
            _selectedSubjectName = _subjects[0].name;
          }
          _isLoadingSubjects = false;
        });
      }
    });
  }

  Future<void> _loadFriends() async {
    final user = AuthService.currentUser;
    if (user == null) return;

    try {
      final myEmail = user.email;
      final myKey = AuthService.sanitizeEmail(myEmail);

      final snapshot = await _dbRef.child('Users').get();
      if (!snapshot.exists || snapshot.value == null) {
        if (mounted) setState(() => _isLoadingFriends = false);
        return;
      }

      final Map<dynamic, dynamic> allUsersMap = snapshot.value as Map<dynamic, dynamic>;
      final myUserMap = allUsersMap[myKey] as Map<dynamic, dynamic>? ?? {};
      final Map<dynamic, dynamic> myFriendsKeysMap = myUserMap['friends'] as Map<dynamic, dynamic>? ?? {};

      final List<FriendData> tempFriends = [];
      final List<FriendData> tempAllUsers = [];

      allUsersMap.forEach((key, value) {
        final userMap = value as Map<dynamic, dynamic>;
        final String email = userMap['email'] ?? '';
        final String fullName = userMap['fullName'] ?? 'User';
        final String xp = (userMap['xp'] ?? 0).toString();

        final sanitizedEmail = AuthService.sanitizeEmail(email);

        if (email.toLowerCase() != myEmail.toLowerCase()) {
          final friend = FriendData(
            name: fullName,
            email: email,
            xp: xp,
          );
          tempAllUsers.add(friend);
          if (myFriendsKeysMap.containsKey(sanitizedEmail)) {
            tempFriends.add(friend);
          }
        }
      });

      if (mounted) {
        setState(() {
          _friendsList = tempFriends;
          _allUsersList = tempAllUsers;
          _isLoadingFriends = false;
        });
      }
    } catch (e) {
      debugPrint("Error loading friends list: $e");
      if (mounted) setState(() => _isLoadingFriends = false);
    }
  }

  Future<void> _generateCompetition() async {
    if (!_formKey.currentState!.validate()) return;
    if (_selectedSubjectId == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please select a subject."), backgroundColor: Colors.redAccent),
      );
      return;
    }

    setState(() => _isCreating = true);

    try {
      // 1. Fetch questions of mixed difficulties
      final questions = await _firebaseService.getCompetitionQuestions(_selectedSubjectId!, _questionCount);

      if (questions.isEmpty) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: Text("Could not retrieve questions for this subject. Try another subject!"),
              backgroundColor: Colors.redAccent,
            ),
          );
          setState(() => _isCreating = false);
        }
        return;
      }

      // 2. Create the competition in Firebase RTDB
      final Map<String, String> invitedFriendsMap = {};
      for (var email in _selectedFriendEmails) {
        final friend = _allUsersList.firstWhere(
          (f) => f.email == email,
          orElse: () => FriendData(name: email, email: email, xp: "0"),
        );
        invitedFriendsMap[email] = friend.name;
      }

      final compId = await _firebaseService.createCompetition(
        title: _titleController.text.trim(),
        description: _descriptionController.text.trim(),
        subjectId: _selectedSubjectId!,
        subjectName: _selectedSubjectName,
        durationMinutes: _duration,
        questionCount: _questionCount,
        invitedFriends: invitedFriendsMap,
        questions: questions,
      );

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text("Competition generated successfully!"), backgroundColor: Colors.cyan),
        );
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => CompetitionLobbyScreen(
              competitionId: compId,
            ),
          ),
        );
      }
    } catch (e) {
      debugPrint("Error creating competition: $e");
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Error: $e"), backgroundColor: Colors.redAccent),
        );
        setState(() => _isCreating = false);
      }
    }
  }

  void _toggleFriendSelection(FriendData friend) {
    final email = friend.email;
    setState(() {
      if (_selectedFriendEmails.contains(email)) {
        _selectedFriendEmails.remove(email);
      } else {
        if (_selectedFriendEmails.length >= 2) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: Text("You can invite a maximum of 2 friends."),
              backgroundColor: Colors.amber,
              duration: Duration(seconds: 2),
            ),
          );
        } else {
          _selectedFriendEmails.add(email);
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final bool isReady = !_isLoadingSubjects && !_isLoadingFriends;

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
                child: _isCreating
                    ? const Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            CircularProgressIndicator(color: Colors.cyanAccent),
                            SizedBox(height: 20),
                            Text(
                              "Generating competition and questions...",
                              style: TextStyle(color: Colors.white70, fontSize: 16),
                            ),
                          ],
                        ),
                      )
                    : !isReady
                        ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                        : SingleChildScrollView(
                            physics: const BouncingScrollPhysics(),
                            padding: const EdgeInsets.symmetric(horizontal: 25.0),
                            child: Form(
                              key: _formKey,
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  const SizedBox(height: 10),
                                  _buildSectionTitle("Competition details"),
                                  const SizedBox(height: 20),
                                  _buildTextField(
                                    controller: _titleController,
                                    hintText: "Title (e.g. History Battle)",
                                    validator: (val) {
                                      if (val == null || val.trim().isEmpty) return "Title is required";
                                      return null;
                                    },
                                  ),
                                  const SizedBox(height: 15),
                                  _buildTextField(
                                    controller: _descriptionController,
                                    hintText: "Description (e.g. Let's see who is the master of History!)",
                                    maxLines: 3,
                                  ),
                                  const SizedBox(height: 20),
                                  _buildSectionTitle("Configuration"),
                                  const SizedBox(height: 15),
                                  _buildSubjectDropdown(),
                                  const SizedBox(height: 15),
                                  _buildQuestionsSlider(),
                                  const SizedBox(height: 15),
                                  _buildDurationSlider(),
                                  const SizedBox(height: 25),
                                  _buildSectionTitle("Invite friends (Max 2)"),
                                  const SizedBox(height: 10),
                                  _buildFriendsSelectionArea(),
                                  const SizedBox(height: 40),
                                  _buildGenerateButton(),
                                  const SizedBox(height: 40),
                                ],
                              ),
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
            "Create Competition",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48), // Spacer to balance back button
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildSectionTitle(String title) {
    return Text(
      title,
      style: GoogleFonts.outfit(
        color: Colors.white,
        fontSize: 18,
        fontWeight: FontWeight.w600,
      ),
    ).animate().fadeIn(delay: 100.ms);
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String hintText,
    int maxLines = 1,
    String? Function(String?)? validator,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 4),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: TextFormField(
        controller: controller,
        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
        maxLines: maxLines,
        validator: validator,
        decoration: InputDecoration(
          hintText: hintText,
          hintStyle: GoogleFonts.outfit(color: Colors.white38),
          border: InputBorder.none,
        ),
      ),
    ).animate().fadeIn(delay: 200.ms).slideX(begin: 0.1);
  }

  Widget _buildSubjectDropdown() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: DropdownButtonHideUnderline(
        child: DropdownButton<String>(
          value: _selectedSubjectId,
          dropdownColor: const Color(0xFF312E81),
          icon: const Icon(Icons.keyboard_arrow_down_rounded, color: Colors.white54),
          style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
          items: _subjects.map((sub) {
            return DropdownMenuItem<String>(
              value: sub.id,
              child: Row(
                children: [
                  Icon(sub.icon, color: sub.iconColor, size: 20),
                  const SizedBox(width: 15),
                  Text(sub.name),
                ],
              ),
            );
          }).toList(),
          onChanged: (val) {
            setState(() {
              _selectedSubjectId = val;
              _selectedSubjectName = _subjects.firstWhere((s) => s.id == val).name;
            });
          },
        ),
      ),
    ).animate().fadeIn(delay: 250.ms).slideX(begin: 0.1);
  }

  Widget _buildQuestionsSlider() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text("Number of Questions", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14)),
            Text("$_questionCount Qs", style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold)),
          ],
        ),
        Slider(
          value: _questionCount.toDouble(),
          min: 5,
          max: 30,
          divisions: 5,
          activeColor: Colors.cyanAccent,
          inactiveColor: Colors.white10,
          onChanged: (val) => setState(() => _questionCount = val.toInt()),
        ),
      ],
    ).animate().fadeIn(delay: 300.ms).slideX(begin: 0.1);
  }

  Widget _buildDurationSlider() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text("Duration (minutes)", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14)),
            Text("$_duration min", style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold)),
          ],
        ),
        Slider(
          value: _duration.toDouble(),
          min: 5,
          max: 60,
          divisions: 11,
          activeColor: Colors.cyanAccent,
          inactiveColor: Colors.white10,
          onChanged: (val) => setState(() => _duration = val.toInt()),
        ),
      ],
    ).animate().fadeIn(delay: 350.ms).slideX(begin: 0.1);
  }

  Widget _buildFriendsSelectionArea() {
    final displayList = _searchQuery.isEmpty
        ? _friendsList
        : _allUsersList.where((u) {
            final q = _searchQuery.toLowerCase();
            return u.name.toLowerCase().contains(q) || u.email.toLowerCase().contains(q);
          }).toList();

    return Column(
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.05),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
          ),
          child: TextField(
            controller: _searchController,
            style: GoogleFonts.outfit(color: Colors.white, fontSize: 15),
            decoration: InputDecoration(
              hintText: "Search friends or users by name/email...",
              hintStyle: GoogleFonts.outfit(color: Colors.white38),
              prefixIcon: const Icon(Icons.search_rounded, color: Colors.white38),
              suffixIcon: _searchQuery.isNotEmpty
                  ? IconButton(
                      icon: const Icon(Icons.close_rounded, color: Colors.white38),
                      onPressed: () {
                        setState(() {
                          _searchController.clear();
                          _searchQuery = "";
                        });
                      },
                    )
                  : null,
              border: InputBorder.none,
            ),
            onChanged: (val) {
              setState(() {
                _searchQuery = val;
              });
            },
          ),
        ).animate().fadeIn(delay: 400.ms),
        const SizedBox(height: 15),
        if (displayList.isEmpty)
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.03),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: Colors.white.withOpacity(0.05)),
            ),
            child: Center(
              child: Text(
                _searchQuery.isEmpty
                    ? "No friends added yet. Type above to search all users!"
                    : "No users found matching \"$_searchQuery\".",
                textAlign: TextAlign.center,
                style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
              ),
            ),
          ).animate().fadeIn()
        else
          ListView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: displayList.length,
            itemBuilder: (context, index) {
              final friend = displayList[index];
              final isSelected = _selectedFriendEmails.contains(friend.email);

              return Container(
                margin: const EdgeInsets.only(bottom: 10),
                decoration: BoxDecoration(
                  color: isSelected ? Colors.cyanAccent.withOpacity(0.08) : Colors.white.withOpacity(0.03),
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(
                    color: isSelected ? Colors.cyanAccent.withOpacity(0.3) : Colors.white.withOpacity(0.05),
                  ),
                ),
                child: ListTile(
                  onTap: () => _toggleFriendSelection(friend),
                  leading: CircleAvatar(
                    backgroundColor: isSelected ? Colors.cyanAccent : Colors.white10,
                    foregroundColor: isSelected ? Colors.black : Colors.white,
                    child: Text(friend.name.isNotEmpty ? friend.name[0].toUpperCase() : 'F'),
                  ),
                  title: Text(
                    friend.name,
                    style: GoogleFonts.outfit(
                      color: isSelected ? Colors.white : Colors.white70,
                      fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                    ),
                  ),
                  subtitle: Text("XP: ${friend.xp}", style: GoogleFonts.outfit(color: Colors.white38, fontSize: 12)),
                  trailing: Checkbox(
                    value: isSelected,
                    activeColor: Colors.cyanAccent,
                    checkColor: Colors.black,
                    onChanged: (val) => _toggleFriendSelection(friend),
                  ),
                ),
              );
            },
          ).animate().fadeIn(),
      ],
    );
  }

  Widget _buildGenerateButton() {
    return SizedBox(
      width: double.infinity,
      child: ElevatedButton(
        onPressed: _generateCompetition,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.cyanAccent,
          foregroundColor: Colors.black,
          padding: const EdgeInsets.symmetric(vertical: 20),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          elevation: 8,
          shadowColor: Colors.cyanAccent.withOpacity(0.4),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.flash_on_rounded),
            const SizedBox(width: 10),
            Text(
              "Generate Quiz",
              style: GoogleFonts.outfit(fontSize: 16, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    ).animate().fadeIn(delay: 450.ms).slideY(begin: 0.1);
  }
}

class FriendData {
  final String name;
  final String email;
  final String xp;

  FriendData({
    required this.name,
    required this.email,
    required this.xp,
  });
}
