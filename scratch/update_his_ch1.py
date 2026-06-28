import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
    {
      "id": "Chap1_Q01",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Isirka dadka Cusmaaniyiinta waa?",
      "options": {
        "a": "Qabiil Turki ah",
        "b": "Carab",
        "c": "Faarisi",
        "d": "Mongol"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q02",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladda Cusmaaniyiintu waxay soo if baxday xilligii?",
      "options": {
        "a": "Qarnigii 10aad",
        "b": "Qarnigii 13aad dabayaaqadiisa",
        "c": "Qarnigii 15aad",
        "d": "Qarnigii 18aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q03",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Aasaasihii magaca Cusmaaniyiinta laga keenay waa?",
      "options": {
        "a": "Cusmaan binu Ardhagural",
        "b": "Orkhaan",
        "c": "Muraad",
        "d": "Suleymaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q04",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu ka dhalatay burburkii dawladdii?",
      "options": {
        "a": "Rome",
        "b": "Seljuuq",
        "c": "Persia",
        "d": "Mamluk"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q05",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay gaartay saddex qaaradood oo kala ah?",
      "options": {
        "a": "Afrika, Aasiya, Yurub",
        "b": "Afrika iyo Aasiya",
        "c": "Yurub iyo Ameerika",
        "d": "Aasiya iyo Australia"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q06",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dardaaranka Cusmaan wuxuu ku saabsanaa?",
      "options": {
        "a": "Ganacsi",
        "b": "Jihaad iyo diinta Islaamka",
        "c": "Cilmiga kaliya",
        "d": "Beeraha"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q07",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay u qaybsantay?",
      "options": {
        "a": "5 gobol",
        "b": "10 gobol",
        "c": "32 gobol",
        "d": "50 gobol"
      },
      "correctAnswer": "c",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q08",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suldaanka Cusmaaniyiinta wuxuu ahaa?",
      "options": {
        "a": "Madaxweynaha kaliya",
        "b": "Awoodda ugu sarreysa",
        "c": "Ganacsade",
        "d": "Qareen"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q09",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Ciidanka Cusmaaniyiintu waxay ku saleysnaayeen?",
      "options": {
        "a": "Badda kaliya",
        "b": "Fardooley iyo ciidanka dhulka",
        "c": "Diyaarado",
        "d": "Taangiyo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q10",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Nidaamka maaliyadeed wuxuu ka koobnaa?",
      "options": {
        "a": "Canshuur iyo kharash",
        "b": "Kaliya ganacsi",
        "c": "Kaliya dagaal",
        "d": "Kaliya beeraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q11",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Hay’adda Islaamiga ah waxay ku saleysneyd?",
      "options": {
        "a": "Shareecada Islaamka",
        "b": "Sharciga Yurub",
        "c": "Dastuur cusub",
        "d": "Xeer qabiil"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q12",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suldaankii ugu caansanaa Cusmaaniyiinta waa?",
      "options": {
        "a": "Cusmaan 1",
        "b": "Orkhaan",
        "c": "Muraad",
        "d": "Selim"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q13",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Conistantinople maanta waxaa loo yaqaan?",
      "options": {
        "a": "Ankara",
        "b": "Istanbul",
        "c": "Izmir",
        "d": "Bursa"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q14",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Aasaasihii Cusmaaniyiinta waxaa uu ka yimid gobolka?",
      "options": {
        "a": "Anatolia",
        "b": "Arabia",
        "c": "India",
        "d": "Europe"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q15",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Ardhagaral wuxuu ahaa?",
      "options": {
        "a": "Boqor Faarisi",
        "b": "Hogaamiyaha Cusmaaniyiinta",
        "c": "Ganacsade",
        "d": "Sarkaal Roman"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q16",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Orkhaan wuxuu xukunka qabtay kadib?",
      "options": {
        "a": "Cusmaan 1",
        "b": "Muraad 1",
        "c": "Selim",
        "d": "Fatix"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q17",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Muraad 1 wuxuu ballaariyay dhulka Cusmaaniyiinta dhanka?",
      "options": {
        "a": "Ameerika",
        "b": "Koonfur Yurub",
        "c": "Australia",
        "d": "Afrika galbeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q18",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Muxammad Al-Faatix wuxuu qabsaday Constantinople sanadkii?",
      "options": {
        "a": "1453",
        "b": "1400",
        "c": "1500",
        "d": "1600"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q19",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Ciidanka Cusmaaniyiinta ee caanka ahaa waa?",
      "options": {
        "a": "Janissaries",
        "b": "Spartans",
        "c": "Samurai",
        "d": "Vikings"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q20",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dowladdii Cusmaaniyiintu waxay dhacday sanadkii?",
      "options": {
        "a": "1914",
        "b": "1920",
        "c": "1924",
        "d": "1930"
      },
      "correctAnswer": "c",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q21",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suleymaan Qaanuuni wuxuu caan ku ahaa?",
      "options": {
        "a": "Sharciga iyo maamulka",
        "b": "Ganacsiga",
        "c": "Beeraha",
        "d": "Farsamada"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q22",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dhaqaale ahaan Cusmaaniyiintu waxay ku tiirsanaayeen?",
      "options": {
        "a": "Canshuur iyo ganacsi",
        "b": "Saliid",
        "c": "Macdan dahab",
        "d": "Warshado"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q23",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay bilaabeen inay ku fidaan Yurub kadib?",
      "options": {
        "a": "Qarnigii 12aad",
        "b": "Qarnigii 14aad",
        "c": "Qarnigii 16aad",
        "d": "Qarnigii 18aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q24",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Xarunta Cusmaaniyiinta markii hore waxay ahayd?",
      "options": {
        "a": "Bursa",
        "b": "Baghdad",
        "c": "Cairo",
        "d": "Rome"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q25",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suldaan Orkhaan wuxuu dhisay?",
      "options": {
        "a": "Ciidan joogto ah",
        "b": "Magaalo cusub",
        "c": "Buundo",
        "d": "Deked"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q26",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladda Cusmaaniyiintu waxay ku tiirsaneyd?",
      "options": {
        "a": "Shareecada Islaamka",
        "b": "Sharciga Rooma",
        "c": "Sharciga Hindiya",
        "d": "Sharciga Afrika"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q27",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Mid ka mid ah sababaha burburka Cusmaaniyiinta waa?",
      "options": {
        "a": "Heshiis la’aan",
        "b": "Horumar dhaqaale",
        "c": "Midnimo siyaasadeed",
        "d": "Koboc ciidan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q28",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suleymaan Qaanuuni wuxuu xukumay xilli?",
      "options": {
        "a": "Horumar sare",
        "b": "Burbur",
        "c": "Dagaal 1aad",
        "d": "Dagaal 2aad"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap1_Q29",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Ardhagaral wuxuu geeriyooday sanadkii?",
      "options": {
        "a": "1288",
        "b": "1300",
        "c": "1326",
        "d": "1400"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q30",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaan binu Ardhagaral wuxuu xukunka qabtay kadib?",
      "options": {
        "a": "Aabihiis dhimashadiisa",
        "b": "Dagaal Yurub",
        "c": "Heshiis Rome",
        "d": "Ganacsi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q31",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Buursa waxay noqotay caasimad sanadkii?",
      "options": {
        "a": "1302",
        "b": "1326",
        "c": "1360",
        "d": "1453"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q32",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaan Al-Gaazi wuxuu caan ku ahaa?",
      "options": {
        "a": "Jihaad iyo fidin",
        "b": "Ganacsi",
        "c": "Beeraha",
        "d": "Farshaxan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q33",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Orkhaan wuxuu xukunka qabtay sanadkii?",
      "options": {
        "a": "1326",
        "b": "1302",
        "c": "1361",
        "d": "1413"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q34",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Muxammad 2aad wuxuu caan ku yahay?",
      "options": {
        "a": "Qabsashadii Istanbul",
        "b": "Burbur dowlad",
        "c": "Ganacsi",
        "d": "Cilmi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q35",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay socotay ilaa?",
      "options": {
        "a": "1924",
        "b": "1900",
        "c": "1950",
        "d": "1800"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q36",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Janissaries waxay ahaayeen?",
      "options": {
        "a": "Ciidan gaar ah",
        "b": "Ganacsato",
        "c": "Diblomaasiyiin",
        "d": "Farmers"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q37",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay isticmaaleen nidaam?",
      "options": {
        "a": "Gobol (Sanjak)",
        "b": "Boqortooyo Europe",
        "c": "Federaal USA",
        "d": "Qabiil kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q38",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Constantinople waxay muhiim u ahayd?",
      "options": {
        "a": "Ganacsiga iyo siyaasadda",
        "b": "Beeraha",
        "c": "Kalluumaysi kaliya",
        "d": "Dhul lama degaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q39",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suleymaan Qaanuuni wuxuu dhisay nidaam?",
      "options": {
        "a": "Sharci adag",
        "b": "Qabiil",
        "c": "Ganacsi kaliya",
        "d": "Militar kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q40",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Sababta ugu weyn burburka Cusmaaniyiinta waa?",
      "options": {
        "a": "Kali talisnimo",
        "b": "Horumar dhaqaale",
        "c": "Midnimo",
        "d": "Awood ciidan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q41",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dowladdii Cusmaaniyiintu waxay ahayd?",
      "options": {
        "a": "Islaami",
        "b": "Buddhist",
        "c": "Christian",
        "d": "Secular kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q42",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Orkhaan waxaa lagu tiriyaa inuu aasaasay?",
      "options": {
        "a": "Ciidanka Cusmaaniyiinta",
        "b": "Magaalo",
        "c": "Dastuur",
        "d": "Warshad"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q43",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Muxammad Al-Faatix wuxuu ku guuleystay?",
      "options": {
        "a": "Furashada Istanbul",
        "b": "Burbur ciidamo",
        "c": "Ganacsi Afrika",
        "d": "Dagaal Hindiya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q44",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay isticmaaleen lacag?",
      "options": {
        "a": "Silver iyo gold coin",
        "b": "Bitcoin",
        "c": "Dollar",
        "d": "Euro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q45",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay burburtay kadib?",
      "options": {
        "a": "Dagaalkii 1aad ee aduunka",
        "b": "Dagaal qabiil",
        "c": "Dagaal badeed",
        "d": "Kacdoon beeraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q46",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Suleymaan Qaanuuni wuxuu caan ku ahaa?",
      "options": {
        "a": "Sharci dejin",
        "b": "Ganacsi",
        "c": "Dhismaha kaliya",
        "d": "Ciyaar"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q47",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay ku faafeen?",
      "options": {
        "a": "Yurub iyo Aasiya",
        "b": "Ameerika",
        "c": "Australia",
        "d": "Antarctica"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q48",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Ardhagaral waa aasaasaha?",
      "options": {
        "a": "Cusmaaniyiinta",
        "b": "Seljuuq",
        "c": "Rome",
        "d": "Mamluk"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q49",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Bursa waxay muhiim u ahayd?",
      "options": {
        "a": "Caasimaddii hore",
        "b": "Deked Ameerika",
        "c": "Magaalo cusub",
        "d": "Kaymo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q50",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay burbureen kadib xukunka?",
      "options": {
        "a": "Sultanate",
        "b": "Democracy",
        "c": "Republic",
        "d": "Empire kale"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q51",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaaniyiintu waxay galeen Aasiyada yar qarnigii?",
      "options": {
        "a": "13aad",
        "b": "10aad",
        "c": "15aad",
        "d": "18aad"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q52",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Cusmaan binu Ardhagaral wuxuu dhintay sanadkii?",
      "options": {
        "a": "1326",
        "b": "1302",
        "c": "1288",
        "d": "1400"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap1_Q53",
      "subjectId": "History",
      "chapterId": "Chapter 1",
      "question": "Buursa waxay noqotay caasimad xilligii suldaan?",
      "options": {
        "a": "Cusmaan bin Ardhagaral",
        "b": "Orkhaan",
        "c": "Muraad",
        "d": "Fatix"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    }
  ]

formatted_questions = []
for q in new_questions_raw:
    q['subjectId'] = 'his'
    q['chapterId'] = 'his_ch1'
    match = re.search(r'Chap1_Q(\d+)', q['id'])
    if match:
        num = int(match.group(1))
        q['id'] = f"His_Ch1_Q{num:02d}"
    formatted_questions.append(q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Remove existing his_ch1 questions
    data['questions'] = [q for q in data['questions'] if q['chapterId'] != 'his_ch1']
    
    # Add new his_ch1 questions
    data['questions'].extend(formatted_questions)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {len(formatted_questions)} questions in seed_data.dart")

# 2. Update seed_data.json
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Remove existing his_ch1 questions from dict
keys_to_remove = [k for k, v in data_json['questions'].items() if v.get('chapterId') == 'his_ch1']
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

