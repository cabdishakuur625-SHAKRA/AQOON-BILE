import json

json_file = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'
dart_file = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'

with open(json_file, 'r', encoding='utf-8') as f:
    current_data = json.load(f)

# Keep only History and Geography
KEEP_SUBJECTS = {'his', 'geo'}

# Filter subjects
current_data['subjects'] = {k: v for k, v in current_data['subjects'].items() if k in KEEP_SUBJECTS}

# Filter chapters
current_data['chapters'] = {k: v for k, v in current_data['chapters'].items() if v['subjectId'] in KEEP_SUBJECTS}

# Filter questions
current_data['questions'] = {k: v for k, v in current_data['questions'].items() if v['subjectId'] in KEEP_SUBJECTS}

# Save seed_data.json
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(current_data, f, indent=2, ensure_ascii=False)

# Sync to seed_data.dart
ID_MAP = {'his': 'History', 'geo': 'Geography'}
CHAPTER_MAP = {
    'his_ch1': 'Chapter 1', 'his_ch2': 'Chapter 2', 'his_ch3': 'Chapter 3',
    'his_ch4': 'Chapter 4', 'his_ch5': 'Chapter 5', 'his_ch6': 'Chapter 6',
    'his_ch7': 'Chapter 7', 'geo_ch1': 'Chapter 1',
}

subjects_list = [{'id': ID_MAP.get(s_id, s_id), 'name': s_info['name']} for s_id, s_info in current_data['subjects'].items()]

chapters_list = []
for c_id, c_info in current_data['chapters'].items():
    s_id = c_info['subjectId']
    chapters_list.append({'id': CHAPTER_MAP.get(c_id, c_id), 'subjectId': ID_MAP.get(s_id, s_id), 'title': c_info['title']})

questions_list = []
for q_id, q_info in current_data['questions'].items():
    s_id = q_info['subjectId']
    c_id = q_info['chapterId']
    questions_list.append({
        'id': q_id,
        'subjectId': ID_MAP.get(s_id, s_id),
        'chapterId': CHAPTER_MAP.get(c_id, c_id),
        'question': q_info['question'],
        'options': q_info['options'],
        'correctAnswer': q_info['correctAnswer'],
        'difficultyLevel': q_info['difficultyLevel']
    })

full_seed = {'subjects': subjects_list, 'chapters': chapters_list, 'questions': questions_list}
new_dart_content = f"const String fullSeedJson = r'''\n{json.dumps(full_seed, indent=2, ensure_ascii=False)}\n''';\n"

with open(dart_file, 'w', encoding='utf-8') as f:
    f.write(new_dart_content)

print(f'Done! Kept subjects: {list(current_data["subjects"].keys())}')
print(f'Chapters remaining: {len(current_data["chapters"])}')
print(f'Questions remaining: {len(current_data["questions"])}')
