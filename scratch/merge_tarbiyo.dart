import 'dart:convert';
import 'dart:io';

void main() async {
  print('Starting merge process...');
  final seedFile = File('lib/services/seed_data.dart');
  
  if (!await seedFile.exists()) {
    print('seed_data.dart not found!');
    return;
  }
  
  final content = await seedFile.readAsString();
  
  final startStr = "const String fullSeedJson = r'''";
  final startIndexRaw = content.indexOf(startStr);
  if (startIndexRaw == -1) {
    print('Could not find fullSeedJson in seed_data.dart');
    return;
  }
  
  final startIndex = content.indexOf('{', startIndexRaw);
  final endIndex = content.lastIndexOf("''';");
  
  if (startIndex == -1 || endIndex == -1) {
    print('Could not find JSON bounds in seed_data.dart');
    return;
  }
  
  final jsonString = content.substring(startIndex, endIndex);
  
  Map<String, dynamic> data;
  try {
    data = jsonDecode(jsonString);
  } catch (e) {
    print('Error parsing JSON from seed_data.dart: $e');
    return;
  }
  
  // 1. Add Tarbiyo subject if not exists
  List<dynamic> subjects = data['subjects'] ?? [];
  bool subjectExists = subjects.any((s) => s['id'] == 'tarbiyo');
  if (!subjectExists) {
    subjects.add({
      'name': 'التربية الإسلامية (Tarbiyo)',
      'id': 'tarbiyo'
    });
    print('Added Tarbiyo subject.');
  }
  data['subjects'] = subjects;
  
  // 2. Add Chapters
  List<dynamic> chapters = data['chapters'] ?? [];
  final newChapters = [
    {'subjectId': 'tarbiyo', 'title': 'الوحدة الأولى', 'id': 'tarbiyo_ch1'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة الثانية', 'id': 'tarbiyo_ch2'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة الثالثة', 'id': 'tarbiyo_ch3'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة الرابعة', 'id': 'tarbiyo_ch4'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة الخامسة', 'id': 'tarbiyo_ch5'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة السادسة', 'id': 'tarbiyo_ch6'},
    {'subjectId': 'tarbiyo', 'title': 'الوحدة السابعة', 'id': 'tarbiyo_ch7'},
  ];
  
  for (var ch in newChapters) {
    if (!chapters.any((c) => c['id'] == ch['id'])) {
      chapters.add(ch);
    }
  }
  data['chapters'] = chapters;
  print('Added 7 Tarbiyo chapters.');
  
  // 3. Read generated questions from scratch folder
  List<dynamic> questions = data['questions'] ?? [];
  
  // Remove existing tarbiyo questions to avoid duplicates if rerun
  questions.removeWhere((q) => q['subjectId'] == 'tarbiyo');
  
  int addedQuestions = 0;
  
  for (int i = 1; i <= 7; i++) {
    final unitFile = File('scratch/unit$i.json');
    if (await unitFile.exists()) {
      try {
        final unitJsonStr = await unitFile.readAsString();
        final List<dynamic> unitQuestions = jsonDecode(unitJsonStr);
        questions.addAll(unitQuestions);
        addedQuestions += unitQuestions.length;
        print('Loaded ${unitQuestions.length} questions from unit$i.json');
      } catch (e) {
        print('Error reading/parsing unit$i.json: $e');
      }
    } else {
      print('scratch/unit$i.json not found yet.');
    }
  }
  
  data['questions'] = questions;
  print('Total Tarbiyo questions merged: $addedQuestions');
  
  // 4. Write back to seed_data.dart
  final encoder = JsonEncoder.withIndent('  ');
  final updatedJsonString = encoder.convert(data);
  
  final newContent = content.substring(0, startIndex + startStr.length) +
                     updatedJsonString +
                     "\n" +
                     content.substring(endIndex);
                     
  await seedFile.writeAsString(newContent);
  print('Successfully updated lib/services/seed_data.dart');
}
