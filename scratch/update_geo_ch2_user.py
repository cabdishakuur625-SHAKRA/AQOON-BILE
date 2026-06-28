import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha 'Nololey' (Biosphere)?", "options": { "a": "Barashada xiddigaha", "b": "Dhammaan noolaha laga helo oogada sare ee dhulka", "c": "Barashada biyaha badda", "d": "Barashada dhagaxyada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Carradu waxay ka dhalataa dhagax burburay iyo isbeddello _____ ah.", "options": { "a": "Cireed", "b": "Kiimiko", "c": "Maangal", "d": "Badda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Waa maxay waxtarka ugu horreeya ee carrada u leedahay dhirta?", "options": { "a": "Inay dhirta hoos siiso", "b": "Inay xididdada dhirta dhulka ku hayso", "c": "Inay dhirta midabayso", "d": "Inay dhirta ka ilaaliso hawada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa ku bama kuwa soo socda ee ka mid ah waxyaabaha ay carrada ka kooban tahay?", "options": { "a": "Biyo iyo Hawo", "b": "Dhalada iyo Birta", "c": "Caagga iyo Dharka", "d": "Kaliya dhagaxyo" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 5, "question": "Kaymaha waxay ka baxaan meelaha laga helo?", "options": { "a": "Biyo aad u yar", "b": "Biyo badan", "c": "Baraf kaliya", "d": "Dhagaxyo kaliya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa ku bama nooca carrada ee ugu bacrinsan?", "options": { "a": "Carro gaduud", "b": "Carro madow", "c": "Carro hurdi", "d": "Carro cowlan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Maxay dhirtu soo saartaa oo lagama maarmaan u ah aadanaha?", "options": { "a": "Kaarboon laba oksaydh", "b": "Oksijiin", "c": "Nitrogen", "d": "Hydrogen" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Aadanuhu maxuu u jaraa dhirta dhulka Soomaaliya?", "options": { "a": "Si uu u beero geedo kale", "b": "Si uu dhuxul uga dhigto", "c": "Si uu u badbaadiyo xayawaanka", "d": "Si uu roob u helo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Haramuhu wuxuu ka baxaa meelaha uu ku da'o roob xaddi ahaan?", "options": { "a": "Aad u badan", "b": "Yar", "c": "Baraf ah", "d": "Ma jiro roob" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Soomaaliya waxay ka tirsan tahay gobollada dabiiciga ah ee?", "options": { "a": "Qaboobaha cirifyada", "b": "Kulaaleyda (Tropical)", "c": "Buuraleyda barafka ah", "d": "Dhex-dhexaadka qabow" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Waa maxay neefka u dhexeeya nololeyda iyo gibilka hawada?", "options": { "a": "Oksijiin kaliya", "b": "Kaarboon laba Oksaydh", "c": "Uumi", "d": "Boodh" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Maxay carrada siisaa dhirta iyo cowska?", "options": { "a": "Midab kaliya", "b": "Biyo iyo macaadinta milixda", "c": "Hoos kaliya", "d": "Dab" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Dhirta gaagaaban ee qallasha marka roobku dhammaado waxaa la yiraahdaa?", "options": { "a": "Kaymo", "b": "Caws", "c": "Haramaha", "d": "Beer" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Maxaa keena midabka gaduudan ee carrada gaduudka ah?", "options": { "a": "Biyo badan", "b": "Burburka birta (Iron oxides)", "c": "Qorraxda", "d": "Haramaha" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Sidee looga gudbi karaa jarista dhirta?", "options": { "a": "In geedka la jaray lagu beddelo mid kale", "b": "In dhulka oo dhan la simo", "c": "In aan geed dambe la arkin", "d": "In la gubo kaymaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 16, "question": "Waa ku bama kuwaan ka mid ah gobollada dabiiciga ah ee dunida?", "options": { "a": "Gobollada kulaaleyda kulul", "b": "Gobollada suuqa", "c": "Gobollada waxbarashada", "d": "Gobollada ciyaaraha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 17, "question": "Maxaa saameeya koritaanka dhirta dabiiciga ah?", "options": { "a": "Roobka iyo heerkulka", "b": "Kaliya waddooyinka", "c": "Magaalooyinka", "d": "Baabuurta" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 18, "question": "Cunnada dadka Soomaaliyeed badankeedu waxay ku tiirsan tahay?", "options": { "a": "Mashiinnada", "b": "Xoolaha (Hilib iyo Caano)", "c": "Cuntooyinka qasacadaysan", "d": "Barafka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Waa maxay waxtarka dhirta dabiiciga ah ee xagga carrada?", "options": { "a": "Waxay ilaalisaa qoyaanka carrada", "b": "Waxay carrada ka dhigtaa dhagax", "c": "Waxay kordhisaa kuleylka carrada", "d": "Carrada ayay guurisaa" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 20, "question": "Xayawaannada aan indhaha lagu arki karin waxaa loo yaqaanaa?", "options": { "a": "Ugaarsade", "b": "Il ma aragto", "c": "Cayayaan", "d": "Daaq cune" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Haddii roobku yaraado Soomaaliya, nolosha dhirta maxaa ku dhaca?", "options": { "a": "Way kobceysaa", "b": "Way abaarsaneysaa (yaraaneysaa)", "c": "Waxba kama beddelna", "d": "Way cagaarneysaa" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Maxay awood u leedahay nololeydu (Biosphere)?", "options": { "a": "Inay dhagax noqoto", "b": "Inay taranto iyo inay kobacdo", "c": "Inay hawada joojiso", "d": "Ma lahan wax awood ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Waa maxay magaca cowska meelaha dhex-dhexaadka ah?", "options": { "a": "Safaana", "b": "Istibsi", "c": "Tundura", "d": "Kaymo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 24, "question": "Falanqee xiriirka ka dhexeya noolaha iyo ma-noolaha ee nololeyda?", "options": { "a": "Way kala go'an yihiin", "b": "Way isla falgelayaan", "c": "Ma lahan wax xiriir ah", "d": "Isma arki karaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Sidee bay carrada u abuurtaa jawi ku habboon dhirta?", "options": { "a": "Ayadoo burburisa dhagaxyada oo isbeddello kiimiko ku dhacaan", "b": "Ayadoo biyaha oo dhan nuugta", "c": "Ayadoo iska fogaysa walxaha orgaaniga ah", "d": "Kaliya ayadoo qorraxda iska celisa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 26, "question": "Waa maxay kaalinta aadanaha ee hagaajinta dhulka?", "options": { "a": "Hagaajinta dhul-beereedka iyo dhismaha", "b": "Jarista dhirta kaliya", "c": "Inuu xayawaanka laayo kaliya", "d": "Dhismaha waddooyinka aan loo baahnayn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 27, "question": "Muxuu kaga duwan yahay Gobolka Kulaaleyda gobollada Qabow?", "options": { "a": "Heerkulka oo sarreeya iyo roob badan", "b": "Baraf joogto ah", "c": "Dhir la'aan", "d": "In aanay qorraxdu ka soo bixin" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 28, "question": "Waa maxay saameynta kala sarreynta dhulka (altitude) ku leedahay dhirta?", "options": { "a": "Markasta oo uuw kordho janjeerka dhulka, waxaa yaraanaya dhirta", "b": "Dhulka janjeera dhirta ayaa ku badan", "c": "Wax saamayn ah ma lahan", "d": "Waxay kordhisaa cufnaanta kaymaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Maxaa keena in xayawaanada dalka ay haajiraan (ka guuraan)?", "options": { "a": "Dagaalada iyo laynta xayawaanka", "b": "Biyo badan", "c": "Dhirta oo badata", "d": "Heerkulka oo hoos u dhaca" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Waa maxay 'Huyuumas' (Humus) oo carrada ku jira?", "options": { "a": "Waa walxaha orgaaniga ah (dhirta iyo xayawaanka qudhuntay)", "b": "Waa dhagaxyo yaryar", "c": "Waa bac kaliya", "d": "Waa birta carrada ku jirta" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Gobolka Badhaalaha (Equatorial), goormay roobabku aad u kordhaan?", "options": { "a": "Guga iyo Dayrta", "b": "Jiilaalka kaliya", "c": "Xagaaga kaliya", "d": "Ma jiro roob kordha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Maxay tahay kaalinta aadanaha ee hagaajinta dhulka?", "options": { "a": "Hagaajinta dhul-beereedka iyo dhismaha", "b": "Jarista dhirta kaliya", "c": "Inuu xayawaanka laayo kaliya", "d": "Dhismaha waddooyinka aan loo baahnayn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sidee bay dhirtu u yareeysaa xaalufka (erosion)?", "options": { "a": "Ayadoo dhulka xididdada ku haysa", "b": "Ayadoo hawada joojisa", "c": "Ayadoo biyaha soo saarta", "d": "Ayadoo dhagaxyada burburisa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Xaggee buu fidsan yahay Gobolka Kulaaleyda (Tropical)?", "options": { "a": "5-23.5 Digrii Waqooyiga iyo Koonfurta dhul baraha", "b": "90 Digrii Waqooyiga", "c": "40-50 Digrii Koonfurta", "d": "Kaliya bartamaha badda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Muxuu 'Barootiinka xoolaha' muhiim ugu yahay dadka?", "options": { "a": "Wuxuu lagama maarmaan u yahay cunto kasto oo dheeli tiran", "b": "Waa cunto aan la cunin", "c": "Waa mid waxyeello leh", "d": "Ma lahan wax nafaqo ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxaa loola jeedaa 'Tuulimaadka' carrada?", "options": { "a": "Dhisidda carrada meelaha cusub", "b": "Burburinta carrada", "c": "Gubista carrada", "d": "Ma lahan wax micno ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Waa maxay farqiga u dhexeeya 'Daaq cune' iyo 'Ugaarsade'?", "options": { "a": "Daaq cunaha wuxuu cunaa dhir, ugaarsaduhuna hilib", "b": "Ugaarsaduhu dhir buu cunaa", "c": "Iska mid bay yihiin", "d": "Daaq cunaha waa il ma aragto" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxay tahay sababta dhirta teel-teelka ah ugu baxdo meelaha qaarkood Soomaaliya?", "options": { "a": "Sababtoo ah roobka oo ku yar", "b": "Sababtoo ah dadka oo badan", "c": "Sababtoo ah carrada oo madow", "d": "Sababtoo ah xayawaanka oo la laayay" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Sidee buu Iftiinku u saameeyaa dhirta?", "options": { "a": "Wuxuu lagama maarmaan u yahay koritaanka (photosynthesis)", "b": "Wuxuu gubaa dhirta oo dhan", "c": "Wax saamayn ah ma lahan", "d": "Wuxuu carrada ka dhigaa mid gaduudan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxaa dhaca marka uu dhammaado xilli roobaadka meelaha cawsku ka baxo?", "options": { "a": "Cawsku wuu qallalaa", "b": "Cawsku wuu sii kordhaa", "c": "Cawsku wuxuu isku beddelaa kaymo", "d": "Ma jiro wax dhaca" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Maxay tahay caqabadda ugu weyn ee haysata xayawaanka Soomaaliya?", "options": { "a": "Daryeel la'aan iyo xaalufinta keymaha", "b": "Biyo badan oo dalka qarqiyay awgeed", "c": "Dhirta oo aad u badan", "d": "Cunto badan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Waa maxay faa'iidada 'Macaadinta milixda' ee carrada ku jirta?", "options": { "a": "Waa quudka ama cuntada dhirta", "b": "Waxay dishaa dhirta", "c": "Waxay beddeshaa midabka badda", "d": "Ma lahan wax faa'iido ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Waa ku bama kuwaan midka saameeya filiqsanaanta xayawaanka?", "options": { "a": "Cimilada iyo dhirta dabiiciga ah", "b": "Muraayadaha", "c": "Ciyaaraha", "d": "Dharka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 44, "question": "Muxuu qofku u isticmaali lahaa qalab kale oo wax lagu karsado halkii dhuxusha?", "options": { "a": "Si looga badbaado jarista dhirta iyo xaalufka", "b": "Sababtoo ah dhuxushu waa qaali kaliya", "c": "Si uusan roob u di'in", "d": "Waxba kama beddelayso deegaanka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Noocyada carrada, keebaa badanaa ku badan burburka birta?", "options": { "a": "Carro gaduud", "b": "Carro madow", "c": "Carro madow", "d": "Carro beer" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 46, "question": "Waa maxay 'Gibilka Nololeyda' (Biosphere shell)?", "options": { "a": "Waa meesha ay isugu yimaadaan carrada, dhirta, iyo aadanaha", "b": "Waa badda hoosteeda kaliya", "c": "Waa hawada sare kaliya", "d": "Waa qeyb ka mid ah qorraxda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 47, "question": "Xilliga jiilaalka, gobollada qabow roobku qaabkee buu u da'aa?", "options": { "a": "Baraf ahaan", "b": "Uumi ahaan", "c": "Dhibic yar", "d": "Ma da'o" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 48, "question": "Muxuu 'Cilmiga Nololeyda' muhiim u yahay?", "options": { "a": "Si loo fahmo xiriirka ka dhexeeya noolaha iyo deegaanka", "b": "Si loo barto baabuurta", "c": "Si loo ogaado taariikhda qadiimiga ah kaliya", "d": "Si loo gubo dhirta" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 49, "question": "Carra guurku ma qeyb ka yahay sameysanka carrada?", "options": { "a": "Haa, waa qeyb muhiim ah", "b": "Maya, waa dhibaato kaliya", "c": "Ma lahan wax xiriir ah", "d": "Waa wax dhaca habeenkii kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 50, "question": "Falanqee is-beddelka ku dhaca neefka Kaarboon laba Oksaydh ee u dhexeeya nololeyda iyo hawada?", "options": { "a": "Waa meerto nolosha ah oo dhirtu nuugto neefkaas aadanuhuna soo daayo", "b": "Waa neef aan wax saameyn ah ku lahayn nolosha", "c": "Waa neef dhirtu ay soo saarto kaliya", "d": "Ma jiro wax xiriir ah oo ka dhexeeya labadooda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Maxay tahay sababta cilmiyaysan ee loogu tixgeliyo carrada inay tahay 'Noolaha iyo Ma-noolaha' falgalalkooda?", "options": { "a": "Sababtoo ah waxay isku darsataa macaadinta (ma-noolaha) iyo orgaanikada (noolaha)", "b": "Sababtoo ah waa dhagax kaliya", "c": "Sababtoo ah biyo ma lahan", "d": "Sababtoo ah aadanaha ayaa sameeyay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Sidee bay 'Daaqista xad-dhaafka ah' u horseedi kartaa abaaraha iyo biyo yarida?", "options": { "a": "Waxay baabi'isaa lakabka dhirta ee carrada haysa iyo qoyaanka", "b": "Waxay keentaa roob badan", "c": "Xoolaha ayaa biyaha cabba dhamaantood", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Dibu-milicsiga nolosha dhirta Soomaaliya, sidee buu roobku u go'aamiyaa filiqsanaanta dhirta?", "options": { "a": "Xaddiga roobka ayaa go'aamiya cufnaanta ama teel-teelka dhirta", "b": "Dhirtu waxay baxdaa iyadoo aan roob u baahnayn", "c": "Dhirtu waxay u guurtaa meelaha qabow", "d": "Roobku wuxuu dilaa dhirta dabiiciga ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Isbarbardhig astaamaha gobollada qaboobaha dhex-dhexaadka ah iyo gobollada qaboobaha cirifyada?", "options": { "a": "Cirifyada waa baraf joogto ah halka dhex-dhexaadku leeyahay xilliyo is-beddela", "b": "Ma lahan wax farqi ah", "c": "Dhex-dhexaadka ayaa ka qabow cirifyada", "d": "Cirifyada ayaa leh dhir badan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Muxuu yahay xiriirka ka dhexeeya heerkulka/iftiinka iyo kala duwanaanshaha dhirta cirifyada iyo kulaaleyda?", "options": { "a": "Kulaaleyda iftiinka badan wuxuu keenaa dhir cufan, cirifyada iftiinka yar wuxuu xaddidaa koritaanka", "b": "Cirifyada ayaa ka dhir badan kulaaleyda", "c": "Iftiinku waxba kama beddelo dhirta", "d": "Iftiinka cirifyada ayaa aad u kulul" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Falanqee dhibaatada 'Gubashada Kaymaha' marka loo eego isbeddelka cimilada?", "options": { "a": "Waxay kordhisaa kuleylka iyo Kaarboon-ka hawada, waxayna baabi'isaa deegaanka", "b": "Waxay kordhisaa roobka", "c": "Waxay faa'iido u tahay xayawaanka", "d": "Waxay carrada ka dhigtaa mid nafaqo badan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sidee bay 'Kala sarreynta dhulka' u go'aamisaa nooca xayawaanka ku noolaan kara gobol?", "options": { "a": "Altitude-ka wuxuu saameeyaa heerkulka iyo dhirta, taas oo xaddidda nooca xayawaanka", "b": "Xayawaannada oo dhan waxay door bidaan buuraha", "c": "Ma lahan wax saameyn ah", "d": "Buuraleyda ma laha xayawaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Maxay tahay sababta loogu tixgeliyo carrada Soomaaliya inay halis ugu jirto 'Carro Burbur'?", "options": { "a": "Dhir la'aanta iyo jarista dhirta oo kordhisa saamaynta dabaysha iyo biyaha", "b": "Biyo badan oo dalka qarqiyay awgeed", "c": "Sababtoo ah dhulku waa siman yahay kaliya", "d": "Sababtoo ah qorraxdu ma jirto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Falanqee waxtarka barootiinka xoolaha ee 'Cunno dheeli tiran'?", "options": { "a": "Waa aasaaska dhismaha jirka iyo caafimaadka bulshada Soomaaliyeed", "b": "Waa cunto aan waxtar badan lahayn", "c": "Waxay keentaa xanuuno kaliya", "d": "Waa mid si fudud loogu beddeli karo haramaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Muxuu yahay micnaha 'Gibilka nololeyda waxa lagu yaqaanaa kala duwanaanshaha waxa uuw ka kooban yahay'?", "options": { "a": "In deegaan kastaa leeyahay noole iyo ma-noole gaar u ah oo isku xiran", "b": "In gobollada oo dhan isku mid yihiin", "c": "In hawada kaliya laga darsado", "d": "In nooluhu uusan u baahnayn ma-noole" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Markaad eegto 'Daaqista xad-dhaafka ah', sidee loogu xallin karaa hab cilmiyeed?", "options": { "a": "In la sameeyo meerto daaq (rotational grazing) iyo in la ilaaliyo bedka dhirta", "b": "In xoolaha oo dhan la gado", "c": "In dhulka laga sifeeyo dhirta", "d": "In xayawaanka loo soo raro magaalooyinka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Waa maxay saamaynta ay 'Ballaarinta dhul beereedka' ku leedahay dheelitirka deegaanka?", "options": { "a": "Waxay yareysaa bedka dhirta dabiiciga ah iyo hooyga xayawaanka", "b": "Waxay kordhisaa tirada kaymaha", "c": "Waxay haysaa qoyaanka carrada", "d": "Waxay joojisaa abaaraha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Maxay 'Iron oxides' muhiim ugu yihiin barashada taariikhda carrada?", "options": { "a": "Waxay muujinayaan heerka burburka birta iyo nidaamka kiimiko ee carrada", "b": "Waxay sheegaan meesha dahabku ku jiro", "c": "Waxay carrada ka dhigaan mid aan biyo nuugin", "d": "Ma lahan wax micno ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Falanqee 'Daryeel la'aanta haysata dhirta' ee Soomaaliya xilligan?", "options": { "a": "Ma jirto qorshe qaran oo lagu badbaadinayo ama lagu abuurayo kaymo cusub", "b": "Dhirta oo dhan ayaa la waraabiyaa maalin walba", "c": "Xayawaanka ayaa daryeela dhirta", "d": "Dhirta looma baahna daryeel" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sidee bay 'Isbeddelada xun ee deegaanka' u saameeyaan socdaalka xayawaanka (migration)?", "options": { "a": "Waxay ku qasbaan inay u raadsadaan meelo biyo iyo daaq leh, taasoo halis gelin karta noloshooda", "b": "Waxay ka dhigaan kuwo aan dhaqaaqin", "c": "Waxay kordhiyaan dhalashada xayawaanka", "d": "Waxay ka dhigaan kuwo aan u baahnayn biyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxay tahay sababta loogu tilmaamay kaymaha 'Qeybta ugu muhiimsan qeybaha dhirta'?", "options": { "a": "Sababtoo ah waa isha ugu weyn ee oksijiinka, hooyga xayawaanka, iyo nidaaminta cimilada", "b": "Sababtoo ah waa meel lagu dhuunto kaliya", "c": "Sababtoo ah ma lahan harame", "d": "Sababtoo ah biyaha ayay iska celiyaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee bay 'Isbeddellada kiimiko' ee carrada ugu duwan yihiin 'Dhagax burburka' jirka ah?", "options": { "a": "Kiimikadu waxay beddeshaa guryaha walaxda, halka burburku yahay is-beddel dhinac qaabka ah", "b": "Is-isku mid bay yihiin", "c": "Kiimikada ayaa ka horreysa mar walba", "d": "Dhagax burburka ayaa ka muhiimsan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Muxuu yahay doorka 'Nitrogen-ka' ama macaadinta milixda ee ay carrada siiso dhirta?", "options": { "a": "Waa aasaaska koritaanka unugyada dhirta iyo soo saarista miraha", "b": "Waxay ka dhigtaa dhirta mid qallalan", "c": "Waxay hor istaagtaa koritaanka", "d": "Ma lahan wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Falanqee 'Gobollada Buuraleyda' xagga kala duwanaanshaha dhirta iyo xayawaanka?", "options": { "a": "Waxay leeyihiin kala duwanaansho toosan (vertical zonation) oo ku xiran joogga sare", "b": "Isku mid bay yihiin meel kasta", "c": "Ma lahan wax dhir ah", "d": "Buuraha oo dhan waa baraf" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Sidee looga hortagi karaa 'Xaalufinta keymaha' ee Soomaaliya si dhab ah?", "options": { "a": "Xoojinta shuruucda deegaanka iyo wacyigelinta bulshada ee tamarta beddelka ah", "b": "Jarista dhammaan dhirta haray", "c": "U raridda dadka meelaha kale", "d": "In laga aamuso dhibaatada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Maxay tahay sababta dhagaxa dhoobada ah ee waagii Kinozoi (cutubkii 1aad) uu xiriir ula leeyahay carrada maanta?", "options": { "a": "Waa aasaaska ay ka dhashaan qaar ka mid ah noocyada carrada dhoobada ah ee maanta", "b": "Ma lahan wax xiriir ah", "c": "Waa dhagax dhowaan dhashay", "d": "Carradu waxay ka dhalataa hawada kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Is-falgelinta noolaha iyo ma-noolaha, sidee bay u saamaysaa bacriminta carrada?", "options": { "a": "Noolaha dhintay ee qudhuntay (ma-noole noqday) ayaa nafaqeeya carrada", "b": "Wax saamayn ah ma lahan", "c": "Ma-noolaha ayaa dila noolaha mar walba", "d": "Nooluhu carrada ayuu wada cunaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Maxay tahay sababta 'Oksijiinka' loogu tixgeliyo inuu yahay wax soo saar dhirta?", "options": { "a": "Sababtoo ah dhirtu waxay ka soo saartaa hannaanka photosynthesis", "b": "Sababtoo ah dhirtu waxay ka neefsataa hawada", "c": "Sababtoo ah aadanaha ayaa u dhiiba", "d": "Oksijiinku dhulka ayuu ka yimaadaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Falanqee 'Gobolka Dhex-dhexaadka ah' (Temperate) iyo cowska Istibsi?", "options": { "a": "Waa deegaan cimiladiisu dhex-dhexaad tahay oo ku habboon cowska nafaqada leh", "b": "Waa meel aad u kulul", "c": "Waa meel aanay dhirtu ka bixi karin", "d": "Cimiladu waa baraf joogto ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Sidee bay 'Waddo jeexidda' iyo 'Macdan qodashada' u saameeyaan nololeyda?", "options": { "a": "Waxay keenaan go'idda iyo kala qeybinta deegaanka dabiiciga ah", "b": "Waxay kordhiyaan dhirta", "c": "Waxay badbaadiyaan xayawaanka", "d": "Wax saameyn ah kuma lahan carrada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Muxuu yahay gunaanadka 'Cilmiga Nololeyda' ee mustaqbalka aadanaha?", "options": { "a": "In badbaadada aadanaha ay ku xiran tahay ilaalinta dheelitirka nololeyda iyo deegaanka", "b": "In aadanuhu iska noolaan karo isagoo deegaanka gubaya", "c": "In dhirtu aysan muhiim ahayn mustaqbalka", "d": "In xayawaanka oo dhan la baabi'iyo si magaalooyin loo dhisno" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Maxay tahay ujeeddada 'Isbeddellada diinaamikada' ee dhulka (Biosphere context)?", "options": { "a": "Waa dhaqdhaqaaqa iyo is-beddellada joogtada ah ee saameeya dhammaan nolosha", "b": "Waa dhulka oo aan dhaqaaqin", "c": "Waa biyaha badda oo qalala", "d": "Waa hawada oo istaagta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 78, "question": "Sidee bay 'Uumi-baxa' iyo roobka uga qayb qaataan nolosha dhirta Soomaaliya?", "options": { "a": "Waxay xukumaan qoyaanka iyo helitaanka biyaha ee dhirta dabiiciga ah", "b": "Waxay dilaan dhirta kulul", "c": "Ma lahan wax saameyn ah", "d": "Uumi-baxu wuxuu abuuraa dhagaxyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Maxay tahay sababta loogu baahan yahay 'Cunno dheeli tiran' oo barootiin leh xilliyada abaaraha?", "options": { "a": "Si kor loogu qaado difaaca jirka iyo badbaadada dadka tabaalaysan", "b": "Ma lahan wax muhiimad ah", "c": "Si xoolaha loo badbaadiyo kaliya", "d": "Si carrada loo nafaqeeyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 80, "question": "Falanqee saamaynta 'Abaaraha soo laalaabtay' ku leeyihiin dhirta 'Haramaha'?", "options": { "a": "Xataa haramaha way adkaysan waayaan haddii abaartu dheeraato, taas oo keenta xaaluf guud", "b": "Haramaha way ka dhashaan abaaraha", "c": "Haramaha waxay u baahan yihiin biyo badan", "d": "Abaaruhu waxay kordhiyaan kaymaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Sidee bay 'Il ma aragto' (microorganisms) uga qay qaataan bacriminta carrada?", "options": { "a": "Waxay burburiyaan walxaha orgaaniga ah iyagoo u beddelaya nafaqo dhirtu nuugi karto", "b": "Waxay dilaan dhirta", "c": "Waxay carrada ka dhigaan dhagax", "d": "Waxay cabbaan biyaha carrada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 82, "question": "Muxuu yahay xiriirka u dhexeeya 'Gubashada kaymaha' iyo yarayska roobka?", "options": { "a": "Kaymaha oo la gubo waxay yareeyaan uumiga (transpiration), taas oo yaraysa roobka", "b": "Gubashadu roob ayay keentaa", "c": "Ma lahan wax xiriir ah", "d": "Roobku wuxuu ka yimaadaa dhagaxyada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 83, "question": "Maxay tahay sababta loogu tixgeliyo 'Nololeyda' inay tahay gibil aad u khafiif ah oo dhulka ku hareeraysan?", "options": { "a": "Sababtoo ah nolosha kaliya waxay ka jirtaa dhowr kiiloomitir oo kor iyo hoos ah", "b": "Sababtoo ah waa mid aad u weyn", "c": "Sababtoo ah meel kasta oo dhulka ah nolol ayaa ka jirta", "d": "Sababtoo ah waa mid adag sida birta" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch2_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch2',
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
    
    # Remove existing geo_ch2 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch2']
    
    # Check if geo_ch2 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch2' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 2aad: Nololeyda iyo Deegaanka",
            "id": "geo_ch2"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch2':
                c['title'] = "Cutubka 2aad: Nololeyda iyo Deegaanka"
                break
    
    # Add new geo_ch2 questions
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

    # Remove existing geo_ch2 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch2']
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
