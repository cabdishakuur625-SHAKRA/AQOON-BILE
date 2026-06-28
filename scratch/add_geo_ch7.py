import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
    {
      "id": "Chap7_Q1",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Qeex waxa loola jeedo sanaaca?",
      "options": {
        "a": "waa in maadooyinka caydhiinka laga beddelo qaabkoodii dabiiciga ahaa loona beddelo qaab kale",
        "b": "waa beerashada kaliya",
        "c": "waa ganacsi kaliya",
        "d": "waa socdaal"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q2",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Kala sooc noocyada warshadaha?",
      "options": {
        "a": "Qadiimi, fudud, waxsoosaar, wax beddelo, casri",
        "b": "Beeraha kaliya",
        "c": "Kalluumeysi",
        "d": "Gaadiid"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q3",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Tiri kaabayaasha warshadaha?",
      "options": {
        "a": "Alaabta ceeriin, tamar, gaadiid, suuq, raasamaal, shaqaale",
        "b": "Biyo kaliya",
        "c": "Dhul kaliya",
        "d": "Cimilada"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q4",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Tilmaan goobaha warshadaha dunida?",
      "options": {
        "a": "Galbeedka Yurub, Waqooyiga Ameerika, Ruushka, Koonfur Bari Aasiya",
        "b": "Soomaaliya kaliya",
        "c": "Saxaraha",
        "d": "Badweynta"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q5",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Maxaa loola jeedaa tamar?",
      "options": {
        "a": "waa awoodda lagu qabto shaqo",
        "b": "waa biyo",
        "c": "waa dhul",
        "d": "waa gaadiid"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q6",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Kala sooc ilaha tamarta?",
      "options": {
        "a": "Cusboonaan iyo aan cusboonaan",
        "b": "Beer iyo biyo",
        "c": "Dhul iyo badda",
        "d": "Dadka iyo xoolaha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q7",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Gaadiid iyo isgaarsiin maxaa loola jeedaa?",
      "options": {
        "a": "daabulidda dadka iyo badeecada",
        "b": "beerashada",
        "c": "macdan qodis",
        "d": "dhismo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q8",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Kala sooc noocyada gaadiidka?",
      "options": {
        "a": "Berri, badda, cirka",
        "b": "Beer, biyo, dhul",
        "c": "Warshad, suuq",
        "d": "Cimilo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q9",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Maxaa loola jeedaa geddis?",
      "options": {
        "a": "badeeco la daabulo lana geeyo suuqa",
        "b": "biyo",
        "c": "dhul",
        "d": "cimilo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },

    {
      "id": "Chap7_Q10",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Caddie ahmiyadda gaadiidka?",
      "options": {
        "a": "ballaarinta ganacsiga iyo dhaqaalaha",
        "b": "yareynta dadka",
        "c": "kororka roobka",
        "d": "dhimista dhulka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q11",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Kala saar astaamaha gaadiidka?",
      "options": {
        "a": "dhul, biyo, cirka",
        "b": "cunto, biyo",
        "c": "dhismo, beer",
        "d": "cimilo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q12",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Ahmiyadda geddiska maxaa ka mid ah?",
      "options": {
        "a": "in la helo badeeco aan la soo saarin",
        "b": "in la yareeyo ganacsiga",
        "c": "in la joojiyo suuqyada",
        "d": "in la joojiyo gaadiidka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q13",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Waxyaabaha saameeya ganacsiga?",
      "options": {
        "a": "siyaasad, tiknoolaji, waxsoosaar, heshiisyo",
        "b": "biyo kaliya",
        "c": "dhul kaliya",
        "d": "cimilada kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q14",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Dalxiiska maxaa loola jeedaa?",
      "options": {
        "a": "socdaal madadaalo, sahmin ama caafimaad",
        "b": "ganacsi kaliya",
        "c": "beerasho",
        "d": "warshado"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q15",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Muhiimadda dalxiiska?",
      "options": {
        "a": "kordhinta dakhliga dalka",
        "b": "yareynta dadweynaha",
        "c": "xiritaanka suuqyada",
        "d": "dhimista gaadiidka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q16",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Noocyada dalxiiska?",
      "options": {
        "a": "caafimaad, dhaqameed, madadaalo, diimeed",
        "b": "beer, biyo",
        "c": "dhul, cimilo",
        "d": "warshado"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q17",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Dalalka ugu horreeya dalxiiska?",
      "options": {
        "a": "Faransiis, Isbayn, Talyaaniga, Turkiga",
        "b": "Soomaaliya kaliya",
        "c": "Kenya kaliya",
        "d": "Eritrea"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q18",
      "subjectId": "Geography",
      "chapterId": "Chapter 7",
      "question": "Waxyaabaha saameeya ganacsiga caalamiga ah?",
      "options": {
        "a": "tiknoolaji, heshiisyo, siyaasad, suuqyo maaliyadeed",
        "b": "biyo kaliya",
        "c": "dhul kaliya",
        "d": "cimilo kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    }
  ]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 7aad: Ilaha Dhaqaale",
  "id": "geo_ch7"
}

# Format IDs correctly for the new questions
formatted_questions = []
for q in new_questions_raw:
    q['subjectId'] = 'geo'
    q['chapterId'] = 'geo_ch7'
    match = re.match(r'Chap7_Q(\d+)', q['id'])
    if match:
        num = int(match.group(1))
        q['id'] = f"Geo_Ch7_Q{num:02d}"
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
