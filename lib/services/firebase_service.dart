import 'dart:convert';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_storage/firebase_storage.dart';
import '../models/subject.dart';
import '../models/chapter.dart';
import '../models/question.dart';
import '../models/paper.dart';
import 'seed_data.dart';
import 'auth_service.dart';

class FirebaseService {
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  Future<void> seedDatabase() async {
    final data = jsonDecode(fullSeedJson);
    
    // 1. Clean up
    await _dbRef.child('Subjects').remove();
    await _dbRef.child('subjects').remove();
    await _dbRef.child('chapters').remove();
    await _dbRef.child('questions').remove();

    final Map<String, Map<String, dynamic>> subjectUpdates = {};
    int count = 0;

    void addUpdate(String subjectId, String path, dynamic value) {
      if (!subjectUpdates.containsKey(subjectId)) {
        subjectUpdates[subjectId] = {};
      }
      subjectUpdates[subjectId]![path] = value;
    }

    // 2. Build updates for Subjects and nested chapters/questions
    for (var s in data['subjects']) {
      final String subjectId = s['id'];
      addUpdate(subjectId, 'Subjects/$subjectId/name', s['name']);
      
      if (s['chapters'] != null) {
        int chapIndex = 1;
        for (var c in s['chapters']) {
          final String chapterId = c['id'] ?? '${subjectId}_ch$chapIndex';
          addUpdate(subjectId, 'Subjects/$subjectId/Chapters/$chapterId/title', c['title']);
          
          if (c['questions'] != null) {
            for (var q in c['questions']) {
              final String qId = q['id'];
              addUpdate(subjectId, 'Subjects/$subjectId/Chapters/$chapterId/Questions/$qId', q);
              count++;
            }
          }
          chapIndex++;
        }
      }
    }

    // 3. Build updates for Chapters from flat list
    if (data['chapters'] != null) {
      for (var c in data['chapters']) {
        final String subjectId = c['subjectId'];
        final String chapterId = c['id'];
        addUpdate(subjectId, 'Subjects/$subjectId/Chapters/$chapterId/title', c['title']);
      }
    }

    // 4. Build updates for Questions from flat list
    if (data['questions'] != null) {
      for (var q in data['questions']) {
        final String subjectId = q['subjectId'];
        final String chapterId = q['chapterId'];
        final String qId = q['id'];
        addUpdate(subjectId, 'Subjects/$subjectId/Chapters/$chapterId/Questions/$qId', q);
        count++;
      }
    }

    // 5. Perform the updates subject-by-subject!
    for (var entry in subjectUpdates.entries) {
      final String subjectId = entry.key;
      final Map<String, dynamic> updates = entry.value;
      debugPrint('Seeding subject "$subjectId" with ${updates.length} nodes...');
      await _dbRef.update(updates);
    }
    debugPrint('Successfully seeded $count total questions via subject-grouped batch updates.');
  }

  Future<void> autoSeedIfNeeded() async {
    try {
      final snapshot = await _dbRef.child('Subjects').limitToFirst(1).get();
      if (!snapshot.exists || snapshot.value == null) {
        debugPrint('Auto-seeding database because "Subjects" node is empty...');
        await seedDatabase();
      } else {
        debugPrint('Database already seeded. Skipping auto-seed check.');
      }
    } catch (e) {
      debugPrint('Error during auto-seed: $e');
    }
  }

  // Local data fallback helper methods
  List<Subject> _getLocalSubjects() {
    try {
      final localData = jsonDecode(fullSeedJson);
      final List<dynamic> subjectsList = localData['subjects'] ?? [];
      return subjectsList.map((s) => Subject.fromMap(s['id'], {
        'name': s['name'],
      })).toList();
    } catch (e) {
      debugPrint('Error getting local subjects: $e');
      return [];
    }
  }

  List<Chapter> _getLocalChapters(String subjectId) {
    try {
      final localData = jsonDecode(fullSeedJson);
      final List<Chapter> chapters = [];
      
      // Check in subjects list first
      for (var s in localData['subjects'] ?? []) {
        if (s['id'] == subjectId && s['chapters'] != null) {
          int chapIndex = 1;
          for (var c in s['chapters']) {
            final String chapterId = c['id'] ?? '${subjectId}_ch$chapIndex';
            chapters.add(Chapter.fromMap(chapterId, {'title': c['title']}));
            chapIndex++;
          }
        }
      }
      
      // Check in flat chapters list
      for (var c in localData['chapters'] ?? []) {
        if (c['subjectId'] == subjectId) {
          chapters.add(Chapter.fromMap(c['id'], {'title': c['title']}));
        }
      }
      
      chapters.sort((a, b) => a.title.compareTo(b.title));
      return chapters;
    } catch (e) {
      debugPrint('Error getting local chapters: $e');
      return [];
    }
  }

