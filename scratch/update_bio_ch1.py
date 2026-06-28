import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Stimulants are drugs that do what to the central nervous system?",
    "options": {
      "a": "Slow down activity",
      "b": "Speed up activity",
      "c": "Stop impulses",
      "d": "Destroy neurons"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Depressants mainly?",
    "options": {
      "a": "Increase brain activity",
      "b": "Slow down brain activity",
      "c": "Increase reflexes",
      "d": "Produce hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Sensory receptors send impulses to the?",
    "options": {
      "a": "Muscles",
      "b": "Central nervous system",
      "c": "Bones",
      "d": "Skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Motor neurons carry impulses to?",
    "options": {
      "a": "Brain only",
      "b": "Muscles and glands",
      "c": "Skin only",
      "d": "Bones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "The basic unit of the nervous system is?",
    "options": {
      "a": "Nephron",
      "b": "Neuron",
      "c": "Cell membrane",
      "d": "Hormone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Myelin sheath function is to?",
    "options": {
      "a": "Slow nerve impulses",
      "b": "Insulate axon and speed up transmission",
      "c": "Produce hormones",
      "d": "Destroy neurons"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Cochlea is responsible for?",
    "options": {
      "a": "Balance",
      "b": "Hearing",
      "c": "Smell",
      "d": "Taste"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "Chemoreceptors detect?",
    "options": {
      "a": "Light",
      "b": "Chemicals",
      "c": "Sound",
      "d": "Heat only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },

  {
    "id": 9,
    "question": "Brain stem consists of?",
    "options": {
      "a": "Cerebrum only",
      "b": "Midbrain, pons and medulla oblongata",
      "c": "Spinal cord only",
      "d": "Cerebellum only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 10,
    "question": "Diencephalon includes?",
    "options": {
      "a": "Thalamus and hypothalamus",
      "b": "Cerebrum and cerebellum",
      "c": "Spinal cord",
      "d": "Muscles"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 11,
    "question": "Resting potential means?",
    "options": {
      "a": "Neuron is active",
      "b": "Neuron is not conducting impulses",
      "c": "Neuron is dividing",
      "d": "Neuron is damaged"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 12,
    "question": "Action potential is?",
    "options": {
      "a": "Electrical impulse in neuron",
      "b": "Muscle contraction only",
      "c": "Hormone release",
      "d": "Blood flow"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 13,
    "question": "Synapse is a junction between?",
    "options": {
      "a": "Two neurons",
      "b": "Two bones",
      "c": "Muscle and bone",
      "d": "Skin layers"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Cerebrum is responsible for?",
    "options": {
      "a": "Reflex only",
      "b": "Thinking, memory and voluntary actions",
      "c": "Breathing only",
      "d": "Digestion only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 15,
    "question": "Cerebellum function is?",
    "options": {
      "a": "Balance and coordination",
      "b": "Hormone production",
      "c": "Digestion",
      "d": "Vision only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 16,
    "question": "Spinal cord mainly controls?",
    "options": {
      "a": "Thinking",
      "b": "Reflex actions and signal transmission",
      "c": "Hormones",
      "d": "Vision"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 17,
    "question": "Motor division of PNS carries impulses to?",
    "options": {
      "a": "CNS",
      "b": "Muscles and glands",
      "c": "Brain only",
      "d": "Skin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 18,
    "question": "Sensory division of PNS carries impulses to?",
    "options": {
      "a": "Muscles",
      "b": "CNS",
      "c": "Bones",
      "d": "Heart"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 19,
    "question": "Rod cells in the eye function in?",
    "options": {
      "a": "Color vision in bright light",
      "b": "Low light vision",
      "c": "Hearing",
      "d": "Balance"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },

  {
    "id": 20,
    "question": "Pons is important because it acts as a?",
    "options": {
      "a": "Digestive organ",
      "b": "Bridge for nerve signals",
      "c": "Bone connector",
      "d": "Hormone gland"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 21,
    "question": "DNA polymerase function is?",
    "options": {
      "a": "Break DNA strands",
      "b": "Synthesize new DNA strands",
      "c": "Make proteins",
      "d": "Destroy RNA"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 22,
    "question": "Helicase enzyme does what?",
    "options": {
      "a": "Joins amino acids",
      "b": "Unwinds DNA double helix",
      "c": "Makes hormones",
      "d": "Forms ribosomes"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 23,
    "question": "Central dogma of biology is?",
    "options": {
      "a": "Protein → DNA → RNA",
      "b": "DNA → RNA → Protein",
      "c": "RNA → DNA → Protein",
      "d": "Protein → RNA → DNA"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 24,
    "question": "Transcription produces?",
    "options": {
      "a": "Protein",
      "b": "RNA",
      "c": "DNA",
      "d": "Lipid"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 25,
    "question": "Translation occurs at the?",
    "options": {
      "a": "Nucleus",
      "b": "Ribosome",
      "c": "Cell membrane",
      "d": "Golgi body"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "tRNA function is to?",
    "options": {
      "a": "Carry amino acids",
      "b": "Store DNA",
      "c": "Make hormones",
      "d": "Break proteins"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 27,
    "question": "Codon is found in?",
    "options": {
      "a": "DNA",
      "b": "mRNA",
      "c": "Protein",
      "d": "Cell membrane"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 28,
    "question": "Anticodon is found in?",
    "options": {
      "a": "mRNA",
      "b": "tRNA",
      "c": "DNA",
      "d": "Protein"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 29,
    "question": "Introns are?",
    "options": {
      "a": "Coding regions",
      "b": "Non-coding regions",
      "c": "Proteins",
      "d": "Enzymes"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 30,
    "question": "Exons are?",
    "options": {
      "a": "Non-coding DNA",
      "b": "Coding regions of genes",
      "c": "Lipids",
      "d": "Hormones"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Bio_Ch1_Q{i+1:02d}"
    q['subjectId'] = 'bio'
    q['chapterId'] = 'bio_ch1'
    formatted_questions.append(q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Remove existing bio_ch1 questions
    data['questions'] = [q for q in data['questions'] if q['chapterId'] != 'bio_ch1']
    
    # Add new bio_ch1 questions
    data['questions'].extend(formatted_questions)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {len(formatted_questions)} questions in seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Remove existing bio_ch1 questions from dict
keys_to_remove = [k for k, v in data_json['questions'].items() if v.get('chapterId') == 'bio_ch1']
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

