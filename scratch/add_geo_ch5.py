import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
    {
      "id": "Ch5_Q1",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Qeex filiqsanaanta dadka dunida?",
      "options": {
        "a": "Kala duwanaanta dhirta",
        "b": "Qaybsanaanta dadka dhulka",
        "c": "Cimilada kaliya",
        "d": "Buuro"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q2",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Ilaha daraaseynta dadka waxaa ka mid ah?",
      "options": {
        "a": "Tirokoobka dadka",
        "b": "Buuro",
        "c": "Biyo",
        "d": "Dhir"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q3",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Hijradda gudaha waa?",
      "options": {
        "a": "Dal kale",
        "b": "Gudaha dalka",
        "c": "Badda",
        "d": "Buuro"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q4",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Cufnaanta dadka waa?",
      "options": {
        "a": "Saamiga dadka iyo dhulka",
        "b": "Cimilada",
        "c": "Buuro",
        "d": "Biyo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q5",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Soomaaliya cufnaanteedu waa?",
      "options": {
        "a": "Sare",
        "b": "Hoose",
        "c": "Aad u sare",
        "d": "Midna"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q6",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Tirokoobka muhiimka ah waxa uu diiwaan geliyaa?",
      "options": {
        "a": "Dhalashada iyo dhimashada",
        "b": "Buuro",
        "c": "Webi",
        "d": "Dhir"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Ch5_Q7",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Dalalka cufnaanta sare leh waxaa ka mid ah?",
      "options": {
        "a": "Bangladesh",
        "b": "Somalia",
        "c": "Canada",
        "d": "Australia"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Ch5_Q8",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Qodobada dabiiciga ah waxaa ka mid ah?",
      "options": {
        "a": "Cimilada",
        "b": "Gaadiidka",
        "c": "Waxbarasho",
        "d": "Dagaal"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Ch5_Q9",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Qodobada aadanaha waxaa ka mid ah?",
      "options": {
        "a": "Socdaalka",
        "b": "Roob",
        "c": "Buuro",
        "d": "Webi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Ch5_Q10",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Sababta dadka magaalooyinka ugu soo guuraan waa?",
      "options": {
        "a": "Adeeg la’aan miyiga",
        "b": "Biyo badan",
        "c": "Buuro",
        "d": "Xeeb"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Ch5_Q11",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Tirokoobka juqraafi waa?",
      "options": {
        "a": "Xog ururin cilmiyeed",
        "b": "Buuro",
        "c": "Webi",
        "d": "Cimilada"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Ch5_Q12",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Taran fatah waa?",
      "options": {
        "a": "Kororka dadka ka badan ilaha dhaqaalaha",
        "b": "Hoos u dhac dadka",
        "c": "Cimilada",
        "d": "Buuro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q13",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Cufnaanta dadka waxaa lagu xisaabiyaa?",
      "options": {
        "a": "Dad ÷ KM²",
        "b": "KM² ÷ Dad",
        "c": "Biyo ÷ Dad",
        "d": "Buuro ÷ Dhul"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q14",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Dadka dunida ugu badan waxay ku nool yihiin?",
      "options": {
        "a": "Aasiya",
        "b": "Afrika",
        "c": "Yurub",
        "d": "Australia"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q15",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Cufnaanta aad u hooseysa waxaa laga helaa?",
      "options": {
        "a": "Australia",
        "b": "Bangladesh",
        "c": "India",
        "d": "China"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q16",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Hijradda dibadda waa?",
      "options": {
        "a": "Dal kale u guurid",
        "b": "Gudaha dalka",
        "c": "Magaalo",
        "d": "Tuulo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q17",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Xiriirka dadka iyo deegaanka waa muhiim sababta oo ah?",
      "options": {
        "a": "Waxay saameeyaan nolosha",
        "b": "Kaliya buuro",
        "c": "Kaliya biyo",
        "d": "Ciyaaro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q18",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Dadka Soomaaliya ugu badan waxay ku nool yihiin?",
      "options": {
        "a": "Magaalooyinka",
        "b": "Buuraha",
        "c": "Lamadegaan",
        "d": "Badda"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q19",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Cimiladu waxay saameysaa dadka sababtoo ah?",
      "options": {
        "a": "Waxay saameysaa nolosha",
        "b": "Buuro",
        "c": "Webi",
        "d": "Dhir"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Ch5_Q20",
      "subjectId": "Geography",
      "chapterId": "Chapter 5",
      "question": "Cilmi baarista dadka waxaa loo isticmaalaa?",
      "options": {
        "a": "Qorsheynta horumarinta",
        "b": "Ciyaaro",
        "c": "Buuro",
        "d": "Biyo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    }
  ]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 5aad: Juqraafiga Dadka",
  "id": "geo_ch5"
}

# Format IDs correctly for the new questions
formatted_questions = []
for q in new_questions_raw:
    q['subjectId'] = 'geo'
    q['chapterId'] = 'geo_ch5'
    match = re.search(r'Ch5_Q(\d+)', q['id'])
    if match:
        num = int(match.group(1))
        q['id'] = f"Geo_Ch5_Q{num:02d}"
    formatted_questions.append(q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Add chapter
    chapter_ids = [c['id'] for c in data['chapters']]
    if new_chapter['id'] not in chapter_ids:
        data['chapters'].append(new_chapter)
        
    # Add questions
    existing_q_ids = {q['id'] for q in data['questions']}
    added_count = 0
    for q in formatted_questions:
        if q['id'] not in existing_q_ids:
            data['questions'].append(q)
            added_count += 1
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added {added_count} questions to seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

if new_chapter['id'] not in data_json['chapters']:
    data_json['chapters'][new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

added_count_json = 0
for q in formatted_questions:
    q_id = q['id']
    if q_id not in data_json['questions']:
        q_copy = q.copy()
        del q_copy['id']
        data_json['questions'][q_id] = q_copy
        added_count_json += 1

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print(f"Added {added_count_json} questions to seed_data.json")