  List<Question> _getLocalQuestions(String subjectId, String chapterId, String difficulty) {
    try {
      final localData = jsonDecode(fullSeedJson);
      final List<Question> questions = [];
      
      // Check in subjects list first
      for (var s in localData['subjects'] ?? []) {
        if (s['id'] == subjectId && s['chapters'] != null) {
          int chapIndex = 1;
          for (var c in s['chapters']) {
            final String currentChapterId = c['id'] ?? '${subjectId}_ch$chapIndex';
            if (currentChapterId == chapterId && c['questions'] != null) {
              for (var q in c['questions']) {
                questions.add(Question.fromMap(q['id'] ?? '', q));
              }
            }
            chapIndex++;
          }
        }
      }
      
      // Check in flat questions list
      for (var q in localData['questions'] ?? []) {
        if (q['subjectId'] == subjectId && q['chapterId'] == chapterId) {
          questions.add(Question.fromMap(q['id'] ?? '', q));
        }
      }
      
      final filtered = questions
          .where((q) => q.difficultyLevel.toLowerCase() == difficulty.toLowerCase())
          .toList();
          
      debugPrint('Local fallback: found ${filtered.length} questions for $difficulty');
      return filtered;
    } catch (e) {
      debugPrint('Error getting local questions: $e');
      return [];
    }
  }

  List<Question> _getLocalChallengeQuestions(String subjectId, String chapterId) {
    try {
      final localData = jsonDecode(fullSeedJson);
      final List<Question> questions = [];
      
      // Check in subjects list first
      for (var s in localData['subjects'] ?? []) {
        if (s['id'] == subjectId && s['chapters'] != null) {
          int chapIndex = 1;
          for (var c in s['chapters']) {
            final String currentChapterId = c['id'] ?? '${subjectId}_ch$chapIndex';
            if (currentChapterId == chapterId && c['questions'] != null) {
              for (var q in c['questions']) {
                questions.add(Question.fromMap(q['id'] ?? '', q));
              }
            }
            chapIndex++;
          }
        }
      }
      
      // Check in flat questions list
      for (var q in localData['questions'] ?? []) {
        if (q['subjectId'] == subjectId && q['chapterId'] == chapterId) {
          questions.add(Question.fromMap(q['id'] ?? '', q));
        }
      }
      
      final filtered = questions
          .where((q) => q.difficultyLevel.toLowerCase() == 'medium' || q.difficultyLevel.toLowerCase() == 'hard')
          .toList();
          
      debugPrint('Local fallback challenge: found ${filtered.length} medium/hard questions');
      return filtered;
    } catch (e) {
      debugPrint('Error getting local challenge questions: $e');
      return [];
    }
  }

  List<Question> _getLocalAllQuestions(String subjectId) {
    try {
      final localData = jsonDecode(fullSeedJson);
      final List<Question> questions = [];
      
      // Check in subjects list first
      for (var s in localData['subjects'] ?? []) {
        if (s['id'] == subjectId && s['chapters'] != null) {
          for (var c in s['chapters']) {
            if (c['questions'] != null) {
              for (var q in c['questions']) {
                questions.add(Question.fromMap(q['id'] ?? '', q));
              }
            }
          }
        }
      }
      
      // Check in flat questions list
      for (var q in localData['questions'] ?? []) {
        if (q['subjectId'] == subjectId) {
          questions.add(Question.fromMap(q['id'] ?? '', q));
        }
      }
      
      return questions;
    } catch (e) {
      debugPrint('Error getting local all questions: $e');
      return [];
    }
  }

  // Subjects
  Future<void> addSubject(String name) async {
    final newSubjectRef = _dbRef.child('Subjects').push();
    await newSubjectRef.set({
      'name': name,
    });
  }

  Stream<List<Subject>> getSubjects() async* {
    yield _getLocalSubjects();
    yield* _dbRef.child('Subjects').onValue.map((event) {
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      debugPrint('getSubjects: Fetched ${data?.length ?? 0} subjects');
      if (data == null || data.isEmpty) {
        return _getLocalSubjects();
      }
      return data.entries.map((e) => Subject.fromMap(e.key, e.value)).toList();
    });
  }

