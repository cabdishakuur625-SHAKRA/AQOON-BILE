import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha filiqsanaanta dadka?", "options": { "a": "Dadka oo u qaybsan si siman", "b": "Dadka oo u filiqsan si aan isla ekeyn", "c": "Dadka oo hal meel ku wada nool", "d": "Dadka oo aan la tirin karin" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa ku bama mid ka mid ah ilaha daraaseynta dadka?", "options": { "a": "Tirokoobka dadka", "b": "Khariidada xiddigaha", "c": "Tirinta dhirta", "d": "Daraasadda badda" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 3, "question": "Maxaa loola jeedaa 'Vital Statistics'?", "options": { "a": "Tirada baabuurta", "b": "Diiwaangelinta dhalashada iyo dhimashada", "c": "Xisaabinta dakhliga", "d": "Cimilada dalka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa ku bama qodob dabiici ah oo saameeya tirada dadka?", "options": { "a": "Gaadiidka", "b": "Cimilada", "c": "Colaadaha", "d": "Xirfadda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Waa maxay 'Hijrada Dibadda'?", "options": { "a": "U guuridda magaalada kale", "b": "U socdaalidda dal kale", "c": "U guuridda miyiga", "d": "Dalxiiska gudaha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Maxaa keena taran fataha (Population Explosion)?", "options": { "a": "Dadka oo yaraada", "b": "Kororka dadka oo ka bata dhaqaalaha", "c": "Dhimashada oo badata", "d": "Dadka oo miyiga u guura" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Halkee ayay dadka Soomaaliyeed ugu badan yihiin?", "options": { "a": "Miyiga fog", "b": "Muqdisho iyo hareeraha webiyada", "c": "Buuraha Goolis", "d": "Lama-degaanka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay 'Cufnaanta dadka'?", "options": { "a": "Saamiga dadka iyo dhulka", "b": "Dhererka dadka", "c": "Miisaanka dadka", "d": "Tirada carruurta kaliya" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 9, "question": "Waa ku bama dalka cufnaantiisu aadka u sarreyso?", "options": { "a": "Soomaaliya", "b": "Bangaaladhesh", "c": "Australia", "d": "Canada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Maxaa saameyn weyn ku leh halka dadku degaan?", "options": { "a": "Midabka dhulka", "b": "Kheyraadka biyaha", "c": "Tirada xiddigaha", "d": "Dhererka geedaha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Tirada dadka Soomaaliya ee 2014 waxay ahayd?", "options": { "a": "5M", "b": "10.5M", "c": "15M", "d": "20M" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa maxay socdaalka dalka gudihiisa ah?", "options": { "a": "Hijrada dibadda", "b": "Hijrada gudaha", "c": "Dalxiis", "d": "Tahriib" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Cilmiga ururinta iyo nidaaminta xogta dadka waa?", "options": { "a": "Juqraafi", "b": "Tirokoob", "c": "Taariikh", "d": "Af-Soomaali" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa ku bama dalka cufnaantiisu aadka u hooseyso?", "options": { "a": "Masar", "b": "Ustaaliya", "c": "Portugal", "d": "Bangaaladhesh" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Maxaa keena in dadku ka cararaan meel?", "options": { "a": "Nabadda", "b": "Colaadaha", "c": "Dhaqaalaha badan", "d": "Cunnada badan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Waa maxay cutubka ka hadla dadka?", "options": { "a": "Juqraafiga dhulka", "b": "Juqraafiga dadka", "c": "Cimilada", "d": "Macdanta" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Halkee bay dadka beeraleyda ah ku badan yihiin?", "options": { "a": "Buuraha", "b": "Webiyada hareerahooda", "c": "Xeebaha", "d": "Miyiga engegan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Maxaa loola jeedaa 'mehradda'?", "options": { "a": "Cimilada", "b": "Xirfadda ama shaqada", "c": "Socdaalka", "d": "Dhalashada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Tirokoobka ma laga helaa maktabadda?", "options": { "a": "Maya", "b": "Haa", "c": "Marna", "d": "Lama oga" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Cufnaanta Soomaaliya ma sareysaa?", "options": { "a": "Haa", "b": "Maya (waa hooseysaa)", "c": "Waa midda ugu sareysa adduunka", "d": "Lama tirin karo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Sidee loo xisaabiyaa cufnaanta dadka?", "options": { "a": "Dadka + Dhulka", "b": "Tirada dadka ÷ Baaxadda dhulka", "c": "Dhulka - Dadka", "d": "Dadka x Dhulka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 22, "question": "Maxay ku kala duwan yihiin gobollada cufnaantoodu dhex-dhexaadka tahay iyo kuwa sareeya?", "options": { "a": "25-50 qof (Dhex-dhexaad), 50-100 qof (Sare)", "b": "10 qof iyo 100 qof", "c": "Miyiga iyo Magaalada", "d": "Badda iyo Beriga" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 23, "question": "Waa maxay ujeeddada Tirokoobka Falanqaynta?", "options": { "a": "Sawiridda dadka", "b": "Xog ka helidda bulsho iyadoo la isticmaalayo muunad (sample)", "c": "Tirinta carruurta kaliya", "d": "Ururinta buugaagta" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 24, "question": "Maxay cimilada u saameysaa socdaalka dibadda?", "options": { "a": "Cimilada xun waxay keentaa in dadku dalka ka baxaan", "b": "Cimilada xun waxay keentaa dalxiis", "c": "Cimilada xun waxay kordhisaa beeraha", "d": "Saameyn ma leh" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 25, "question": "Maxaa ka mid ah qodobbada aadanaha ee saameeya baahsanaanta?", "options": { "a": "Buuraha", "b": "Colaadaha iyo Gaadiidka", "c": "Webiyada", "d": "Macdanta" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Waa maxay farqiga u dhexeeya baahsanaanta dadka iyo cufnaanta?", "options": { "a": "Isla mid baa loola jeedaa", "b": "Baahsanaantu waa filiqsanaanta, cufnaantuna waa saamiga dhulka", "c": "Cufnaantu waa socdaalka", "d": "Baahsanaantu waa dhalashada" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Maxay dadka miyiga ugu soo hijroodaan magaalooyinka Soomaaliya?", "options": { "a": "Raadinta xoolo ka fiican kuwa miyiga", "b": "Raadinta adeegyo sida waxbarasho iyo caafimaad", "c": "Raadinta dhul beereed", "d": "Cimilada magaalada oo roob badan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Waa maxay tusaalaha cufnaanta dhex-dhexaadka ah (25-50 qof)?", "options": { "a": "Portugal", "b": "Masar", "c": "Australia", "d": "Bangaaladhesh" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Waa maxay tusaalaha cufnaanta sare (50-100 qof)?", "options": { "a": "Masar", "b": "Portugal", "c": "Soomaaliya", "d": "Australia" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Sidee bay ilaha biyaha u soo jiitaan dadka?", "options": { "a": "Waxay dhalisaa xirfado sida kalluumeysiga iyo beeraha", "b": "Biyuhu waxay keenaan dhimashada", "c": "Biyuhu waxay yareeyaan gaadiidka", "d": "Ma jiraan wax ay soo jiitaan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Waa maxay Tirokoobka Tilmaamidda?", "options": { "a": "Midka ka hadla mustaqbalka", "b": "Kan ku tiirsan muuqaal xilli iyo goob gaar ah", "c": "Kan lagu tiriyo xoolaha kaliya", "d": "Daraasadda badda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Waa maxay saameynta 'Kheyraadka Macdanta' ee dadka?", "options": { "a": "Waxay dadka ka fogaysaa goobta", "b": "Waxay soo jiidataa dadka iyo shaqaalaha", "c": "Waxay yareysaa cufnaanta", "d": "Waxay keentaa dhalashada" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Maxaa loola jeedaa 'Vital statistics'?", "options": { "a": "Xogta xoolaha", "b": "Diiwaangelinta dhalashada, dhimashada iyo guurka", "c": "Heerka roobka", "d": "Tirada baabuurta" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay Soomaaliya ugu jirtaa gobolka cufnaantiisu hooseyso?", "options": { "a": "Dhulka oo yar darteed", "b": "Saamiga dadka oo yar marka loo eego baaxadda dhulka", "c": "Dadka oo dhan oo magaalo jooga", "d": "Webiyada oo aan jirin" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Waa maxay ujeeddada laga leeyahay jaangoynta hababka tirokoobka?", "options": { "a": "Si loo lumiyo xogta", "b": "Si loo soo saaro natiijooyin sax ah iyo go'aanno habboon", "c": "Si loo badiyo dadka", "d": "Ma lahan wax ujeeddo ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxay ku xiran tahay aqlabiyadda aadanaha ee deegaanka?", "options": { "a": "Cufnaanta dadka", "b": "Dhererka buuraha", "c": "Tirada maraakiibta", "d": "Midabka biyaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Maxaa lagu gartaa 'Taran fataha'?", "options": { "a": "Dhalashada oo yar", "b": "Kororka dadka oo ka sare mara ilaha dhaqaalaha", "c": "Xirfadda oo badata", "d": "Miyiga oo dadku ku nagaadaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Halkee laga helaa xogaha dheeriga ah ee juqraafiga?", "options": { "a": "Webiyada", "b": "Maktabadaha iyo daraasaadka", "c": "Miyiga fog", "d": "Suuqa kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Waa ku bama qodob saameeya baahsanaanta dadka oo ku saabsan kala sarreynta dhulka?", "options": { "a": "Cimilada", "b": "Relief", "c": "Gaadiidka", "d": "Colaadaha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxay tahay muhiimadda ay 'socdaalladu' u leeyihiin daraasadda dadka?", "options": { "a": "In la ogaado dhaqdhaqaaqa iyo filiqsanaanta dadka", "b": "In la ogaado tirada baabuurta", "c": "In la ogaado meesha xooluhu joogaan", "d": "Muhiim ma ahan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Falanqee xiriirka ka dhexeeya qodobbada dabiiciga ah iyo kuwa aadanaha ee saameeya tirada dadka?", "options": { "a": "Ma lahan wax xiriir ah", "b": "Waa xiriir adag; dabiiciga ayaa inta badan saameeya go'aannada aadanaha (sida hijrada)", "c": "Aadanaha ayaa abuura dabiiciga", "d": "Xiriirkoodu waa mid ku kooban ganacsiga kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 42, "question": "Maxaa loola jeedaa 'Heer falgalka dhulka iyo dadka'?", "options": { "a": "Dagaal dhex mara dadka iyo dhulka", "b": "Sida dadku u adeegsadaan kheyraadka dhulka iyo saamaynta ay ku leeyihiin", "c": "Sawiridda khariidada", "d": "Tirinta dadka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 43, "question": "Sidee bay colaaduhu u beddelaan cufnaanta dadka ee gobol gaar ah?", "options": { "a": "Waxay kordhiyaan dhalashada", "b": "Waxay keenaan barakac iyo in dadku ka cararaan goobta, taas oo yareyneysa cufnaanta", "c": "Waxay keenaan kheyraad macdan", "d": "Ma saameeyaan cufnaanta" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 44, "question": "Maxay tahay sababta cilmiyeed ee Soomaaliya loogu tixgeliyo dal cufnaantiisu hooseyso (10-25 qof)?", "options": { "a": "Sababtoo ah waa dal yar", "b": "Sababtoo ah bedka dhulka ayaa weyn marka loo eego tirada dadka ee 10.5M ah", "c": "Sababtoo ah dadka ma degganaan karaan dhulka", "d": "Sababtoo ah biyaha ayaa ku yar" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 45, "question": "Falanqee aragtida Qur'aanka ee ku saabsan koobidda nimcooyinka Eebbe marka la eego tirokoobka?", "options": { "a": "Waa la tiri karaa waana la koobi karaa", "b": "Waa la tiri karaa balse suurta gal ma ahan in la ogaado inta ay sii jireyso (koobid la'aan)", "c": "Lama tiri karo haba yaraatee", "d": "Tirokoobku waa mid khuseeya aadanaha kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 46, "question": "Maxay ku kala duwan yihiin 'Tirokoobka Tilmaamidda' iyo 'Tirokoobka Falanqaynta' marka la eego habka shaqada?", "options": { "a": "Tilmaamiddu waa ururin xog, Falanqayntu waa muunad ka qaadid", "b": "Tilmaamiddu waa mid qaldan", "c": "Falanqayntu waa mid ku kooban buugaagta", "d": "Isma laha haba yaraatee" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 47, "question": "Maxaa keeni kara 'Population Explosion' (Taran fataha) gobol dabiici ahaan qani ah?", "options": { "a": "Dhimashada oo badata", "b": "Dhalashada oo aad u kororta iyo ilaha dhaqaalaha oo laga saro maro", "c": "Dadka oo dalka ka baxa", "d": "Gaadiidka oo badana" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 48, "question": "Sidee bay 'xirfadaha' dadka (mehradda) u saameeyaan cufnaanta magaalooyinka?", "options": { "a": "Magaalooyinka waxay soo jiitaan dadka leh xirfadaha warshadaha iyo adeegyada", "b": "Xirfadda waxay yareysaa dadka magaalada", "c": "Magaalooyinka waa meel xoolaha lagu dhaqdo kaliya", "d": "Xirfadda ma saameyso filiqsanaanta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 49, "question": "Maxay tahay caqabadda haysata tirokoobka rasmiga ah ee Soomaaliya?", "options": { "a": "Dhaqaalo la'aan kaliya", "b": "Nidaam la'aan iyo xaaladaha socdaalada oo aan la diiwaangalin", "c": "Dadka oo aan oggolayn", "d": "Dhulka oo aad u yar" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 50, "question": "Caddee farqiga u dhexeeya 'Vital statistics' iyo 'Population Census'?", "options": { "a": "Vital waa dhalasho/dhimasho, Census waa tirinta guud ee dadka", "b": "Census waa dhalashada kaliya", "c": "Vital waa tirinta xoolaha", "d": "Isla mid baa loola jeedaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Falanqee doorka 'Gaadiidka' ee baahsanaanta dadka?", "options": { "a": "Meelaha gaadiidka u dhow dadka ayaa ku yar", "b": "Gaadiidku wuxuu sahlayaa socdaalka iyo in dadku degaan meelaha leh isgaarsiinta habboon", "c": "Gaadiidka wuxuu dilaa dadka kaliya", "d": "Gaadiidka ma saameeyo dadka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 52, "question": "Sidee bay 'Kala sarreynta dhulka' (Relief) u saameysaa cufnaanta dadka?", "options": { "a": "Buuraha dhaadheer dadku way ku badan yihiin", "b": "Bannaannada iyo dhulka siman dadka ayaa ku badan marka loo eego buuraha", "c": "Relief saameyn ma leh", "d": "Dadku waxay degaan badda dhexdeeda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Maxaa loola jeedaa 'Bulshada tirokoobka' marka laga hadlayo astaamaha guud?", "options": { "a": "Koox dad ah oo aan is lahayn", "b": "Koox leh astaamo ka dhexeeya oo daraasadda tirakoobku ku wareegeyso", "c": "Dadka dhintay kaliya", "d": "Maraakiibta badda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Muxuu yahay xiriirka ka dhexeeya heerkulka (cimilo) iyo dhalashada/dhimashada?", "options": { "a": "Ma jiro xiriir", "b": "Cimilada xun waxay kordhin kartaa dhimashada ama socdaalka", "c": "Cimilada kulul waxay kordhisaa dhalashada", "d": "Cimiladu waa mid dadka wada disha" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxay dadku ugu badan yihiin hareeraha webiyada Shabelle iyo Jubba?", "options": { "a": "Sababtoo ah waa meelo qabow", "b": "Sababtoo ah kheyraadka biyaha iyo beeraha ayaa ka jira", "c": "Sababtoo ah waa meelo ay gaadiidku ku badan yihiin", "d": "Ma jirto sabab gaar ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Falanqee 'Socdaalka miyiga ilaa magaalada' saameynta uu ku leeyahay waxsoosaarka miyiga?", "options": { "a": "Wuu kordhiyaa waxsoosaarka", "b": "Wuu daciifiyaa waxsoosaarka miyiga maadaama shaqaalihii ka baxayaan", "c": "Waxba ma beddelo", "d": "Wuxuu miyiga ka dhigaa magaalo" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 57, "question": "Caddee sababta cilmiga tirokoobka loogu yeero 'hannaan aqoon ku dhisan'?", "options": { "a": "Sababtoo ah waa ururin kaliya", "b": "Sababtoo ah wuxuu leeyahay habab nidaamsan oo ururin, falanqayn iyo go'aan qaadasho ah", "c": "Sababtoo ah buugaagta ayaa lagu qoraa", "d": "Ma jiro sabab cad" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Waa maxay tusaalaha ugu wanaagsan ee cufnaanta aadka u hooseysa ee dunida?", "options": { "a": "Masar", "b": "Australia (10 qof/km² ka yar)", "c": "China", "d": "India" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Sidee buu tirokoobku u caawiyaa dowladda dhanka dhaqaalaha?", "options": { "a": "Wuxuu u sheegaa tirada baabuurta dalka", "b": "Wuxuu ka caawiyaa qorsheynta adeegyada bulshada iyo barashada korarka dadka", "c": "Wuxuu dowladda ka dhigaa mid qani ah", "d": "Saameyn ma lahan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Maxaa keeni kara in goob cimiladeedu fiican tahay dadku ku yaraadaan?", "options": { "a": "Colaadaha iyo dhibaatooyinka siyaasadeed", "b": "Biyaha oo badan darteed", "c": "Magaalooyinka oo fog", "d": "Xirfadda oo yar" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Waa maxay ujeeddada dhabta ah ee diiwaangelinta socdaalada?", "options": { "a": "In la ogaado dadka dalxiiska taya", "b": "In lala socdo baahsanaanta iyo isbeddelka tirada dadka ee goob gaar ah", "c": "In la ogaado tirada diyaaradaha", "d": "Ma jiro ujeeddo" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 62, "question": "Falanqee micnaha 'saamiga dadka marka loo eego baaxadda dhulka'?", "options": { "a": "Waa tirada guud ee dadka", "b": "Waa cufnaanta tirada dadka", "c": "Waa baaxadda dhul daaqsimeedka", "d": "Waa tirada carruurta kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 63, "question": "Muxuu yahay farqiga u dhexeeya 'baahsanaanta' iyo 'cufnaanta' xagga xisaabinta?", "options": { "a": "Midna lama xisaabiyo", "b": "Baahsanaantu waa filiqsanaanta muuqaal ahaan, cufnaantuna waa qaab xisaabeed (division)", "c": "Isla mid baa la xisaabiyaa", "d": "Cufnaantu waa isku darista labada tiro" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxay tahay sababta dalka Soomaaliya uu ugu xun yahay 'tirokoobyada muhiimka ah'?", "options": { "a": "Dadka oo aad u badan darteed", "b": "Daryeel la'aan iyo xarumo diiwaangalin oo aan jirin", "c": "Ma rabaan inay carruur dhalato", "d": "Dalku waa lama-degaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sidee bay 'macdanaha' u saameeyaan deegaannada cidla ahaa?", "options": { "a": "Waxay ka dhigaan meel cufnaanteedu sareyso sababtoo ah shaqaalaha soo degaya", "b": "Waxay ka dhigaan meel dadka laga saaro", "c": "Ma badalaan cufnaanta", "d": "Waxay keenaan baraf" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxaa dhacaya haddii dadku u guuraan dal cimiladiisu aad u qabow tahay?", "options": { "a": "Cufnaanta dalkaas ayaa kordheysa", "b": "Dhalashada ayaa yaraaneysa kaliya", "c": "Saameyn ma lahan", "d": "Dalkaas ayaa burburaya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Falanqee xiriirka ka dhexeeya 'heerka dhimashada' iyo cufnaanta?", "options": { "a": "Dhimashadu waxay yareysaa cufnaanta dadka ee goob gaar ah", "b": "Dhimashadu waxay kordhisaa cufnaanta", "c": "Ma lahan wax xiriir ah", "d": "Xiriirku waa mid dhaqaale kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Muxuu yahay ujeeddada laga leeyahay soo ururinta xogaha juqraafiga?", "options": { "a": "Si loo ogaado taariikhda", "b": "Si loo nidaamiyo lana soo bandhigo natiijooyin cilmiyeed oo bulshada khuseeya", "c": "Si loo barto luuqado cusub", "d": "Si loo tiriyo dhirta" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 69, "question": "Sidee bay 'dhibaatooyinka siyaasadeed' u saameeyaan dhalashada dadka?", "options": { "a": "Waxay dhiirigeliyaan dhalashada", "b": "Waxay yareeyaan xasiloonida, taas oo keeni karta koror dhimasho iyo hoos u dhac dadka goobta jooga", "c": "Waxba ma beddelaan", "d": "Siyaasaddu ma saameyso dadka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 70, "question": "Maxaa ugu dambeeya ee lagu soo koobi karaa daraasadda dadka ee cutubkan?", "options": { "a": "Tirinta dadka waa wax fudud", "b": "Filiqsanaanta iyo cufnaanta dadka waxay ku xiran yihiin qodobbada dabiiciga iyo kuwa aadanaha", "c": "Dadka adduunka oo dhan waa isku mid", "d": "Juqraafigu ma khuseeyo dadka" }, "correctAnswer": "b", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch5_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch5',
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
    
    # Remove existing geo_ch5 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch5']
    
    # Check if geo_ch5 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch5' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 5aad: Juqraafiga Dadka",
            "id": "geo_ch5"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch5':
                c['title'] = "Cutubka 5aad: Juqraafiga Dadka"
                break
    
    # Add new geo_ch5 questions
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

    # Remove existing geo_ch5 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch5']
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
