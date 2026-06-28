import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": "Geo_Ch3_Q01",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay kala duwanaashiyaha deegaanka?",
    "options": {
      "a": "Isbeddelka cimilada oo kaliya",
      "b": "Kala duwanaanshaha noolaha iyo hiddo-sidaha dhirta iyo xoolaha",
      "c": "Kaliya dhirta dunida",
      "d": "Kaliya carrada iyo biyaha"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q02",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa keena burburka deegaanka kaymaha?",
    "options": {
      "a": "Roob badan",
      "b": "Beerashada iyo ballaarinta magaalooyinka",
      "c": "Koritaanka dhirta",
      "d": "Qabowga cimilada"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q03",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay wasakhowga deegaanka?",
    "options": {
      "a": "Nadiifinta deegaanka",
      "b": "Isbeddel iyo daryeel la’aan deegaanka ku timaada",
      "c": "Koritaanka dhirta",
      "d": "Kordhinta biyaha"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q04",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay xaaluf?",
    "options": {
      "a": "Kordhinta carrada",
      "b": "Hoos u dhac ku yimaada carrada iyo dhirta",
      "c": "Koritaanka xoolaha",
      "d": "Biyo badan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q05",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay xarfashada carrada?",
    "options": {
      "a": "Koritaanka dhirta",
      "b": "Dhaqdhaqaaq tartiib ah oo ciidda ah oo dabayl iyo biyo keeno",
      "c": "Sameynta roobka",
      "d": "Nadiifinta hawada"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q06",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay daadad?",
    "options": {
      "a": "Qabow daran",
      "b": "Biyo badan oo roobka ka dhasha",
      "c": "Koritaanka dhirta",
      "d": "Dabayl xooggan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q07",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Kala duwanaashiyaha noolaha waxa uu faa’iido u leeyahay?",
    "options": {
      "a": "Yaraynta wax soo saarka",
      "b": "Horumarinta deegaanka iyo dhaqaalaha",
      "c": "Burburinta deegaanka",
      "d": "Kordhinta wasakhowga"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch3_Q08",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay sababta ugu weyn ee xaalufka Soomaaliya?",
    "options": {
      "a": "Roob badan",
      "b": "Jarista dhirta iyo abaaraha",
      "c": "Koritaanka dhirta",
      "d": "Biyo badan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q09",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa keena wasakhowga biyaha?",
    "options": {
      "a": "Dhirta",
      "b": "Warshadaha iyo qashinka",
      "c": "Roobka",
      "d": "Carrada"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q10",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay nabaad guur?",
    "options": {
      "a": "Kordhinta dhirta",
      "b": "Dhulka oo bacrimin waaya",
      "c": "Koritaanka xoolaha",
      "d": "Roob badan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q11",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay sababta ugu weyn ee daadadka?",
    "options": {
      "a": "Roob xad dhaaf ah",
      "b": "Dhir badan",
      "c": "Qabow",
      "d": "Carrada qalalan"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q12",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa ka mid ah dhibaatooyinka xaalufka?",
    "options": {
      "a": "Kordhinta wax soo saarka",
      "b": "Horumar dhaqaale",
      "c": "Hoos u dhac horumar bulsho",
      "d": "Koritaanka dhirta"
    },
    "correctAnswer": "c",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q13",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa sababa xarfashada carrada?",
    "options": {
      "a": "Dhirta oo badan",
      "b": "Dabayl iyo biyo",
      "c": "Roob yar",
      "d": "Heerkul hoose"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q14",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa loo isticmaalaa dhirta dabiiciga ah?",
    "options": {
      "a": "Kaliya dhismo",
      "b": "Cunto, tamar iyo daaq xoolaad",
      "c": "Kaliya qurxin",
      "d": "Burburin deegaanka"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch3_Q15",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay sababta midabka cas ee carrada gaduudan?",
    "options": {
      "a": "Biyaha",
      "b": "Iron oxides (birta oksaydhkeeda)",
      "c": "Dhirta",
      "d": "Qorraxda"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q16",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay muhiimadda oksijiinka ee dhirta?",
    "options": {
      "a": "Waxay dishaa dhirta",
      "b": "Waxay taageertaa nolosha aadanaha iyo xayawaanka",
      "c": "Waxay yareysaa biyaha",
      "d": "Waxay burburisaa carrada"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q17",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa ka mid ah xalalka xaalufka?",
    "options": {
      "a": "Jarista dhirta",
      "b": "Beerista dhir cusub",
      "c": "Kordhinta dabka",
      "d": "Burburinta kaymaha"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q18",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Maxaa keena filiqsanaanta xayawaanka?",
    "options": {
      "a": "Dhir badan",
      "b": "Cimilada, dhirta iyo kala sarreynta dhulka",
      "c": "Biyo badan",
      "d": "Carrada nadiifta ah"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q19",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Gobollada dabiiciga ah waa maxay?",
    "options": {
      "a": "Meelo isku mid ah cimilada iyo dhirta leh",
      "b": "Meelo warshado leh",
      "c": "Meelo biyo la’aan ah",
      "d": "Meelo magaalooyin ah"
    },
    "correctAnswer": "a",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q20",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Soomaaliya waxay ka tirsan tahay gobolkee?",
    "options": {
      "a": "Gobollada qabowga",
      "b": "Gobollada kulaaleyda",
      "c": "Gobollada cirifyada",
      "d": "Gobollada buuraleyda"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q21",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay sababta ugu weyn ee daadadka u keenaan khasaaro?",
    "options": {
      "a": "Biyo la’aan",
      "b": "Biyo xad dhaaf ah oo aan la maarayn",
      "c": "Dhir badan",
      "d": "Qabow"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q22",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay muhiimadda carrada?",
    "options": {
      "a": "Burburinta dhirta",
      "b": "Koritaanka dhirta iyo beeraha",
      "c": "Yaraynta roobka",
      "d": "Kordhinta dabka"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q23",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay saameynta xarfashada carrada?",
    "options": {
      "a": "Kordhinta wax soo saarka",
      "b": "Hoos u dhac wax soo saar and dhir",
      "c": "Kordhinta roobka",
      "d": "Hagaajinta deegaanka"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch3_Q24",
    "subjectId": "geo",
    "chapterId": "geo_ch3",
    "question": "Waa maxay xaaladda ugu weyn ee deegaanka Soomaaliya?",
    "options": {
      "a": "Dhir badan iyo biyo badan",
      "b": "Jarista dhirta, abaaro iyo daadad",
      "c": "Cimilada qabow",
      "d": "Biyo joogto ah"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  }
]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 3aad: Isbeddellada iyo Dhibaatooyinka Deegaanka",
  "id": "geo_ch3"
}

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
    for q in new_questions_raw:
        if q['id'] not in existing_q_ids:
            data['questions'].append(q)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

if new_chapter['id'] not in data_json['chapters']:
    data_json['chapters'][new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

for q in new_questions_raw:
    q_id = q['id']
    q_data = q.copy()
    del q_data['id']
    data_json['questions'][q_id] = q_data

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print("Updated seed_data.json")