  // Chapters
  Future<void> addChapter(String subjectId, String title) async {
    await _dbRef.child('Subjects').child(subjectId).child('Chapters').push().set({
      'title': title,
    });
  }

  Stream<List<Chapter>> getChapters(String subjectId) async* {
    yield _getLocalChapters(subjectId);
    yield* _dbRef.child('Subjects').child(subjectId).child('Chapters').onValue.map((event) {
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      debugPrint('getChapters: Fetched ${data?.length ?? 0} chapters for $subjectId');
      if (data == null || data.isEmpty) {
        return _getLocalChapters(subjectId);
      }
      final chapters = data.entries.map((e) => Chapter.fromMap(e.key, e.value)).toList();
      chapters.sort((a, b) => a.title.compareTo(b.title));
      return chapters;
    });
  }

  // Questions
  Future<void> addQuestion({
    required String subjectId,
    required String chapterId,
    required String question,
    required Map<String, String> options,
    required String correctAnswer,
    required String difficultyLevel,
  }) async {
    await _dbRef.child('Subjects').child(subjectId).child('Chapters').child(chapterId).child('Questions').push().set({
      'question': question,
      'options': options,
      'correctAnswer': correctAnswer,
      'difficultyLevel': difficultyLevel,
    });
  }

  Future<List<Question>> getQuestions(String subjectId, String chapterId, String difficulty) async {
    final path = 'Subjects/$subjectId/Chapters/$chapterId/Questions';
    debugPrint('Fetching questions from path: $path');
    
    try {
      final event = await _dbRef.child(path).once().timeout(const Duration(seconds: 4));
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      
      if (data == null || data.isEmpty) {
        debugPrint('No data found at path: $path, using local fallback');
        return _getLocalQuestions(subjectId, chapterId, difficulty);
      }
      
      debugPrint('Raw data found: ${data.length} items');
      
      final allQuestions = data.entries
          .map((e) => Question.fromMap(e.key, e.value))
          .toList();
          
      final filtered = allQuestions
          .where((q) => q.difficultyLevel.toLowerCase() == difficulty.toLowerCase())
          .toList();
          
      debugPrint('Filtered to $difficulty: ${filtered.length} questions');
      if (filtered.isEmpty) {
        return _getLocalQuestions(subjectId, chapterId, difficulty);
      }
      return filtered;
    } catch (e) {
      debugPrint('Error fetching questions from database: $e, falling back to local');
      return _getLocalQuestions(subjectId, chapterId, difficulty);
    }
  }

  Future<List<Question>> getChallengeQuestions(String subjectId, String chapterId) async {
    final path = 'Subjects/$subjectId/Chapters/$chapterId/Questions';
    debugPrint('Fetching challenge questions (medium & hard) from path: $path');
    
    try {
      final event = await _dbRef.child(path).once().timeout(const Duration(seconds: 4));
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      
      if (data == null || data.isEmpty) {
        debugPrint('No data found at path: $path, using local fallback');
        return _getLocalChallengeQuestions(subjectId, chapterId);
      }
      
      debugPrint('Raw data found: ${data.length} items');
      
      final allQuestions = data.entries
          .map((e) => Question.fromMap(e.key, e.value))
          .toList();
          
      final filtered = allQuestions
          .where((q) => q.difficultyLevel.toLowerCase() == 'medium' || q.difficultyLevel.toLowerCase() == 'hard')
          .toList();
          
      debugPrint('Filtered challenge questions (medium/hard): ${filtered.length} questions');
      if (filtered.isEmpty) {
        return _getLocalChallengeQuestions(subjectId, chapterId);
      }
      return filtered;
    } catch (e) {
      debugPrint('Error fetching challenge questions from database: $e, falling back to local');
      return _getLocalChallengeQuestions(subjectId, chapterId);
    }
  }

