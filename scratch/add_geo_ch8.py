import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "question": "Sohdin siyaasadeed waa maxay?",
    "options": {
      "a": "Dhul dabiici ah oo buur ah",
      "b": "Xuduud ay dadku sameeyeen si danahooda loo ilaaliyo",
      "c": "Webiyo dabiici ah",
      "d": "Badaha adduunka"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Jiid iyo sohdin maxaa lagu kala saaraa?",
    "options": {
      "a": "Jiidu waa is beddeli karaa",
      "b": "Sohdintu waa dabiici",
      "c": "Jiidu waa siyaasadeed",
      "d": "Labaduba waa isku mid"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Sohdintu maxay ka caawisaa dowladaha?",
    "options": {
      "a": "Ganacsi kaliya",
      "b": "Ilaalinta amniga iyo xadka",
      "c": "Kordhinta dadka",
      "d": "Biyo qabatin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Xuduud dabiici ah tusaale waa maxay?",
    "options": {
      "a": "Buuro",
      "b": "Khad sawir ah",
      "c": "Warqad",
      "d": "Xeer"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Kashmiir inta badan waa maxay?",
    "options": {
      "a": "Buuraha iyo harooyin",
      "b": "Desert",
      "c": "Jasiirad",
      "d": "Bad"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Ruhinga waa maxay?",
    "options": {
      "a": "Qabiil Hinduu",
      "b": "Muslimiinta Barma",
      "c": "Yuhuud",
      "d": "Carab"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Biyaha caalamiga ah waa maxay?",
    "options": {
      "a": "Biyo gaar ah",
      "b": "Biyo aan dowlad xad lahayn",
      "c": "Harooyin",
      "d": "Wabiyaal"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Falastiin xaggee ku taallaa?",
    "options": {
      "a": "Afrika",
      "b": "Koonfur bari badda dhexe",
      "c": "Ameerika",
      "d": "Asia bari fog"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "question": "Israa’iil goormaa la aasaasay?",
    "options": {
      "a": "1948",
      "b": "1930",
      "c": "1955",
      "d": "1920"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Magaca Falastiin xaggee laga keenay?",
    "options": {
      "a": "Badda Lija",
      "b": "Afrika",
      "c": "Asia",
      "d": "Europe"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "question": "Xuduud dabiici ah maxaa lagu gartaa?",
    "options": {
      "a": "Khariidad kaliya",
      "b": "Buuraha iyo webiyada",
      "c": "Qoraal",
      "d": "Dhismaha"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Xuduud handasi ah waa maxay?",
    "options": {
      "a": "Dabiici",
      "b": "Khad dad sameeyay",
      "c": "Bad",
      "d": "Buuro"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Kashmiir maxaa ka dhigay muran?",
    "options": {
      "a": "Cimilada",
      "b": "Xuduud iyo gumeysi",
      "c": "Biyaha",
      "d": "Dhirta"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Sohdinta dowladuhu maxay maraan?",
    "options": {
      "a": "2 heer",
      "b": "3 heer",
      "c": "4 heer",
      "d": "5 heer"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },
  {
    "question": "Webiga u dhexeeya USA iyo Mexico waa?",
    "options": {
      "a": "Nile",
      "b": "Riyojaraid",
      "c": "Amazon",
      "d": "Danube"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Kashmiir boqolkiiba intee Muslimiin ah?",
    "options": {
      "a": "60%",
      "b": "70%",
      "c": "80%",
      "d": "90%"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },
  {
    "question": "Ingiriiska Hindiya goormuu qabsaday?",
    "options": {
      "a": "1819",
      "b": "1850",
      "c": "1900",
      "d": "1750"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Hindiya goormay xorowday?",
    "options": {
      "a": "1945",
      "b": "1947",
      "c": "1950",
      "d": "1930"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Miyanmaar goormay ka go’day Ingiriiska?",
    "options": {
      "a": "1937",
      "b": "1940",
      "c": "1920",
      "d": "1950"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "question": "Biyaha gudaha maxay yihiin?",
    "options": {
      "a": "Bad furan",
      "b": "Biyo gudaha dalka",
      "c": "Webi kaliya",
      "d": "Roob"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "question": "Asalka Kashmiir murankiisu waa maxay?",
    "options": {
      "a": "Cimilo",
      "b": "Gumeysi iyo xuduud",
      "c": "Ganacsi",
      "d": "Biyo"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Sohdinta siyaasadeed maxay ilaalisaa?",
    "options": {
      "a": "Kaliya ganacsi",
      "b": "Amniga iyo jiritaanka dalka",
      "c": "Cimilada",
      "d": "Dhirta"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Isticmaarku maxuu sababay?",
    "options": {
      "a": "Nabad",
      "b": "Xuduudo muran leh",
      "c": "Midnimo",
      "d": "Koboc"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Biyaha caalamiga ah waa maxay?",
    "options": {
      "a": "Biyo dowlad leedahay",
      "b": "Biyo furan",
      "c": "Haro",
      "d": "Webi"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Raso qaaradeed waa maxay?",
    "options": {
      "a": "Buur",
      "b": "Dhul badda hoostiisa ah",
      "c": "Lamadegaan",
      "d": "Webi"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Soomaaliya xuduudaha badankoodu waa?",
    "options": {
      "a": "Dabiici",
      "b": "Handasi",
      "c": "Qani",
      "d": "Furan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Xiriirka gumeystaha iyo xuduudaha waa?",
    "options": {
      "a": "Toos",
      "b": "Taban oo muran keena",
      "c": "Nabad",
      "d": "Ganacsi"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Juqraafiga siyaasadeed waxa uu daraaseeyaa?",
    "options": {
      "a": "Dhirta",
      "b": "Siyaasadda iyo juqraafiga",
      "c": "Xayawaanka",
      "d": "Biyaha"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Soomaaliya dhul ay sheegato waa sababta?",
    "options": {
      "a": "Cimilo",
      "b": "Xuduud gumeysi",
      "c": "Dhir",
      "d": "Dalxiis"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "question": "Sohdin siyaasadeed maxay saamaysaa marka dadka kordhaan?",
    "options": {
      "a": "Yaraan",
      "b": "Fidid",
      "c": "Baaba",
      "d": "Joojin"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 8aad: Juqraafiga Siyaasadda",
  "id": "geo_ch8"
}

# Format IDs correctly for the new questions
formatted_questions = []
for i, q in enumerate(new_questions_raw):
    q['id'] = f"Geo_Ch8_Q{i+1:02d}"
    q['subjectId'] = 'geo'
    q['chapterId'] = 'geo_ch8'
    formatted_questions.append(q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Add chapter
    chapter_ids = [c['id'] for c in data['chapters']]
    if new_chapter['id'] not in chapter_ids:
        data['chapters'].append(new_chapter)
        
    # Add questions
    existing_q_ids = {q['id'] for q in data['questions']}
    added_count = 0
    for q in formatted_questions:
        if q['id'] not in existing_q_ids:
            data['questions'].append(q)
            added_count += 1
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added {added_count} questions to seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

if new_chapter['id'] not in data_json['chapters']:
    data_json['chapters'][new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

added_count_json = 0
for q in formatted_questions:
    q_id = q['id']
    if q_id not in data_json['questions']:
        q_copy = q.copy()
        del q_copy['id']
        data_json['questions'][q_id] = q_copy
        added_count_json += 1

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print(f"Added {added_count_json} questions to seed_data.json")
