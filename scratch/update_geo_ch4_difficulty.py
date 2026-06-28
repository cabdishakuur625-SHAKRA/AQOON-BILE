import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
    {
      "id": "Chap4_Q1",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya falaki ahaan inta u dhaxaysa waa?",
      "options": {
        "a": "2° Koonfur ilaa 12° Waqooyi",
        "b": "10° ilaa 20°",
        "c": "0° ilaa 5°",
        "d": "15° ilaa 25°"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q2",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxay dhacdaa qaaradda?",
      "options": {
        "a": "Aasiya",
        "b": "Yurub",
        "c": "Afrika",
        "d": "Ameerika"
      },
      "correctAnswer": "c",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q3",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya deris lama aha?",
      "options": {
        "a": "Itoobiya",
        "b": "Kenya",
        "c": "Jabuuti",
        "d": "Sudan"
      },
      "correctAnswer": "d",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q4",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waa buundo isku xirta qaaradaha?",
      "options": {
        "a": "Afrika, Aasiya, Yurub",
        "b": "Afrika iyo Ameerika",
        "c": "Aasiya iyo Ameerika",
        "d": "Yurub iyo Australia"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q5",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Istiraatiijiyadda Soomaaliya waxay muhiim u tahay?",
      "options": {
        "a": "Ganacsiga caalamiga ah",
        "b": "Ciyaaraha",
        "c": "Beeraha kaliya",
        "d": "Macdanta"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q6",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Gobollada Soomaaliya waxaa ugu horeeya?",
      "options": {
        "a": "Jubbada Hoose",
        "b": "Hargeysa",
        "c": "Garoowe",
        "d": "Kismaayo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q7",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Noocyada dhulka Soomaaliya waxaa ka mid ah?",
      "options": {
        "a": "Bannaano, buuro, dulo",
        "b": "Kaliya buuro",
        "c": "Kaliya biyo",
        "d": "Kaliya lamadegaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q8",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Buurta ugu dheer Soomaaliya waa?",
      "options": {
        "a": "Buurta Suurad",
        "b": "Buurta Kilimanjaro",
        "c": "Buurta Golis",
        "d": "Buurta Everest"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q9",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Waxyaabaha saameeya cimilada waxaa ka mid ah?",
      "options": {
        "a": "Cadceedda iyo dabaysha",
        "b": "Kaliya dhulka",
        "c": "Kaliya badda",
        "d": "Kaliya buuraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q10",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Joogga sare wuxuu saameeyaa?",
      "options": {
        "a": "Heerkulka",
        "b": "Midabka dhulka",
        "c": "Dhismaha",
        "d": "Waddooyinka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q11",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxay dhacdaa bariga qaaradda?",
      "options": {
        "a": "Afrika",
        "b": "Aasiya",
        "c": "Yurub",
        "d": "Ameerika"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q12",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Xadka Soomaaliya ugu dheer waa kan ay la wadaagto?",
      "options": {
        "a": "Itoobiya",
        "b": "Kenya",
        "c": "Jabuuti",
        "d": "Eritrea"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q13",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxay leedahay xeeb dheer oo ku taalla?",
      "options": {
        "a": "Badweynta Hindiya",
        "b": "Badda Mediterranean",
        "c": "Atlantic",
        "d": "Pacific"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q14",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Cimilada Soomaaliya guud ahaan waa?",
      "options": {
        "a": "Kul iyo qalalan",
        "b": "Qabow",
        "c": "Baraf leh",
        "d": "Roob joogto ah"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q15",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Roobabka Soomaaliya waa?",
      "options": {
        "a": "Aan joogto ahayn",
        "b": "Joogto ah",
        "c": "Baraf",
        "d": "Marnaba ma da’o"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q16",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Dhulka Soomaaliya inta badan waa?",
      "options": {
        "a": "Bannaan",
        "b": "Buuro kaliya",
        "c": "Biyo kaliya",
        "d": "Baraf"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q17",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Kalluumeysiga Soomaaliya waxa saameeya?",
      "options": {
        "a": "Raasamaal yari",
        "b": "Baraf",
        "c": "Buuro",
        "d": "Dhul qalalan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q18",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Dhaqaalaha Soomaaliya ugu weyn waa?",
      "options": {
        "a": "Xoolo dhaqasho",
        "b": "Warshado",
        "c": "Macdan",
        "d": "Tiknoolaji"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q19",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Caqabadaha Soomaaliya waxaa ka mid ah?",
      "options": {
        "a": "Abaaro",
        "b": "Baraf badan",
        "c": "Dhul qoyan",
        "d": "Roob joogto ah"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q20",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Webiyada Soomaaliya waxay keenaan?",
      "options": {
        "a": "Fatahaad",
        "b": "Baraf",
        "c": "Buuro",
        "d": "Lamadegaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q21",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxa ay muhiim u tahay ganacsiga sababta oo ah?",
      "options": {
        "a": "Meel istiraatiiji ah",
        "b": "Buuro badan",
        "c": "Baraf",
        "d": "Kaymo badan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q22",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Cufnaanta dadka Soomaaliya guud ahaan waa?",
      "options": {
        "a": "Hoose",
        "b": "Sare",
        "c": "Aad u sare",
        "d": "Midna ma jiro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q23",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Reer miyi Soomaaliya waxay ku tiirsan yihiin?",
      "options": {
        "a": "Xoolo",
        "b": "Warshado",
        "c": "Banking",
        "d": "Tiknoolaji"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q24",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Dalxiiska Soomaaliya waxa hor istaaga?",
      "options": {
        "a": "Amni darro",
        "b": "Baraf",
        "c": "Dhul yar",
        "d": "Kaymo badan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q25",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxa ay leedahay ilaha dhaqaale ee ugu muhiimsan?",
      "options": {
        "a": "Beeraha iyo xoolaha",
        "b": "Warshado",
        "c": "Saliid badan",
        "d": "Tiknoolaji"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q26",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Dhirta Soomaaliya waxay saameyn ku leedahay?",
      "options": {
        "a": "Heerkulka",
        "b": "Macdanta",
        "c": "Waddooyinka",
        "d": "Gaadiidka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q27",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Ganacsiga Soomaaliya inta badan waa?",
      "options": {
        "a": "Dibadda ku tiirsan",
        "b": "Warshado gudaha ah",
        "c": "Tiknoolaji",
        "d": "Suuq la’aan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q28",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Gaadiidka Soomaaliya waxaa ugu badan?",
      "options": {
        "a": "Waddooyin",
        "b": "Tareen",
        "c": "Metro",
        "d": "Tram"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q29",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Webiyada Jubba iyo Shabeelle waxay keenaan?",
      "options": {
        "a": "Fatahaad",
        "b": "Baraf",
        "c": "Buuro",
        "d": "Lamadegaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q30",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxay ka tirsan tahay Dunida?",
      "options": {
        "a": "Hore",
        "b": "Cusub",
        "c": "Baraf",
        "d": "Kaymo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q31",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Cimilada Soomaaliya waxaa saameeya dabaylaha?",
      "options": {
        "a": "Mansuunka",
        "b": "Polar",
        "c": "Snow",
        "d": "Ice"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q32",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waxaa ku badan?",
      "options": {
        "a": "Xoolo dhaqato",
        "b": "Warshado",
        "c": "Robot",
        "d": "Macdan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q33",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Caqabadaha xoolaha waxaa ka mid ah?",
      "options": {
        "a": "Abaaro",
        "b": "Baraf",
        "c": "Biyo badan",
        "d": "Kaymo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q34",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Beeraha Soomaaliya waxaa saameeya?",
      "options": {
        "a": "Biyo yari",
        "b": "Baraf",
        "c": "Kaymo",
        "d": "Buuro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q35",
      "subjectId": "Geography",
      "chapterId": "Chapter 4",
      "question": "Soomaaliya waa dal ku yaalla?",
      "options": {
        "a": "Geeska Afrika",
        "b": "Galbeedka Afrika",
        "c": "Waqooyiga Yurub",
        "d": "Koonfur Ameerika"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    }
  ]

# Format IDs correctly for the new questions
formatted_questions = []
for q in new_questions_raw:
    q['subjectId'] = 'geo'
    q['chapterId'] = 'geo_ch4'
    match = re.match(r'Chap4_Q(\d+)', q['id'])
    if match:
        num = int(match.group(1))
        q['id'] = f"Geo_Ch4_Q{num:02d}"
    formatted_questions.append(q)

new_questions_map = {q['id']: q for q in formatted_questions}

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Update questions in place
    updated_count = 0
    for idx, q in enumerate(data['questions']):
        if q['id'] in new_questions_map:
            data['questions'][idx] = new_questions_map[q['id']]
            updated_count += 1
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {updated_count} questions in seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

updated_count_json = 0


for q in formatted_questions:
    q_id = q['id']
    if q_id in data_json['questions']:
        q_copy = q.copy()
        del q_copy['id']
        data_json['questions'][q_id] = q_copy
        updated_count_json += 1

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print(f"Updated {updated_count_json} questions in seed_data.json")
