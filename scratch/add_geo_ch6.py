import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
    {
      "id": "Cut6_Q1",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Sheeg sababaha keena in loo hayaamo magaalooyinka?",
      "options": {
        "a": "Nolosha miyiga oo liidata",
        "b": "Cimilada wanaagsan",
        "c": "Buuro badan",
        "d": "Badda"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q2",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Falanqee astaamaha bulshada magaalada jooga ah?",
      "options": {
        "a": "Tirada dadka oo badan",
        "b": "Dhul bannaan",
        "c": "Xoolo badan",
        "d": "Beeraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q3",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Soo jeedi xal ku habboon dhibaatooyinka ka jira degmo magaaleedka?",
      "options": {
        "a": "Yareynta fiditaanka magaalooyinka",
        "b": "Kordhinta barafka",
        "c": "Xiritaanka waddooyinka",
        "d": "Yareynta biyaha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q4",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Sheeg shaqooyinka magaalada ee kala duwan?",
      "options": {
        "a": "Ganacsi, maamul, warshado",
        "b": "Kaliya beeraha",
        "c": "Kaliya xoolo",
        "d": "Kaliya kalluumeysi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q5",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Falanqee dhibaatooyinka magaalada?",
      "options": {
        "a": "Ciriiri waddooyin",
        "b": "Baraf badan",
        "c": "Kaymo",
        "d": "Buuraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q6",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Soo jeedi xal ku haboon dhibaatooyinka magaalada?",
      "options": {
        "a": "Horumarinta adeegyada",
        "b": "Xiritaanka magaalada",
        "c": "Yareynta dadka",
        "d": "Joojinta gaadiidka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Cut6_Q7",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Ka hadal magaalooyinka Soomaaliya?",
      "options": {
        "a": "Muqdisho waa ugu weyn",
        "b": "Kaliya tuulooyin",
        "c": "Baraf leh",
        "d": "Lamadegaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q8",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Falanqee kaalinta socdaalka uu ku leeyahay magaalooyinka?",
      "options": {
        "a": "Kordhinta dadka magaalada",
        "b": "Yareynta biyaha",
        "c": "Kordhinta buuraha",
        "d": "Yareynta dhulka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Cut6_Q9",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Sheeg waxa ay ku kala duwan yihiin magaalooyinka Soomaaliya?",
      "options": {
        "a": "Tirada dadka",
        "b": "Cimilada kaliya",
        "c": "Buuraha",
        "d": "Badaha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q10",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Qeex micnaha magaalo?",
      "options": {
        "a": "Deegaan dad badan ku nool yihiin",
        "b": "Dhul bannaan",
        "c": "Buur",
        "d": "Webi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q11",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Maxaa loola jeedaa degmo magaaleed?",
      "options": {
        "a": "Fiditaanka magaalooyinka",
        "b": "Buuro",
        "c": "Biyo",
        "d": "Dhul miyi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q12",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Falanqee degmooyinka Soomaaliya?",
      "options": {
        "a": "Gobollo kala duwan",
        "b": "Hal magaalo",
        "c": "Hal tuulo",
        "d": "Hal webi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Cut6_Q13",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Isku xir magaalooyinka iyo shaqadooda",
      "options": {
        "a": "Sax",
        "b": "Qalad",
        "c": "Lama yaqaan",
        "d": "Ma jiro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Cut6_Q14",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Mid ka mid ah astaamaha magaalada ma aha?",
      "options": {
        "a": "Xiriir xoog leh",
        "b": "Dad badan",
        "c": "Ciriiri",
        "d": "Ganacsi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q15",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Tusaale magaalo waxbarasho?",
      "options": {
        "a": "Oxford",
        "b": "Muqdisho",
        "c": "Kismaayo",
        "d": "Hobyo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Cut6_Q16",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Maxaad ku micneyn lahayd warshadaha Muqdisho?",
      "options": {
        "a": "Horumar",
        "b": "Hoos u dhac",
        "c": "Baraf",
        "d": "Buur"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Cut6_Q17",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Kaalinta furdooyinka ee ganacsiga?",
      "options": {
        "a": "Canshuur",
        "b": "Cimilada",
        "c": "Buuraha",
        "d": "Biyaha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Cut6_Q18",
      "subjectId": "Geography",
      "chapterId": "Chapter 6",
      "question": "Sababaha socdaalka reer miyiga?",
      "options": {
        "a": "Adeegyo iyo shaqo",
        "b": "Buuraha",
        "c": "Badda",
        "d": "Dhul bannaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    }
]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 6: Deegaanka Magaalooyinka",
  "id": "geo_ch6"
}

# Format IDs correctly for the new questions
formatted_questions = []
for q in new_questions_raw:
    q['subjectId'] = 'geo'
    q['chapterId'] = 'geo_ch6'
    match = re.match(r'Cut6_Q(\d+)', q['id'])
    if match:
        num = int(match.group(1))
        q['id'] = f"Geo_Ch6_Q{num:02d}"
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