  Future<List<Question>> getMockExamQuestions(String subjectId, Map<String, int> distribution) async {
    final List<Question> examQuestions = [];
    debugPrint('Fetching Mock Exam Questions for Subject: $subjectId');
    debugPrint('Distribution requested: $distribution');
    
    try {
      final snapshot = await _dbRef.child('Subjects').child(subjectId).child('Chapters').once().timeout(const Duration(seconds: 4));
      final Map<dynamic, dynamic>? chaptersData = snapshot.snapshot.value as Map<dynamic, dynamic>?;
      
      List<Question> allSubjectQuestions = [];
      
      if (chaptersData == null || chaptersData.isEmpty) {
        debugPrint('No chapters found for subject: $subjectId at path: Subjects/$subjectId/Chapters, using local fallback');
        allSubjectQuestions = _getLocalAllQuestions(subjectId);
      } else {
        debugPrint('Found ${chaptersData.length} chapters.');
        for (var chapterEntry in chaptersData.entries) {
          final chapterValue = chapterEntry.value as Map<dynamic, dynamic>;
          final Map<dynamic, dynamic>? questionsData = chapterValue['Questions'] as Map<dynamic, dynamic>?;
          
          if (questionsData != null) {
            for (var questionEntry in questionsData.entries) {
              allSubjectQuestions.add(Question.fromMap(questionEntry.key, questionEntry.value));
            }
          }
        }
      }
      
      if (allSubjectQuestions.isEmpty) {
        allSubjectQuestions = _getLocalAllQuestions(subjectId);
      }
      
      debugPrint('Total questions collected for subject: ${allSubjectQuestions.length}');
      
      for (var entry in distribution.entries) {
        final difficulty = entry.key.toLowerCase();
        final count = entry.value;
        
        final filtered = allSubjectQuestions
            .where((q) => q.difficultyLevel.toLowerCase() == difficulty)
            .toList();
        
        debugPrint('Found ${filtered.length} questions for difficulty: $difficulty. Requested: $count');
        
        filtered.shuffle();
        examQuestions.addAll(filtered.take(count));
      }
      
      examQuestions.shuffle();
      debugPrint('Returning ${examQuestions.length} questions for the mock exam.');
    } catch (e) {
      debugPrint('Error fetching mock exam questions: $e, falling back to local');
      final allSubjectQuestions = _getLocalAllQuestions(subjectId);
      for (var entry in distribution.entries) {
        final difficulty = entry.key.toLowerCase();
        final count = entry.value;
        
        final filtered = allSubjectQuestions
            .where((q) => q.difficultyLevel.toLowerCase() == difficulty)
            .toList();
        
        filtered.shuffle();
        examQuestions.addAll(filtered.take(count));
      }
      examQuestions.shuffle();
    }
    
    return examQuestions;
  }

  // Firebase Storage Reference
  final FirebaseStorage _storage = FirebaseStorage.instance;

  // Upload Paper PDF to Storage
  Future<String> uploadPaperPdf(String fileName, Uint8List fileBytes) async {
    try {
      final ref = _storage.ref().child('papers/$fileName');
      final uploadTask = ref.putData(
        fileBytes,
        SettableMetadata(contentType: 'application/pdf'),
      );
      final snapshot = await uploadTask;
      final downloadUrl = await snapshot.ref.getDownloadURL();
      return downloadUrl;
    } catch (e) {
      debugPrint('Error uploading PDF: $e');
      rethrow;
    }
  }

  // Add Paper
  Future<void> addPaper(Paper paper) async {
    await _dbRef.child('Papers').child(paper.id).set(paper.toMap());
  }

  // Stream Papers
  Stream<List<Paper>> getPapers() {
    return _dbRef.child('Papers').onValue.map((event) {
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      if (data == null) return [];
      return data.entries.map((e) {
        final Map<dynamic, dynamic> mapVal = e.value as Map<dynamic, dynamic>;
        return Paper.fromMap(e.key, mapVal);
      }).toList();
    });
  }

  // Delete Paper
  Future<void> deletePaper(String paperId, String? firebaseStorageUrl) async {
    // Delete from Realtime Database
    await _dbRef.child('Papers').child(paperId).remove();

    // Optionally delete from Storage if it's a storage URL
    if (firebaseStorageUrl != null && firebaseStorageUrl.contains('firebasestorage.googleapis.com')) {
      try {
        final ref = _storage.refFromURL(firebaseStorageUrl);
        await ref.delete();
      } catch (e) {
        debugPrint('Error deleting file from Storage: $e');
      }
    }
  }

  // ─── Competition Service Methods ──────────────────────────────────────────

