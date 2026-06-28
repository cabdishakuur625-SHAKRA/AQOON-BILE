import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "A nucleotide is made up of?",
    "options": {
      "a": "Protein, lipid, carbohydrate",
      "b": "Sugar, phosphate group, nitrogenous base",
      "c": "DNA and RNA",
      "d": "Amino acid, enzyme, hormone"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "In DNA base pairing, Adenine pairs with?",
    "options": {
      "a": "Guanine",
      "b": "Cytosine",
      "c": "Thymine",
      "d": "Uracil"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "In DNA base pairing, Guanine pairs with?",
    "options": {
      "a": "Thymine",
      "b": "Adenine",
      "c": "Cytosine",
      "d": "Uracil"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Codon is found in?",
    "options": {
      "a": "DNA",
      "b": "mRNA",
      "c": "tRNA",
      "d": "rRNA"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Anticodon is found in?",
    "options": {
      "a": "mRNA",
      "b": "DNA",
      "c": "tRNA",
      "d": "rRNA"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Transcription occurs in?",
    "options": {
      "a": "Cytoplasm only",
      "b": "Nucleus",
      "c": "Cell membrane",
      "d": "Ribosome only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Translation occurs at?",
    "options": {
      "a": "Ribosomes",
      "b": "Nucleus",
      "c": "Mitochondria",
      "d": "Golgi body"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "DNA stores genetic information in the form of?",
    "options": {
      "a": "Proteins",
      "b": "Lipids",
      "c": "Nucleotide sequence",
      "d": "Hormones"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 9,
    "question": "RNA contains which base instead of thymine?",
    "options": {
      "a": "Adenine",
      "b": "Guanine",
      "c": "Uracil",
      "d": "Cytosine"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 10,
    "question": "DNA replication is called semiconservative because?",
    "options": {
      "a": "Both strands are destroyed",
      "b": "Each new DNA has one old and one new strand",
      "c": "No strands are copied",
      "d": "It happens only once"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },

  {
    "id": 11,
    "question": "Helicase function is to?",
    "options": {
      "a": "Join amino acids",
      "b": "Unwind DNA strands",
      "c": "Make ribosomes",
      "d": "Break proteins"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 12,
    "question": "DNA polymerase function is to?",
    "options": {
      "a": "Break DNA",
      "b": "Synthesize new DNA strands",
      "c": "Destroy RNA",
      "d": "Make proteins"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 13,
    "question": "Genetic code refers to?",
    "options": {
      "a": "Protein structure",
      "b": "Sequence of bases in DNA",
      "c": "Cell membrane structure",
      "d": "Blood type system"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Intron is a?",
    "options": {
      "a": "Coding region of DNA",
      "b": "Non-coding region of DNA",
      "c": "Protein",
      "d": "Enzyme"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 15,
    "question": "Exon is a?",
    "options": {
      "a": "Coding region of gene",
      "b": "Non-coding region",
      "c": "Enzyme",
      "d": "Lipid"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 16,
    "question": "mRNA carries information from?",
    "options": {
      "a": "Protein to DNA",
      "b": "DNA to ribosome",
      "c": "Ribosome to nucleus",
      "d": "Protein to nucleus"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 17,
    "question": "tRNA function is to?",
    "options": {
      "a": "Carry amino acids",
      "b": "Store DNA",
      "c": "Make enzymes",
      "d": "Break proteins"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 18,
    "question": "Central dogma is?",
    "options": {
      "a": "Protein → DNA → RNA",
      "b": "DNA → RNA → Protein",
      "c": "RNA → DNA → Protein",
      "d": "Protein → RNA → DNA"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 19,
    "question": "Transcription produces?",
    "options": {
      "a": "DNA",
      "b": "RNA",
      "c": "Protein",
      "d": "Lipid"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 20,
    "question": "Translation results in formation of?",
    "options": {
      "a": "DNA",
      "b": "RNA",
      "c": "Protein",
      "d": "Carbohydrate"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },

  {
    "id": 21,
    "question": "The sequence of amino acids is determined by?",
    "options": {
      "a": "DNA structure",
      "b": "mRNA codons",
      "c": "tRNA shape",
      "d": "Cell membrane"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 22,
    "question": "During transcription, DNA is used to make?",
    "options": {
      "a": "Protein",
      "b": "RNA",
      "c": "Lipid",
      "d": "Glucose"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 23,
    "question": "Which enzyme joins nucleotides during DNA replication?",
    "options": {
      "a": "Helicase",
      "b": "DNA polymerase",
      "c": "Ligase",
      "d": "Pepsin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 24,
    "question": "DNA replication is important because?",
    "options": {
      "a": "It destroys DNA",
      "b": "It produces identical copies of DNA",
      "c": "It makes proteins",
      "d": "It produces RNA only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 25,
    "question": "Anticodon pairs with?",
    "options": {
      "a": "DNA strand",
      "b": "mRNA codon",
      "c": "Protein",
      "d": "Enzyme"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "Which structure carries genetic information from nucleus to cytoplasm?",
    "options": {
      "a": "tRNA",
      "b": "mRNA",
      "c": "DNA",
      "d": "Ribosome"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 27,
    "question": "Introns are removed during?",
    "options": {
      "a": "Translation",
      "b": "RNA processing",
      "c": "Replication",
      "d": "Mutation"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 28,
    "question": "Exons are important because they?",
    "options": {
      "a": "Do not code for proteins",
      "b": "Code for proteins",
      "c": "Destroy RNA",
      "d": "Block transcription"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 29,
    "question": "Which process converts mRNA into protein?",
    "options": {
      "a": "Transcription",
      "b": "Replication",
      "c": "Translation",
      "d": "Mutation"
    },
    "correctAnswer": "c",
    "difficultyLevel": "hard"
  },
  {
    "id": 30,
    "question": "The flow of genetic information is best described as?",
    "options": {
      "a": "Protein → DNA → RNA",
      "b": "DNA → RNA → Protein",
      "c": "RNA → Protein → DNA",
      "d": "DNA → Protein → RNA"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 4: Genetics and DNA",
  "id": "bio_ch4"
}

# Format IDs correctly for the new questions
formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Bio_Ch4_Q{i+1:02d}"
    q['subjectId'] = 'bio'
    q['chapterId'] = 'bio_ch4'
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

