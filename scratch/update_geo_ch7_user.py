import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha Sanaaca?", "options": { "a": "In alaabta la iska iibiyo", "b": "In maadooyinka caydhiinka laga beddelo qaabkoodii dabiiciga ahaa", "c": "In dhulka la fasho", "d": "In xoolaha la dhaqdo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa ku bama mid ka mid ah kaabayaasha warshadaha?", "options": { "a": "Cimilada", "b": "Alaabta ceeriin", "c": "Dhulka daaqsiinta", "d": "Webiyada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Waa maxay Tamar?", "options": { "a": "Waa awoodda lagu qabto shaqo", "b": "Waa gawaarida dheereeya", "c": "Waa alaabta la dhoofiyo", "d": "Waa dakhliga dalka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa ku bama tusaale ka mid ah tamarta aan la cusboonaysiin Karin?", "options": { "a": "Cadceedda", "b": "Saliidda (Bitroolka)", "c": "Dabaysha", "d": "Biyaha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Waa ku bama tusaale ka mid ah tamarta dib loo cusboonaysiin karo?", "options": { "a": "Dhuxul dhagaxa", "b": "Tamarta Cadceedda", "c": "Gaaska dabiiciga", "d": "Yuraaniyamka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Maxaa loola jeedaa Gaadiid?", "options": { "a": "In meel la iska fariisto", "b": "Daabulidda dadka iyo badeecada", "c": "In wax la beero", "d": "In xafiis la tago" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Noocyada gaadiidka imisa baa loo kala saaraa?", "options": { "a": "2 nooc", "b": "3 nooc", "c": "5 nooc", "d": "10 nooc" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay ujeeddada Dalxiiska?", "options": { "a": "Madadaalo, sahmin iyo caafimaad", "b": "In dalka laga guuro", "c": "In shaqo laga fariisto", "d": "In la barto qoraalka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 9, "question": "Waa ku bama dalka ugu horreeya xagga dalxiiska dunida?", "options": { "a": "Meksiko", "b": "Faransiiska", "c": "Turkiga", "d": "Tayland" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa maxay Geddis?", "options": { "a": "In wax la dhisoo", "b": "Badeeco laga soo daabulo goobaha waxsoosaarka lana geeyo suuqa", "c": "In gaadiidka la kordhiyo", "d": "In tamarta la kaydiyo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Midkee baa ka mid ah tilmaamaha gaadiidka dhulka?", "options": { "a": "Xawaaraha (degdeg)", "b": "Xamuulka oo aad u culus", "c": "Kharash aad u badan", "d": "Wuxuu maraa biyaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa maxay Ra’sal maal?", "options": { "a": "Shaqaalaha", "b": "Lacagta ama hantida lagu bilaabo warshadda", "c": "Alaabta ceeriin", "d": "Gaadiidka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Magaalooyinka ugu horreeya warshadaha dunida midkee baa ku jira?", "options": { "a": "Koonfurta Afrika", "b": "Galbeedka Yurub", "c": "Bartamaha Aasiya", "d": "Bariga Australia" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa ku bama tamarta laga helo qashinka beeraha iyo haraaga xoolaha?", "options": { "a": "Tamarta Nukliyeerka", "b": "Tamarta Bayoomaaska", "c": "Tamarta Biyaha", "d": "Dhuxul dhagaxa" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Waa ku bama dalxiiska la xiriira nasashada?", "options": { "a": "Dalxiis caafimaad", "b": "Dalxiis madadaalo", "c": "Dalxiis dhaqameed", "d": "Dalxiis isir" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Fogaanta u dhexeyso biraha tareenka ee xariiqda ciriiriga ah waa?", "options": { "a": "100cm", "b": "106cm", "c": "143.5cm", "d": "160cm" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Waa maxay ahmiyadda dhoofinta waxsoosaarka dheeriga ah?", "options": { "a": "In dadka la siiyo si bilaash ah", "b": "In dhaqaale laga sameeyo", "c": "In la gubo", "d": "In la kaydiyo waligeed" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Gaadiidka cirka waxaa lagu gartaa?", "options": { "a": "Loodsanaan iyo xawaare sare", "b": "Inuu gaabis yahay", "c": "Inuu jaban yahay", "d": "Inuu dhulka ku socdo" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 19, "question": "Sidee bay sanaacadu u kordhisaa qiimaha alaabta cayriinka ah?", "options": { "a": "Ayadoo laga dhigayo mid dabiici ah", "b": "Ayadoo loo beddelayo qaab kale oo faa'ido u leh aadanaha", "c": "Ayadoo miyiga lagu celinayo", "d": "Ayadoo la yareynayo shaqaalaha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 20, "question": "Kala sooc noocyada warshadaha, midkee baa ka mid ah?", "options": { "a": "Warshadaha casriga ah iyo kuwa qadiimiga ah", "b": "Warshadaha beeraha kaliya", "c": "Warshadaha badda", "d": "Warshadaha hawada" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 21, "question": "Muxuu gaadiidka biyuhu ugu muhiim yahay ganacsiga caalamiga ah?", "options": { "a": "Sababtoo ah wuxuu qaadaa xammuul aad u badan kharashkiisuna waa yar yahay", "b": "Sababtoo ah waa kan ugu dhaqsaha badan", "c": "Sababtoo ah wuxuu tagaa meel kasta oo dhul ah", "d": "Ma lahan muhiimad weyn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 22, "question": "Waa maxay farqiga u dhexeeya tamarta cusboonaata iyo tan aan cusboonaan?", "options": { "a": "Tan cusboonaata waa mid dhamaata", "b": "Tan cusboonaata waa mid aan dhamaanin oo qof walba heli karo", "c": "Ma lahan wax farqi ah", "d": "Tan aan cusboonaan waa mid ka raqiisan tan kale" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 23, "question": "Maxay tahay ahmiyadda ay sayladuhu (suuqyada) u leeyihiin warshadaha?", "options": { "a": "In lagu kaydiyo alaabta ceeriin", "b": "In lagu iibiyo waxsoosaarka warshadda", "c": "In lagu tababaro shaqaalaha", "d": "In lagu kordhiyo tamarta" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 24, "question": "Waa ku bama dalalka ku jira 10-ka ugu horreeya dalxiiska dunida?", "options": { "a": "Shiinaha, Talyaaniga, iyo Ingiriiska", "b": "Soomaaliya, Itoobiya, iyo Kenya", "c": "Suudaan, Yemen, iyo Liibiya", "d": "Hindiya, Pakistan, iyo Afgaanistaan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 25, "question": "Sidee bay tiknoolojiyadu u saameysaa dhaqdhaqaaqa ganacsiga?", "options": { "a": "Waxay keentaa in ganacsigu istaago", "b": "Waxay dardar gelisaa isgaarsiinta iyo sarrifka lacagaha", "c": "Waxay daciifisaa bangiyada", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Waa maxay kaalinta bangiyada ee ganacsiga?", "options": { "a": "In ay fududeeyaan adeegyada maaliyadeed iyo sarrifka", "b": "In ay soo saaraan alaabta ceeriin", "c": "In ay daabulaan dadka", "d": "In ay dhisaan waddooyinka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 27, "question": "Kala saar xariiqda dhexdhexaadka ah iyo tan ballaaran ee tareenka?", "options": { "a": "Dhexdhexaadku waa 143.5cm, ballaaranna waa 160cm", "b": "Dhexdhexaadku waa 100cm, ballaaranna waa 200cm", "c": "Dhexdhexaadku waa 160cm, ballaaranna waa 143.5cm", "d": "Labaduba waa isku mid" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 28, "question": "Maxaa loola jeedaa 'Dalxiis Caafimaad'?", "options": { "a": "In loo safro meel loogu talagalay daaweyn ama soo kabasho", "b": "In loo safro meel taariikhi ah", "c": "In loo safro meel lagu ciyaaro", "d": "In la booqdo qoyska" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Muxuu dalxiisku u kordhiyaa dakhliga dalka?", "options": { "a": "Sababtoo ah dalxiisayaashu waxay dalka keenaan lacag qalaad", "b": "Sababtoo ah dalxiisayaashu waxay dalka ka qaataan alaab", "c": "Sababtoo ah waxay dilaan dhaqaalaha", "d": "Ma kordhiyo dakhliga" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Waa ku bama mid ka mid ah astaamaha gaadiidka cirka?", "options": { "a": "Xawaare sare iyo loodsanaan", "b": "Kharash yar", "c": "Inuu qaado xamuul ka culus maraakiibta", "d": "Inuu dhulka dhex maro" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Maxaa ka mid ah waxyaabaha saameeya dhaqdhaqaaqa ganacsiga?", "options": { "a": "Xiriirka siyaasadeed ee dalalka ka dhexeeya", "b": "Cimilada maalinlaha ah", "c": "Tirada xoolaha ee miyiga jooga", "d": "In dadku ay wada hadlaan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Waa maxay muhiimadda tamarta biyaha (hydro energy)?", "options": { "a": "Waxaa laga dhaliyaa koronto iyadoo la adeegsanayo dhaqdhaqaaqa biyaha", "b": "Waxaa loo isticmaalaa in lagu cabo kaliya", "c": "Waxay keentaa biyo yaraan", "d": "Ma lahan wax faa'ido ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sidee bay unugyada cadceedda (Solar cells) u shaqeeyaan?", "options": { "a": "Waxay nuugaan ileyska qorraxda waxayna u beddelaan koronto", "b": "Waxay soo saaraan biyo kulul oo kaliya", "c": "Waxay u baahan yihiin dabaysha", "d": "Waxay u baahan yihiin saliid" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Geddiska maxaa lagu gartaa?", "options": { "a": "Waa dhaqdhaqaaq badeecada lagu gaarsiinayo halka looga baahan yahay", "b": "Waa in wax la soo saaro kaliya", "c": "Waa in tamarta la qariyo", "d": "Waa in gaadiidka la yareeyo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Xiriirka u dhexeeya 'Kala duwanaanshaha waxsoosaarka' iyo 'Ganacsiga'?", "options": { "a": "Kala duwanaanshuhu waa aasaaska ganacsiga si wax loo isweydaarsado", "b": "Kala duwanaanshuhu wuxuu joojiyaa ganacsiga", "c": "Ma lahan wax xiriir ah", "d": "Isla mid baa loola jeedaa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxay shaqaaluhu muhiim u yihiin warshadda?", "options": { "a": "Si ay u fuliyaan hawlaha waxsoosaarka", "b": "Si ay alaabta u cunaan", "c": "Si ay u fariistaan kaliya", "d": "Shaqaale looma baahna" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Tilmaan mid ka mid ah goobaha warshadaha dunida?", "options": { "a": "Ruushka", "b": "Bartamaha Afrika", "c": "Koonfurta Ameerika", "d": "Geeska Afrika" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxaa loola jeedaa 'Dalxiis Dhaqameed'?", "options": { "a": "In la barto hidaha iyo dhaqanka dadka kale", "b": "In la daweeyo xanuunada", "c": "In la raadiyo isirka", "d": "In la soo booqdo beeraha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Maxaa loola jeedaa 'Warshadaha wax beddelo'?", "options": { "a": "In alaab la beddelo si ay u yeelato tayo ka wanaagsan", "b": "In alaabta la tuuro", "c": "In la soo saaro alaab ceeriin ah kaliya", "d": "In la xiro warshadda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 40, "question": "Waa ku bama tamarta loo yaqaanno tamarta nukliyeerka?", "options": { "a": "Yuraaniyam", "b": "Dhuxul dhagax", "c": "Gaaska dabiiciga", "d": "Qoryaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Sidee bay wacyigelinta muhiimadda dalxiiska u horumarisaa dalxiiska?", "options": { "a": "Waxay dadka ku dhiirigelisaa inay u safraan nasasho iyo madadaalo", "b": "Waxay dadka ka dhigtaa inay guriga joogaan", "c": "Waxay yareysaa dakhliga", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Maxay tahay ahmiyadda gaadiidka xagga xiriirka dhaqaalaha?", "options": { "a": "Wuxuu ballaariyaa isweydaarsiga ganacsiga ee dalalka", "b": "Wuxuu yareeyaa xiriirka", "c": "Wuxuu keenaa khasaare", "d": "Wuxuu ka dhigaa dalka mid go'doon ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Magaalada Detroit (Mareykanka) maxay tusaale u tahay?", "options": { "a": "Magaalo warshadeed (Detroit waa tusaale caan ah laakiin halkan Bariga Ameerika Waqooyi ayaa ku xusan)", "b": "Magaalo diimeed", "c": "Magaalo beeraha", "d": "Magaalo aan waxba laga soo saarin" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 44, "question": "Falanqee sida ay u kala duwan yihiin tamarta cadceedda iyo tamarta biyaha ee habka looga faa'ideysto?", "options": { "a": "Cadceedda waxaa loo isticmaala unugyo (cells), biyaha waxaa loo isticmaalaa dhaqdhaqaaqa hirarka", "b": "Ma lahan wax farqi ah", "c": "Cadceedda laguma dhaliyo koronto", "d": "Biyaha laguma dhaliyo koronto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 45, "question": "Sidee bay 'Sanaacadu' u kordhisaa faa'idada ay maadooyinka caydhiinka u leeyihiin aadanaha?", "options": { "a": "Ayadoo laga dhigayo alaab la isticmaali karo oo muddo dheer jirta", "b": "Ayadoo lagu tuurayo badda", "c": "Ayadoo laga dhigayo kuwo aan qiimo lahayn", "d": "Ayadoo miyiga looga tagayo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 46, "question": "Maxay tahay sababta Galbeedka Yurub iyo Bariga Ameerikada Waqooyi ay u yihiin goobaha warshadaha dunida ugu weyn?", "options": { "a": "Sababtoo ah waxay leeyihiin kaabayaasha warshadaha oo dhammaystiran iyo tiknoolojiyad sare", "b": "Sababtoo ah dadka jooga ayaa jecel warshadaha", "c": "Sababtoo ah dhulkay ku yaallaan", "d": "Sababtoo ah ma lahan beeraha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 47, "question": "Sidee bay tamarta bayoomaasku (biomass) u caawinaysaa deegaanka?", "options": { "a": "Waxay ka faa'ideysataa qashinka beeraha iyo haraaga xoolaha si tamar looga helo", "b": "Waxay wasakhaysaa deegaanka", "c": "Waxay joojisaa korontada", "d": "Ma lahan wax faa'ido deegaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 48, "question": "Falanqee doorka 'Ra'sal maalka' (Capital) ee horumarka warshadaha?", "options": { "a": "Waa laf dhabarta lagu iibsado qalabka, lagu bixiyo mushaharka laguna ballaariyo waxsoosaarka", "b": "Waa mid aan muhiim ahayn", "c": "Waa shaqaalaha oo kaliya", "d": "Waa alaabta dalka ka baxda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 49, "question": "Maxay tahay sababta gaadiidka cirka loogu tixgeliyo inuu yahay kan ugu 'loodsanaan' badan?", "options": { "a": "Sababtoo ah wuxuu leeyahay dhaqdhaqaaq iyo jihooyin badan oo furan", "b": "Sababtoo ah wuxuu ku socdaa dhulka", "c": "Sababtoo ah kharashkiisa ayaa yar", "d": "Sababtoo ah maraakiibta ayaa ka dhaqsi badan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 50, "question": "Sidee buu dalxiisku u saameeyaa 'Iskudheelitirnaanta dhaqaalaha dunida'?", "options": { "a": "Wuxuu dib u qaybiyaa hantida adduunka isagoo lacagta ka wareejinaya dalalka qaniga ah una wareejinaya dalalka dalxiiska leh", "b": "Wuxuu hantida u ururiyaa hal meel", "c": "Wuxuu yareeyaa ganacsiga caalamiga ah", "d": "Ma saameeyo dhaqaalaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Maxaa keena in tamarta aan cusboonaan ay 'dhamaato'?", "options": { "a": "Sababtoo ah waa kuwo dabiici ah oo xaddidan oo aan dib loo abuuri karin waqti dhow", "b": "Sababtoo ah dadka ayaa si xun u isticmaala", "c": "Sababtoo ah roobka ayaan di'in", "d": "Sababtoo ah qorraxda ayaa baabi'isa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Sidee bay 'Ururada Dhaqaale' u saameeyaan dhaqdhaqaaqa ganacsiga?", "options": { "a": "Waxay sameeyaan heshiisyo ganacsi oo fududeeya dhoofinta iyo soo dejinta", "b": "Waxay joojiyaan ganacsiga dalalka", "c": "Waxay kordhiyaan canshuurta", "d": "Ma lahan door muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Falanqee xiriirka u dhexeeya 'Gaadiidka' iyo 'Geddiska'?", "options": { "a": "Gaadiidku waa aaladda lagu fuliyo geddiska si badeecada loo geeyo suuqa", "b": "Geddiska ayaa ka horreeya gaadiidka", "c": "Labaduba wax xiriir ah ma lahan", "d": "Waa hal shay oo magacyo kala duwan leh" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Muxuu 'Dalxiis deegaaneedka' u yahay maalgashi suubban?", "options": { "a": "Sababtoo ah wuxuu dhowraa deegaanka isagoo laga faa'ideysanayo quruxdiisa", "b": "Sababtoo ah wuxuu baabi'iyaa dhirta", "c": "Sababtoo ah waa mid qaali ah", "d": "Sababtoo ah looma baahna maalgashi" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxay tahay sababta loo kala saaro cabirka dhabbaha tareenka (Rails)?", "options": { "a": "Si loogu waafajiyo baaxadda tareenka iyo culeyska uu qaadayo", "b": "Si dadku ay u lugeeyaan", "c": "Si looga fogaado shilalka gawaarida", "d": "Ma lahan sabab gaar ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Sidee buu 'Wasakhowga magaalada' u saameeyaa ilaha tamarta?", "options": { "a": "Wasakhowgu wuxuu ku qasbaa aadanaha inay raadiyaan tamar nadiif ah oo cusboonaata", "b": "Wasakhowgu wuxuu kordhiyaa saliidda", "c": "Wasakhowgu wuxuu nadiifiyaa hawada", "d": "Ma saameeyo tamarta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Falanqee 'Dalxiis qar-iskaturnimo' (Adventure tourism)?", "options": { "a": "Waa dalxiis khatar iyo sahmin ku dheehan tahay oo lagu tagayo meelo adag", "b": "Waa dalxiis lagu nasto huteelada", "c": "Waa dalxiis caafimaad", "d": "Waa dalxiis guriga dhexdiisa ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Maxay 'Warshadaha waxsoosaarka' u yihiin kuwa ugu muhiimsan dhaqaalaha dalka?", "options": { "a": "Sababtoo ah waxay abuuraan badeecooyin cusub iyo shaqooyin fara badan", "b": "Sababtoo ah waxay cunaan lacag badan", "c": "Sababtoo ah waxay yareeyaan dadka", "d": "Sababtoo ah laguma iibiyo suuqa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay tahay sababta 'Tamarta Biyaha' looga isticmaalo hirarka badaha?", "options": { "a": "Si looga dhaliyo awood koronto oo dabiici ah", "b": "Si biyaha looga dhigo kuwo macaan", "c": "Si maraakiibta loo xawaareeyo", "d": "Si looga hortago daadadka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Sidee bay shirkadaha dalxiiska u horumariyaan dalxiiska caalamiga ah?", "options": { "a": "Ayagoo fududeeya safarrada, huteelada iyo hagidda dalxiisayaasha", "b": "Ayagoo lacagta ka qaata dadka saboolka ah", "c": "Ayagoo joojiya safarrada", "d": "Ma lahan door muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Falanqee qodobka 'Is-cusbooneysiinta' ee tamarta?", "options": { "a": "Waa ilo dabiici ah oo aan gudhayn inta koonka uu jiro sida cadceedda", "b": "Waa ilo u baahan in maalin kasta la iibsado", "c": "Waa ilo dhamaada marka la isticmaalo", "d": "Isla mid baa loola jeedaa bitroolka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Muxuu 'Heerka nolosha oo sare u kaca' u kordhiyaa dalxiiska?", "options": { "a": "Sababtoo ah dadku waxay helayaan lacag dheeraad ah oo ay ugu safraan dalxiis", "b": "Sababtoo ah dadku waxay jecel yihiin gurigooda", "c": "Sababtoo ah nolosha ayaa adkaata", "d": "Ma lahan wax xiriir ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Maxay tahay saamaynta tiknoolojiyada sare ee goobaha warshadaha?", "options": { "a": "Waxay kordhisaa waxsoosaarka waxayna yareysaa khaladaadka", "b": "Waxay joojisaa shaqada gabi ahaanba", "c": "Waxay u baahan tahay shaqaale aan aqoon lahayn", "d": "Waxay kordhisaa kharashka si aan loo baahnayn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxay tahay sababta 'Saliidda (Bitroolka)' loogu tixgeliyo il tamar oo xaddidan?", "options": { "a": "Sababtoo ah kaydkeeda dhulka ku jira waa mid dhamaanaya oo aan dib u abuurmayn", "b": "Sababtoo ah waa qaali", "c": "Sababtoo ah looma isticmaalo gawaarida", "d": "Sababtoo ah waa la cusbooneysiin karaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Waa maxay ujeeddada laga leeyahay 'Iskudheelitirnaanta waxa la dhoofinayo iyo waxa la soo dejinayo'?", "options": { "a": "Si loo ilaaliyo dhaqaalaha dalka loona yareeyo deynta", "b": "Si dalka loo xiro gabi ahaanba", "c": "Si dalka laga dhigo mid sabool ah", "d": "Si canshuurta loo joojiyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Sidee buu 'Dalxiis isirka la xariira' (Ancestral tourism) u shaqeeyaa?", "options": { "a": "Waa in qofku booqdo halkii ay ka soo jeedeen awoowayaashiis", "b": "Waa in loo safro meel cusub", "c": "Waa in la daawado xayawaanka", "d": "Waa in la barto cilmiga xidigaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Maxay tahay ahmiyadda 'Mishiinnada' ee warshadaha casriga ah?", "options": { "a": "Waxay dedejiyaan waxsoosaarka waxayna beddelaan shaqadii gacanta ee cusleyd", "b": "Waxay yareeyaan tayada alaabta", "c": "Waxay cunaan tamarta oo kaliya faa'idona ma lahan", "d": "Looma baahna mishiinno" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Falanqee 'Ilaha tamarta aan la cusboonaysiin Karin' khatarta ay u leeyihiin mustaqbalka?", "options": { "a": "Waxay dhowaan ka dhamaan doonaan adduunka, taas oo keeni karta qalalaase tamar", "b": "Waxay yihiin kuwo waligood joogaya", "c": "Waxay dhowraan deegaanka", "d": "Ma lahan wax khatar ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Sidee bay 'Sarrifka lacagaha' u saameeyaan ganacsiga caalamiga ah?", "options": { "a": "Waxay suurageliyaan in dalalku isku iibsadaan badeecadaha iyagoo isticmaalaya lacago kala duwan", "b": "Waxay xiraan ganacsiga", "c": "Waxay yareeyaan dakhliga shirkadaha", "d": "Ma saameeyaan ganacsiga" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Maxay tahay sababta 'Gaadiidka Badda' loogu tixgeliyo inuu leeyahay kharash yar?", "options": { "a": "Sababtoo ah wuxuu qaadaa mug aad u weyn hal mar, isagoo isticmaalaya waddooyin dabiici ah (badaha)", "b": "Sababtoo ah waa kan ugu dhaqsaha badan", "c": "Sababtoo ah saliid badan ma isticmaalo", "d": "Sababtoo ah maraakiibtu waa yaryar yihiin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Falanqee doorka 'Tiknoolojiyada' ee beddelka qaabka maadooyinka caydhiinka?", "options": { "a": "Waxay suuragelisaa in walxo dabiici ah loo beddelo qalab casri ah oo tayo leh", "b": "Tiknoolojiyadu ma saameyso sanaacada", "c": "Waxay dib u dhigtaa waxsoosaarka", "d": "Waxay yareysaa qiimaha alaabta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sidee buu 'Dalxiiska wadar ahaan' (Group tourism) u saameeyaa horumarka dhaqaalaha?", "options": { "a": "Wuxuu kordhiyaa tirada dadka imanaya hal mar, taas oo dakhli badan u keenta huteelada iyo adeegyada", "b": "Wuxuu yareeyaa dakhliga", "c": "Wuxuu keenaa buuq kaliya", "d": "Wuxuu joojiya dalxiiska shaqsiga ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Maxay tahay ahmiyadda 'Ilaha tamarta ee dib loo cusboonaysiin karo' u leeyihiin dalka saboolka ah?", "options": { "a": "Waxay siin karaan tamar raqiis ah oo aan dhamaanayn sida cadceedda", "b": "Waa kuwo aad u qaali ah oo aan la isticmaali karin", "c": "Waxay u baahan yihiin saliid badan", "d": "Ma lahan wax muhiimad ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Falanqee 'Siyaasadaha ganacsi' ee dowladda?", "options": { "a": "Waa xeerarka dowladdu ku maamusho dhoofinta iyo soo dejinta si ay u dhowrto ganacsiga gudaha", "b": "Waa in ganacsiga la siiyo dad gaar ah kaliya", "c": "Waa in ganacsiga la joojiyo", "d": "Ma jiraan siyaasado ganacsi" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Sidee bay 'Adeegyada Isgaarsiinta' u saameeyaan gaadiidka?", "options": { "a": "Waxay gacan ka geystaan la socodka iyo hagidda gaadiidka meel kasta oo uu joogo", "b": "Waxay joojiyaan dhaqdhaqaaqa gaadiidka", "c": "Waxay kordhiyaan kharashka gawaarida", "d": "Ma saameeyaan gaadiidka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Maxaad ku micneyn lahayd 'Magaalooyinka Warshadaha' ee Ruushka?", "options": { "a": "Waa goobo lagu soo saaro qalabka culculus iyo tamarta nukliyeerka", "b": "Waa goobo lagu nasto kaliya", "c": "Waa goobo aan la oggolayn in la galo", "d": "Waa goobo beeraha laga fasho" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Waa maxay gunaanadka ahmiyadda 'Ilaha Dhaqaale' ee horumarka aadanaha?", "options": { "a": "Waa aasaaska nolosha casriga ah ee kor u qaada nolosha iyo barwaaqada", "b": "Waa waxyaabo aan loo baahnayn", "c": "Waa waxyaabo dhibaato u keena aadanaha kaliya", "d": "Waa waxyaabo miyiga ka jira kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch7_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch7',
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
    
    # Remove existing geo_ch7 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch7']
    
    # Check if geo_ch7 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch7' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 7aad: Sanaacada iyo Tamarta",
            "id": "geo_ch7"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch7':
                c['title'] = "Cutubka 7aad: Sanaacada iyo Tamarta"
                break
    
    # Add new geo_ch7 questions
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

    # Remove existing geo_ch7 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch7']
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
