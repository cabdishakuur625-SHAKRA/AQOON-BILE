import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "question": "Hypothalamus iyo pituitary gland maxay sameeyaan?",
    "options": {
      "a": "Waxay burburiyaan unugyada",
      "b": "Waxay xakameeyaan hormoonnada endocrine system",
      "c": "Waxay sameeyaan dhiig",
      "d": "Waxay sameeyaan laf"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Pituitary gland waxaa loo yaqaan?",
    "options": {
      "a": "Heart gland",
      "b": "Master gland",
      "c": "Skin gland",
      "d": "Bone gland"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Pancreas waxay soo saartaa?",
    "options": {
      "a": "Insulin iyo glucagon",
      "b": "Oxygen",
      "c": "Bone cells",
      "d": "Skin cells"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Thyroid gland waxay xakameysaa?",
    "options": {
      "a": "Metabolism",
      "b": "Vision",
      "c": "Hearing",
      "d": "Taste"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Gonads function waa?",
    "options": {
      "a": "Hormones sex iyo gametes",
      "b": "Digestion",
      "c": "Breathing",
      "d": "Blood flow"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Endocrine glands waxay hormoonnada ku sii daayaan?",
    "options": {
      "a": "Ducts",
      "b": "Bloodstream",
      "c": "Skin",
      "d": "Bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Negative feedback waa?",
    "options": {
      "a": "Kordhiya signalka",
      "b": "Joojiya signalka asalka ah",
      "c": "Sameeya hormone cusub",
      "d": "Burburiya cell"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Positive feedback waa?",
    "options": {
      "a": "Yareeya hormone",
      "b": "Kordhiya hormone production",
      "c": "Joojiya brain",
      "d": "Burburiya blood"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Insulin function waa?",
    "options": {
      "a": "Kordhinta blood sugar",
      "b": "Hoos u dhigista blood sugar",
      "c": "Joojinta breathing",
      "d": "Kordhinta pressure"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Glucagon function waa?",
    "options": {
      "a": "Hoos u dhig glucose",
      "b": "Kordhi glucose blood",
      "c": "Jooji hormones",
      "d": "Samee bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Exocrine glands waa?",
    "options": {
      "a": "Waxay galaan blood directly",
      "b": "Waxay isticmaalaan ducts",
      "c": "Waxay sameeyaan bones",
      "d": "Waxay sameeyaan oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Amino acid hormones waxay sameeyaan?",
    "options": {
      "a": "Pass membrane freely",
      "b": "Bind receptors on membrane",
      "c": "Destroy cells",
      "d": "Form bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Steroid hormones waa?",
    "options": {
      "a": "Water soluble only",
      "b": "Lipid soluble and enter cell",
      "c": "Only blood based",
      "d": "Only skin based"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Homeostasis waxaa lagu ilaaliyaa?",
    "options": {
      "a": "Feedback mechanisms",
      "b": "Bones",
      "c": "Muscles",
      "d": "Skin"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Pituitary gland maxay xakameysaa?",
    "options": {
      "a": "All endocrine glands",
      "b": "Only heart",
      "c": "Only lungs",
      "d": "Only skin"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Dwarfism waxaa keena?",
    "options": {
      "a": "Too much growth hormone",
      "b": "Too little growth hormone",
      "c": "Too much insulin",
      "d": "Too much oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Gigantism waxaa keena?",
    "options": {
      "a": "Too little growth hormone",
      "b": "Too much growth hormone",
      "c": "Too much glucose",
      "d": "Too little oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Pancreas waa endocrine iyo exocrine sababtoo ah?",
    "options": {
      "a": "Waxay isticmaashaa ducts iyo blood secretion",
      "b": "Waxay sameysaa bones",
      "c": "Waxay sameysaa skin",
      "d": "Waxay sameysaa hair"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Adrenal gland function waa?",
    "options": {
      "a": "Controls stress and metabolism",
      "b": "Controls vision",
      "c": "Controls hearing",
      "d": "Controls digestion only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Thyroid hormone function waa?",
    "options": {
      "a": "Controls metabolic rate",
      "b": "Controls bones only",
      "c": "Controls skin only",
      "d": "Controls muscles only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Feedback mechanism function waa?",
    "options": {
      "a": "Disrupt homeostasis",
      "b": "Maintain homeostasis",
      "c": "Destroy cells",
      "d": "Stop hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Pituitary gland maxaa loogu yeeraa master gland?",
    "options": {
      "a": "Waxay xakameysaa endocrine glands kale",
      "b": "Waxay sameysaa bones",
      "c": "Waxay sameysaa skin",
      "d": "Waxay sameysaa blood"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Hormones function waa?",
    "options": {
      "a": "Control body processes",
      "b": "Only digestion",
      "c": "Only breathing",
      "d": "Only skin"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Endocrine system function waa?",
    "options": {
      "a": "Controls body via hormones",
      "b": "Controls bones only",
      "c": "Controls skin only",
      "d": "Controls heart only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Steroid hormones waxay sameeyaan maxay?",
    "options": {
      "a": "Enter nucleus and affect DNA",
      "b": "Stay outside cell",
      "c": "Destroy cells",
      "d": "Form bones"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 2: The Endocrine System",
  "id": "bio_ch2"
}

# Format IDs correctly for the new questions
formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Bio_Ch2_Q{i+1:02d}"
    q['subjectId'] = 'bio'
    q['chapterId'] = 'bio_ch2'
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

