import 'dart:convert';
import 'dart:io';

void main() {
  try {
    final content = File('lib/services/seed_data.dart').readAsStringSync();
    final startStr = "const String fullSeedJson = r'''";
    final startRaw = content.indexOf(startStr);
    final start = content.indexOf('{', startRaw);
    final end = content.lastIndexOf("''';");
    final jsonString = content.substring(start, end);
    jsonDecode(jsonString);
    print('Valid JSON!');
  } catch(e) {
    print('Invalid JSON: $e');
  }
}
