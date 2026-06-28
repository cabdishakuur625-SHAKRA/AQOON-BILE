import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Species diversity refers to?",
    "options": {
      "a": "Variety of genes in a population",
      "b": "Number of different species in a community",
      "c": "Number of individuals in a species",
      "d": "Size of ecosystem"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Genetic diversity refers to?",
    "options": {
      "a": "Variety of ecosystems",
      "b": "Variety of genes within a species",
      "c": "Number of species",
      "d": "Number of habitats"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Biodiversity includes?",
    "options": {
      "a": "Only animals",
      "b": "Only plants",
      "c": "Genes, species and ecosystems",
      "d": "Only microorganisms"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Greenhouse effect is a process that?",
    "options": {
      "a": "Cools the Earth",
      "b": "Warms the Earth",
      "c": "Destroys ozone layer",
      "d": "Produces oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Primary cause of modern extinction is?",
    "options": {
      "a": "Habitat destruction",
      "b": "Increased oxygen",
      "c": "More rainfall",
      "d": "Plant growth"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Biological magnification refers to?",
    "options": {
      "a": "Decrease of toxins in food chain",
      "b": "Increase of toxins in food chain",
      "c": "Growth of plants",
      "d": "Increase of oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Conservation biology focuses on?",
    "options": {
      "a": "Destroying ecosystems",
      "b": "Protecting biodiversity",
      "c": "Increasing pollution",
      "d": "Climate change only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "Reserves are important because they?",
    "options": {
      "a": "Increase pollution",
      "b": "Protect wildlife and habitats",
      "c": "Destroy forests",
      "d": "Increase hunting"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 9,
    "question": "Acid rain is mainly caused by?",
    "options": {
      "a": "Oxygen and water vapor",
      "b": "Sulfur and nitrogen oxides",
      "c": "Carbon dioxide only",
      "d": "Helium gas"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 10,
    "question": "Pollution is defined as?",
    "options": {
      "a": "Natural recycling process",
      "b": "Release of harmful substances into environment",
      "c": "Growth of plants",
      "d": "Animal migration"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 11,
    "question": "Bioindicators are?",
    "options": {
      "a": "Machines used in labs",
      "b": "Living organisms that show ecosystem health",
      "c": "Chemical fertilizers",
      "d": "Artificial sensors"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": 12,
    "question": "Ecosystem diversity refers to?",
    "options": {
      "a": "Variety of ecosystems in a region",
      "b": "One species in an area",
      "c": "One gene type",
      "d": "One habitat only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },

  {
    "id": 13,
    "question": "Which best describes greenhouse effect?",
    "options": {
      "a": "Conversion of heat into light",
      "b": "Trapping of heat in Earth's atmosphere",
      "c": "Loss of atmospheric gases",
      "d": "Increase in oxygen level"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 14,
    "question": "Which is NOT a cause of extinction?",
    "options": {
      "a": "Habitat destruction",
      "b": "Climate change",
      "c": "Overharvesting",
      "d": "Increased biodiversity"
    },
    "correctAnswer": "d",
    "difficultyLevel": "medium"
  },
  {
    "id": 15,
    "question": "Biomagnification occurs when toxins?",
    "options": {
      "a": "Decrease in food chain",
      "b": "Increase at higher trophic levels",
      "c": "Disappear in water",
      "d": "Become harmless"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 16,
    "question": "DDT becomes most concentrated in?",
    "options": {
      "a": "Producers",
      "b": "Top predators",
      "c": "Soil only",
      "d": "Water only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 17,
    "question": "Conservation biology aims to?",
    "options": {
      "a": "Increase extinction",
      "b": "Protect species and ecosystems",
      "c": "Increase pollution",
      "d": "Reduce oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 18,
    "question": "Restoration biology is focused on?",
    "options": {
      "a": "Creating new diseases",
      "b": "Repairing damaged ecosystems",
      "c": "Increasing hunting",
      "d": "Deforestation"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 19,
    "question": "Acid rain damages plants by?",
    "options": {
      "a": "Increasing nutrients",
      "b": "Removing soil nutrients",
      "c": "Adding oxygen",
      "d": "Increasing growth rate"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 20,
    "question": "Global warming mainly results from?",
    "options": {
      "a": "Greenhouse gases",
      "b": "Increase in fish",
      "c": "Decrease in plants",
      "d": "Volcanic rocks only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": 21,
    "question": "Eutrophication is?",
    "options": {
      "a": "Air cleaning process",
      "b": "Water pollution due to nutrients",
      "c": "Soil formation",
      "d": "Animal reproduction"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 22,
    "question": "Hotspots are areas with?",
    "options": {
      "a": "Low biodiversity",
      "b": "High endemic species and risk of extinction",
      "c": "No plants",
      "d": "Only water bodies"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 23,
    "question": "Genetic diversity is important because it?",
    "options": {
      "a": "Reduces adaptation",
      "b": "Increases survival ability",
      "c": "Stops evolution",
      "d": "Kills species"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": 24,
    "question": "Species diversity helps ecosystems by?",
    "options": {
      "a": "Weakening stability",
      "b": "Increasing stability",
      "c": "Stopping food chains",
      "d": "Reducing oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },

  {
    "id": 25,
    "question": "Greenhouse gases include?",
    "options": {
      "a": "Oxygen and nitrogen",
      "b": "Carbon dioxide and methane",
      "c": "Helium and neon",
      "d": "Hydrogen only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 26,
    "question": "Highest toxin concentration in food chains is found in?",
    "options": {
      "a": "Producers",
      "b": "Primary consumers",
      "c": "Top carnivores",
      "d": "Decomposers"
    },
    "correctAnswer": "c",
    "difficultyLevel": "hard"
  },
  {
    "id": 27,
    "question": "Biomagnification increases along?",
    "options": {
      "a": "Food web upward",
      "b": "Soil only",
      "c": "Air only",
      "d": "Plants only"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 28,
    "question": "Acid rain forms when sulfur oxides combine with?",
    "options": {
      "a": "Helium",
      "b": "Water vapor",
      "c": "Nitrogen gas",
      "d": "Oxygen only"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 29,
    "question": "Habitat destruction leads to?",
    "options": {
      "a": "Increased biodiversity",
      "b": "Species extinction",
      "c": "More oxygen",
      "d": "Stable ecosystems"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 30,
    "question": "Overexploitation means?",
    "options": {
      "a": "Sustainable use of resources",
      "b": "Excessive use of species",
      "c": "Plant growth",
      "d": "Natural balance"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 31,
    "question": "Pollution affects biodiversity by?",
    "options": {
      "a": "Improving habitats",
      "b": "Damaging ecosystems",
      "c": "Increasing reproduction",
      "d": "Increasing oxygen"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 32,
    "question": "Climate change impacts include?",
    "options": {
      "a": "Stable temperatures",
      "b": "Droughts and reduced crops",
      "c": "More biodiversity",
      "d": "No environmental change"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 33,
    "question": "Acid rain removes which nutrients from soil?",
    "options": {
      "a": "Calcium and potassium",
      "b": "Hydrogen only",
      "c": "Oxygen only",
      "d": "Helium and neon"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 34,
    "question": "Conservation reserves are important because they?",
    "options": {
      "a": "Increase hunting",
      "b": "Protect endangered species",
      "c": "Destroy habitats",
      "d": "Increase pollution"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 35,
    "question": "Which is a threat to biodiversity?",
    "options": {
      "a": "Habitat loss",
      "b": "Photosynthesis",
      "c": "Seed dispersal",
      "d": "Pollination"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 36,
    "question": "Ecosystem biodiversity includes diversity of?",
    "options": {
      "a": "Genes only",
      "b": "Species only",
      "c": "Habitats and ecosystems",
      "d": "Proteins only"
    },
    "correctAnswer": "c",
    "difficultyLevel": "hard"
  },
  {
    "id": 37,
    "question": "Greenhouse effect leads to?",
    "options": {
      "a": "Global cooling",
      "b": "Global warming",
      "c": "No change",
      "d": "Soil formation"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 38,
    "question": "Pollution types include?",
    "options": {
      "a": "Air, water and soil",
      "b": "Only air",
      "c": "Only water",
      "d": "Only soil"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": 39,
    "question": "Climate change increases?",
    "options": {
      "a": "Crop yield stability",
      "b": "Heat and drought",
      "c": "Biodiversity always",
      "d": "Water purity"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": 40,
    "question": "Oil spills mainly affect?",
    "options": {
      "a": "Only land",
      "b": "Marine ecosystems",
      "c": "Only air",
      "d": "Rocks"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "bio",
  "title": "Chapter 7: Ecology and Biodiversity",
  "id": "bio_ch7"
}

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Bio_Ch7_Q{i+1:02d}"
    q['subjectId'] = 'bio'
    q['chapterId'] = 'bio_ch7'
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

