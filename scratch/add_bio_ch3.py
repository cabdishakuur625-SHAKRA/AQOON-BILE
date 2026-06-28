import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Axial skeleton consists of?",
    "options": {
      "a": "Arms and legs",
      "b": "Skull, vertebral column, ribs and sternum",
      "c": "Hips only",
      "d": "Hands only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Appendicular skeleton includes?",
    "options": {
      "a": "Skull only",
      "b": "Arms, legs, shoulders and hips",
      "c": "Ribs only",
      "d": "Spine only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Bone is defined as?",
    "options": {
      "a": "Muscle tissue",
      "b": "Connective tissue with different shapes",
      "c": "Blood tissue",
      "d": "Nerve tissue"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Cartilage contains cells called?",
    "options": {
      "a": "Osteocytes",
      "b": "Chondrocytes",
      "c": "Neurons",
      "d": "Leukocytes"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Exoskeleton is?",
    "options": {
      "a": "Internal skeleton",
      "b": "External skeleton",
      "c": "Muscle system",
      "d": "Nervous system"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Endoskeleton is?",
    "options": {
      "a": "External skeleton",
      "b": "Internal skeleton",
      "c": "Skin layer",
      "d": "Blood system"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Fixed joints allow?",
    "options": {
      "a": "Full movement",
      "b": "No movement",
      "c": "Limited movement",
      "d": "Rotation only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 8,
    "question": "Semi-movable joints allow?",
    "options": {
      "a": "No movement",
      "b": "Limited movement",
      "c": "Free movement",
      "d": "Muscle movement"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 9,
    "question": "Movable joints allow?",
    "options": {
      "a": "No movement",
      "b": "Limited movement",
      "c": "Free movement",
      "d": "Skin movement"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },
  {
    "id": 10,
    "question": "Arthritis is?",
    "options": {
      "a": "Bone growth",
      "b": "Inflammation of joints",
      "c": "Skin disease",
      "d": "Muscle growth"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 11,
    "question": "Osteoporosis is?",
    "options": {
      "a": "Strong bones",
      "b": "Weak bones that break easily",
      "c": "Muscle disease",
      "d": "Skin disease"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 12,
    "question": "Synovial fluid function is?",
    "options": {
      "a": "Increase friction",
      "b": "Reduce friction in joints",
      "c": "Break bones",
      "d": "Produce blood"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 13,
    "question": "Skeletal muscle is?",
    "options": {
      "a": "Involuntary muscle",
      "b": "Voluntary muscle",
      "c": "Heart muscle",
      "d": "Skin muscle"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 14,
    "question": "Cardiac muscle is?",
    "options": {
      "a": "Voluntary muscle",
      "b": "Involuntary heart muscle",
      "c": "Skin muscle",
      "d": "Bone muscle"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 15,
    "question": "Smooth muscle is found in?",
    "options": {
      "a": "Bones",
      "b": "Internal organs",
      "c": "Skin only",
      "d": "Heart only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 16,
    "question": "Sarcomere is?",
    "options": {
      "a": "Unit of muscle contraction",
      "b": "Bone cell",
      "c": "Skin cell",
      "d": "Blood cell"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 17,
    "question": "Fast-twitch muscle fibers are?",
    "options": {
      "a": "Endurance fibers",
      "b": "Fatigue quickly",
      "c": "Very slow",
      "d": "Non-functional"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 18,
    "question": "Slow-twitch muscle fibers are?",
    "options": {
      "a": "Low endurance",
      "b": "High endurance",
      "c": "No oxygen use",
      "d": "Only for speed"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 19,
    "question": "Flexor muscles function is?",
    "options": {
      "a": "Straighten joints",
      "b": "Bend joints",
      "c": "Break bones",
      "d": "Protect skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 20,
    "question": "Extensor muscles function is?",
    "options": {
      "a": "Bend joints",
      "b": "Straighten joints",
      "c": "Stop blood",
      "d": "Produce hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 21,
    "question": "Skin main layers are?",
    "options": {
      "a": "Bone and muscle",
      "b": "Epidermis and dermis",
      "c": "Heart and liver",
      "d": "Blood and bone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 22,
    "question": "Sebaceous gland produces?",
    "options": {
      "a": "Sweat",
      "b": "Sebum (oil)",
      "c": "Blood",
      "d": "Oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 23,
    "question": "Skin functions include?",
    "options": {
      "a": "Protection and temperature regulation",
      "b": "Digestion",
      "c": "Blood pumping",
      "d": "Breathing only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 24,
    "question": "Common skin diseases include?",
    "options": {
      "a": "Acne and eczema",
      "b": "Malaria",
      "c": "Diabetes",
      "d": "Asthma"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 3: Skeletal, Muscular & Integumentary Systems",
  "id": "bio_ch3"
}

# Format IDs correctly for the new questions
formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Bio_Ch3_Q{i+1:02d}"
    q['subjectId'] = 'bio'
    q['chapterId'] = 'bio_ch3'
    formatted_questions.append(q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Add chapter
    chapter_ids = [c['id'] for c in data.get('chapters', [])]
    if new_chapter['id'] not in chapter_ids:
        data.setdefault('chapters', []).append(new_chapter)
        
    # Add questions
    existing_q_ids = {q['id'] for q in data.get('questions', [])}
    added_count = 0
    for q in formatted_questions:
        if q['id'] not in existing_q_ids:
            data.setdefault('questions', []).append(q)
            added_count += 1
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added {added_count} questions to seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

if new_chapter['id'] not in data_json.get('chapters', {}):
    data_json.setdefault('chapters', {})[new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

added_count_json = 0
for q in formatted_questions:
    q_id = q['id']
    if q_id not in data_json.get('questions', {}):
        q_copy = q.copy()
        del q_copy['id']
        data_json.setdefault('questions', {})[q_id] = q_copy
        added_count_json += 1

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print(f"Added {added_count_json} questions to seed_data.json")

