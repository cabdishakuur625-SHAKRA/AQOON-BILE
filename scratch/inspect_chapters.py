import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

seed_file_path = 'lib/services/seed_data.dart'
with open(seed_file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "const String fullSeedJson = r'''"
start_idx = content.find('{', content.find(start_str))
end_idx = content.rfind("''';")

if start_idx != -1 and end_idx != -1:
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Let's print subject ids and their chapter titles
    subjects = data.get('subjects', [])
    chapters = data.get('chapters', [])
    
    print("Subjects and their chapters in seed_data.dart:")
    for sub in subjects:
        sub_id = sub['id']
        sub_name = sub['name']
        sub_chaps = [c for c in chapters if c.get('subjectId') == sub_id]
        print(f"Subject: {sub_name} ({sub_id})")
        for ch in sub_chaps:
            print(f"  - Chapter ID: {ch['id']} | Title: {ch['title']}")
