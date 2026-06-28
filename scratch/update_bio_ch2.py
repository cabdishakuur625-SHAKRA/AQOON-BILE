import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Hypothalamus and pituitary gland control the release of?",
    "options": {
      "a": "Digestive enzymes",
      "b": "Hormones in endocrine system",
      "c": "Bone cells",
      "d": "Blood cells"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Endocrine glands release hormones directly into?",
    "options": {
      "a": "Ducts",
      "b": "Bloodstream",
      "c": "Skin",
      "d": "Organs"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Exocrine glands secrete substances through?",
    "options": {
      "a": "Blood",
      "b": "Ducts",
      "c": "Neurons",
      "d": "Hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Insulin function is to?",
    "options": {
      "a": "Increase blood sugar",
      "b": "Decrease blood sugar",
      "c": "Break bones",
      "d": "Increase heartbeat"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Glucagon function is to?",
    "options": {
      "a": "Lower blood glucose",
      "b": "Increase blood glucose",
      "c": "Stop breathing",
      "d": "Form muscles"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Pituitary gland is known as?",
    "options": {
      "a": "Digestive gland",
      "b": "Master gland",
      "c": "Skin gland",
      "d": "Bone gland"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Homeostasis is maintained by?",
    "options": {
      "a": "Random changes",
      "b": "Feedback mechanisms",
      "c": "Bone growth",
      "d": "Muscle contraction"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },

  {
    "id": 8,
    "question": "Which gland produces insulin and glucagon?",
    "options": {
      "a": "Thyroid",
      "b": "Pancreas",
      "c": "Pituitary",
      "d": "Adrenal"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 9,
    "question": "Thyroid gland controls?",
    "options": {
      "a": "Digestion",
      "b": "Metabolic rate",
      "c": "Bone length",
      "d": "Skin color"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 10,
    "question": "Adrenal gland controls?",
    "options": {
      "a": "Stress response and blood pressure",
      "b": "Vision",
      "c": "Hearing",
      "d": "Bone growth"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 11,
    "question": "Negative feedback mechanism means?",
    "options": {
      "a": "Increases hormone action",
      "b": "Reduces initial stimulus",
      "c": "Stops all body functions",
      "d": "Creates new glands"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 12,
    "question": "Positive feedback mechanism means?",
    "options": {
      "a": "Reduces response",
      "b": "Increases response",
      "c": "Stops hormones",
      "d": "Destroys glands"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 13,
    "question": "Endocrine glands differ from exocrine glands because?",
    "options": {
      "a": "Use ducts",
      "b": "Release hormones into blood",
      "c": "Do not function",
      "d": "Produce bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Pancreas is both endocrine and exocrine because?",
    "options": {
      "a": "Produces only enzymes",
      "b": "Produces hormones and enzymes",
      "c": "Produces blood",
      "d": "Produces bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },

  {
    "id": 15,
    "question": "Steroid hormones can enter cells because they are?",
    "options": {
      "a": "Water soluble",
      "b": "Lipid soluble",
      "c": "Protein only",
      "d": "Non functional"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 16,
    "question": "Amino acid hormones act by binding to?",
    "options": {
      "a": "Cell membrane receptors",
      "b": "Bone cells",
      "c": "Blood cells",
      "d": "DNA directly"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 17,
    "question": "Thyroid hormones mainly control?",
    "options": {
      "a": "Metabolism",
      "b": "Bone breaking",
      "c": "Skin color",
      "d": "Heart structure"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 18,
    "question": "Gigantism is caused by?",
    "options": {
      "a": "Low insulin",
      "b": "Excess growth hormone",
      "c": "Low calcium",
      "d": "Low thyroid hormone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 19,
    "question": "Dwarfism is caused by?",
    "options": {
      "a": "High growth hormone",
      "b": "Low growth hormone",
      "c": "High insulin",
      "d": "Low glucose"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 20,
    "question": "Feedback mechanisms are important for?",
    "options": {
      "a": "Homeostasis",
      "b": "Bone formation",
      "c": "Skin color",
      "d": "Digestion only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },

  {
    "id": 21,
    "question": "Pituitary gland is called master gland because?",
    "options": {
      "a": "It controls all endocrine glands",
      "b": "It digests food",
      "c": "It produces blood",
      "d": "It forms bones"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 22,
    "question": "Pancreas is exocrine because it?",
    "options": {
      "a": "Uses ducts",
      "b": "Releases hormones only",
      "c": "Produces bones",
      "d": "Controls brain"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 23,
    "question": "Insulin lowers blood glucose by?",
    "options": {
      "a": "Storing glucose in cells",
      "b": "Breaking bones",
      "c": "Increasing glucose",
      "d": "Stopping breathing"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 24,
    "question": "Glucagon increases blood glucose by?",
    "options": {
      "a": "Breaking down glycogen",
      "b": "Reducing oxygen",
      "c": "Stopping liver",
      "d": "Forming bones"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 25,
    "question": "Steroid hormones act by?",
    "options": {
      "a": "Binding cell membrane receptors",
      "b": "Entering nucleus and changing gene activity",
      "c": "Breaking bones",
      "d": "Blocking blood flow"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "Homeostasis is maintained mainly by?",
    "options": {
      "a": "Hormones and feedback systems",
      "b": "Bones",
      "c": "Skin only",
      "d": "Muscles only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  }
]

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
    
    # Remove existing bio_ch2 questions
    data['questions'] = [q for q in data['questions'] if q['chapterId'] != 'bio_ch2']
    
    # Add new bio_ch2 questions
    data['questions'].extend(formatted_questions)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {len(formatted_questions)} questions in seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Remove existing bio_ch2 questions from dict
keys_to_remove = [k for k, v in data_json['questions'].items() if v.get('chapterId') == 'bio_ch2']
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
