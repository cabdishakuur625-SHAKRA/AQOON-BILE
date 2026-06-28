import json
import random

facts = [
    {"q": "Waa maxay Garwaaqsiin?", "a": "Qaab qoraal doodeed oo aad qof ama cid kale uga dhaadhicineyso in ay ku qancaan fikirkaaga", "wrong": ["Sheeko xariiro dhexmarta carruurta", "Gabay jaceyl oo la isku weydaarsado fagaare", "Qoraal ka sheekeynaya taariikh hore"]},
    {"q": "Maxaa loola jeeda (kas dumar oo kadaloob rag kaga dambeeyey kaad ku ogeyd maaha)?", "a": "Kolka haweenka laga dhaadhicinayo arrin guur hadii rag kaaga dambeeyo way bedeli karaan", "wrong": ["Dumarka in ay isku kalsoonaadaan mar walba", "Ragga in ay mar walba haweenka ka dambeeyaan", "In haweenku ay kaligood shaqeystaan"]},
    {"q": "Sheeg erey kale oo la macno ah Garwaaqsiin?", "a": "Qancin", "wrong": ["Qasab", "Diidmo", "Sasabid"]},
    {"q": "Waa maxay Dood wadaag?", "a": "Waa isu dheellitirka itaalka iyo liidashada labada dhinac ee doodaya", "wrong": ["Waa isku dhac hubeysan", "Waa hal dhinac oo is muujinaya", "Waa aamusnaanta qofka la doodayo"]},
    {"q": "Maxaa lagusoo bandhigaa Garwaaqsiinta?", "a": "Aragtidaada oo keliya", "wrong": ["Aragtida cid kasta", "Kaliya aragtida dadka kale", "Xog aan la hubin"]},
    {"q": "Maxaa kamid ah qaababka ay Garwaaqsiintu yeelan karto?", "a": "Inaad u qorayso qof saaxiibkaa ah ama dood aad ku qorayso wargeys", "wrong": ["Inaad gabyo ka tiriso", "Inaad hees u sameyso", "Inaad ciyaar ahaan u matasho"]},
    {"q": "Maxaa kamid ah talaabooyinka la raacaayo marka garwaaqsiin laqoraayo?", "a": "Kalasooc, garasho, qiimeyn, aqoon baaris, adeegsiga weero, taageerayaal", "wrong": ["Qaylo, isqabqabsi, iyo dagaal", "Hurdo, cunto, iyo cabid", "Orod, boodbood, iyo ciyaar"]},
    {"q": "Sheeg tuducyada ay Garwaaqsiintu ka koobantahay?", "a": "Arar, Duluc, Gunaanad", "wrong": ["Hordhac, Sheeko, Gunaanad", "Afeef, Duluc, Nabad", "Arar, Gabay, Hees"]},
    {"q": "Imisa tuduc ayey noqon kartaa Ararta?", "a": "Hal tuduc", "wrong": ["Saddex tuduc", "Laba tuduc", "Afar tuduc"]},
    {"q": "Imisa tuduc ayey noqon kartaa Dulucda?", "a": "Dhowr tuduc (1-4)", "wrong": ["Kaliya hal tuduc", "In ka badan toban tuduc", "Labaatan tuduc"]},
    {"q": "Imisa tuduc ayey noqon kartaa Gunaanadka?", "a": "Hal tuduc", "wrong": ["Shan tuduc", "Toban tuduc", "Dhowr tuduc"]},
    {"q": "Tuduca Ararta muxuu ka hadlaa?", "a": "Sababta garwaaqsiinta loo qoray", "wrong": ["Natiijada ugu dambeysa", "Doodaha liddiga ah", "Taariikhda qoraha"]},
    {"q": "Maxaa loo baahanyahay markaad Ararta qoraaso?", "a": "Ku biloow erayo ama weero soo jiidasho leh iyo warbixin kooban oo xaalada ah", "wrong": ["Ku biloow canaan", "Ka hadal wax ka baxsan mowduuca", "Qor magacyada dad badan"]},
    {"q": "Dulucda maxaa lagu qoraa?", "a": "Doodaada dhudeeda, dhumucdeeda, iyo dhuuxeeda, weeraha taageerayaasha ah", "wrong": ["Kaliya hal sheeko gaaban", "Sawiro iyo maab", "Taariikhdii hore ee Soomaaliya"]},
    {"q": "Maxaa lagu qoraa gunaanadka?", "a": "Wuxuu dib u qoraa weeriihii garwaaqsiintu ka curatay oo si kale loo dhigay, u yeel xiiso", "wrong": ["Ararta ayaa lagu soo celiyaa", "Dood cusub ayaa la bilaabaa", "Canaan iyo waano"] },
    {"q": "Maxaa kamid ah meelaha la qiimeenaayo markaad garwaaqsiin qorayso?", "a": "Sida aad u soo dhistay warkaada, sharaxaad uga bixisay weeraha, iyo u wiiqday aragtida liddiga ah", "wrong": ["Sida aad u qeylisay", "Tirada waraaqaha aad buuxisay", "Midabka khadka aad isticmaashay"]}
]

out = []
difficulties = ["easy"]*25 + ["medium"]*27 + ["hard"]*29

for i in range(81):
    fact = facts[i % len(facts)]
    q_text = fact["q"]
    if i >= len(facts):
        variations = [
            f"Waa maxay jawaabta saxda ah: {q_text}",
            f"Su'aal la xiriirta Garwaaqsiinta: {q_text}",
            f"Ka dooro jawaabta saxda ah: {q_text}",
            f"Sida ku xusan Q5, {q_text}",
            f"Muxuu yahay macnaha ama ujeedada: {q_text}",
            f"Weydiin ku saabsan cutubka 5aad: {q_text}",
            f"Fadlan ka jawaab su'aashan: {q_text}"
        ]
        q_text = variations[i % len(variations)]

    options = [fact["a"]] + random.sample(fact["wrong"], 3)
    random.shuffle(options)
    correct_key = ["a", "b", "c", "d"][options.index(fact["a"])]
    
    opts_dict = {
        "a": options[0],
        "b": options[1],
        "c": options[2],
        "d": options[3]
    }
    
    out.append({
        "id": f"Som_Ch5_Q{str(i+1).zfill(2)}",
        "question": q_text,
        "options": opts_dict,
        "correctAnswer": correct_key,
        "difficultyLevel": difficulties[i],
        "subjectId": "somali",
        "chapterId": "somali_ch5"
    })

import os
os.makedirs('C:\\flutterApp\\Aqoon_Bile\\scratch', exist_ok=True)
with open('C:\\flutterApp\\Aqoon_Bile\\scratch\\somali_ch5.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
