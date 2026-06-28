import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'

with open(DART_FILE, 'r', encoding='utf-8') as f:
    dart_content = f.read()

json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
current_data = json.loads(json_match.group(1))

# Keep only History
new_data = {
    "subjects": [s for s in current_data['subjects'] if s['id'] == 'his'],
    "chapters": [c for c in current_data['chapters'] if c['subjectId'] == 'his'],
    "questions": [q for q in current_data['questions'] if q['subjectId'] == 'his']
}

# If History is empty (it shouldn't be), try 'History'
if not new_data['subjects']:
    new_data = {
        "subjects": [s for s in current_data['subjects'] if s['id'] == 'History'],
        "chapters": [c for c in current_data['chapters'] if c['subjectId'] == 'History'],
        "questions": [q for q in current_data['questions'] if q['subjectId'] == 'History']
    }

new_json_str = json.dumps(new_data, indent=2, ensure_ascii=False)
new_dart_content = dart_content.replace(json_match.group(1).strip(), new_json_str)

with open(DART_FILE, 'w', encoding='utf-8') as f:
    f.write(new_dart_content)

print(f"Cleanup complete! Kept only History. Total Questions: {len(new_data['questions'])}")
