import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha 'Magaalo'?", "options": { "a": "Deegaan dadku ku yar yihiin", "b": "Deegaan ay ku noolyihiin dad farabadan oo leh astaamo u gaar ah", "c": "Goob xoolaha lagu dhaqdo", "d": "Dhul beereed kaliya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa ku bama magaalada ugu weyn Soomaaliya?", "options": { "a": "Hargeysa", "b": "Muqdisho", "c": "Kismaayo", "d": "Baydhabo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Maxaa keena in loo hayaamo magaalooyinka?", "options": { "a": "Raadinta waxbarasho iyo adeeg caafimaad", "b": "In la helo dhul daaqsimeed", "c": "Cimilada miyiga oo qabow", "d": "In la tiriyo xoolaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 4, "question": "Magaalada Maka al-Mukarama waa noocee?", "options": { "a": "Magaalo ganacsi", "b": "Magaalo diimeed", "c": "Magaalo warshadeed", "d": "Magaalo ciidan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Magaalada Dubay waxaa loo yaqaannaa?", "options": { "a": "Magaalo aqooneed", "b": "Magaalo ganacsi", "c": "Magaalo diimeed", "d": "Magaalo ciidan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa ku bama dhibaatada ugu daran ee magaalada soo wajahda?", "options": { "a": "Biya la'aanta", "b": "Geedaha oo badan", "c": "Dadka oo yaraada", "d": "Dhaqanka oo iska weyn" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 7, "question": "Magaalada Oxford waa noocee?", "options": { "a": "Magaalo maamul", "b": "Magaalo waxbarasho (aqooneed)", "c": "Magaalo ganacsi", "d": "Magaalo warshadeed" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa ku bama astaamaha bulshada magaalada?", "options": { "a": "Isdhexgalka dadka oo aad u sarreeya", "b": "Tirada dadka oo aad u badan", "c": "Heerka nolosha oo jaban", "d": "Dumarka oo ka badan ragga" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Maxaa keena buuqa magaalada?", "options": { "a": "Geedaha", "b": "Gawaarida iyo warshadaha", "c": "Xoolaha", "d": "Roobka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa ku bama magaalada labaad ee ugu weyn Soomaaliya?", "options": { "a": "Berbera", "b": "Hargeysa", "c": "Boosaaso", "d": "Garowe" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Waa maxay shaqada magaalada Riyaad (Sida ku xusan casharka)?", "options": { "a": "Diimeed", "b": "Warshadaha", "c": "Ganacsi", "d": "Aqooneed" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Maxaa loola jeedaa 'Degmo magaaleed'?", "options": { "a": "Fiditaanka magaalooyinka", "b": "Meelaha lagu guuro", "c": "Cimilada magaalada", "d": "Isgaarsiinta" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 13, "question": "Waa ku bama gobolka ay ku taal magaalada Boosaaso?", "options": { "a": "Nugaal", "b": "Bari", "c": "Mudug", "d": "Sool" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa ku bama gobolka ay ku taal magaalada Baydhabo?", "options": { "a": "Bakool", "b": "Bay", "c": "Gedo", "d": "Mudug" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Magaalada Detroit (Mareykanka) waa noocee?", "options": { "a": "Magaalo diimeed", "b": "Magaalo warshadeed", "c": "Magaalo maamul", "d": "Magaalo aqooneed" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Soomaaliya waxay leedahay qiyaastii inta magaalo oo waaweyn?", "options": { "a": "10", "b": "22", "c": "50", "d": "100" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Waa ku bama mid ka mid ah dhibaatooyinka magaalada?", "options": { "a": "Ciriiriga waddooyinka", "b": "Biyo aad u badan", "c": "Waddooyin bannaan", "d": "Aamusnaan badan" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 18, "question": "Maxaa loo canshuuraa alaabta furdooyinka?", "options": { "a": "Si loo dhiirigeliyo qashinka", "b": "Si dakhli looga helo ganacsiga dalka soo galaya ama ka baxaya", "c": "Si loo yareeyo tirada dadka", "d": "Si loo kordhiyo biyaha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Halkee bay ku taal magaalada Garoowe?", "options": { "a": "Bari", "b": "Nugaal", "c": "Mudug", "d": "Sool" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Waa maxay dhibaatada ka dhalata qashinka?", "options": { "a": "Nadaafad darro iyo wasakh", "b": "Biyo nadiif ah", "c": "Aamusnaan", "d": "Fiditaanka dhulka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 21, "question": "Waa ku bama degmo ka tirsan gobolka Banaadir?", "options": { "a": "Balcad", "b": "Hodan", "c": "Jowhar", "d": "Afgooye" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Magaalada Tokyo waa noocee?", "options": { "a": "Diimeed", "b": "Ganacsi", "c": "Ciidan", "d": "Beeraha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Muxuu dakhliga hoose ee reer miyiga u saameeyaa socdaalka magaalada?", "options": { "a": "Wuxuu ku qasbaa inay raadsadaan fursado shaqo oo ka fiican", "b": "Wuxuu ka dhigaa inay miyiga sii joogaan", "c": "Wuxuu yareeyaa dhalashada", "d": "Wuxuu kordhiyaa xoolaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 24, "question": "Maxay magaalada ugu badan yihiin ragga marka loo eego dumarka?", "options": { "a": "Sababtoo ah dumarka ma shaqeeyaan", "b": "Sababtoo ah ragga ayaa u badan kuwa u soo hayaama shaqo iyo dhaqaale raadis", "c": "Sababtoo ah dumarka miyiga ayay jecel yihiin", "d": "Ma jiro farqi u dhexeeya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Sidee loo yareyn karaa dhibaatada fiditaanka magaalooyinka ee dhul daaqsimeedka?", "options": { "a": "In magaalada lagu fidiyo dhulka beeraha", "b": "In la xaddido fiditaanka loona qoondeeyo meel gaar ah", "c": "In magaalada la dhisin", "d": "In dadka miyiga lagu celiyo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Waa maxay doorka socdaalka ee kala duwanaashiyaha kobaca gobolada?", "options": { "a": "Ma lahan wax door ah", "b": "Socdaalka gudaha iyo dibadda ayaa bixiya kororka dadka ee magaalo gaar ah", "c": "Socdaalku wuxuu dilaa magaalooyinka", "d": "Socdaalku wuxuu yareeyaa ganacsiga" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Maxay isdhexgalka dadka magaalada u hooseeyaa?", "options": { "a": "Sababtoo ah dadku isma yaqaannaan", "b": "Sababtoo ah dadku way badan yihiin, qof walbaana dantiisa ayuu ku mashquulsan yahay", "c": "Sababtoo ah dadka magaalada ma hadlaan", "d": "Sababtoo ah ma jiraan goobo lagu kulmo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Maxaad ku micneyn lahayd warshadaha oo ku badan magaalada?", "options": { "a": "Magaaladu waxay cagta saartay wadadii horumarka", "b": "Magaaladu waxay noqotay meel wasakh ah", "c": "Magaaladu waxay lumisay ganacsigii", "d": "Ma lahan macno weyn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Waa ku bama magaalo ku taal gobolka Shabeellada Hoose?", "options": { "a": "Marka", "b": "Jowhar", "c": "Beledweyne", "d": "Gaalkacyo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Waa ku bama degmo ku taal gobolka Bari?", "options": { "a": "Qandala", "b": "Eyl", "c": "Galdogob", "d": "Taleex" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Maxay tahay sababta ugu weyn ee qoysaska reer miyiga u guuraan?", "options": { "a": "Si ay u helaan waxbarasho sare ubadkooda", "b": "Si ay u helaan hawo nadiif ah", "c": "Si ay u badsadaan xoolaha", "d": "Si ay u barto luuqado cusub" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Waa ku bama dhibaato ka dhalata gawaarida iyo diyaaradaha ee magaalada?", "options": { "a": "Biyo yaraan", "b": "Buuqa magaalada", "c": "Cunto yaraan", "d": "Qashin badan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sidee loo xallin karaa dhibaatada qashinka ee magaalada?", "options": { "a": "In qashinka la gubto guriga dhexdiisa", "b": "In si joogto ah looga fogeeyo gudaha magaalada loona geeyo meel gaar ah", "c": "In qashinka la dhex tuuro waddooyinka", "d": "In dadka lagu ganaaxo qashinka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay Muqdisho dadka ku nool uga badan yihiin Hargeysa?", "options": { "a": "Sababtoo ah waa caasimadda dalka", "b": "Sababtoo ah Hargeysa waa magaalo yar", "c": "Sababtoo ah biyaha ayaa ku badan", "d": "Ma jiro farqi weyn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Waa ku bama degmo ka tirsan gobolka Shabeellada Dhexe?", "options": { "a": "Balcad", "b": "Afgooye", "c": "Qoryooley", "d": "Wanlaweyn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Waa maxay micnaha 'Magaalo Maamul'?", "options": { "a": "Magaalo lagu cibaadeysto", "b": "Magaalo ay ku yaallaan xafiisyada dowladda iyo siyaasadda", "c": "Magaalo leh warshado badan", "d": "Magaalo waxbarasho" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Magaalada Lyon (Faransiiska) waa noocee?", "options": { "a": "Diimeed", "b": "Warshadeed", "c": "Ciidan", "d": "Beeraha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Waa ku bama degmo ku taal gobolka Hiiraan?", "options": { "a": "Beledweyne", "b": "Jowhar", "c": "Gaalkacyo", "d": "Garowe" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Muxuu xiriirka bulshada magaalada u hooseeyaa?", "options": { "a": "Dadka oo is jecel", "b": "Dadka oo aad u badan iyo xiriirka oo ah mid xirfadeed oo kooban", "c": "Dadka oo hadda miyiga ka yimid", "d": "Isgaarsiinta oo xun" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Magaalada Calaykara (Aqooneed) tusaale ahaan halkan kuma taal, laakiin maxay tusaale u tahay?", "options": { "a": "Magaalo ganacsi", "b": "Magaalo waxbarasho", "c": "Magaalo ciidan", "d": "Magaalo diimeed" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Maxaa xal u noon kara ciriiriga waddooyinka?", "options": { "a": "In gawaarida la mamnuuco", "b": "In la ballaariyo waddooyinka lana helo nidaam taraafik", "c": "In dadku lugeeyaan", "d": "In magaalo cusub la dhisto" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Goobta lagu canshuuro alaabta dalka soo galaysa waa?", "options": { "a": "Suuqa", "b": "Furdooyinka (Ports)", "c": "Dugsiyada", "d": "Warshadaha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 43, "question": "Halkee bay ku taal magaalada Boorame?", "options": { "a": "Waqooyi Galbeed", "b": "Awdal", "c": "Sanaag", "d": "Togdheer" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Magaalada Kismaayo waa caasimadda gobolka?", "options": { "a": "Jubbada Dhexe", "b": "Jubbada Hoose", "c": "Gedo", "d": "Bay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 45, "question": "Halkee bay ku taal magaalada Ceerigaabo?", "options": { "a": "Sanaag", "b": "Sool", "c": "Togdheer", "d": "Bari" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxaa loola jeedaa 'heerka nolosha oo aad u sarreeya' ee magaalada?", "options": { "a": "Magaalada oo dhismaheedu sareeyo", "b": "Nolosha oo qaali ah marka loo eego miyiga", "c": "Dadka oo dhererkoodu sareeyo", "d": "Magaalada oo buur saaran" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 47, "question": "Magaalada Berbera waxay ku taal gobolka?", "options": { "a": "Awdal", "b": "Waqooyi Galbeed", "c": "Togdheer", "d": "Sanaag" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 48, "question": "Falanqee saamaynta ay ku leedahay nolosha miyiga daciifnimada adeegyada sida biyaha iyo caafimaadka?", "options": { "a": "Waxay keentaa hayaan xooggan oo loo soo galayo magaalooyinka", "b": "Waxay dhiirigelisaa in miyiga la joogo", "c": "Waxay kordhisaa waxsoosaarka beeraha", "d": "Ma lahan wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 49, "question": "Muxuu dakhliga qofka reer miyiga ah u yahay qodob muhiim u ah 'Urbanization'?", "options": { "a": "Dakhliga hoose wuxuu ku qasbaa inuu magaalada u shaqo tago si uu nolosha qoyskiisa u daboolo", "b": "Dakhliga hoose wuxuu ka dhigaa qofka mid magaalada neceb", "c": "Dakhliga hoose wuxuu badshaa xoolaha", "d": "Dakhligu ma saameeyo magaalada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 50, "question": "Sidee buu socdaalku u kala duwaa kobaca magaalooyinka Soomaaliya?", "options": { "a": "Magaalada soo jiidata socdaalka ugu badan waxay noqotaa tan ugu kobaca badan xagga tirada iyo dhaqaalaha", "b": "Socdaalku wuxuu daciifiyaa magaalooyinka", "c": "Magaalada dadka ka baxayaan ayaa aad u kobocda", "d": "Socdaalku waa mid u dhexeeya miyiga kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Falanqee sababta ay magaalada Muqdisho ugu badan tahay tirada dadka marka loo eego Hargeysa?", "options": { "a": "Sababtoo ah waa xarunta maamulka, ganacsiga iyo fursadaha shaqo ee dalka ugu badan", "b": "Sababtoo ah cimilada Muqdisho ayaa ka wanaagsan", "c": "Sababtoo ah Hargeysa ma lahan furdooyin", "d": "Sababtoo ah waa magaalada ugu dhow miyiga" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Maxaa xal u noon kara in warshaduhu aysan dhibaato u geysan dadka magaalada?", "options": { "a": "In warshadaha laga dhisayo gudaha magaalada", "b": "In warshadaha laga dhigo meel ka baxsan magaalada (Industrial zones)", "c": "In warshadaha la xiro", "d": "In dadka magaalada laga saaro" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Falanqee xiriirka u dhexeeya 'magaalo ganacsi' iyo 'furdooyinka' (Ports)?", "options": { "a": "Furdooyinka waxay u fududeeyaan magaalooyinka inay noqdaan xarun ganacsi oo caalami ah", "b": "Ma lahan wax xiriir ah", "c": "Furdooyinka waxay yareeyaan ganacsiga", "d": "Furdooyinka waxay kordhiyaan dhalashada carruurta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Maxay tahay caqabadda ugu weyn ee qashin fogeynta magaalada?", "options": { "a": "Ma lahan wax caqabad ah", "b": "Tubbooyinka iyo meelaha qashinka laga saaro oo ciriiri ah ama aan jirin", "c": "Qashinka oo ah mid aan la fogeyn karin", "d": "Dadka oo qashinka jecel" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxaad ku micneyn lahayd xaqiiqda ah in 'isdhexgalka dadka magaalada uu hooseeyo'?", "options": { "a": "Waa calaamad muujinaysa kala fogaanshaha bulsho ee ka dhasha ciriiriga iyo mashquulka", "b": "Waa calaamad muujinaysa nabadda", "c": "Waa dhibaato dhaqan", "d": "Waa mid keenta in magaaladu burburto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Sidee bay dhibaatooy primary qoyska ee miyiga u saameeyaan tirada dadka magaalada?", "options": { "a": "Waxay keenaan barakac iyo hayaan qofku kaga baxayo miyiga si uu nabad uga helo magaalada", "b": "Waxay keenaan in dadku miyiga ku dhintaan", "c": "Waxay kordhiyaan beeraha", "d": "Ma lahan wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Waa maxay ujeeddada laga leeyahay in xal loo helo ciriiriga waddooyinka?", "options": { "a": "Si loo kordhiyo gawaarida", "b": "Si loo dedejiyo dhaqdhaqaaqa ganacsiga iyo nolosha maalinlaha ah", "c": "Si magaalada loo qurxiyo kaliya", "d": "Si dadku u lugeeyaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Muxuu yahay farqiga u dhexeeya 'magaalo maamul' iyo 'magaalo warshadeed'?", "options": { "a": "Maamulku waa siyaasad, warshadeeduna waa waxsoosaar", "b": "Isla mid baa loola jeedaa", "c": "Warshadeedu waa mid aqooneed", "d": "Maamulku waa mid diimeed" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay 'biya la'aanta' u tahay dhibaatada ugu daran ee magaalada?", "options": { "a": "Sababtoo ah magaaladu ma lahan webiyo", "b": "Sababtoo ah biyuhu waa nolosha dadka, tirada badan ee magaaladana waxay u baahan tahay biyo ku filan", "c": "Sababtoo ah dadku waxay biyaha u isticmaalaan si xun", "d": "Sababtoo ah roobka ma da'o" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Maxay tahay kaalinta 'furdooyinka' (Ports) ee dhaqaalaha magaalooyinka sida Berbera iyo Boosaaso?", "options": { "a": "Waxay noqdaan ilaha ugu weyn ee dakhliga canshuurta iyo ganacsiga dibadda", "b": "Waxay soo jiitaan kalluunka", "c": "Waxay yareeyaan dadka", "d": "Ma lahan kaalin muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sidee loo horumarin karaa helitaanka baahiyaha maalinlaha ah ee bulshada magaalada?", "options": { "a": "In la kordhiyo suuqyada iyo in la fududeeyo helitaanka raashinka iyo biyaha", "b": "In dadka laga qaado lacag badan", "c": "In baahiyahaas la dhimmo", "d": "In la yareeyo warshadaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Muxuu wasakhowga magaaladu u yahay dhibaato taagan?", "options": { "a": "Sababtoo ah wuxuu dhibaato u geystaa caafimaadka dadka iyo deegaanka", "b": "Sababtoo ah magaalada ayaa wasakh jecel", "c": "Sababtoo ah qashinka waa la gubaa", "d": "Saameyn ma leh" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Waa maxay tusaalaha xog juqraafi oo muujinaya sababta socdaalka reer miyiga?", "options": { "a": "Fursado shaqo iyo daboolidda adeegyada aasaasiga ah sida waxbarashada sare", "b": "In ay dalxiis u tagaan", "c": "In ay xoolaha ku iibiyaan magaalada", "d": "In ay soo arkaan caasimadda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxay magaalooyinka Soomaaliya ugu kala duwan yihiin tirada dadka?", "options": { "a": "Sababtoo ah socdaalka dibadda iyo gudaha oo u badan magaalooyinka waaweyn", "b": "Sababtoo ah magaalooyinka qaarkood ma lahan biyo", "c": "Sababtoo ah dadku waxay jecel yihiin gobolladooda", "d": "Ma jiro sabab cilmiyeed" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Magaalada Muqdisho waxay ka kooban tahay inta degmo?", "options": { "a": "10", "b": "17 (iyo ka badan markii dambe)", "c": "5", "d": "22" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 66, "question": "Falanqee doorka 'magaalo ciidan'?", "options": { "a": "Magaalo loo qoondeeyay saldhigyada iyo tababarka ciidanka", "b": "Magaalo ay ka jiraan dagaallo", "c": "Magaalo ay dadka oo dhami askar yihiin", "d": "Magaalo aan la gali karin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee buu fiditaanka magaaladu u saameeyaa dhul daaqsimeedka?", "options": { "a": "Wuxuu yareeyaa dhulki xooluhu daaqayeen, taas oo dhibaato ku ah xoolaha", "b": "Wuxuu kordhiyaa cowska", "c": "Wuxuu keenaa roob badan", "d": "Ma saameeyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Waa ku bama degmo ku taal gobolka Bakool?", "options": { "a": "Xudur", "b": "Baydhabo", "c": "Garbahaarey", "d": "Kismaayo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Maxaa xal u noon kara 'biya la'aanta' magaalada?", "options": { "a": "In biyo ku filan la gaarsiiyo bulshada lana ballaariyo ilaha biyaha", "b": "In dadku biyaha yareeyaan", "c": "In magaalada laga guuro", "d": "In la sugo roobka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Falanqee xiriirka u dhexeeya 'heerka nolosha oo sareeya' iyo magaalada?", "options": { "a": "Mashquulka iyo baahida adeegyo badan waxay kordhiyaan kharashka nolosha", "b": "Magaalada ayaa ah meel dadku qani ku yihiin", "c": "Magaalada nolosheedu waa mid jaban", "d": "Ma jiro xiriir dhaqaale" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Magaalada Jilib waxay ku taal gobolka?", "options": { "a": "Jubbada Hoose", "b": "Jubbada Dhexe", "c": "Gedo", "d": "Bay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 72, "question": "Waa ku bama degmo ku taal gobolka Sool?", "options": { "a": "Laascaanood", "b": "Ceerigaabo", "c": "Garowe", "d": "Buraan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Falanqee doorka 'magaalo aqooneed' ee horumarka bulshada?", "options": { "a": "Waxay soo saartaa dad aqoon leh oo dalka horumariya", "b": "Waxay kordhisaa tirada carruurta", "c": "Waxay yareysaa ganacsiga", "d": "Ma lahan door muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Muxuu xalka dhibaatooyinka magaalada u baahan yahay 'qorsheyn magaalo' (Urban planning)?", "options": { "a": "Si looga fogaado ciriiri, biyo yaraan iyo wasakh", "b": "Si magaalada loo dhiso meel kasta", "c": "Si dadka miyiga looga hortago", "d": "Si ganacsiga loo xiro" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Sidee buu socdaalka dibadda u saameeyaa kobaca magaalooyinka?", "options": { "a": "Wuxuu kordhiyaa dakhliga iyo dadka soo galaya, taas oo kordhisa baaxadda magaalada", "b": "Wuxuu yareeyaa dadka dalka jooga", "c": "Wuxuu dilaa ganacsiga gudaha", "d": "Ma saameeyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Maxay dadka reer miyiga ah u raadsadaan 'fursado shaqo' magaalooyinka?", "options": { "a": "Sababtoo ah miyiga ma lahan shaqo dakhli lacageed leh oo joogto ah", "b": "Sababtoo ah waxay jecel yihiin shaqada warshadaha", "c": "Sababtoo ah magaalada ayaa looga shaqeeyaa si yar", "d": "Si ay u noqdaan askar" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Waa ku bama degmo ku taal gobolka Mudug?", "options": { "a": "Gaalkacyo", "b": "Galdogob", "c": "Hobyo", "d": "Dhamaan kuwan kor ku xusan" }, "correctAnswer": "d", "difficultyLevel": "hard" },
  { "id": 78, "question": "Falanqee 'Wasakhowga magaalada' dhibka uu u leeyahay tubbooyinka biyaha?", "options": { "a": "Qashinka wuxuu xiraa tubbooyinka, taas oo keenta in biyuhu wasakhoobaan ama fadhiistaan", "b": "Wuu nadiifiyaa", "c": "Wuxuu kordhiyaa socodka biyaha", "d": "Saameyn ma leh" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Maxaad ku soo koobi lahayd farqiga u dhexeeya miyiga iyo magaalada xagga adeegga?", "options": { "a": "Miyiga adeegyadu waa kuwo dabiici ah, magaaladana waa kuwo casri ah oo nidaamsan", "b": "Magaaladu ma lahan adeeg", "c": "Miyiga adeegga ayaa ka fiican", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch6_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch6',
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
    
    # Remove existing geo_ch6 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch6']
    
    # Check if geo_ch6 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch6' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 6aad: Magaalooyinka",
            "id": "geo_ch6"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch6':
                c['title'] = "Cutubka 6aad: Magaalooyinka"
                break
    
    # Add new geo_ch6 questions
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

    # Remove existing geo_ch6 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch6']
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
