import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import '../services/firebase_service.dart';
import '../models/subject.dart';
import '../models/paper.dart';

class AddPaperScreen extends StatefulWidget {
  const AddPaperScreen({super.key});

  @override
  State<AddPaperScreen> createState() => _AddPaperScreenState();
}

class _AddPaperScreenState extends State<AddPaperScreen> with SingleTickerProviderStateMixin {
  final _formKey = GlobalKey<FormState>();
  final _firebaseService = FirebaseService();

  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _subjectController = TextEditingController();
  final TextEditingController _urlController = TextEditingController();

  String _selectedYear = '2025';
  
  bool _isLoading = false;
  late TabController _tabController;

  // File Picker variables
  String? _selectedFileName;
  Uint8List? _selectedFileBytes;

  final List<String> _years = ['2021', '2022', '2023', '2024', '2025'];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    _titleController.dispose();
    _subjectController.dispose();
    _urlController.dispose();
    super.dispose();
  }

  Future<void> _pickFile() async {
    try {
      final result = await FilePicker.platform.pickFiles(
        type: FileType.custom,
        allowedExtensions: ['pdf'],
        withData: true, // Crucial: loads bytes into memory across all platforms
      );

      if (result != null && result.files.isNotEmpty) {
        final file = result.files.first;
        setState(() {
          _selectedFileName = file.name;
          _selectedFileBytes = file.bytes;
        });
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error picking file: $e')),
      );
    }
  }

  void _submit() async {
    if (!_formKey.currentState!.validate()) return;
    
    final subjectName = _subjectController.text.trim();
    if (subjectName.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Please enter a subject name')),
      );
      return;
    }
    final subjectId = subjectName.toLowerCase().replaceAll(' ', '_');

    String pdfUrl = '';

    setState(() => _isLoading = true);

    try {
      if (_tabController.index == 0) {
        // Upload file method
        if (_selectedFileBytes == null || _selectedFileName == null) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Please select a PDF file to upload')),
          );
          setState(() => _isLoading = false);
          return;
        }

        // Upload to Firebase Storage
        final timestamp = DateTime.now().millisecondsSinceEpoch;
        final uniqueFileName = '${timestamp}_$_selectedFileName';
        pdfUrl = await _firebaseService.uploadPaperPdf(uniqueFileName, _selectedFileBytes!);
      } else {
        // Direct URL method
        pdfUrl = _urlController.text.trim();
        if (pdfUrl.isEmpty) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Please enter a PDF URL')),
          );
          setState(() => _isLoading = false);
          return;
        }
      }

      // Add record to Firebase Realtime Database
      final paperId = DateTime.now().millisecondsSinceEpoch.toString();
      final newPaper = Paper(
        id: paperId,
        title: _titleController.text.trim(),
        subjectId: subjectId,
        subjectName: subjectName,
        year: _selectedYear,
        pdfUrl: pdfUrl,
        uploadedAt: DateTime.now().millisecondsSinceEpoch,
      );

      await _firebaseService.addPaper(newPaper);

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Past Paper added successfully! 🎉')),
        );
        Navigator.pop(context);
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error: $e')),
        );
      }
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: const Text('Add Past Paper', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Container(
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF1A237E), Color(0xFF311B92), Color(0xFF4A148C)],
          ),
        ),
        child: SafeArea(
          child: _isLoading
              ? const Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CircularProgressIndicator(color: Colors.white),
                      SizedBox(height: 16),
                      Text(
                        'Uploading & Saving Paper...',
                        style: TextStyle(color: Colors.white70, fontSize: 16, fontWeight: FontWeight.w500),
                      ),
                    ],
                  ),
                )
              : SingleChildScrollView(
                  padding: const EdgeInsets.all(24.0),
                  child: Form(
                    key: _formKey,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // Title Field
                        TextFormField(
                          controller: _titleController,
                          style: const TextStyle(color: Colors.white),
                          decoration: InputDecoration(
                            labelText: 'Paper Title (e.g. Form 4 Afsoomaali Weydiimo)',
                            labelStyle: TextStyle(color: Colors.white.withOpacity(0.7)),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: BorderSide(color: Colors.white.withOpacity(0.3)),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: const BorderSide(color: Colors.white),
                            ),
                            filled: true,
                            fillColor: Colors.white.withOpacity(0.1),
                          ),
                          validator: (value) => value == null || value.isEmpty ? 'Please enter a title' : null,
                        ),
                        const SizedBox(height: 20),

                        // Subject Text Field
                        TextFormField(
                          controller: _subjectController,
                          style: const TextStyle(color: Colors.white),
                          decoration: InputDecoration(
                            labelText: 'Subject Name (e.g. Physics, History, Af-Soomaali)',
                            labelStyle: TextStyle(color: Colors.white.withOpacity(0.7)),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: BorderSide(color: Colors.white.withOpacity(0.3)),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: const BorderSide(color: Colors.white),
                            ),
                            filled: true,
                            fillColor: Colors.white.withOpacity(0.1),
                          ),
                          validator: (value) => value == null || value.isEmpty ? 'Please enter a subject name' : null,
                        ),
                        const SizedBox(height: 20),

                        // Year Selection Dropdown
                        DropdownButtonFormField<String>(
                          dropdownColor: const Color(0xFF311B92),
                          style: const TextStyle(color: Colors.white),
                          value: _selectedYear,
                          decoration: InputDecoration(
                            labelText: 'Academic Year',
                            labelStyle: TextStyle(color: Colors.white.withOpacity(0.7)),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: BorderSide(color: Colors.white.withOpacity(0.3)),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(16),
                              borderSide: const BorderSide(color: Colors.white),
                            ),
                            filled: true,
                            fillColor: Colors.white.withOpacity(0.1),
                          ),
                          items: _years.map((year) {
                            return DropdownMenuItem<String>(
                              value: year,
                              child: Text(year),
                            );
                          }).toList(),
                          onChanged: (val) {
                            if (val != null) {
                              setState(() {
                                _selectedYear = val;
                              });
                            }
                          },
                        ),
                        const SizedBox(height: 30),

                        // Method tabs container
                        const Text(
                          'PDF Document Source',
                          style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 12),
                        Container(
                          decoration: BoxDecoration(
                            color: Colors.white.withOpacity(0.1),
                            borderRadius: BorderRadius.circular(16),
                          ),
                          child: Column(
                            children: [
                              TabBar(
                                controller: _tabController,
                                indicatorColor: Colors.cyanAccent,
                                labelColor: Colors.cyanAccent,
                                unselectedLabelColor: Colors.white70,
                                tabs: const [
                                  Tab(icon: Icon(Icons.cloud_upload_rounded), text: 'Upload PDF'),
                                  Tab(icon: Icon(Icons.link_rounded), text: 'Paste URL'),
                                ],
                              ),
                              SizedBox(
                                height: 160,
                                child: TabBarView(
                                  controller: _tabController,
                                  children: [
                                    // Pick File Tab
                                    Padding(
                                      padding: const EdgeInsets.all(16.0),
                                      child: Column(
                                        mainAxisAlignment: MainAxisAlignment.center,
                                        children: [
                                          ElevatedButton.icon(
                                            onPressed: _pickFile,
                                            icon: const Icon(Icons.file_present_rounded),
                                            label: const Text('Choose PDF File'),
                                            style: ElevatedButton.styleFrom(
                                              backgroundColor: Colors.white.withOpacity(0.15),
                                              foregroundColor: Colors.white,
                                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                                              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                                            ),
                                          ),
                                          const SizedBox(height: 12),
                                          Text(
                                            _selectedFileName ?? 'No file selected (maximum 5MB recommended)',
                                            textAlign: TextAlign.center,
                                            style: TextStyle(
                                              color: _selectedFileName != null ? Colors.cyanAccent : Colors.white60,
                                              fontSize: 13,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                    // Link Tab
                                    Padding(
                                      padding: const EdgeInsets.all(16.0),
                                      child: Center(
                                        child: TextFormField(
                                          controller: _urlController,
                                          style: const TextStyle(color: Colors.white),
                                          decoration: InputDecoration(
                                            labelText: 'Direct PDF URL (http/https)',
                                            labelStyle: TextStyle(color: Colors.white.withOpacity(0.7)),
                                            enabledBorder: OutlineInputBorder(
                                              borderRadius: BorderRadius.circular(12),
                                              borderSide: BorderSide(color: Colors.white.withOpacity(0.3)),
                                            ),
                                            focusedBorder: OutlineInputBorder(
                                              borderRadius: BorderRadius.circular(12),
                                              borderSide: const BorderSide(color: Colors.white),
                                            ),
                                            filled: true,
                                            fillColor: Colors.white.withOpacity(0.05),
                                          ),
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 40),

                        // Submit Button
                        SizedBox(
                          width: double.infinity,
                          height: 56,
                          child: ElevatedButton(
                            onPressed: _submit,
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Colors.blueAccent,
                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                              elevation: 4,
                            ),
                            child: const Text(
                              'Save Past Paper',
                              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
        ),
      ),
    );
  }
}
