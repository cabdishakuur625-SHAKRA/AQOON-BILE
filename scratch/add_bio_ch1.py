import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "question": "Stimulants are drugs that ______.",
    "options": {
      "a": "Slow down brain function",
      "b": "Speed up central nervous system activity",
      "c": "Stop nerve impulses",
      "d": "Destroy neurons"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Depressants are drugs that ______.",
    "options": {
      "a": "Speed up brain function",
      "b": "Slow down brain function",
      "c": "Increase reflex",
      "d": "Improve vision"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Sensory receptors function is to ______.",
    "options": {
      "a": "Carry impulses to CNS",
      "b": "Control muscles",
      "c": "Produce hormones",
      "d": "Digest food"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Motor neuron function is to ______.",
    "options": {
      "a": "Carry impulses to CNS",
      "b": "Carry impulses from CNS to muscles",
      "c": "Store memory",
      "d": "Control digestion"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Myelin sheath is ______.",
    "options": {
      "a": "Blood cell",
      "b": "Fatty insulation of axon",
      "c": "Hormone",
      "d": "Enzyme"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Cochlea is responsible for ______.",
    "options": {
      "a": "Smell",
      "b": "Hearing",
      "c": "Taste",
      "d": "Vision"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Chemoreceptors respond to ______.",
    "options": {
      "a": "Light",
      "b": "Chemicals",
      "c": "Sound",
      "d": "Heat"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Neuron is ______.",
    "options": {
      "a": "Basic unit of nervous system",
      "b": "Muscle cell",
      "c": "Blood cell",
      "d": "Bone cell"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Dendrites receive ______.",
    "options": {
      "a": "Hormones",
      "b": "Nerve impulses",
      "c": "Blood",
      "d": "Oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Brain stem consists of ______.",
    "options": {
      "a": "Cerebrum only",
      "b": "Midbrain, pons and medulla oblongata",
      "c": "Cerebellum only",
      "d": "Spinal cord only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Thalamus is part of ______.",
    "options": {
      "a": "Cerebrum",
      "b": "Diencephalon",
      "c": "Spinal cord",
      "d": "Cerebellum"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Resting potential is ______.",
    "options": {
      "a": "Active nerve state",
      "b": "Non-conducting nerve fibre",
      "c": "Muscle contraction",
      "d": "Hormone release"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Action potential is ______.",
    "options": {
      "a": "Permanent nerve state",
      "b": "Change in membrane potential caused by stimulus",
      "c": "Blood pressure",
      "d": "Heart beat"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Synapse is ______.",
    "options": {
      "a": "Connection between neurons",
      "b": "Bone joint",
      "c": "Skin layer",
      "d": "Blood vessel"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Cerebrum controls ______.",
    "options": {
      "a": "Memory and thinking",
      "b": "Only digestion",
      "c": "Only breathing",
      "d": "Only heartbeat"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Spinal cord function is ______.",
    "options": {
      "a": "Digest food",
      "b": "Transfer information and reflex actions",
      "c": "Produce hormones",
      "d": "Control vision"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Cerebellum function is ______.",
    "options": {
      "a": "Controls balance and coordination",
      "b": "Controls digestion",
      "c": "Controls hearing",
      "d": "Controls skin"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "question": "Medulla oblongata controls ______.",
    "options": {
      "a": "Voluntary movement",
      "b": "Involuntary functions like breathing",
      "c": "Vision only",
      "d": "Memory"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Alzheimer disease is a ______.",
    "options": {
      "a": "Nervous system disease",
      "b": "Skin disease",
      "c": "Bone disease",
      "d": "Eye disease"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  }
]

new_subject = {
  "id": "bio",
  "name": "Biology"
}

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 1: The Nervous System",
  "id": "bio_ch1"
}

# Format IDs correctly for the new questions
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
    
    # Add subject if not exists
    subject_ids = [s['id'] for s in data.get('subjects', [])]
    if new_subject['id'] not in subject_ids:
        data.setdefault('subjects', []).append(new_subject)

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
    print(f"Added subject, chapter, and {added_count} questions to seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Add subject
if new_subject['id'] not in data_json.get('subjects', {}):
    data_json.setdefault('subjects', {})[new_subject['id']] = {
        "name": new_subject['name']
    }

# Add chapter
if new_chapter['id'] not in data_json.get('chapters', {}):
    data_json.setdefault('chapters', {})[new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

# Add questions
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
print(f"Added subject, chapter, and {added_count_json} questions to seed_data.json")
