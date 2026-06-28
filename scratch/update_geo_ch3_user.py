import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay wasakhow?", "options": { "a": "Waa hagaajinta deegaanka", "b": "Waa isbeddel iyo daryeel la’aan ku timaada deegaanka", "c": "Waa daryeelka xayawaanka", "d": "Waa abuurista dhir cusub" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Sheeg hal nooc oo wasakhowga ka mid ah?", "options": { "a": "Wasakhowga dhawaqa", "b": "Wasakhowga biyaha", "c": "Wasakhowga iftiinka", "d": "Wasakhowga dharka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Waa maxay xarfashada ciida?", "options": { "a": "Waa ciidda oo biyo noqota", "b": "Waa dhaqaaq tartiib ah ee ciidda oo ay dabeyshu dhaqaajiso", "c": "Waa beeridda dhirta", "d": "Waa dhismaha daaraha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Maxaa keena daadadka inta badan?", "options": { "a": "Dabaylaha xoogga leh", "b": "Xaddiga da’aaga roobka oo bata", "c": "Qorraxda oo kululaata", "d": "Ciyaarta carruurta" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Waa maxay nabaad guur?", "options": { "a": "Waa nafaqaddaro dhulka gaartay aawgeed in geedo soo bixi waayaan", "b": "Waa dhirta oo si fiican u baxda", "c": "Waa roobka oo yaraada kaliya", "d": "Waa dhismaha waddooyinka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 6, "question": "Sheeg mid ka mid ah dhibaatooyinka deegaanka Soomaaliya?", "options": { "a": "Baraf ka dhasha oo aan la filayn", "b": "Jaridda dhirta", "c": "Warshado aad u badan", "d": "Dhul go’o dhif ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Kala duwanaashiyaha deegaanka waxaa loola jeedaa kala duwanaashiyaha _____.", "options": { "a": "Dharka", "b": "Noolaha", "c": "Baabuurta", "d": "Waddooyinka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Wasakhowga hawada maxaa keeni kara?", "options": { "a": "Warshadaha", "b": "Cawska", "c": "Biyaha saafi ah", "d": "Xiddigaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 9, "question": "Waa maxay xaaluf?", "options": { "a": "Hoos u dhac ku yimaada carrada dhulka qallalan", "b": "Sare u kac ku yimaada wax soo saarka", "c": "Waa daryeelka dhirta", "d": "Waa dhisidda seerooyin" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 10, "question": "Maxaa dhibaato weyn gaarsiiya kaymaha dunida?", "options": { "a": "Ilaalinta xayawaanka", "b": "Baahidda beerashada iyo fiditaanka magaalooyinka", "c": "Roobka yar", "d": "Ciyaaraha deegaanka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Sheeg hal khasaaro oo ka dhasha daadadka?", "options": { "a": "Naf iyo maal oo luma", "b": "Dhirta oo badata", "c": "Carrada oo nafaqo hesha", "d": "Magaalooyinka oo quruxsada" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 12, "question": "Wasakhoowga carrada waa nooc ka mid ah wasakhowga deegaanka.", "options": { "a": "Sax", "b": "Khalad", "c": "Lama yaqaan", "d": "Mararka qaarkood" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 13, "question": "Xarfashada carrada waxaa loola jeedaa dhaqaaqa ciidda ee ay dabeyshu _____.", "options": { "a": "Joojiso", "b": "Dhaqaajiso", "c": "Gubto", "d": "Abuurto" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Maxay tahay muhiimadda kala duwanaashiyaha deegaanka?", "options": { "a": "Waa kala duwanaanta cimilada", "b": "Waa kala duwanaanta guryaha", "c": "Waa kala duwanaanta luqadaha", "d": "Ma lahan muhiimad" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 15, "question": "Abaaruhu ma ka mid yihiin dhibaatooyinka deegaanka Soomaaliya?", "options": { "a": "Haa", "b": "Maya", "c": "Kaliya xagaaga", "d": "Kaliya deegaanka badda" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 16, "question": "Maxaa loo adeegsadaa in looga hortago daadadka?", "options": { "a": "Agab bixiya digniin xilli hore", "b": "Gubista dhirta", "c": "Ciriirinta tubooyinka", "d": "Ma lahan ka hortag" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 17, "question": "Xaalufku wuxuu hakiyaa horumarka _____ dalka.", "options": { "a": "Dhaqaalaha", "b": "Ciyaaraha", "c": "Heesaha", "d": "Waddooyinka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 18, "question": "Wasakhowga cunnada ma suurtagal baa?", "options": { "a": "Haa, waa dhibaato deegaan", "b": "Maya, cunnadu ma wasakhoowdo", "c": "Kaliya badda dhexdeeda", "d": "Kaliya warshadaha dhexdeeda" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 19, "question": "Kala duwanaashiyaha nooluhu wuxuu hormariyaa wax soo saarka _____.", "options": { "a": "Deegaanka", "b": "Baabuurta", "c": "Daaraha", "d": "Dharka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 20, "question": "Tubooyinka biyaha qaada oo ciriiri noqda waxay sababaan?", "options": { "a": "Daadad", "b": "Abaar", "c": "Xaaluf", "d": "Nabaad guur" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 21, "question": "Dhulka oo go’o waa mid ka mid ah dhibaatooyinka _____.", "options": { "a": "Daadadka", "b": "Cimilada qabow", "c": "Dhirta badan", "d": "Xiddigaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 22, "question": "Maxaa keena in geedo soo bixi waayaan?", "options": { "a": "Nabaad guurka", "b": "Roobka badan", "c": "Beerashada saxda ah", "d": "Ilaalinta deegaanka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 23, "question": "Sidee buu aadanuhu u saameeyaa deegaanka marka loo eego xaalufka?", "options": { "a": "Howlaha aadanaha ayaa keena hoos u dhaca carrada", "b": "Aadanuhu wax saameyn ah ma lahan", "c": "Aadanuhu roobka ayuu joojiyaa", "d": "Aadanuhu dhulka ayuu kordhiyaa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 24, "question": "Waa maxay xalka ugu habboon ee looga hortago xaalufka?", "options": { "a": "Jarista dhirta", "b": "Dhiirigelinta cilmi baarista iyo wacyigelinta deegaanka", "c": "Ballaarinta magaalooyinka", "d": "Joojinta roobka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Maxay yihiin sababaha xarfashada carrada?", "options": { "a": "Baabi'inta dhirta iyo daaqa aan loo meel dayin", "b": "Beeridda dhirta badan", "c": "Dhismaha tubooyinka biyaha", "d": "Ilaalinta seerooyinka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 26, "question": "Sidee looga hortagi karaa daadadka magaalooyinka?", "options": { "a": "In la daryeelo meelaha unugul iyo ilaalinta magaalooyinka", "b": "In la xiro tubooyinka", "c": "In dhulka la simo", "d": "In la kordhiyo burburka waddooyinka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 27, "question": "Wasakhowga deegaanku maxuu ku dhashay (ka sokow wasakhda)?", "options": { "a": "Musiibooyin kumannaan dad ah ku dhintaan", "b": "Sare u kac dhaqaale", "c": "In dhirtu si dhaqso ah u baxdo", "d": "In hawadu nadiif noqoto" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 28, "question": "Maxaa loola jeedaa 'Seero deegaan'?", "options": { "a": "Meel la ilaaliyo si deegaanka loo xafido", "b": "Meel lagu gubo dhirta", "c": "Meel loogu talagalay warshadaha", "d": "Meel dadka laga saaro" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Dhibaatada deegaanka Soomaaliya maxay u horseedaa?", "options": { "a": "Wasakhowga biyaha, hawada iyo nabaad guurka", "b": "In dalka baraf ka kordho", "c": "In dadku noqdaan kuwo hodan ah", "d": "In la helo biyo saafi ah oo badan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Xarfashada biyaha keenaan waa nooc ka mid ah xarfashada carrada.", "options": { "a": "Sax", "b": "Khalad", "c": "Kaliya dabeysha ayaa keenta", "d": "Biyuhu xarfasho ma keenaan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Maxaa dhaca haddii la baabi’iyo dhirta hakin lahayd bacaadka?", "options": { "a": "Waxaa kordha xarfashada carrada", "b": "Ciidda ayaa istaagta", "c": "Magaalooyinka ayaa quruxsada", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Waa maxay 'Bacaad cilin'?", "options": { "a": "Waa hab looga hortago xarfashada ciidda", "b": "Waa ciidda oo la gubo", "c": "Waa ciidda oo la kaxaysto", "d": "Waa ciidda oo la wasakheeyo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sidee buu wasakhowga u saameeyaa maalgashiga ilaha dabiiciga ah?", "options": { "a": "Wuxuu keenaa musiibooyin iyo cudurro cusub", "b": "Wuxuu kordhiyaa faa'iidada", "c": "Wuxuu nadiifiyaa ilaha dabiiciga", "d": "Ma saameeyo maalgashiga" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxaa sababa in carrada awoodi weydo inay dhuuqdo biyaha?", "options": { "a": "Biyaha oo aad u xad dhaaf noqda", "b": "Carrada oo nafaqo badan", "c": "Dhirta oo aad u badan", "d": "Qorraxda oo yar" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Daaqa aan loo meel dayin waa sabab keenta _____.", "options": { "a": "Xarfashada carrada", "b": "Ilaalinta deegaanka", "c": "Dhaqaalaha oo kordha", "d": "Roobka oo bata" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxay tahay khatarta deegaan ee ugu badan ee aadanaha waxyeeleyn karta?", "options": { "a": "Wasakhoowga iyo isbeddelka cimilada", "b": "Dhirta oo badata", "c": "Xoolaha oo bata", "d": "Biyaha oo nadiif noqda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Filiqsanaanta daadadka waxaa loo yareyn karaa ayadoo dadka loo jiheeyo _____.", "options": { "a": "Kafaa’ideysiga dhul beereedka", "b": "Inay magaalooyinka dhistaan", "c": "Inay geedaha jaraan", "d": "Inay tubooyinka xiraan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 38, "question": "Burburka waddooyinka ma ka qey qaataa daadadka?", "options": { "a": "Haa, waa sabab dhab ah", "b": "Maya, wax saameyn ah ma lahan", "c": "Kaliya haddii roobka yaraado", "d": "Waddooyinku biyaha ayay dhuuqaan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Waa maxay saameynta xarfashada carrada ku leedahay dhirta?", "options": { "a": "Bixitaankii dhirta oo gaabis noqda", "b": "Dhirta oo dhaqso u baxda", "c": "Dhirta oo nafaqo hesha", "d": "Dhirta oo midab beddelata" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxaa kordhiya daneynta caalamka ee kala duwanaashiyaha noolaha?", "options": { "a": "Inuu hormariyo wax soo saarka iyo dhaqaalaha dunida", "b": "Inuu keeno abaaraha", "c": "Inuu yareeyo tirada dadka", "d": "Sabab ma lahan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Jaridda dhirta Soomaaliya waxay keentaa nabaad guurka _____.", "options": { "a": "Carrada iyo dhirta", "b": "Baabuurta", "c": "Ciyaaraha", "d": "Waddooyinka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Xarfashada dabeyshu keento waxaa loo yareyn karaa ayadoo la _____.", "options": { "a": "Beero dhir", "b": "Jaro dhirta", "c": "Dhisidda daaraha dhabarkooda", "d": "Ma jiro xal" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Musiibooyinka daadadka ma saameeyaan xoolaha?", "options": { "a": "Haa, xoolaha waxyeello ayaa soo gaarta", "b": "Maya, xoolaha way u roon tahay", "c": "Kaliya haddii xooluhu yaryar yihiin", "d": "Xoolaha badda kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 44, "question": "Maxaa loo baahan yahay in lagu sameeyo meelaha daadadka khatarta ugu jira?", "options": { "a": "Tiro koob iIyo daryeel gaar ah", "b": "In la iska daayo", "c": "In laga guuro gabi ahaanba", "d": "In la gubo dhulkaas" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Si xun u isticmaalka carrada maxay keentaa?", "options": { "a": "Xarfashada carrada", "b": "Bacrinta carrada", "c": "Nadiifinta carrada", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 46, "question": "Fayrasyo cusub maxaa keeni kara sida uu qabo cutubka?", "options": { "a": "Dhibaatada deegaanka iyo wasakhowga", "b": "Ilaalinta dhirta", "c": "Roobka nadiifka ah", "d": "Cimilada dhex-dhexaadka ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 47, "question": "Xarfashada carrada waxaa saameyn ku leh habdhaqanka _____.", "options": { "a": "Aadanaha", "b": "Xiddigaha", "c": "Lama-degaanka", "d": "Badda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 48, "question": "Cilmi baaris buuxda maxay ka tartaa xarfashada?", "options": { "a": "In la ogaado sababaha loogana hortago", "b": "In la kordhiyo xarfashada", "c": "Ma tarto waxba", "d": "Waa lacag lumis kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 49, "question": "Falanqee xiriirka ka dhexeeya fiditaanka magaalooyinka iyo burburka kaymaha dunida?", "options": { "a": "Magaalooyinka waxay u baahan yihiin dhul, taas oo keenta in kaymaha la jaro lana baabi'iyo deegaanka dabiiciga ah", "b": "Magaalooyinka waxay caawiyaan kaymaha inay koraan", "c": "Ma lahan wax xiriir ah", "d": "Kaymaha ayaa magaalooyinka dhex baxa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 50, "question": "Maxay tahay sababta cilmiyaysan ee loo daneeyo kala duwanaashiyaha noolaha dunida maanta?", "options": { "a": "Sababtoo ah waxay aasaas u tahay wax soo saarka deegaanka iyo xasilloonida dhaqaalaha dunida", "b": "Sababtoo ah waa hiwaayad caalami ah", "c": "Si loo baabi'iyo cudurada kaliya", "d": "Sabab ma lahan oo cilmi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Sidee bay wasakhowga hawada, biyaha, iyo carrada u horseedaan musiibooyin dad badani ku dhintaan?", "options": { "a": "Waxay dilaan ilaha nolosha, waxayna keenaan cudurro dilaa ah iyo isbeddel cimilada oo halis ah", "b": "Waxay keenaan musiibooyin dabiici ah oo kaliya", "c": "Waxay keenaan in dadku dalka ka cararaan", "d": "Ma horseedaan musiibooyin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Falanqee saamaynta ay ku leedahay xarfashada carrada wax soo saarka beeraha?", "options": { "a": "Waxay kaxaysaa lakabka bacrin ah, taas oo hoos u dhigta wax soo saarka iyo bixitaanka dhirta", "b": "Waxay kordhisaa nafaqada beeraha", "c": "Beeraha ayay qurux ka dhigtaa", "d": "Beeruhu ma saameeyaan xarfashada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Maxaa loola jeedaa 'Kala duwanaashiyaha hiddo sidaha' ee dhirta iyo xoolaha?", "options": { "a": "Waa kala duwanaanta qaab dhismeedka DNA-da ee u oggolaanaya noolaha inay la qabsadaan deegaanka", "b": "Waa birta noolaha kaliya", "c": "Waa tirada xayawaanka oo la kordhiyo", "d": "Waa daryeelka caafimaadka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Sidee looga hortagi karaa xarfashada carrada ee ay biyaha iyo dabeyshu keenaan si joogto ah?", "options": { "a": "In la isku daro cilmi baaris, bacaad cilin, beeridda dhirta iyo xafidida deegaanka", "b": "In biyaha meel kasta laga xiro", "c": "In dabeysha la joojiyo", "d": "Ma jiro xal cilmiyeed oo waara" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Falanqee doorka 'Wacyi deegaanka' ee xallinta dhibaatooyinka xaalufka?", "options": { "a": "Wuxuu dadka ku buraarujiyaa khatarta deegaanka iyo sidii looga qayb qaadan lahaa ilaalintiisa", "b": "Waa barashada luqadaha deegaanka kaliya", "c": "Wax saameyn ah ma lahan", "d": "Wuxuu kordhiyaa jarista dhirta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Maxay tahay sababta 'Haraaga qalabka dhismaha' loogu tixgeliyo sabab keenta daadadka?", "options": { "a": "Waxay xiraan tubooyinka biyaha qaada, taas oo keenta inay biyuhu ku fatahaan waddooyinka", "b": "Waxay keenaan roob badan", "c": "Waxay burburiyaan daruuraha", "d": "Ma keenaan daadad" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sidee buu xaalufku u hakiyaa 'Horumarka Bulshada'?", "options": { "a": "Wuxuu yareeyaa ilaha nolosha, wuxuuna abuuraa faqri iyo barakac", "b": "Wuxuu kordhiyaa heesta bulshada", "c": "Wuxuu keenaa in magaalooyin cusub la dhiso", "d": "Ma saameyo bulshada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Maxay tahay khatarta ugu weyn ee haysata deegaanka Soomaaliya marka loo eego 'Wasakhowga Biyaha'?", "options": { "a": "Yaraanta biyo nadiif ah iyo nabaad guurka ilaha biyaha", "b": "Biyo badan oo dalka qarqiyay", "c": "Biyaha oo baraf noqday", "d": "Biyaha oo midab beddeshay kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Falanqee xiriirka u dhexeeya 'Daaqa aan loo meel dayin' iyo nabaad guurka dhirta?", "options": { "a": "Xoolaha waxay cunaan dhirta curdunka ah iyagoon fursad u siin inay koraan, taas oo dhulka ka dhigta qaawan", "b": "Daaqu wuxuu caawiyaa dhirta", "c": "Xoolaha dhirta ma cunaan", "d": "Daaqu wuxuu keenaa roobka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Maxaa loola jeedaa 'Isbeddelka Cimilada' marka laga hadlayo dhibaatooyinka deegaanka?", "options": { "a": "Waa isbeddelka fog ee heerkulka iyo habka roobka ee dunida oo saameeya nolosha", "b": "Waa isbeddelka maalinlaha ah ee hawada", "c": "Waa qorraxda oo soo baxda kaliya", "d": "Waa dayaxa oo madoobaada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sidee bay 'Tubooyinka biyaha oo ciriiri noqda' u saameeyaan naqshadda magaalooyinka?", "options": { "a": "Waxay daciifiyaan kaabayaasha magaalooyinka, waxayna keenaan burburka waddooyinka iyo daaraha", "b": "Waxay magaalooyinka ka dhigaan kuwo nadiif ah", "c": "Waxay kordhiyaan dhismaha", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Falanqee faa'iidada 'Digniinta xilli hore' ee maaraynta musiibooyinka?", "options": { "a": "Waxay oggolaataa in dadka iyo maalka la badbaadiyo ka hor inta aysan musiibadu dhicin", "b": "Waa mid waqti lumis ah", "c": "Waxay kordhisaa cabsida kaliya", "d": "Waxay baajisaa roobka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Sidee bay 'Fiditaanka magaalooyinka' iyo 'Maalgashiga ilaha dabiiciga' isku khilaafi karaan?", "options": { "a": "Maalgashigu wuxuu u baahan yahay daryeel, halka fiditaanku inta badan burburiyo ilahaas dabiiciga ah", "b": "Mar walba way isla shaqeeyaan", "c": "Fiditaanku maalgashiga ayuu kordhiyaa", "d": "Khilaaf ma jiro" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxay tahay sababta cilmiyaysan ee looga hortago 'Falidda beeraha xilli aan munaasib ahayn'?", "options": { "a": "Si looga badbaadiyo carrada inay u nuglaato carra guurka iyo xarfashada", "b": "Si dadku u naxaan kaliya", "c": "Si dhirta loo baabi'iyo", "d": "Ma lahan sabab cilmi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Falanqee saamaynta 'Wasakhowga Carrada' ku leeyahay silsiladda cunnada (food chain)?", "options": { "a": "Sunta carrada waxay gashaa dhirta, ka dibna xoolaha iyo aadanaha, taas oo keenta cudurro", "b": "Carradu cunnada ma saamayso", "c": "Sunta carrada waxay kordhisaa barotiinka", "d": "Carradu si dhaqso ah ayay isku nadiifisaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxaa loola jeedaa 'Dhaqaaq tartiib ah ee ciidda' ee ku jira qeexidda xarfashada carrada?", "options": { "a": "Waa barakaca ciidda oo dhaca muddo dheer oo ay sababto dabaysha", "b": "Waa ciidda oo meel looga soo kaxaystay baabuur", "c": "Waa ciidda oo istaagtay meel", "d": "Waa ciidda oo biyo noqotay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee bay 'Seerooyinka deegaanka' u caawiyaan ilaalinta kala duwanaashiyaha noolaha?", "options": { "a": "Waxay bixiyaan hooy ammaan ah oo noolaha looga ilaaliyo howlaha aadanaha ee guracan", "b": "Waxay baabi'iyaan xayawaanka duurjoogta ah", "c": "Waxay kordhiyaan wasakhowga", "d": "Waxay daciifiyaan dhirta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Maxay tahay saamaynta mustaqbalka fog ee 'Isbeddelka Cimilada' ku leeyahay Soomaaliya?", "options": { "a": "Waxay keeni kartaa abaaraha joogto noqda iyo dabar go'a dhirta iyo xoolaha", "b": "Waxay dalka ka dhigaysaa mid qabow mar walba", "c": "Waxay kordhisaa wax soo saarka beeraha", "d": "Saameyn ma yeelan doonto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Falanqee 'Wasakhowga iyo Daryeel la’aanta' deegaanka tusaale ahaan warshadaha?", "options": { "a": "Warshaduhu waxay soo daayaan haraaga sun ah oo dila deegaanka haddii aan daryeel jirin", "b": "Warshaduhu deegaanka way nadiifiyaan", "c": "Ma jiraan warshado wasakheeya deegaanka", "d": "Daryeelku ma khuseeyo warshadaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Maxay tahay sababta loogu baahan yahay 'Tiro koobka meelaha daadadka khatarta ugu jira'?", "options": { "a": "Si loo diyaariyo tallaabooyinka ka hortagga ah ee ku habboon deegaan kasta", "b": "Si dadka looga saaro dalka oo dhan", "c": "Waa tirada dadka kaliya", "d": "Waa mashruuc lacag lumis ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Isbarbardhig dhibaatooyinka 'Xarfashada dabeysha' iyo 'Xarfashada biyaha'?", "options": { "a": "Dabeyshu waxay xarfisaa dhulka qallalan, biyuhuna waxay guuriyaan carrada xilli roobaadka", "b": "Isku mid bay yihiin xilli kasta", "c": "Dabeysha ayaa ka khatarsan biyaha mar walba", "d": "Biyaha xarfasho ma keenaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sidee bay 'Dhibaatada Deegaanka' u saamaysaa mustaqbalka 'Noolaha' dunida?", "options": { "a": "Waxay keentaa dabar go’ (extinction) iyo is-beddel ku yimaada silsiladda nolosha", "b": "Waxay ka dhigtaa noolaha kuwo ka xoog badan", "c": "Wax saameyn ah ma yeelan doonto", "d": "Nooluhu deegaan ma u baahna" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Maxaa keenaya in 'Fayrasyada cusub' ay ka dhashaan dhibaatada deegaanka?", "options": { "a": "Dheelitirka deegaanka oo xumaaday ayaa keena in fayrasyada xayawaanka u soo gudbaan aadanaha", "b": "Waa arrin ku timid nasiib kaliya", "c": "Cimilada qabow ayaa dhalisa fayrasyada", "d": "Fayrasyada deegaanka ma khuseeyaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Falanqee saamaynta 'Nabaad guurka carrada' ku leeyahay kheyraadka biyaha Soomaaliya?", "options": { "a": "Carrada guurta waxay xirtaa biyo-xireennada waxayna wasakhaysaa ilaha biyaha", "b": "Nabaad guurka wuxuu sifeeyaa biyaha", "c": "Carradu biyaha ma gaarto", "d": "Nabaad guurku wuxuu kordhiyaa roobka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Maxay tahay sababta loogu tixgeliyo 'Ilaalinta Magaalooyinka' tallaabo looga hortago daadadka?", "options": { "a": "Magaalooyinka la ilaaliyo waxay leeyihiin tubooyin nadiif ah iyo nidaam biyo-mareen oo sax ah", "b": "Sababtoo ah magaalooyinka lama gubo", "c": "Si dadku u dareemaan ammaan kaliya", "d": "Ma lahan xiriir toos ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Sidee looga faa'iideysan karaa 'Dhul beereedka' si looga badbaado daadadka?", "options": { "a": "In dhul beereedka loo naqshadeeyo sidii ay u nuugi lahaayeen biyaha xad dhaafka ah (buffer zones)", "b": "In beeraha laga saaro magaalooyinka", "c": "In beeraha laga dhigo tubooyin", "d": "Beeruhu ma nuugaan biyaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Maxay tahay sababta 'Daryeelka meelaha unugul' loogu tixgeliyo xal deegaan?", "options": { "a": "Waxay yareysaa khatarta musiibooyinka ka hor intaysan dhicin", "b": "Waa daryeelka xayawaanka kaliya", "c": "Si dhulku u quruxsado", "d": "Waa mashruuc gaaban oo kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 78, "question": "Falanqee dhibaatada 'Jarista dhirta' marka laga eego dhinaca 'Oksijiinka' hawada?", "options": { "a": "Dhirta oo la jaro waxay yaraysaa soo saarista Oksijiinka waxayna kordhisaa Kaarboon-ka", "b": "Dhirta oo la jaro Oksijiinka ayay kordhisaa", "c": "Oksijiinku dhirta ma khuseeyo", "d": "Hawada ma saameyo jarista dhirta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Sidee bay 'Habdhaqanka aadanaha ee guracan' u horseedaan xarfashada ciidda ee dhismaha?", "options": { "a": "In ciidda laga qodo meelo aan munaasib ahayn si guryo loogu dhiso, taas oo deegaanka baabi'isa", "b": "Dhismaha daaraha ayaa ciidda soo celiya", "c": "Aadanuhu ciidda ma dhaqaajiyo", "d": "Dhismaha wuxuu ka hortagaa xarfashada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 80, "question": "Maxay tahay saamaynta 'Isbeddelka Cimilada' ku leeyahay silsiladda dhaqaalaha dunida?", "options": { "a": "Waxay daciifisaa wax soo saarka, waxay kordhisaa khasaaraha musiibooyinka, waxayna xasilooni darro ku keentaa suuqyada", "b": "Waxay kordhisaa faa'iidada shirkadaha", "c": "Dhaqaalaha ma khuseeyo cimilada", "d": "Waxay yaraysaa canshuurta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Falanqee 'Wasakhowga biyaha' iyo saamaynta ay ku leedahay kheyraadka badda?", "options": { "a": "Sunta iyo bacaha waxay dilaan kalluunka iIyo dhirta badda, taas oo baabi'isa kheyraadkaas", "b": "Wasakhowga badda wuxuu nafaqeeyaa kalluunka", "c": "Badda looma wasakheyn karo gabi ahaanba", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 82, "question": "Maxay tahay sababta loogu baahan yahay 'Ka hortagga xaaluf guurka' (Soil degradation)?", "options": { "a": "Si loo ilaaliyo bacriminta dhulka iyo sugnaanta cuntada (food security)", "b": "Si dhulka looga dhigo baraf", "c": "Si xoolaha loo laayo", "d": "Ma lahan muhiimad qaran" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 83, "question": "Gunaanad ahaan, sidee buu 'Kala duwanaashiyaha noolaha' u yahay isha nolosha aadanaha?", "options": { "a": "Wuxuu bixiyaa cuntada, daawada, hawada nadiifka ah, iyo dheelitirka cimilada ee aadanuhu u baahan yahay", "b": "Aadanuhu uma baahna noole kale", "c": "Nooluhu waa khatar ku ah aadanaha kaliya", "d": "Waa qurux kaliya ee ma lahan waxtar dhab ah" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch3_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch3',
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
    
    # Remove existing geo_ch3 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch3']
    
    # Check if geo_ch3 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch3' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 3aad: Dadka iyo Deegaanka",
            "id": "geo_ch3"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch3':
                c['title'] = "Cutubka 3aad: Dadka iyo Deegaanka"
                break
    
    # Add new geo_ch3 questions
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

    # Remove existing geo_ch3 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch3']
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