  Future<List<Question>> getCompetitionQuestions(String subjectId, int count) async {
    List<Question> allQuestions = [];
    try {
      final snapshot = await _dbRef.child('Subjects').child(subjectId).child('Chapters').once().timeout(const Duration(seconds: 4));
      final Map<dynamic, dynamic>? chaptersData = snapshot.snapshot.value as Map<dynamic, dynamic>?;
      if (chaptersData != null && chaptersData.isNotEmpty) {
        for (var chapterEntry in chaptersData.entries) {
          final chapterValue = chapterEntry.value as Map<dynamic, dynamic>;
          final Map<dynamic, dynamic>? questionsData = chapterValue['Questions'] as Map<dynamic, dynamic>?;
          if (questionsData != null) {
            for (var questionEntry in questionsData.entries) {
              allQuestions.add(Question.fromMap(questionEntry.key, questionEntry.value));
            }
          }
        }
      }
    } catch (e) {
      debugPrint('Error fetching competition questions from DB: $e');
    }

    if (allQuestions.isEmpty) {
      allQuestions = _getLocalAllQuestions(subjectId);
    }

    // Group questions by difficulty
    final easyQs = allQuestions.where((q) => q.difficultyLevel.toLowerCase() == 'easy').toList();
    final mediumQs = allQuestions.where((q) => q.difficultyLevel.toLowerCase() == 'medium').toList();
    final hardQs = allQuestions.where((q) => q.difficultyLevel.toLowerCase() == 'hard').toList();

    // Select questions representing a mix of easy, medium, and hard
    int targetEasy = (count * 0.4).round();
    int targetMedium = (count * 0.4).round();
    int targetHard = count - targetEasy - targetMedium;

    easyQs.shuffle();
    mediumQs.shuffle();
    hardQs.shuffle();

    List<Question> selected = [];

    // Take from easy
    final takenEasy = easyQs.take(targetEasy).toList();
    selected.addAll(takenEasy);

    // Take from medium
    final takenMedium = mediumQs.take(targetMedium).toList();
    selected.addAll(takenMedium);

    // Take from hard
    final takenHard = hardQs.take(targetHard).toList();
    selected.addAll(takenHard);

    // If we still need more questions (due to list being short in some categories)
    if (selected.length < count) {
      final remaining = allQuestions.where((q) => !selected.contains(q)).toList();
      remaining.shuffle();
      selected.addAll(remaining.take(count - selected.length));
    }

    selected.shuffle();
    return selected.take(count).toList();
  }

  Future<String> createCompetition({
    required String title,
    required String description,
    required String subjectId,
    required String subjectName,
    required int durationMinutes,
    required int questionCount,
    required Map<String, String> invitedFriends, // Map of email -> fullName
    required List<Question> questions,
  }) async {
    final creator = AuthService.currentUser;
    if (creator == null) throw Exception("User must be logged in to create a competition.");

    final newCompRef = _dbRef.child('Competitions').push();
    final String compId = newCompRef.key!;

    final sanitizedCreatorEmail = AuthService.sanitizeEmail(creator.email);

    final Map<String, dynamic> scoresMap = {
      sanitizedCreatorEmail: {
        'fullName': creator.fullName,
        'score': 0,
        'completed': false,
        'email': creator.email,
        'status': 'creator',
      }
    };

    // Save initial details in the leaderboard using in-memory names
    invitedFriends.forEach((email, fullName) {
      final sanitized = AuthService.sanitizeEmail(email);
      scoresMap[sanitized] = {
        'fullName': fullName.isNotEmpty ? fullName : email,
        'score': 0,
        'completed': false,
        'email': email,
        'status': 'waiting',
      };

      // Send real-time notification to the invited friend
      final notificationId = (DateTime.now().millisecondsSinceEpoch + sanitized.hashCode).toString();
      _dbRef.child('Users/$sanitized/notifications/$notificationId').set({
        'id': notificationId,
        'type': 'competition_invite',
        'title': 'New Competition Invitation',
        'message': 'You have been invited to join the competition: ${title.trim()}',
        'timestamp': DateTime.now().millisecondsSinceEpoch,
        'isRead': false,
        'competitionId': compId,
        'senderEmail': creator.email,
        'senderName': creator.fullName,
      });
    });

    final compData = {
      'id': compId,
      'title': title.trim(),
      'description': description.trim(),
      'subjectId': subjectId,
      'subjectName': subjectName,
      'duration': durationMinutes,
      'questionCount': questionCount,
      'creatorEmail': creator.email,
      'creatorName': creator.fullName,
      'invitedEmails': invitedFriends.keys.toList(),
      'status': 'active',
      'createdAt': ServerValue.timestamp,
      'questions': questions.map((q) => q.toMap()).toList(),
      'scores': scoresMap,
      'quizStarted': false,
      'lobbyTimerStart': ServerValue.timestamp,
    };

    await newCompRef.set(compData);
    return compId;
  }

