import json
import os

JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": "Geo_Ch1_Q01",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Qeex cilmiga jiyooloojiga?",
    "options": {
      "a": "Cilmiga barashada xiddigaha",
      "b": "Cilmiga barashada isbeddellada iyo dhaqdhaqaaqa dhulka iyo ilaha tamarta",
      "c": "Cilmiga barashada xayawaanka",
      "d": "Cilmiga barashada hawada"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q02",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Tilmaan laamaha ugu muhiimsan ee cilmiga jiyooloojiga?",
    "options": {
      "a": "Jiyooloojiga bay’ada, handasada, waxbarashada, saliidda iyo dhaqaalaha",
      "b": "Cilmiga kimistariga",
      "c": "Cilmiga xisaabta",
      "d": "Cilmiga siyaasadda"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q03",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Caddee waayada jiyooloojiga?",
    "options": {
      "a": "Hal waqti kaliya",
      "b": "Afar waayo oo kala duwan sida kambiriyan, paleozoic, mesozoic, cenozoic",
      "c": "Laba waayo oo kaliya",
      "d": "Waqti aan kala soocnayn"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q04",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Falanqee ahmiyadda dhaqaale ee waayada jiyooloojiga?",
    "options": {
      "a": "Waxay bixiyaan kaliya carro",
      "b": "Waxay bixiyaan macdano, saliid, dhuxul iyo dhagaxyo dhisme",
      "c": "Waxay bixiyaan biyo kaliya",
      "d": "Waxba ma soo saaraan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q05",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Waa maxay kaalinta culimada muslimiinta ee jiyooloojiga?",
    "options": {
      "a": "Waxba kama aysan qayb qaadan",
      "b": "Waxay horumariyeen cabbirka dhulka iyo wareegiisa",
      "c": "Waxay burburiyeen cilmiga",
      "d": "Waxay diideen sayniska"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q06",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Qaab dhismeedka jiyooloojiga Soomaaliya waxa uu ka yimid?",
    "options": {
      "a": "Badweynta Hindiya",
      "b": "Sagxaddii hore ee Afrika",
      "c": "Qaaradda Yurub",
      "d": "Qaaradda Aasiya"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q07",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Tilmaan xilliyada jiyooloojiga Soomaaliya?",
    "options": {
      "a": "Afar xilli jiyooloji",
      "b": "Hal xilli",
      "c": "Laba xilli kaliya",
      "d": "Saddex xilli kaliya"
    },
    "correctAnswer": "a",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q08",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Saameynta dhaqdhaqaaqyada gilgil ee Soomaaliya waxay la xiriirtaa?",
    "options": {
      "a": "Sameysanka buuro cusub oo Afrika ah",
      "b": "Sameysanka Gacanka Cadmeed iyo Badda Cas",
      "c": "Samaysanka lamadegaanka",
      "d": "Roobab badan"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch1_Q09",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Midkee ka mid ah carrada Soomaaliya?",
    "options": {
      "a": "Carro baraf",
      "b": "Carro foolkaano",
      "c": "Carro barafaysan",
      "d": "Carro badda kaliya"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q10",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Dhibaatada ugu weyn ee carrada Soomaaliya waa?",
    "options": {
      "a": "Carro badan",
      "b": "Carro guur iyo nabaad guur",
      "c": "Carro bacrin ah",
      "d": "Carro dhagax ah"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q11",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Cilmiga jiyooloojiga waxa uu daraaseeyaa?",
    "options": {
      "a": "Kaliya hawada",
      "b": "Dhagaxa, biyaha iyo hawada dhulka",
      "c": "Kaliya xiddigaha",
      "d": "Kaliya badda"
    },
    "correctAnswer": "b",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q12",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Waaga koowaad ee jiyooloojiga Soomaaliya waa?",
    "options": {
      "a": "Ka muuqda dhulka Soomaaliya",
      "b": "Badanaa wuu baaba’ay ama qarsoon yahay",
      "c": "Waa kan ugu cusub",
      "d": "Waa kan ugu gaaban"
    },
    "correctAnswer": "b",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q13",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Sababta kala duwanaanshaha berriga Soomaaliya waa?",
    "options": {
      "a": "Roobab badan",
      "b": "Dhaqdhaqaaq dhul iyo nabaad guur",
      "c": "Dhir badan",
      "d": "Baraf"
    },
    "correctAnswer": "b",
    "difficultyLevel": "hard"
  },
  {
    "id": "Geo_Ch1_Q14",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Da’da dhulka waxaa lagu qiyaasaa ku dhawaad?",
    "options": {
      "a": "2000 milyan sano",
      "b": "3000 milyan sano",
      "c": "4000 milyan sano",
      "d": "1000 milyan sano"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  },
  {
    "id": "Geo_Ch1_Q15",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Da’da qolofta dhulka waxaa lagu qiyaasaa ku dhawaad?",
    "options": {
      "a": "1500 milyan sano",
      "b": "500 milyan sano",
      "c": "300 milyan sano",
      "d": "100 milyan sano"
    },
    "correctAnswer": "a",
    "difficultyLevel": "medium"
  },
  {
    "id": "Geo_Ch1_Q16",
    "subjectId": "geo",
    "chapterId": "geo_ch1",
    "question": "Waaga ugu dheer ee jiyooloojiga waa?",
    "options": {
      "a": "Waaga cusub",
      "b": "Waaga labaad (mesozoic)",
      "c": "Waaga koowaad",
      "d": "Waaga afaraad"
    },
    "correctAnswer": "c",
    "difficultyLevel": "easy"
  }
]

new_chapter = {
  "subjectId": "geo",
  "title": "Cutubka 1aad: Cilmiga Jiyooloojiga iyo Qaab Dhismeedka Soomaaliya",
  "id": "geo_ch1"
}

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update subjects
if "geo" not in data['subjects']:
    data['subjects']['geo'] = {"name": "Geography"}

# Update chapters
if new_chapter['id'] not in data['chapters']:
    data['chapters'][new_chapter['id']] = {
        "subjectId": new_chapter['subjectId'],
        "title": new_chapter['title']
    }

# Update questions
for q in new_questions_raw:
    q_id = q['id']
    q_data = q.copy()
    del q_data['id']
    data['questions'][q_id] = q_data

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {JSON_FILE}")
