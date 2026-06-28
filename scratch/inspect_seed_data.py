import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

seed_file_path = 'lib/services/seed_data.dart'
with open(seed_file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("File length:", len(content))
start_str = "const String fullSeedJson = r'''"
start_idx = content.find('{', content.find(start_str))
end_idx = content.rfind("''';")
print("Bounds indices:", start_idx, end_idx)

if start_idx != -1 and end_idx != -1:
    json_string = content[start_idx:end_idx].strip()
    print("Parsed JSON substring length:", len(json_string))
    data = json.loads(json_string)
    print("Subjects:")
    for sub in data.get('subjects', []):
        print(" -", sub)
    print("Number of chapters:", len(data.get('chapters', [])))
    print("Number of questions:", len(data.get('questions', [])))
    geo_chaps = [c for c in data.get('chapters', []) if c.get('subjectId') == 'geo']
    print("Geography chapters:", len(geo_chaps))
    for c in geo_chaps:
        print("  -", c)
    geo_questions = [q for q in data.get('questions', []) if q.get('subjectId') == 'geo']
    print("Total Geography questions:", len(geo_questions))
    
    # check difficulty counts per chapter
    for c in geo_chaps:
        ch_id = c['id']
        ch_qs = [q for q in geo_questions if q.get('chapterId') == ch_id]
        easy_qs = [q for q in ch_qs if q.get('difficultyLevel') == 'easy']
        med_qs = [q for q in ch_qs if q.get('difficultyLevel') == 'medium']
        hard_qs = [q for q in ch_qs if q.get('difficultyLevel') == 'hard']
        print(f"Chapter {ch_id}: Easy: {len(easy_qs)}, Medium: {len(med_qs)}, Hard: {len(hard_qs)}, Total: {len(ch_qs)}")