  Future<void> markCompetitionExpired(String competitionId) async {
    await _dbRef.child('Competitions/$competitionId').update({
      'status': 'expired',
    });
  }

  Stream<List<Map<String, dynamic>>> streamCompetitions() {
    final user = AuthService.currentUser;
    if (user == null) return Stream.value([]);

    return _dbRef.child('Competitions').onValue.map((event) {
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      if (data == null) return [];

      final List<Map<String, dynamic>> results = [];
      final int now = DateTime.now().millisecondsSinceEpoch;

      data.forEach((key, value) {
        final comp = Map<String, dynamic>.from(value as Map);

        final creatorEmail = comp['creatorEmail'] as String? ?? '';
        final invitedList = List<dynamic>.from(comp['invitedEmails'] ?? []);

        bool isParticipant = creatorEmail.toLowerCase() == user.email.toLowerCase() ||
            invitedList.any((email) => email.toString().toLowerCase() == user.email.toLowerCase());

        if (isParticipant) {
          final String status = comp['status'] ?? '';
          final bool quizStarted = comp['quizStarted'] ?? false;
          final int createdAt = comp['createdAt'] ?? 0;

          bool isExpired = false;

          if (!quizStarted && createdAt > 0 && (now - createdAt) > 120000) {
            // Check if any friend has accepted/joined
            final Map<dynamic, dynamic> scores = comp['scores'] as Map<dynamic, dynamic>? ?? {};
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
              isExpired = true;
              if (status == 'active') {
                // Set to expired in Firebase asynchronously
                _dbRef.child('Competitions/${comp['id']}/status').set('expired');
                comp['status'] = 'expired';
              }
            }
          }

          if (!isExpired && status != 'expired') {
            results.add(comp);
          }
        }
      });

      // Sort by createdAt desc
      results.sort((a, b) {
        final int timeA = a['createdAt'] ?? 0;
        final int timeB = b['createdAt'] ?? 0;
        return timeB.compareTo(timeA);
      });

      return results;
    });
  }

  Future<void> submitCompetitionScore({
    required String competitionId,
    required int score,
    required int timeTakenSeconds,
  }) async {
    final user = AuthService.currentUser;
    if (user == null) return;

    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    final scorePath = 'Competitions/$competitionId/scores/$sanitizedEmail';

    await _dbRef.child(scorePath).update({
      'score': score,
      'completed': true,
      'completedAt': ServerValue.timestamp,
      'timeTaken': timeTakenSeconds,
    });
  }

  Future<void> setParticipantReady(String competitionId, {bool ready = true}) async {
    final user = AuthService.currentUser;
    if (user == null) return;

    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    final statusPath = 'Competitions/$competitionId/scores/$sanitizedEmail';

    await _dbRef.child(statusPath).update({
      'status': ready ? 'ready' : 'waiting',
    });

    // Also add them back to invitedEmails if they were not there (e.g. if they previously declined it)
    final snapshot = await _dbRef.child('Competitions/$competitionId/invitedEmails').get();
    if (snapshot.exists && snapshot.value != null) {
      final List<dynamic> invitedList = List<dynamic>.from(snapshot.value as List);
      bool alreadyInvited = invitedList.any((email) => email.toString().toLowerCase() == user.email.toLowerCase());
      if (!alreadyInvited) {
        invitedList.add(user.email);
        await _dbRef.child('Competitions/$competitionId/invitedEmails').set(invitedList);
      }
    }
  }

  Future<void> startCompetitionQuiz(String competitionId) async {
    // 1. Update quizStarted to true
    await _dbRef.child('Competitions/$competitionId').update({
      'quizStarted': true,
    });

    // 2. Fetch competition details to get title and participant list
    final snapshot = await _dbRef.child('Competitions/$competitionId').get();
    if (!snapshot.exists || snapshot.value == null) return;

    final compData = Map<String, dynamic>.from(snapshot.value as Map);
    final String title = compData['title'] ?? 'Competition';
    final String creatorEmail = compData['creatorEmail'] ?? '';
    final Map<dynamic, dynamic> scores = compData['scores'] as Map<dynamic, dynamic>? ?? {};

    // 3. Send notification to all ready participants (excluding creator)
    scores.forEach((key, val) {
      final pMap = val as Map<dynamic, dynamic>;
      final String email = pMap['email'] ?? '';
      final String status = pMap['status'] ?? 'waiting';

      if (email.toLowerCase() != creatorEmail.toLowerCase() && status == 'ready') {
        final sanitizedEmail = AuthService.sanitizeEmail(email);
        final notificationId = (DateTime.now().millisecondsSinceEpoch + sanitizedEmail.hashCode).toString();

        _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'competition_started',
          'title': 'Competition Started!',
          'message': 'The competition "$title" has started! Tap to join the quiz.',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
          'competitionId': competitionId,
          'senderEmail': creatorEmail,
        });
      }
    });
  }

  Stream<Map<String, dynamic>?> streamCompetition(String competitionId) {
    return _dbRef.child('Competitions/$competitionId').onValue.map((event) {
      final value = event.snapshot.value;
      if (value == null) return null;
      return Map<String, dynamic>.from(value as Map);
    });
  }

  Stream<List<Map<String, dynamic>>> streamNotifications(String sanitizedEmail) {
    if (sanitizedEmail.isEmpty) return Stream.value([]);
    return _dbRef.child('Users/$sanitizedEmail/notifications').onValue.map((event) {
      final value = event.snapshot.value;
      if (value == null) return [];
      final List<Map<String, dynamic>> results = [];
      if (value is Map) {
        value.forEach((key, val) {
          if (val != null) {
            results.add(Map<String, dynamic>.from(val as Map));
          }
        });
      } else if (value is List) {
        for (var val in value) {
          if (val != null) {
            results.add(Map<String, dynamic>.from(val as Map));
          }
        }
      }
      // Sort desc by timestamp
      results.sort((a, b) {
        final int tA = a['timestamp'] ?? 0;
        final int tB = b['timestamp'] ?? 0;
        return tB.compareTo(tA);
      });
      return results;
    });
  }


  Future<void> markNotificationRead(String notificationId) async {
    final user = AuthService.currentUser;
    if (user == null) return;
    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    await _dbRef.child('Users/$sanitizedEmail/notifications/$notificationId').update({
      'isRead': true,
    });
  }

  Future<void> markAllNotificationsRead() async {
    final user = AuthService.currentUser;
    if (user == null) return;
    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    final snapshot = await _dbRef.child('Users/$sanitizedEmail/notifications').get();
    if (snapshot.exists && snapshot.value != null) {
      final Map<dynamic, dynamic> notifications = snapshot.value as Map<dynamic, dynamic>;
      final Map<String, dynamic> updates = {};
      notifications.forEach((key, value) {
        updates['$key/isRead'] = true;
      });
      await _dbRef.child('Users/$sanitizedEmail/notifications').update(updates);
    }
  }

  Future<void> declineCompetition(String competitionId) async {
    final user = AuthService.currentUser;
    if (user == null) return;

    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    final statusPath = 'Competitions/$competitionId/scores/$sanitizedEmail';

    await _dbRef.child(statusPath).update({
      'status': 'declined',
    });

    // Clean up from invitedEmails list to keep it synchronized
    final snapshot = await _dbRef.child('Competitions/$competitionId/invitedEmails').get();
    if (snapshot.exists && snapshot.value != null) {
      final List<dynamic> invitedList = List<dynamic>.from(snapshot.value as List);
      invitedList.removeWhere((email) => email.toString().toLowerCase() == user.email.toLowerCase());
      await _dbRef.child('Competitions/$competitionId/invitedEmails').set(invitedList);
    }

    // Send a real-time notification to the creator
    final compSnapshot = await _dbRef.child('Competitions/$competitionId').get();
    if (compSnapshot.exists && compSnapshot.value != null) {
      final compData = Map<String, dynamic>.from(compSnapshot.value as Map);
      final String creatorEmail = compData['creatorEmail'] ?? '';
      final String title = compData['title'] ?? 'Competition';
      final String declinerName = user.fullName ?? user.email ?? 'A friend';

      if (creatorEmail.isNotEmpty && creatorEmail.toLowerCase() != user.email.toLowerCase()) {
        final creatorSanitized = AuthService.sanitizeEmail(creatorEmail);
        final notificationId = (DateTime.now().millisecondsSinceEpoch + creatorSanitized.hashCode).toString();
        await _dbRef.child('Users/$creatorSanitized/notifications/$notificationId').set({
          'id': notificationId,
          'type': 'competition_declined',
          'title': 'Invitation Declined',
          'message': '$declinerName has declined your invitation to the competition: $title',
          'timestamp': DateTime.now().millisecondsSinceEpoch,
          'isRead': false,
          'competitionId': competitionId,
          'senderEmail': user.email,
          'senderName': declinerName,
        });
      }
    }
  }

  // ─── Progress Tracking Logging & Fetching ──────────────────

  Future<void> logExamQuizAttempt({
    required String type, // 'quiz' or 'mock_exam'
    required String subjectId,
    required String subjectName,
    required int score,
    required int totalQuestions,
  }) async {
    final user = AuthService.currentUser;
    if (user == null) return;

    final sanitizedEmail = AuthService.sanitizeEmail(user.email);
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    final logPath = 'Users/$sanitizedEmail/exam_quiz_history/$timestamp';

    await _dbRef.child(logPath).set({
      'type': type,
      'subjectId': subjectId,
      'subjectName': subjectName,
      'score': score,
      'totalQuestions': totalQuestions,
      'timestamp': timestamp,
    });
  }

  Stream<Map<String, int>> streamWeeklyXp(String email) {
    final sanitizedEmail = AuthService.sanitizeEmail(email);
    return _dbRef.child('Users/$sanitizedEmail/xp_history').onValue.map((event) {
      final value = event.snapshot.value;
      if (value == null) return {};
      final Map<dynamic, dynamic> map = value as Map<dynamic, dynamic>;

      final Map<String, int> result = {};
      map.forEach((key, val) {
        result[key.toString()] = int.tryParse(val.toString()) ?? 0;
      });
      return result;
    });
  }

  Stream<List<Map<String, dynamic>>> streamExamQuizHistory(String email) {
    final sanitizedEmail = AuthService.sanitizeEmail(email);
    return _dbRef.child('Users/$sanitizedEmail/exam_quiz_history').onValue.map((event) {
      final value = event.snapshot.value;
      if (value == null) return [];
      final Map<dynamic, dynamic> map = value as Map<dynamic, dynamic>;

      final List<Map<String, dynamic>> list = [];
      map.forEach((key, val) {
        list.add(Map<String, dynamic>.from(val as Map));
      });

      // Sort by timestamp desc
      list.sort((a, b) => (b['timestamp'] as int? ?? 0).compareTo(a['timestamp'] as int? ?? 0));
      return list;
    });
  }

  Future<void> seedDemoProgressDataIfEmpty(String email) async {
    final sanitizedEmail = AuthService.sanitizeEmail(email);

    // Check if xp_history or exam_quiz_history already exists
    final xpSnap = await _dbRef.child('Users/$sanitizedEmail/xp_history').get();
    final historySnap = await _dbRef.child('Users/$sanitizedEmail/exam_quiz_history').get();

    if (!xpSnap.exists && !historySnap.exists) {
      final now = DateTime.now();
      // Find Monday of the current week (weekday: 1 = Monday, 7 = Sunday)
      final monday = now.subtract(Duration(days: now.weekday - 1));

      final String wedDate = monday.add(const Duration(days: 2)).toIso8601String().split('T')[0];
      final String thuDate = monday.add(const Duration(days: 3)).toIso8601String().split('T')[0];
      final String satDate = monday.add(const Duration(days: 5)).toIso8601String().split('T')[0];

      // Update User profile directly for matching metrics
      await _dbRef.child('Users/$sanitizedEmail').update({
        'xp': 490,
        'coins': 120,
      });

      // Seed XP history
      await _dbRef.child('Users/$sanitizedEmail/xp_history').set({
        wedDate: 70,
        thuDate: 380,
        satDate: 40,
      });

      // Seed quiz/exam history (matching mockup stats: 0/20 Geography, 1/10 Technology, 0/10 History)
      final baseTime = now.subtract(const Duration(days: 1)).millisecondsSinceEpoch;
      await _dbRef.child('Users/$sanitizedEmail/exam_quiz_history').set({
        '${baseTime - 3600000}': {
          'type': 'mock_exam',
          'subjectId': 'geo',
          'subjectName': 'Juqraafi',
          'score': 0,
          'totalQuestions': 20,
          'timestamp': baseTime - 3600000,
        },
        '${baseTime - 1800000}': {
          'type': 'mock_exam',
          'subjectId': 'tech',
          'subjectName': 'Technology',
          'score': 1,
          'totalQuestions': 10,
          'timestamp': baseTime - 1800000,
        },
        '$baseTime': {
          'type': 'mock_exam',
          'subjectId': 'his',
          'subjectName': 'Taariikh',
          'score': 0,
          'totalQuestions': 10,
          'timestamp': baseTime,
        },
      });
      debugPrint("FirebaseService: Seeded initial progress metrics for test user $email");
    }
  }
}
