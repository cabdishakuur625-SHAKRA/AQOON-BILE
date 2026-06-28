import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_chapter_data = {
  "chapter": "Ch6",
  "multipleChoiceQuestions": {
    "easy": [
      {
        "id": 1,
        "question": "Biotechnology involves the use of:",
        "options": {
          "a": "Only animals",
          "b": "Living organisms or biological systems",
          "c": "Only chemicals",
          "d": "Only machines"
        },
        "correctAnswer": "b"
      },
      {
        "id": 2,
        "question": "A plasmid is found in:",
        "options": {
          "a": "Plants only",
          "b": "Bacteria",
          "c": "Animals only",
          "d": "Viruses only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 3,
        "question": "Genetic engineering is:",
        "options": {
          "a": "Natural selection",
          "b": "Direct manipulation of genes",
          "c": "Cell division",
          "d": "Protein digestion"
        },
        "correctAnswer": "b"
      },
      {
        "id": 4,
        "question": "Transformation in bacteria is:",
        "options": {
          "a": "Cell death",
          "b": "Uptake of foreign DNA",
          "c": "Digestion of food",
          "d": "Cell respiration"
        },
        "correctAnswer": "b"
      },
      {
        "id": 5,
        "question": "PCR is used to:",
        "options": {
          "a": "Destroy DNA",
          "b": "Copy DNA",
          "c": "Cut proteins",
          "d": "Make hormones"
        },
        "correctAnswer": "b"
      },
      {
        "id": 6,
        "question": "Gel electrophoresis is used to:",
        "options": {
          "a": "Separate DNA fragments",
          "b": "Grow bacteria",
          "c": "Make proteins",
          "d": "Kill viruses"
        },
        "correctAnswer": "a"
      },
      {
        "id": 7,
        "question": "DNA fingerprinting is mainly used in:",
        "options": {
          "a": "Cooking",
          "b": "Forensic science",
          "c": "Plant growth",
          "d": "Respiration"
        },
        "correctAnswer": "b"
      },
      {
        "id": 8,
        "question": "Gene therapy is used to:",
        "options": {
          "a": "Replace faulty genes",
          "b": "Destroy all DNA",
          "c": "Stop cell division",
          "d": "Increase mutations"
        },
        "correctAnswer": "a"
      },
      {
        "id": 9,
        "question": "A transgenic organism contains:",
        "options": {
          "a": "No DNA",
          "b": "Foreign DNA",
          "c": "Only RNA",
          "d": "Only proteins"
        },
        "correctAnswer": "b"
      },
      {
        "id": 10,
        "question": "Human Genome Project aimed to study:",
        "options": {
          "a": "Plant genes",
          "b": "Human DNA",
          "c": "Animal behavior",
          "d": "Virus structure"
        },
        "correctAnswer": "b"
      }
    ],
    "medium": [
      {
        "id": 11,
        "question": "Proteomics is the study of:",
        "options": {
          "a": "DNA structure",
          "b": "Proteins",
          "c": "Cells only",
          "d": "Genes only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 12,
        "question": "Genomics is the study of:",
        "options": {
          "a": "Proteins",
          "b": "Entire genome",
          "c": "Only enzymes",
          "d": "Only RNA"
        },
        "correctAnswer": "b"
      },
      {
        "id": 13,
        "question": "Bioethics deals with:",
        "options": {
          "a": "Plant growth",
          "b": "Ethical issues in biotechnology",
          "c": "Animal hunting",
          "d": "Water cycle"
        },
        "correctAnswer": "b"
      },
      {
        "id": 14,
        "question": "Restriction enzymes are used to:",
        "options": {
          "a": "Join DNA",
          "b": "Cut DNA",
          "c": "Make proteins",
          "d": "Destroy cells"
        },
        "correctAnswer": "b"
      },
      {
        "id": 15,
        "question": "Recombinant DNA technology involves:",
        "options": {
          "a": "Mixing DNA from different sources",
          "b": "Only human DNA",
          "c": "Only bacterial DNA",
          "d": "No DNA manipulation"
        },
        "correctAnswer": "a"
      },
      {
        "id": 16,
        "question": "Plasmids are used in genetic engineering as:",
        "options": {
          "a": "Enzymes",
          "b": "Vectors",
          "c": "Hormones",
          "d": "Cells"
        },
        "correctAnswer": "b"
      },
      {
        "id": 17,
        "question": "One goal of the Human Genome Project was:",
        "options": {
          "a": "Destroy genes",
          "b": "Identify all human genes",
          "c": "Create animals",
          "d": "Stop mutations"
        },
        "correctAnswer": "b"
      },
      {
        "id": 18,
        "question": "Gene cloning produces:",
        "options": {
          "a": "One copy of DNA",
          "b": "Multiple copies of a gene",
          "c": "Proteins only",
          "d": "Cells only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 19,
        "question": "Transgenic crops are useful because they:",
        "options": {
          "a": "Grow slower",
          "b": "Resist pests and diseases",
          "c": "Need more water",
          "d": "Die easily"
        },
        "correctAnswer": "b"
      },
      {
        "id": 20,
        "question": "DNA sequencing is used to:",
        "options": {
          "a": "Identify order of bases",
          "b": "Destroy DNA",
          "c": "Make proteins",
          "d": "Cut cells"
        },
        "correctAnswer": "a"
      },
      {
        "id": 21,
        "question": "In oil spill cleanup, bacteria are used in:",
        "options": {
          "a": "Fermentation",
          "b": "Bioremediation",
          "c": "Photosynthesis",
          "d": "Respiration"
        },
        "correctAnswer": "b"
      },
      {
        "id": 22,
        "question": "PCR is important in:",
        "options": {
          "a": "Cloning animals only",
          "b": "Medical and forensic science",
          "c": "Cooking food",
          "d": "Plant irrigation"
        },
        "correctAnswer": "b"
      },
      {
        "id": 23,
        "question": "Gel electrophoresis separates DNA based on:",
        "options": {
          "a": "Color",
          "b": "Size",
          "c": "Shape only",
          "d": "Temperature"
        },
        "correctAnswer": "b"
      },
      {
        "id": 24,
        "question": "Gene therapy is mainly used for:",
        "options": {
          "a": "Treating genetic diseases",
          "b": "Food production",
          "c": "Animal cloning",
          "d": "Water purification"
        },
        "correctAnswer": "a"
      }
    ],
    "hard": [
      {
        "id": 25,
        "question": "Recombinant DNA technology is widely used in production of:",
        "options": {
          "a": "Insulin and vaccines",
          "b": "Plastic only",
          "c": "Fossil fuels",
          "d": "Metals"
        },
        "correctAnswer": "a"
      },
      {
        "id": 26,
        "question": "A transgenic organism is best described as:",
        "options": {
          "a": "Organism without DNA",
          "b": "Organism with foreign DNA",
          "c": "Dead organism",
          "d": "Virus only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 27,
        "question": "The Human Genome Project was completed to:",
        "options": {
          "a": "Map human genes and DNA sequence",
          "b": "Create new animals",
          "c": "Stop evolution",
          "d": "Destroy bacteria"
        },
        "correctAnswer": "a"
      },
      {
        "id": 28,
        "question": "Proteomics is different from genomics because it studies:",
        "options": {
          "a": "DNA",
          "b": "Proteins",
          "c": "Cells only",
          "d": "Chromosomes only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 29,
        "question": "Restriction enzymes are important because they:",
        "options": {
          "a": "Join DNA strands",
          "b": "Cut DNA at specific sites",
          "c": "Destroy proteins",
          "d": "Make RNA"
        },
        "correctAnswer": "b"
      },
      {
        "id": 30,
        "question": "DNA fingerprinting is mainly used for:",
        "options": {
          "a": "Plant breeding only",
          "b": "Crime investigation and paternity testing",
          "c": "Cooking food",
          "d": "Water cleaning"
        },
        "correctAnswer": "b"
      },
      {
        "id": 31,
        "question": "Bioremediation uses:",
        "options": {
          "a": "Chemicals only",
          "b": "Microorganisms to clean pollution",
          "c": "Machines only",
          "d": "Fire"
        },
        "correctAnswer": "b"
      },
      {
        "id": 32,
        "question": "Gene cloning involves:",
        "options": {
          "a": "Producing identical copies of a gene",
          "b": "Destroying DNA",
          "c": "Making hormones only",
          "d": "Changing chromosomes randomly"
        },
        "correctAnswer": "a"
      },
      {
        "id": 33,
        "question": "PCR is essential in:",
        "options": {
          "a": "DNA amplification",
          "b": "Protein digestion",
          "c": "Cell respiration",
          "d": "Photosynthesis"
        },
        "correctAnswer": "a"
      },
      {
        "id": 34,
        "question": "Gene therapy works by:",
        "options": {
          "a": "Replacing or fixing faulty genes",
          "b": "Destroying all cells",
          "c": "Stopping mutations permanently",
          "d": "Reducing oxygen"
        },
        "correctAnswer": "a"
      },
      {
        "id": 35,
        "question": "One major ethical concern in biotechnology is:",
        "options": {
          "a": "Bioethics",
          "b": "Weather change",
          "c": "Plant growth rate",
          "d": "Soil color"
        },
        "correctAnswer": "a"
      }
    ]
  }
}

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 6: Biotechnology",
  "id": "bio_ch6"
}

formatted_questions = []
q_idx = 1
for diff in ["easy", "medium", "hard"]:
    for q in new_chapter_data["multipleChoiceQuestions"][diff]:
        q['id'] = f"Bio_Ch6_Q{q_idx:02d}"
        q['subjectId'] = 'bio'
        q['chapterId'] = 'bio_ch6'
        q['difficultyLevel'] = diff
        formatted_questions.append(q)
        q_idx += 1

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

