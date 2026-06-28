import 'package:flutter/material.dart';
import '../services/firebase_service.dart';
import '../models/subject.dart';
import '../models/chapter.dart';

class AddQuestionScreen extends StatefulWidget {
  const AddQuestionScreen({super.key});

  @override
  State<AddQuestionScreen> createState() => _AddQuestionScreenState();
}

class _AddQuestionScreenState extends State<AddQuestionScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  final _questionController = TextEditingController();
  final _optA = TextEditingController();
  final _optB = TextEditingController();
  final _optC = TextEditingController();
  final _optD = TextEditingController();

  String? _selectedSubjectId;
  String? _selectedChapterId;
  String _selectedCorrect = 'a';
  String _selectedDifficulty = 'easy';
  bool _isLoading = false;

  void _submit() async {
    if (_selectedSubjectId == null || _selectedChapterId == null || _questionController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Please fill all fields')));
      return;
    }

    setState(() => _isLoading = true);
    try {
      await _firebaseService.addQuestion(
        subjectId: _selectedSubjectId!,
        chapterId: _selectedChapterId!,
        question: _questionController.text,
        options: {
          'a': _optA.text,
          'b': _optB.text,
          'c': _optC.text,
          'd': _optD.text,
        },
        correctAnswer: _selectedCorrect,
        difficultyLevel: _selectedDifficulty,
      );
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Question added!')));
        _questionController.clear();
        _optA.clear();
        _optB.clear();
        _optC.clear();
        _optD.clear();
      }
    } catch (e) {
      if (mounted) ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error: $e')));
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: const Text('Add Question', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF1A237E), Color(0xFF311B92)],
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              children: [
                // Subject Dropdown
                StreamBuilder<List<Subject>>(
                  stream: _firebaseService.getSubjects(),
                  builder: (context, snapshot) {
                    final subjects = snapshot.data ?? [];
                    return DropdownButtonFormField<String>(
                      value: _selectedSubjectId,
                      dropdownColor: const Color(0xFF311B92),
                      style: const TextStyle(color: Colors.white),
                      decoration: _inputDecoration('Select Subject'),
                      items: subjects.map((s) => DropdownMenuItem(value: s.id, child: Text(s.name))).toList(),
                      onChanged: (val) {
                        setState(() {
                          _selectedSubjectId = val;
                          _selectedChapterId = null;
                        });
                      },
                    );
                  },
                ),
                const SizedBox(height: 16),
                // Chapter Dropdown
                if (_selectedSubjectId != null)
                  StreamBuilder<List<Chapter>>(
                    stream: _firebaseService.getChapters(_selectedSubjectId!),
                    builder: (context, snapshot) {
                      final chapters = snapshot.data ?? [];
                      return DropdownButtonFormField<String>(
                        value: _selectedChapterId,
                        dropdownColor: const Color(0xFF311B92),
                        style: const TextStyle(color: Colors.white),
                        decoration: _inputDecoration('Select Chapter'),
                        items: chapters.map((c) => DropdownMenuItem(value: c.id, child: Text(c.title))).toList(),
                        onChanged: (val) => setState(() => _selectedChapterId = val),
                      );
                    },
                  ),
                const SizedBox(height: 16),
                TextField(controller: _questionController, style: const TextStyle(color: Colors.white), decoration: _inputDecoration('Question'), maxLines: 2),
                const SizedBox(height: 16),
                TextField(controller: _optA, style: const TextStyle(color: Colors.white), decoration: _inputDecoration('Option A')),
                const SizedBox(height: 8),
                TextField(controller: _optB, style: const TextStyle(color: Colors.white), decoration: _inputDecoration('Option B')),
                const SizedBox(height: 8),
                TextField(controller: _optC, style: const TextStyle(color: Colors.white), decoration: _inputDecoration('Option C')),
                const SizedBox(height: 8),
                TextField(controller: _optD, style: const TextStyle(color: Colors.white), decoration: _inputDecoration('Option D')),
                const SizedBox(height: 16),
                Row(
                  children: [
                    Expanded(
                      child: DropdownButtonFormField<String>(
                        value: _selectedCorrect,
                        dropdownColor: const Color(0xFF311B92),
                        style: const TextStyle(color: Colors.white),
                        decoration: _inputDecoration('Correct Answer'),
                        items: ['a', 'b', 'c', 'd'].map((o) => DropdownMenuItem(value: o, child: Text('Option ${o.toUpperCase()}'))).toList(),
                        onChanged: (val) => setState(() => _selectedCorrect = val!),
                      ),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: DropdownButtonFormField<String>(
                        value: _selectedDifficulty,
                        dropdownColor: const Color(0xFF311B92),
                        style: const TextStyle(color: Colors.white),
                        decoration: _inputDecoration('Difficulty'),
                        items: ['easy', 'medium', 'hard'].map((l) => DropdownMenuItem(value: l, child: Text(l.toUpperCase()))).toList(),
                        onChanged: (val) => setState(() => _selectedDifficulty = val!),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 32),
                SizedBox(
                  width: double.infinity,
                  height: 56,
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _submit,
                    style: ElevatedButton.styleFrom(backgroundColor: Colors.orangeAccent.shade700, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16))),
                    child: _isLoading ? const CircularProgressIndicator(color: Colors.white) : const Text('Add Question', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white)),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  InputDecoration _inputDecoration(String label) {
    return InputDecoration(
      labelText: label,
      labelStyle: TextStyle(color: Colors.white.withOpacity(0.7)),
      filled: true,
      fillColor: Colors.white.withOpacity(0.1),
      enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(16), borderSide: BorderSide(color: Colors.white.withOpacity(0.3))),
      focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(16), borderSide: const BorderSide(color: Colors.white)),
    );
  }
}
