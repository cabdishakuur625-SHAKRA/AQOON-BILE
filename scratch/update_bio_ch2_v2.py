import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "The hypothalamus is located in the:",
    "options": {
      "a": "Spinal cord",
      "b": "Brain",
      "c": "Pancreas",
      "d": "Kidney"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "The pituitary gland is also called the:",
    "options": {
      "a": "Thyroid gland",
      "b": "Master gland",
      "c": "Sweat gland",
      "d": "Adrenal gland"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Insulin is produced by the:",
    "options": {
      "a": "Thyroid gland",
      "b": "Pancreas",
      "c": "Liver",
      "d": "Kidney"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Glucagon increases:",
    "options": {
      "a": "Blood glucose level",
      "b": "Blood calcium level",
      "c": "Oxygen level",
      "d": "Water level"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Hormones are secreted directly into the:",
    "options": {
      "a": "Ducts",
      "b": "Bloodstream",
      "c": "Skin",
      "d": "Lungs"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Exocrine glands release substances through:",
    "options": {
      "a": "Blood",
      "b": "Nerves",
      "c": "Ducts",
      "d": "Muscles"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "The thyroid gland regulates:",
    "options": {
      "a": "Digestion",
      "b": "Metabolic rate",
      "c": "Bone length",
      "d": "Vision"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "Gonads produce:",
    "options": {
      "a": "Sweat",
      "b": "Hormones and gametes",
      "c": "Enzymes",
      "d": "Urine"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 9,
    "question": "Homeostasis means:",
    "options": {
      "a": "Body movement",
      "b": "Internal balance",
      "c": "Digestion",
      "d": "Breathing"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 10,
    "question": "Hormones travel through the:",
    "options": {
      "a": "Blood",
      "b": "Air",
      "c": "Nerves only",
      "d": "Bones"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },

  {
    "id": 11,
    "question": "The pancreas is both endocrine and exocrine because it:",
    "options": {
      "a": "Produces blood cells",
      "b": "Releases hormones and digestive enzymes",
      "c": "Controls breathing",
      "d": "Produces bile only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 12,
    "question": "Negative feedback means:",
    "options": {
      "a": "Increasing a process continuously",
      "b": "Stopping a process when normal is reached",
      "c": "Destroying hormones",
      "d": "Making more cells"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 13,
    "question": "Positive feedback causes:",
    "options": {
      "a": "Reduction of a process",
      "b": "Increase in a process",
      "c": "No change",
      "d": "Cell death"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Insulin function is to:",
    "options": {
      "a": "Increase blood sugar",
      "b": "Decrease blood sugar",
      "c": "Increase calcium",
      "d": "Decrease oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 15,
    "question": "Hormones are chemical messengers produced by:",
    "options": {
      "a": "Nervous system",
      "b": "Endocrine glands",
      "c": "Bones",
      "d": "Skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 16,
    "question": "The adrenal gland is responsible for:",
    "options": {
      "a": "Vision",
      "b": "Stress response",
      "c": "Hearing",
      "d": "Smell"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 17,
    "question": "Amino acid hormones act by binding to:",
    "options": {
      "a": "DNA directly",
      "b": "Cell membrane receptors",
      "c": "Bone cells",
      "d": "Blood cells"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 18,
    "question": "Steroid hormones can enter cells because they are:",
    "options": {
      "a": "Water soluble",
      "b": "Lipid soluble",
      "c": "Solid",
      "d": "Large proteins"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 19,
    "question": "The pituitary gland controls other glands by releasing:",
    "options": {
      "a": "Enzymes",
      "b": "Hormones",
      "c": "Oxygen",
      "d": "Blood"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 20,
    "question": "Feedback mechanisms help maintain:",
    "options": {
      "a": "Growth",
      "b": "Homeostasis",
      "c": "Movement",
      "d": "Digestion only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },

  {
    "id": 21,
    "question": "The hypothalamus controls the pituitary gland by releasing:",
    "options": {
      "a": "Digestive juices",
      "b": "Releasing and inhibiting hormones",
      "c": "Oxygen",
      "d": "Blood cells"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 22,
    "question": "Glucagon is secreted when blood glucose is:",
    "options": {
      "a": "High",
      "b": "Low",
      "c": "Constant",
      "d": "Zero"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 23,
    "question": "The target of hormones is called:",
    "options": {
      "a": "Bone",
      "b": "Target cells",
      "c": "Blood",
      "d": "Skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 24,
    "question": "Which hormone regulates calcium level in blood?",
    "options": {
      "a": "Insulin",
      "b": "Parathyroid hormone",
      "c": "Glucagon",
      "d": "Adrenaline"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 25,
    "question": "Steroid hormones mainly affect:",
    "options": {
      "a": "Cytoplasm only",
      "b": "DNA in nucleus",
      "c": "Blood plasma",
      "d": "Cell wall"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "Protein hormones cannot enter cells because they are:",
    "options": {
      "a": "Lipid soluble",
      "b": "Too large",
      "c": "Gas molecules",
      "d": "Ions"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 27,
    "question": "Dwarfism is caused by:",
    "options": {
      "a": "Excess insulin",
      "b": "Low growth hormone",
      "c": "High calcium",
      "d": "High oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 28,
    "question": "Gigantism is caused by:",
    "options": {
      "a": "Low growth hormone",
      "b": "Excess growth hormone",
      "c": "Low insulin",
      "d": "Low thyroid hormone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 29,
    "question": "The pancreas secretes hormones into:",
    "options": {
      "a": "Ducts only",
      "b": "Bloodstream",
      "c": "Skin",
      "d": "Bone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 30,
    "question": "Thyroid hormone mainly controls:",
    "options": {
      "a": "Reflex action",
      "b": "Metabolic rate",
      "c": "Blood pressure only",
      "d": "Digestion only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 31,
    "question": "Endocrine glands are ductless because they:",
    "options": {
      "a": "Have tubes",
      "b": "Release hormones directly into blood",
      "c": "Produce sweat",
      "d": "Store oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 32,
    "question": "Homeostasis is maintained mainly by:",
    "options": {
      "a": "Nervous system only",
      "b": "Feedback mechanisms",
      "c": "Bones",
      "d": "Muscles"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 33,
    "question": "Insulin helps convert glucose into:",
    "options": {
      "a": "Protein",
      "b": "Glycogen",
      "c": "Oxygen",
      "d": "Fat only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 34,
    "question": "The master gland is called so because it:",
    "options": {
      "a": "Produces food",
      "b": "Controls other endocrine glands",
      "c": "Controls bones",
      "d": "Controls skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 35,
    "question": "Positive feedback is important in:",
    "options": {
      "a": "Maintaining balance",
      "b": "Rapid completion of processes",
      "c": "Reducing hormones",
      "d": "Stopping reactions"
    },
    "correctAnswer": "b",
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

