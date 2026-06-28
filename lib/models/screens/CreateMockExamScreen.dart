import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/firebase_service.dart';
import '../subject.dart';
import 'MockExamQuestionScreen.dart';

class CreateMockExamScreen extends StatefulWidget {
  const CreateMockExamScreen({super.key});

  @override
  State<CreateMockExamScreen> createState() => _CreateMockExamScreenState();
}

class _CreateMockExamScreenState extends State<CreateMockExamScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  List<Subject> _subjects = [];
  String? _selectedSubjectId;
  String _selectedSubjectName = "";
  bool _isLoading = true;

  int _duration = 30;
  int _easyCount = 1;
  int _mediumCount = 1;
  int _hardCount = 1;

  @override
  void initState() {
    super.initState();
    _loadSubjects();
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
          _isLoading = false;
        });
      }
    });
  }

  int get _totalQuestions => _easyCount + _mediumCount + _hardCount;



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
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                    : SingleChildScrollView(
                        padding: const EdgeInsets.symmetric(horizontal: 25.0),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const SizedBox(height: 10),
                            _buildSectionTitle("Configure your mock exam"),
                            const SizedBox(height: 20),
                            _buildSubjectDropdown(),
                            const SizedBox(height: 15),
                            _buildDurationSlider(),
                            const SizedBox(height: 30),
                            _buildSectionTitle("Difficulty Distribution"),
                            const SizedBox(height: 10),
                            Text(
                              "Total questions must be between 15 and 45",
                              style: GoogleFonts.outfit(color: Colors.white54, fontSize: 12),
                            ),
                            const SizedBox(height: 20),
                            _buildDifficultySlider("Easy Questions (1-15)", _easyCount.toDouble(), 1, 15, Colors.greenAccent, (val) {
                              setState(() {
                                int newVal = val.toInt();
                                if (newVal + _mediumCount + _hardCount <= 45) {
                                  _easyCount = newVal;
                                }
                              });
                            }),
                            _buildDifficultySlider("Medium Questions (1-20)", _mediumCount.toDouble(), 1, 20, Colors.orangeAccent, (val) {
                              setState(() {
                                int newVal = val.toInt();
                                if (_easyCount + newVal + _hardCount <= 45) {
                                  _mediumCount = newVal;
                                }
                              });
                            }),
                            _buildDifficultySlider("Hard Questions (1-10)", _hardCount.toDouble(), 1, 10, Colors.redAccent, (val) {
                              setState(() {
                                int newVal = val.toInt();
                                if (_easyCount + _mediumCount + newVal <= 45) {
                                  _hardCount = newVal;
                                }
                              });
                            }),
                            const SizedBox(height: 30),
                            _buildExamSummary(),
                            const SizedBox(height: 30),
                            _buildCreateButton(),
                            const SizedBox(height: 40),
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
            "Create Mock Exam",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48),
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
    ).animate().fadeIn(delay: 200.ms);
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
          min: 10,
          max: 120,
          divisions: 11,
          activeColor: Colors.cyanAccent,
          inactiveColor: Colors.white10,
          onChanged: (val) => setState(() => _duration = val.toInt()),
        ),
      ],
    ).animate().fadeIn(delay: 400.ms).slideX(begin: 0.1);
  }

  Widget _buildDifficultySlider(String label, double value, double min, double max, Color color, Function(double) onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(label, style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14)),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 2),
              decoration: BoxDecoration(color: color.withOpacity(0.1), borderRadius: BorderRadius.circular(10)),
              child: Text(value.toInt().toString(), style: TextStyle(color: color, fontWeight: FontWeight.bold)),
            ),
          ],
        ),
        SliderTheme(
          data: SliderThemeData(
            trackHeight: 4,
            thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 8),
            activeTrackColor: color,
            inactiveTrackColor: Colors.white10,
            thumbColor: color,
          ),
          child: Slider(
            value: value,
            min: min,
            max: max,
            onChanged: onChanged,
          ),
        ),
        const SizedBox(height: 10),
      ],
    ).animate().fadeIn(delay: 500.ms);
  }

  Widget _buildExamSummary() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(25),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.1),
        borderRadius: BorderRadius.circular(25),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Exam Summary",
            style: GoogleFonts.outfit(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 20),
          _buildSummaryItem("Total Questions", _totalQuestions.toString(), Colors.white),
          _buildSummaryItem("Duration", "$_duration minutes", Colors.white),
          const Divider(color: Colors.white10, height: 30),
          _buildSummaryItem("Easy", "$_easyCount", Colors.greenAccent),
          _buildSummaryItem("Medium", "$_mediumCount", Colors.orangeAccent),
          _buildSummaryItem("Hard", "$_hardCount", Colors.redAccent),
        ],
      ),
    ).animate().fadeIn(delay: 600.ms).scale(curve: Curves.easeOutBack);
  }

  Widget _buildSummaryItem(String label, String value, Color color) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: GoogleFonts.outfit(color: Colors.white60, fontSize: 14)),
          Text(value, style: GoogleFonts.outfit(color: color, fontSize: 14, fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }

  Widget _buildCreateButton() {
    bool isValid = _totalQuestions >= 15 && _totalQuestions <= 45;

    return SizedBox(
      width: double.infinity,
      child: ElevatedButton(
        onPressed: isValid ? () {
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(
              builder: (context) => MockExamQuestionScreen(
                subjectId: _selectedSubjectId!,
                subjectName: _selectedSubjectName,
                distribution: {
                  'Easy': _easyCount,
                  'Medium': _mediumCount,
                  'Hard': _hardCount,
                },
                durationMinutes: _duration,
              ),
            ),
          );
        } : null,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.cyanAccent,
          foregroundColor: Colors.black,
          disabledBackgroundColor: Colors.white10,
          padding: const EdgeInsets.symmetric(vertical: 20),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          elevation: 8,
          shadowColor: Colors.cyanAccent.withOpacity(0.5),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.edit_note_rounded),
            const SizedBox(width: 10),
            Text(
              "Create Mock Exam",
              style: GoogleFonts.outfit(fontSize: 16, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    ).animate().fadeIn(delay: 800.ms).slideY(begin: 0.2);
  }
}
