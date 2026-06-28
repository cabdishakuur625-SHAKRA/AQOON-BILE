import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  {
    "id": 1,
    "question": "Halkee ayay Soomaaliya kaga taal qaaradda Afrika?",
    "options": { "a": "Galbeedka", "b": "Bariga", "c": "Waqooyiga", "d": "Koonfurta" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 2,
    "question": "Waa ku bama caasimadda dalka Soomaaliya?",
    "options": { "a": "Hargeysa", "b": "Kismaayo", "c": "Muqdisho", "d": "Garowe" },
    "correctAnswer": "c", "difficultyLevel": "easy"
  },
  {
    "id": 3,
    "question": "Waa ku bama buurta ugu dheer Soomaaliya?",
    "options": { "a": "Goolis", "b": "Suurad", "c": "Sifa", "d": "Cal-madow" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 4,
    "question": "Mila ayay Soomaaliya xornimada qaadatay?",
    "options": { "a": "1960", "b": "1964", "c": "1991", "d": "1954" },
    "correctAnswer": "a", "difficultyLevel": "easy"
  },
  {
    "id": 5,
    "question": "Immisa dal ayay Soomaaliya soohdin (xuduud) la leedahay?",
    "options": { "a": "2 dal", "b": "3 dal", "c": "4 dal", "d": "5 dal" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 6,
    "question": "Waa ku bama dalka ugu xuduudda dheer Soomaaliya?",
    "options": { "a": "Jabuuti", "b": "Kiinya", "c": "Itoobiya", "d": "Yaman" },
    "correctAnswer": "c", "difficultyLevel": "easy"
  },
  {
    "id": 7,
    "question": "Waa ku bama isha ugu weyn ee dhaqaalaha Soomaaliya?",
    "options": { "a": "Beeraha", "b": "Xoolaha", "c": "Kalluunka", "d": "Warshadaha" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 8,
    "question": "Waa ku bama magaalada dhacda koonfurta fog ee dalka?",
    "options": { "a": "Boosaaso", "b": "Kismaayo", "c": "Berbera", "d": "Beledweyne" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 9,
    "question": "Waa ku bama labada webi ee mara Soomaaliya?",
    "options": { "a": "Niil iyo Atbara", "b": "Jubba iyo Shabelle", "c": "Tana iyo Galana", "d": "Zambezi iyo Congo" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 10,
    "question": "Immisa boqolkiiba dadka Soomaaliyeed ayaa ah xoolo dhaqato?",
    "options": { "a": "14%", "b": "30%", "c": "65%", "d": "10%" },
    "correctAnswer": "c", "difficultyLevel": "easy"
  },
  {
    "id": 11,
    "question": "Waa ku bama dalka xuduudda ugu gaaban la leh Soomaaliya (58km)?",
    "options": { "a": "Itoobiya", "b": "Kiinya", "c": "Jabuuti", "d": "Eritrea" },
    "correctAnswer": "c", "difficultyLevel": "easy"
  },
  {
    "id": 12,
    "question": "Maxaa keena daadadka badanaa ka dhaca koonfurta Soomaaliya?",
    "options": { "a": "Badda oo soo kacda", "b": "Fatahaadda webiyada", "c": "Dhulgariir", "d": "Dabaylo xooggan" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 13,
    "question": "Halkee ayay u badan yihiin buuraleyda Soomaaliya?",
    "options": { "a": "Koonfurta", "b": "Waqooyiga", "c": "Galbeedka", "d": "Bartamaha" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 14,
    "question": "Waa maxay diinta dadka Soomaaliyeed ay wadaagaan?",
    "options": { "a": "Kirishtaan", "b": "Islaam", "c": "Hindu", "d": "Budhis" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 15,
    "question": "Waa ku bama gobolka ay ku taal caasimadda Muqdisho?",
    "options": { "a": "Banaadir", "b": "Shabelle Hoose", "c": "Shabelle Dhexe", "d": "Hiiraan" },
    "correctAnswer": "a", "difficultyLevel": "easy"
  },
  {
    "id": 16,
    "question": "Waa ku bama gobolka ku yaal barta ugu bariisaneysa Afrika (Xaafuun)?",
    "options": { "a": "Bari", "b": "Mudug", "c": "Nugaal", "d": "Sool" },
    "correctAnswer": "a", "difficultyLevel": "easy"
  },
  {
    "id": 17,
    "question": "Maxay tahay sababta reer miyigu ugu badan yihiin Soomaaliya?",
    "options": { "a": "Magaalo la'aan", "b": "Tiirsanaanta xoolaha", "c": "Dagaallo", "d": "Cimilada qabow" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 18,
    "question": "Waa ku bama dalka kaga beegan Soomaaliya dhanka koonfurta?",
    "options": { "a": "Itoobiya", "b": "Kiinya", "c": "Jabuuti", "d": "Suudaan" },
    "correctAnswer": "b", "difficultyLevel": "easy"
  },
  {
    "id": 19,
    "question": "Xaggee buu ku dherersan yahay taxanaha Buuraleyda Goolis?",
    "options": { "a": "Xeebta waqooyi", "b": "Xeebta bari", "c": "Xuduudda Kiinya", "d": "Webiga Shabelle" },
    "correctAnswer": "a", "difficultyLevel": "easy"
  },
  {
    "id": 20,
    "question": "Maxaa ka mid ah astaamaha dadka Soomaaliyeed?",
    "options": { "a": "Geesinimo", "b": "Sinaan", "c": "Aftahannimo", "d": "Dhammaan waa sax" },
    "correctAnswer": "d", "difficultyLevel": "easy"
  },
  {
    "id": 21,
    "question": "Waa maxay loolalka ay dhaxeyso Soomaaliya falaki ahaan?",
    "options": { "a": "2⁰ K iyo 12⁰ W", "b": "5⁰ K iyo 10⁰ W", "c": "0⁰ iyo 15⁰ W", "d": "2⁰ W iyo 12⁰ K" },
    "correctAnswer": "a", "difficultyLevel": "medium"
  },
  {
    "id": 22,
    "question": "Sidee ayay u fooraartaan dulaha (plateaus) Soomaaliya?",
    "options": { "a": "Koonfur ilaa Waqooyi", "b": "Waqooyi galbeed ilaa koonfur bari", "c": "Bari ilaa Galbeed", "d": "Koonfur bari ilaa Waqooyi galbeed" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 23,
    "question": "Waa ku bama celceliska joogga sare ee bannaannada Soomaaliya?",
    "options": { "a": "500m", "b": "1000m", "c": "2000m", "d": "100m" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 24,
    "question": "Waa maxay saameynta joogga sare ee magaalada Hargeysa xagga huurka?",
    "options": { "a": "Wuu kordhiyaa", "b": "Wuu dhimaa (55%)", "c": "Saameyn ma leh", "d": "Wuxuu ka dhigaa 100%" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 25,
    "question": "Waa ku bama abaartii galaafatay 25% xoolaha Soomaaliya?",
    "options": { "a": "1953", "b": "1974-1975", "c": "1961", "d": "1991" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 26,
    "question": "Maxaa lagu tilmaamaa xuduudaha Soomaaliya iyo deriska?",
    "options": { "a": "Kuwa ugu nabadda badan", "b": "Kuwa ugu xasaasisan Afrika", "c": "Kuwa aan jirin", "d": "Kuwa ugu gaaban" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 27,
    "question": "Waa ku bama ahmiyadda istiraatiijiyadeed ee dalka?",
    "options": { "a": "Waa buundo isku xirta 3 qaaradood", "b": "Waa dhul go'doon ah", "c": "Waa dhul baraf ah", "d": "Waa dhul aan la geli karin" },
    "correctAnswer": "a", "difficultyLevel": "medium"
  },
  {
    "id": 28,
    "question": "Haddii gobollada laga soo bilaabo Koonfur, kee baa u dambeeya?",
    "options": { "a": "Banaadir", "b": "Awdal", "c": "Bari", "d": "Mudug" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 29,
    "question": "Maxaa saameyn weyn ku leh cimilada koonfurta Soomaaliya?",
    "options": { "a": "Barafka", "b": "Cufnaanta dhirta", "c": "Warshadaha", "d": "Gawaarida" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 30,
    "question": "Waa ku bama celceliska huurka ee magaalada Kismaayo?",
    "options": { "a": "55%", "b": "71%", "c": "40%", "d": "90%" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 31,
    "question": "Waa ku bama sanadkii ay dhaceen roobabkii mahigaanka ahaa ee socday 6-da bilood?",
    "options": { "a": "1953", "b": "1961", "c": "1974", "d": "2000" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 32,
    "question": "Maxaa hor taagan in si sax ah dadka loo tiro koobo?",
    "options": { "a": "Aqoon la'aan", "b": "Isgaarsiinta oo xun", "c": "Khibrad yarida agabka", "d": "Dhammaan waa sax" },
    "correctAnswer": "d", "difficultyLevel": "medium"
  },
  {
    "id": 33,
    "question": "Immisa boqolkiiba ayay beeshu (sectors) beeraleyda ka tahay dhaqaalaha?",
    "options": { "a": "65%", "b": "14%", "c": "1%", "d": "12%" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 34,
    "question": "Waa ku bama hannaanka ugu badan ee dadku u filiqsan yihiin?",
    "options": { "a": "Isku dheelitiran", "b": "Aan isku dheelitirneyn", "c": "Magaalo kaliya", "d": "Xeebta kaliya" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 35,
    "question": "Maxay tahay ahmiyadda qaab dhismeedka da'da?",
    "options": { "a": "Waxay xiriir la leedahay dhaqaalaha", "b": "Waxay sheegtaa tirada buuraha", "c": "Waxay xiriir la leedahay roobka", "d": "Muhiim ma ahan" },
    "correctAnswer": "a", "difficultyLevel": "medium"
  },
  {
    "id": 36,
    "question": "Waa ku bama dhoofinta guud ee xoolaha Soomaaliya?",
    "options": { "a": "50%", "b": "80%", "c": "20%", "d": "100%" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 37,
    "question": "Maxaa ka mid ah caqabadaha dabiiciga ah ee xoolaha?",
    "options": { "a": "Abaarta", "b": "Biyo yarida", "c": "Xanuunnada", "d": "Dhammaan waa sax" },
    "correctAnswer": "d", "difficultyLevel": "medium"
  },
  {
    "id": 38,
    "question": "Waa maxay ujeeddada looga guurayo xoolo dhaqashada dhaqameed?",
    "options": { "a": "Si loo yareeyo xoolaha", "b": "Si loo gaaro mid casri ah", "c": "Si dadku u nabaad-guuraan", "d": "Ma jirto sabab" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 39,
    "question": "Immisa boqolkiiba ayaa dhulka Soomaaliya ku haboon beerashada?",
    "options": { "a": "1%", "b": "12.9%", "c": "50%", "d": "80%" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 40,
    "question": "Immisa hektar ayay u dhigantaa 2 malyan oo fadaan?",
    "options": { "a": "1 malyan", "b": "2.7 malyan", "c": "10 malyan", "d": "0.5 malyan" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 41,
    "question": "Waa maxay caqabadda ugu weyn ee haysata kalluun cunidda?",
    "options": { "a": "Kalluunka oo xun", "b": "Dhaqamo hore", "c": "Biyo yari", "d": "Barafka" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 42,
    "question": "Waa ku bama kaalinta warshadaha ee dhaqaalaha Soomaaliya?",
    "options": { "a": "Mid aad u sareysa", "b": "Ma lahan kaalin muhiim ah", "c": "Waa isha koowaad", "d": "Ma jiraan warshado" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 43,
    "question": "Maxay tahay astaanta ganacsiga dibadda ee Soomaaliya?",
    "options": { "a": "Kutiirsanaanta alaabta caydhiinka", "b": "Dhoofinta qalabka elegtarooniga", "c": "Dhoofinta baabuurta", "d": "Ma jiro ganacsi" },
    "correctAnswer": "a", "difficultyLevel": "medium"
  },
  {
    "id": 44,
    "question": "Maxaa ka maqan gaadiidka Soomaaliya?",
    "options": { "a": "Baabuur", "b": "Tareenno", "c": "Diyaarado", "d": "Doomaha" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 45,
    "question": "Waa maxay muhiimadda badda xagga xiriirka?",
    "options": { "a": "Waxay xirtaa dalka", "b": "Waxay isku xirtaa dunida", "c": "Waxay keentaa abaarta", "d": "Muhiim ma ahan" },
    "correctAnswer": "b", "difficultyLevel": "medium"
  },
  {
    "id": 46,
    "question": "Falanqee saameynta falaki ee 2⁰ K iyo 12⁰ W ku leeyihiin heerkulka dalka?",
    "options": { "a": "Wuxuu keenaa heerkul hooseeya", "b": "Wuxuu keenaa celcelis heerkul sarreeyo", "c": "Wuxuu keenaa roob joogto ah", "d": "Saameyn ma leh" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 47,
    "question": "Maxay xuduudda Soomaaliya iyo Itoobiya/Kiinya u tahay mid xasaasi ah?",
    "options": { "a": "Biyo yari darteed", "b": "Loolka gobollada Soomaali Galbeed iyo Waqooyi Bari", "c": "Dagaallo sokeeye darteed", "d": "Xuduudda oo gaaban darteed" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 48,
    "question": "Sidee buu goobta juqraafi ee Soomaaliya u saameeyaa awoodda siyaasadeed?",
    "options": { "a": "Waxay xoojisaa dhaqaalaha iyo difaaca", "b": "Waxay daciifisaa dawladnimada", "c": "Waxay ka dhigtaa dal aan la arki karin", "d": "Saameyn kuma lahan siyaasadda" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 49,
    "question": "Caddee farqiga u dhaxeeya 'Jiidda Banaannada' iyo 'Jiidda Dulaha' ee Soomaaliya?",
    "options": { "a": "Bannaannada waa koonfur, duluhu waa 1/3 dalka oo fooraara", "b": "Bannaannada waa buuro, duluhu waa badda", "c": "Ma jiraan wax farqi ah", "d": "Duluhu waa koonfur kaliya" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 50,
    "question": "Maxaa keena in roobka Soomaaliya uu noqdo mid aan 'nidaamsanayn'?",
    "options": { "a": "Fadhiga falaki ahaan", "b": "Buuraha Goolis", "c": "Dabaylaha badda", "d": "Dhirta oo yar" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 51,
    "question": "Falanqee doorka 'Kanaalka Suweys' ku leeyahay ahmiyadda Soomaaliya?",
    "options": { "a": "Wuxuu Soomaaliya ka dhigaa marin ganacsi caalami ah", "b": "Wuxuu Soomaaliya ka dhigaa meel cidla ah", "c": "Wuxuu keenaa biyo yari", "d": "Waa wado loogu talagalay xoolaha" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 52,
    "question": "Isbarbar dhig dhibaatadii abaartii 1953 iyo 1974?",
    "options": { "a": "1953 waxay dishay 1/3 duunyada, 1974 waxay dishay 25% xoolaha", "b": "Labaduba waa isku mid", "c": "1974 roob baa da'ay", "d": "Ma jirin wax abaaro ah" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 53,
    "question": "Maxaa sababa in huurku uu ka yaraado Hargeysa (55%) marka loo eego Kismaayo (71%)?",
    "options": { "a": "Hargeysa oo badda ku dhow", "b": "Joogga sare iyo ka fogaanshaha xeebta", "c": "Hargeysa oo dhir badan", "d": "Kismaayo oo buuro leh" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 54,
    "question": "Caddee sababta cilmiyeed ee heerkulku ugu hooseeyo Buuraleyda Goolis?",
    "options": { "a": "Badda darteed", "b": "Joogga sare ee dhul dhuleedka", "c": "Magaalooyinka oo fog", "d": "Xoolaha oo jooga" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 55,
    "question": "Maxay tahay caqabadda 'aadanaha' ee haysata waaxda xoolaha?",
    "options": { "a": "Abaarta", "b": "Aqoon yarida habka casriga ah", "c": "Xanuunnada", "d": "Biyo yarida" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 56,
    "question": "Falanqee xiriirka ka dhaxeeya qulqulka webiyada iyo daryeel la'aanta biyo-xireennada?",
    "options": { "a": "Waxay keentaa horumar", "b": "Waxay sababtaa fatahaado naf iyo maal galaafata", "c": "Waxay dhalisaa koronto", "d": "Saameyn ma leh" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 57,
    "question": "Sidee bay 'dabaylaha mansuunka' u saameeyaan cimilada xeebaha?",
    "options": { "a": "Waxay keenaan baraf", "b": "Waxay beddelaan jihada iyo huurka xeebta", "c": "Waxay yareeyaan kheyraadka badda", "d": "Ma jiraan wax dabaylo ah" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 58,
    "question": "Maxaa loola jeedaa 'Hannaanka isku dheelitirnaan' ee filiqsanaanta dadka?",
    "options": { "a": "In dadku si isla eg u degan yihiin dhulka", "b": "In dadku magaalo kaliya degan yihiin", "c": "In dadku aysan dalka deganeyn", "d": "Waa dadka xoolo dhaqatada ah" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 59,
    "question": "Waa maxay caqabadda 'aadanaha' ee ugu weyn ee waaxda beeraha?",
    "options": { "a": "Dhibaatada milixda", "b": "Faragelinta hay'adaha caalamiga ah", "c": "Keydin la'aan", "d": "Carrada oo go'da" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 60,
    "question": "Maxay tahay ujeeddada Wakaaladda Agabka Beeraha?",
    "options": { "a": "Inay xoolaha quudiso", "b": "Dadaalladii xukuumaddii hore ee horumarinta beeraha", "c": "Inay badda ilaaliso", "d": "Inay canshuur qaaddo" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 61,
    "question": "Isbarbar dhig habka waraabka ee 'sanaaciga' iyo kan 'roobka'?",
    "options": { "a": "11kun fadaan (sanaaci) vs 10kun fadaan (roob)", "b": "Roobka ayaa ka badan", "c": "Labaduba waa isku mid", "d": "Ma jiro hab sanaaci ah" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 62,
    "question": "Maxaa keena 'Dhaqamada awooweyaasha' inay yareeyaan faa'iidada kalluunka?",
    "options": { "a": "Kalluunka oo xasaasiyad leh", "b": "Fahamka khaldan ee ah inuu xaaraan yahay", "c": "Kalluunka oo qaali ah", "d": "Kalluunka oo aan la helin" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 63,
    "question": "Falanqee 'Bixinta badeecadaha raasamaalka' ee ganacsiga dibadda?",
    "options": { "a": "Waa dhoofinta caanaha", "b": "Waa soo iibsashada agabka waxsoosaarka iyo shidaalka", "c": "Waa iibinta dhulka", "d": "Waa canshuurta dekedaha" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 64,
    "question": "Waa maxay caqabadda ugu weyn ee 'Kaabayaasha' gaadiidka?",
    "options": { "a": "Gaadiid la'aan", "b": "Masaafooyinka oo aad u kala fog iyo waddooyin xun", "c": "Batrool la'aan", "d": "Dadka oo aan socon" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 65,
    "question": "Maxay dalxiiska Soomaaliya looga faa'iideysan waayay?",
    "options": { "a": "Goobo ma jiraan", "b": "Daryeel la'aan iyo horumarin la'aan", "c": "Dadka ma jecla dalxiiska", "d": "Biyaha ayaa badan" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 66,
    "question": "Caddee sababta dhaqaalaha Soomaaliya uu u tabar daran yahay?",
    "options": { "a": "Kheyraad la'aan", "b": "Awoodi waaga ka faa'ideysiga ilaha jira", "c": "Dadka oo yar", "d": "Badda oo yar" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 67,
    "question": "Maxaa lagu tilmaamaa xiriirka ka dhexeeya juqraafiga iyo awoodda siyaasadeed?",
    "options": { "a": "Xiriir aan jirin", "b": "Xiriir weyn oo saameeya dhaqaalaha iyo difaaca", "c": "Xiriir daciif ah", "d": "Xiriir ku kooban buuraha" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 68,
    "question": "Sidee bay dhirtu u yareysaa heerkulka koonfurta Soomaaliya?",
    "options": { "a": "Waxay keentaa dabaylo kulul", "b": "Waxay qaboojisaa hawada (saamiga dhirta oo sarreeya)", "c": "Waxay celisaa roobka", "d": "Saameyn ma leh" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 69,
    "question": "Waa maxay ahmiyadda ay 'Cufnaanta dhirta' u leedahay cimilada?",
    "options": { "a": "Waxay dhintaa roobka", "b": "Waxay saameyn ku leedahay hoos u dhaca heerkulka", "c": "Waxay kordhisaa huurka xeebta kaliya", "d": "Waxay dabooshaa badda" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 70,
    "question": "Maxaa looga baahan yahay waaxda xoolaha si loo horumariyo?",
    "options": { "a": "In la joojiyo dhoofinta", "b": "In la sameeyo xarumo lagu keydiyo warbixinnada", "c": "In la yareeyo calafka", "d": "In dadka miyiga laga soo saaro" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 71,
    "question": "Waa maxay farqiga u dhexeeya 'Bannaannada Fatahyada' iyo 'Bannaan Xeebeedyada'?",
    "options": { "a": "Fatahyada ayaa ka hodansan xeebeedyada", "b": "Xeebeedyada ayaa ka hodansan", "c": "Iska mid bay yihiin", "d": "Ma jiraan bannaanno fatahyo ah" },
    "correctAnswer": "a", "difficultyLevel": "hard"
  },
  {
    "id": 72,
    "question": "Maxaa keena loolka siyaasadeed ee mandiqadda Geeska Afrika?",
    "options": { "a": "Barafka", "b": "Kaalinta siyaasadeed ee u dhaxaysa Soomaaliya iyo Itoobiya", "c": "Kalluunka", "d": "Warshadaha" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 73,
    "question": "Falanqee 'Hannaanka waxsoosaarka oo ah mid loogu talagalay nolosha'?",
    "options": { "a": "Waa beerasho loogu talagalay ganacsi caalami ah", "b": "Waa beerasho quutul-daruuriga ah (Home consumption)", "c": "Waa warshadayn casri ah", "d": "Waa xoolo dhaqasho kaliya" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 74,
    "question": "Waa maxay dhibaatada 'Milixda Carrada' ee beeraha?",
    "options": { "a": "Waxay kordhisaa waxsoosaarka", "b": "Waxay daciifisaa tayada dhulka iyo dalagga", "c": "Waxay keentaa roob", "d": "Saameyn ma leh" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 75,
    "question": "Sidee bay 'Filiqsanaanta biyaha iyo berriga' u saameeyaan cimilada?",
    "options": { "a": "Ma saameeyaan", "b": "Waxay go'aamiyaan huurka iyo heerkulka aagga", "c": "Waxay keenaan dhulgariir", "d": "Waxay yareeyaan xoolaha" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 76,
    "question": "Maxaa lagu gartaa 'Aftahannimada' dadka Soomaaliyeed?",
    "options": { "a": "Aamusnaan", "b": "Cabirka dareenka iyo suugaanta", "c": "Dagaal kaliya", "d": "Aqoon la'aan" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 77,
    "question": "Falanqee doorka 'Calaf isku dheelitirnaanta' ee xoolaha?",
    "options": { "a": "Waa in xoolaha la siiyo biyo kaliya", "b": "Waa nafaqeynta xoolaha si loo helo waxsoosaar tayo leh", "c": "Waa dhibaatada ugu weyn ee xoolaha", "d": "Muhiim ma ahan" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 78,
    "question": "Maxaa loola jeedaa 'Muuqaallada dhulka oogada sare'?",
    "options": { "a": "Badda iyo Hawada", "b": "Bannaannada, dulaha iyo buuraleyda", "c": "Magaalooyinka iyo tuulooyinka", "d": "Dadka iyo xoolaha" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 79,
    "question": "Waa maxay ahmiyadda xarun keyd warbixineed u leedahay xoolaha?",
    "options": { "a": "Si loo yareeyo canshuurta", "b": "Si loo ogaado tirada iyo tayada si loo qorsheeyo horumar", "c": "Si loogu dalxiiso", "d": "Ma leh wax ahmiyad ah" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  },
  {
    "id": 80,
    "question": "Maxaa ugu dambeeya ee lagu soo koobi karo juqraafiga Soomaaliya?",
    "options": { "a": "Waa dhul faqiir ah", "b": "Waa dhul istiraatiiji ah oo leh kheyraad badan balse u baahan horumarin", "c": "Waa dhul buuro kaliya ah", "d": "Waa dhul aan la degganaan karin" },
    "correctAnswer": "b", "difficultyLevel": "hard"
  }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch4_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch4',
        'question': q['question'],
        'options': {k.lower(): str(v) for k, v in q['options'].items()},
        'correctAnswer': q['correctAnswer'].lower(),
        'difficultyLevel': q['difficultyLevel']
    }
    formatted_questions.append(formatted_q)

# 1. Update seed_data.dart
with open(DART_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r"fullSeedJson = r'''(.*?)'''", content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    # Remove existing geo_ch4 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch4']
    
    # Check if geo_ch4 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch4' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 4aad: Juqraafiga Soomaaliya",
            "id": "geo_ch4"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch4':
                c['title'] = "Cutubka 4aad: Juqraafiga Soomaaliya"
                break
    
    # Add new geo_ch4 questions
    data['questions'].extend(formatted_questions)
            
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {len(formatted_questions)} questions in seed_data.dart")
else:
    print("Could not find fullSeedJson in seed_data.dart")

# 2. Update seed_data.json if exists
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data_json = json.load(f)

    # Remove existing geo_ch4 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch4']
    for k in keys_to_remove:
        del data_json['questions'][k]

    # Add new ones
    added_count_json = 0
    if 'questions' not in data_json:
        data_json['questions'] = {}
        
    for q in formatted_questions:
        q_id = q['id']
        q_copy = q.copy()
        del q_copy['id']
        data_json['questions'][q_id] = q_copy
        added_count_json += 1

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, indent=2, ensure_ascii=False)
    print(f"Updated {added_count_json} questions in seed_data.json")
else:
    print(f"{JSON_FILE} not found. Skipping.")
