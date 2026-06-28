import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Axial skeleton includes which of the following?",
    "options": {
      "a": "Limbs and girdles",
      "b": "Skull and vertebral column",
      "c": "Hands and feet",
      "d": "Shoulder bones only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Appendicular skeleton includes:",
    "options": {
      "a": "Skull and ribs",
      "b": "Vertebral column",
      "c": "Limbs and girdles",
      "d": "Brain case"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Bone is a type of:",
    "options": {
      "a": "Muscle tissue",
      "b": "Connective tissue",
      "c": "Nervous tissue",
      "d": "Epithelial tissue"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Cartilage cells are called:",
    "options": {
      "a": "Osteocytes",
      "b": "Chondrocytes",
      "c": "Leukocytes",
      "d": "Erythrocytes"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Exoskeleton is found:",
    "options": {
      "a": "Inside body",
      "b": "Outside body",
      "c": "In blood",
      "d": "In muscles"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Endoskeleton is located:",
    "options": {
      "a": "Outside body",
      "b": "Inside body",
      "c": "On skin",
      "d": "In blood"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "A long bone example is:",
    "options": {
      "a": "Skull",
      "b": "Femur",
      "c": "Rib",
      "d": "Scapula"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "Osteoporosis causes:",
    "options": {
      "a": "Strong bones",
      "b": "Weak bones",
      "c": "Muscle growth",
      "d": "Skin thickening"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 9,
    "question": "Synovial fluid function is to:",
    "options": {
      "a": "Produce blood",
      "b": "Reduce friction in joints",
      "c": "Form bones",
      "d": "Strengthen muscles"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 10,
    "question": "Ossification is:",
    "options": {
      "a": "Muscle contraction",
      "b": "Bone formation",
      "c": "Skin growth",
      "d": "Blood production"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 11,
    "question": "Arthritis is:",
    "options": {
      "a": "Bone fracture",
      "b": "Joint inflammation",
      "c": "Muscle tear",
      "d": "Skin disease"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 12,
    "question": "Sunlight helps bones by producing:",
    "options": {
      "a": "Vitamin A",
      "b": "Vitamin D",
      "c": "Vitamin C",
      "d": "Vitamin K"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },

  {
    "id": 13,
    "question": "Fixed joints allow:",
    "options": {
      "a": "Free movement",
      "b": "No movement",
      "c": "Muscle growth",
      "d": "Blood flow"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Semi-movable joints allow:",
    "options": {
      "a": "No movement",
      "b": "Limited movement",
      "c": "Full movement",
      "d": "Muscle contraction"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 15,
    "question": "Movable joints allow:",
    "options": {
      "a": "No movement",
      "b": "Limited movement",
      "c": "Free movement",
      "d": "Bone growth only"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },
  {
    "id": 16,
    "question": "The basic unit of skeletal muscle is:",
    "options": {
      "a": "Neuron",
      "b": "Sarcomere",
      "c": "Osteon",
      "d": "Chondrocyte"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 17,
    "question": "Fast twitch muscles have:",
    "options": {
      "a": "More myoglobin",
      "b": "Fewer mitochondria",
      "c": "Slow contraction",
      "d": "High endurance"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 18,
    "question": "Slow twitch muscles are used for:",
    "options": {
      "a": "Short bursts",
      "b": "Endurance activities",
      "c": "No movement",
      "d": "Reflex only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 19,
    "question": "Flexor muscles:",
    "options": {
      "a": "Straighten joints",
      "b": "Bend joints",
      "c": "Break bones",
      "d": "Produce hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 20,
    "question": "Extensor muscles:",
    "options": {
      "a": "Bend joints",
      "b": "Straighten joints",
      "c": "Destroy muscles",
      "d": "Produce blood"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 21,
    "question": "Muscle fatigue is caused by:",
    "options": {
      "a": "High oxygen only",
      "b": "Low oxygen and waste build-up",
      "c": "High sugar only",
      "d": "Bone damage"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 22,
    "question": "Heart muscle does not fatigue because:",
    "options": {
      "a": "No blood supply",
      "b": "Many mitochondria",
      "c": "No nerves",
      "d": "No contraction"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 23,
    "question": "Skin has two main layers:",
    "options": {
      "a": "Bone and muscle",
      "b": "Epidermis and dermis",
      "c": "Nerve and blood",
      "d": "Fat and bone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 24,
    "question": "Skin functions include:",
    "options": {
      "a": "Digestion only",
      "b": "Protection and temperature regulation",
      "c": "Bone formation",
      "d": "Blood pumping"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },

  {
    "id": 25,
    "question": "Arthritis is mainly:",
    "options": {
      "a": "Muscle disease",
      "b": "Joint inflammation",
      "c": "Skin infection",
      "d": "Bone cancer"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "Rheumatoid arthritis is:",
    "options": {
      "a": "Age related only",
      "b": "Not age related",
      "c": "Bone disease",
      "d": "Muscle disease"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 27,
    "question": "Bone formation process is called:",
    "options": {
      "a": "Digestion",
      "b": "Ossification",
      "c": "Respiration",
      "d": "Excretion"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 28,
    "question": "Myosin and actin are involved in:",
    "options": {
      "a": "Bone formation",
      "b": "Muscle contraction",
      "c": "Skin growth",
      "d": "Blood formation"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 29,
    "question": "Muscle injuries in football include:",
    "options": {
      "a": "Only bone fracture",
      "b": "Strain and cramps",
      "c": "Only skin cuts",
      "d": "Only nerve damage"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 30,
    "question": "Synovial fluid is found in:",
    "options": {
      "a": "Muscles",
      "b": "Joints",
      "c": "Skin",
      "d": "Bones only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 31,
    "question": "Sebaceous glands produce:",
    "options": {
      "a": "Sweat",
      "b": "Sebum (oil)",
      "c": "Blood",
      "d": "Bone cells"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 32,
    "question": "Hair is mainly composed of:",
    "options": {
      "a": "Bone cells",
      "b": "Keratin",
      "c": "Blood",
      "d": "Muscle fibers"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 33,
    "question": "Nails are made of:",
    "options": {
      "a": "Calcium only",
      "b": "Keratin",
      "c": "Blood cells",
      "d": "Fat"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 34,
    "question": "Skin disorders include:",
    "options": {
      "a": "Malaria",
      "b": "Acne and eczema",
      "c": "Diabetes",
      "d": "Typhoid"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 35,
    "question": "Oil that prevents skin drying is called:",
    "options": {
      "a": "Bile",
      "b": "Sebum",
      "c": "Glucose",
      "d": "Plasma"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

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
    
    # Remove existing bio_ch3 questions
    data['questions'] = [q for q in data['questions'] if q['chapterId'] != 'bio_ch3']
    
    # Add new bio_ch3 questions
    data['questions'].extend(formatted_questions)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {len(formatted_questions)} questions in seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Remove existing bio_ch3 questions from dict
keys_to_remove = [k for k, v in data_json['questions'].items() if v.get('chapterId') == 'bio_ch3']
for k in keys_to_remove:
    del data_json['questions'][k]

# Add new ones
added_count_json = 0
for q in formatted_questions:
    q_id = q['id']
    q_copy = q.copy()
    del q_copy['id']
    data_json['questions'][q_id] = q_copy
    added_count_json += 1

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print(f"Updated {added_count_json} questions in seed_data.json")

