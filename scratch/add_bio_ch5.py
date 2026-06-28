import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_chapter_data = {
  "chapter": "Ch5",
  "multipleChoiceQuestions": {
    "easy": [
      {
        "id": 1,
        "question": "A dominant gene is one that:",
        "options": {
          "a": "Only shows in homozygous form",
          "b": "Always hides recessive traits",
          "c": "Expresses in both homozygous and heterozygous forms",
          "d": "Does not affect phenotype"
        },
        "correctAnswer": "c"
      },
      {
        "id": 2,
        "question": "A recessive gene is expressed when:",
        "options": {
          "a": "It is in heterozygous form",
          "b": "It is in homozygous form",
          "c": "It is dominant",
          "d": "It is sex-linked only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 3,
        "question": "Genotype refers to:",
        "options": {
          "a": "Physical appearance",
          "b": "Genetic makeup",
          "c": "Environmental effect",
          "d": "Blood type only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 4,
        "question": "Phenotype refers to:",
        "options": {
          "a": "Genetic code",
          "b": "Chromosome number",
          "c": "Physical appearance",
          "d": "DNA sequence only"
        },
        "correctAnswer": "c"
      },
      {
        "id": 5,
        "question": "A heterozygous organism has:",
        "options": {
          "a": "Two identical alleles",
          "b": "Two different alleles",
          "c": "No alleles",
          "d": "Only dominant alleles"
        },
        "correctAnswer": "b"
      },
      {
        "id": 6,
        "question": "A carrier of a recessive disorder is:",
        "options": {
          "a": "Homozygous dominant",
          "b": "Homozygous recessive",
          "c": "Heterozygous",
          "d": "Mutated chromosome"
        },
        "correctAnswer": "c"
      },
      {
        "id": 7,
        "question": "Inheritance patterns are commonly shown using:",
        "options": {
          "a": "Graph",
          "b": "Pedigree chart",
          "c": "Histogram",
          "d": "Pie chart"
        },
        "correctAnswer": "b"
      },
      {
        "id": 8,
        "question": "Punnett squares are used to:",
        "options": {
          "a": "Measure height",
          "b": "Predict genetic outcomes",
          "c": "Show food chains",
          "d": "Show respiration"
        },
        "correctAnswer": "b"
      },
      {
        "id": 9,
        "question": "A karyotype shows:",
        "options": {
          "a": "Genes in a food chain",
          "b": "Chromosomes of a cell",
          "c": "Hormones in blood",
          "d": "Proteins in DNA"
        },
        "correctAnswer": "b"
      },
      {
        "id": 10,
        "question": "Down syndrome is caused by:",
        "options": {
          "a": "Gene mutation only",
          "b": "Extra chromosome 21",
          "c": "Missing X chromosome",
          "d": "Virus infection"
        },
        "correctAnswer": "b"
      }
    ],
    "medium": [
      {
        "id": 11,
        "question": "A heterozygous yellow seed plant (Yy) crossed with green seed plant (yy) produces:",
        "options": {
          "a": "All yellow",
          "b": "All green",
          "c": "50% yellow and 50% green",
          "d": "All mixed color"
        },
        "correctAnswer": "c"
      },
      {
        "id": 12,
        "question": "Sex-linked traits are carried on:",
        "options": {
          "a": "Autosomes",
          "b": "Sex chromosomes",
          "c": "Mitochondria",
          "d": "Ribosomes"
        },
        "correctAnswer": "b"
      },
      {
        "id": 13,
        "question": "Color blindness is usually:",
        "options": {
          "a": "Dominant and autosomal",
          "b": "Recessive and sex-linked",
          "c": "Codominant",
          "d": "Polygenic"
        },
        "correctAnswer": "b"
      },
      {
        "id": 14,
        "question": "A test cross is used to determine:",
        "options": {
          "a": "Blood pressure",
          "b": "Unknown genotype",
          "c": "Height",
          "d": "Blood type only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 15,
        "question": "In a heterozygous cross Aa x Aa, homozygous offspring percentage is:",
        "options": {
          "a": "25%",
          "b": "50%",
          "c": "75%",
          "d": "100%"
        },
        "correctAnswer": "c"
      },
      {
        "id": 16,
        "question": "Chromosomes are best observed in:",
        "options": {
          "a": "Interphase",
          "b": "Metaphase",
          "c": "Prophase only",
          "d": "Cytokinesis"
        },
        "correctAnswer": "b"
      },
      {
        "id": 17,
        "question": "Genes located on the same chromosome are called:",
        "options": {
          "a": "Linked genes",
          "b": "Random genes",
          "c": "Mutated genes",
          "d": "Independent genes"
        },
        "correctAnswer": "a"
      },
      {
        "id": 18,
        "question": "A carrier female for color blindness has genotype:",
        "options": {
          "a": "XnXn",
          "b": "XNXn",
          "c": "XNY",
          "d": "YY"
        },
        "correctAnswer": "b"
      },
      {
        "id": 19,
        "question": "Huntington’s disease is usually:",
        "options": {
          "a": "Recessive",
          "b": "Dominant",
          "c": "Sex-linked",
          "d": "Mitochondrial"
        },
        "correctAnswer": "b"
      },
      {
        "id": 20,
        "question": "A pedigree chart is used to study:",
        "options": {
          "a": "Weather patterns",
          "b": "Inheritance in families",
          "c": "Blood flow",
          "d": "Plant growth only"
        },
        "correctAnswer": "b"
      }
    ],
    "hard": [
      {
        "id": 21,
        "question": "In a dihybrid cross, a heterozygous plant YyRr produces how many types of gametes?",
        "options": {
          "a": "2",
          "b": "4",
          "c": "6",
          "d": "8"
        },
        "correctAnswer": "b"
      },
      {
        "id": 22,
        "question": "Genes that are very close together on a chromosome show:",
        "options": {
          "a": "Independent assortment",
          "b": "High recombination",
          "c": "Low recombination",
          "d": "No inheritance"
        },
        "correctAnswer": "c"
      },
      {
        "id": 23,
        "question": "A male with genotype XnY for color blindness is:",
        "options": {
          "a": "Normal",
          "b": "Carrier",
          "c": "Color blind",
          "d": "Homozygous dominant"
        },
        "correctAnswer": "c"
      },
      {
        "id": 24,
        "question": "Down syndrome karyotype shows:",
        "options": {
          "a": "Monosomy",
          "b": "Trisomy 21",
          "c": "XXY",
          "d": "XO"
        },
        "correctAnswer": "b"
      },
      {
        "id": 25,
        "question": "If a trait is recessive, it is expressed only when:",
        "options": {
          "a": "One allele is present",
          "b": "Two dominant alleles are present",
          "c": "Two recessive alleles are present",
          "d": "One dominant allele is present"
        },
        "correctAnswer": "c"
      },
      {
        "id": 26,
        "question": "A cross between YyRr and yyrr is called:",
        "options": {
          "a": "Monohybrid cross",
          "b": "Test cross",
          "c": "Self cross",
          "d": "Back cross only"
        },
        "correctAnswer": "b"
      },
      {
        "id": 27,
        "question": "Linkage reduces:",
        "options": {
          "a": "Mutation",
          "b": "Recombination frequency",
          "c": "DNA replication",
          "d": "Protein synthesis"
        },
        "correctAnswer": "b"
      },
      {
        "id": 28,
        "question": "If a father has Huntington’s disease (dominant), children have:",
        "options": {
          "a": "No chance of disease",
          "b": "Some chance of inheriting it",
          "c": "All children affected",
          "d": "Only daughters affected"
        },
        "correctAnswer": "b"
      },
      {
        "id": 29,
        "question": "The correct ratio in a monohybrid cross is:",
        "options": {
          "a": "3:1",
          "b": "1:1",
          "c": "9:3:3:1",
          "d": "2:2"
        },
        "correctAnswer": "a"
      },
      {
        "id": 30,
        "question": "A karyotype is used to detect:",
        "options": {
          "a": "Blood diseases",
          "b": "Chromosomal abnormalities",
          "c": "Enzyme activity",
          "d": "Hormone levels"
        },
        "correctAnswer": "b"
      }
    ]
  }
}

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 5: Heredity and Mendel's Laws",
  "id": "bio_ch5"
}

formatted_questions = []
q_idx = 1
for diff in ["easy", "medium", "hard"]:
    for q in new_chapter_data["multipleChoiceQuestions"][diff]:
        q['id'] = f"Bio_Ch5_Q{q_idx:02d}"
        q['subjectId'] = 'bio'
        q['chapterId'] = 'bio_ch5'
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

