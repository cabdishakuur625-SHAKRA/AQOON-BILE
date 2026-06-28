import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Remove Biology subject if it was just added and is empty (or just leave it)
    # But let's follow user's lead and move everything to geo
    
    # 1. Update Chapters: Rename bio_ch2 to geo_ch2
    new_chapters = []
    for c in data['chapters']:
        if c['id'] == 'bio_ch2':
            c['id'] = 'geo_ch2'
            c['subjectId'] = 'geo'
            new_chapters.append(c)
        else:
            new_chapters.append(c)
    data['chapters'] = new_chapters
    
    # 2. Update Questions: Rename Bio_Ch2_QXX to Geo_Ch2_QXX and change subjectId
    for q in data['questions']:
        if q['chapterId'] == 'bio_ch2' or q['id'].startswith('Bio_Ch2'):
            q['id'] = q['id'].replace('Bio_Ch2', 'Geo_Ch2')
            q['subjectId'] = 'geo'
            q['chapterId'] = 'geo_ch2'
            
    # 3. Clean up Biology if no chapters left
    bio_chapters = [c for c in data['chapters'] if c['subjectId'] == 'bio']
    if not bio_chapters:
        data['subjects'] = [s for s in data['subjects'] if s['id'] != 'bio']
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated seed_data.dart: Migrated Bio Chapter 2 to Geo Chapter 2")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Migrate chapters
if "bio_ch2" in data_json['chapters']:
    ch_data = data_json['chapters'].pop("bio_ch2")
    ch_data['subjectId'] = 'geo'
    data_json['chapters']['geo_ch2'] = ch_data

# Migrate questions
new_questions = {}
for q_id, q_val in data_json['questions'].items():
    if q_id.startswith('Bio_Ch2'):
        new_id = q_id.replace('Bio_Ch2', 'Geo_Ch2')
        q_val['subjectId'] = 'geo'
        q_val['chapterId'] = 'geo_ch2'
        new_questions[new_id] = q_val
    else:
        new_questions[q_id] = q_val
data_json['questions'] = new_questions

# Remove Biology subject if empty
bio_has_chapters = any(c['subjectId'] == 'bio' for c in data_json['chapters'].values())
if not bio_has_chapters:
    data_json['subjects'].pop('bio', None)

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print("Updated seed_data.json: Migrated Bio Chapter 2 to Geo Chapter 2")
