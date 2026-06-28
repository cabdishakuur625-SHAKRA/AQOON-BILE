import 'dart:io';
import 'dart:convert';

void main() {
  final seedFile = File('lib/services/seed_data.dart');
  var content = seedFile.readAsStringSync();

  final startIndexRaw = content.indexOf(r"const String fullSeedJson = r'''");
  final startIndex = content.indexOf('{', startIndexRaw);
  final endIndex = content.lastIndexOf("''';");
  
  if (startIndex == -1 || endIndex == -1) {
    print("Could not find json boundaries.");
    return;
  }
  
  final jsonString = content.substring(startIndex, endIndex);
  
  Map<String, dynamic> data;
  try {
    data = jsonDecode(jsonString);
  } catch (e) {
    print("Error decoding existing json: $e");
    return;
  }
  
  Map<String, dynamic> somaliSubject = {
    "name": "Somali",
    "chapters": []
  };
  
  for (int i = 1; i <= 9; i++) {
    final chFile = File('scratch/somali_ch$i.json');
    if (!chFile.existsSync()) {
      print("Warning: scratch/somali_ch$i.json does not exist. Skipping.");
      continue;
    }
    
    try {
      final chContent = chFile.readAsStringSync();
      final List<dynamic> questions = jsonDecode(chContent);
      
      String title = "Cutubka $i"; 
      if (i == 1) title = "Qoraal Sharraxeed";
      if (i == 2) title = "Beeraha";
      if (i == 3) title = "Miisaanka Maansada";
      if (i == 4) title = "Mudnaan Badan";
      if (i == 5) title = "Garwaaqsiin";
      if (i == 6) title = "Geyiga Soomaaliya";
      if (i == 7) title = "Dood Dheellitiran";
      if (i == 8) title = "Sahan";
      if (i == 9) title = "Yaa Tahay?";
      
      somaliSubject["chapters"].add({
        "title": title,
        "questions": questions
      });
      print("Loaded Chapter $i with ${questions.length} questions.");
    } catch (e) {
      print("Error loading chapter $i: $e");
    }
  }
  
  List<dynamic> subjects = data["subjects"];
  int existingIdx = subjects.indexWhere((s) => s["name"]?.toString().toLowerCase() == "somali");
  
  if (existingIdx != -1) {
    subjects[existingIdx] = somaliSubject;
    print("Updated existing Somali subject.");
  } else {
    subjects.add(somaliSubject);
    print("Added new Somali subject.");
  }
  
  final updatedJson = const JsonEncoder.withIndent('  ').convert(data);
  
  seedFile.writeAsStringSync(content.substring(0, startIndex) + updatedJson + "\n''';\n");
  print("Successfully merged Somali subject into seed_data.dart!");
}
