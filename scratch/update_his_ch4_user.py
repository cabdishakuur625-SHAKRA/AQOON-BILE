import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Halkee ayuu ku dhashay halyeyga Cumar Mukhtaar?", "options": { "a": "Bingazi", "b": "Janzuur (Bariga Liibiya)", "c": "Tripoli", "d": "Kafra" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Sanadkee ayuu dhashay Cumar Mukhtaar?", "options": { "a": "1911", "b": "1862", "c": "1931", "d": "1900" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Waa ku weeye labadii qof ee midoobay si ay u jabiyaan ciidankii Ingiriiska ee Suudaan?", "options": { "a": "Cumar Mukhtaar iyo Axmed Shariif", "b": "Cabdullaahi bin Xaamid iyo Cusmaan", "c": "Nelson Mandela iyo Thabo Mbeki", "d": "Sheekh Saadaat iyo Cumar Makram" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa maxay magaca garabka ciidanka ee ururka ANC uu sameystay 1961?", "options": { "a": "Warankii Ummadda", "b": "Kacdoonka Azhar", "c": "Sanuuniyiinta", "d": "Halganka Koonfur Afrika" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 5, "question": "Goormee ayaa la daldalay Cumar Mukhtaar (Dagaalkii u dambeeyay)?", "options": { "a": "16 May 1913", "b": "11 Sebtembar 1931", "c": "20 Maarso 1800", "d": "8 Jannaayo 1912" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Immisa qof ayaa isugu yimid Masjidka Azhar kacdoonkii Qaahira?", "options": { "a": "5,000 qof", "b": "15,000 qof", "c": "50,000 qof", "d": "1,000 qof" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Waa kuma hogaamiyihii ugu horreeyay ee garabka ciidanka ANC?", "options": { "a": "Thabo Mbeki", "b": "Nelson Mandela", "c": "FW de Klerk", "d": "Jacob Zuma" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay ujeeddada ugu weyn ee dhaqdhaqaaqa Koonfur Afrika?", "options": { "a": "In dalka la iibiyo", "b": "Ka hortagga midab takoorka (Apartheid)", "c": "In la caawiyo Ingiriiska", "d": "In la qabsado Jaad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Yaa madax u ahaa kacdoonkii ka dhanka ahaa Faransiiska ee Masar?", "options": { "a": "Cumar Makram", "b": "Sheekh Saadaat", "c": "Axmed Maxruuqi", "d": "Suleymaan Xalabi" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Immisa sano ayuu socday dagaalkii u dhexeeyay Talyaaniga iyo Cumar Mukhtaar?", "options": { "a": "10 sano", "b": "20 sano", "c": "30 sano", "d": "5 sano" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Sanadkee ayaa la asaasay ururka ANC ee Koonfur Afrika?", "options": { "a": "1948", "b": "1912", "c": "1961", "d": "1994" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa kuma ardaygii Azhar ee dilay Janaraalkii Faransiiska Kiliibar?", "options": { "a": "Maxamed Cabdullahi", "b": "Suleymaan Xalabi", "c": "Saciid Cabdulqaadir", "d": "Axmed Waali" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Waa maxay sababta dhalisay dhaqdhaqaaqa Mahdiga ee Suudaan?", "options": { "a": "In la raaco Talyaaniga", "b": "La dagaalanka gumeysiga Ingiriiska", "c": "In la midoobo Faransiiska", "d": "Dhismaha warshado" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Qabiilkee ayuu Cumar Mukhtaar ka aruuriyay kunka (1,000) dagaalyahan markii hore?", "options": { "a": "Biniin", "b": "Cubayd", "c": "Sanuuniyiin", "d": "Qusuur" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Magaaladee ayuu Cumar Mukhtaar ka bilaabay abaabulka ciidanka markii uu soo laabtay?", "options": { "a": "Bingazi", "b": "Zaawiyata Qusuur", "c": "Kafra", "d": "Tripoli" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Waa maxay go'aanka dhabta ah ee Cumar Mukhtaar marka uu cadawga la hadlayo?", "options": { "a": "Waan is dhiibaynaa", "b": "Waan guuleysanaynaa ama waan dhimanaynaa", "c": "Nabad ayaan rabaa", "d": "Lacag na siiya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Muxuu Faransiisku ku sameeyay Masjidka Azhar markii uu galay ciidankoodu?", "options": { "a": "Way qurxiyeen", "b": "Way boobeen kutubadii, masaaxiftiina way ku tumanadeen", "c": "Way xireen oo keliya", "d": "Waxba kama ay samayn" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Waa maxay sababta dhalisay dhaqdhaqaaqa Cumar Mukhtaar?", "options": { "a": "Inuu ganacsi bilaabo", "b": "Soo gelitaankii Talyaaniga ee dalka Liibiya", "c": "Inuu aado Jaad", "d": "Inuu la dagaalamo Faransiiska Masar" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Waa ku weeye labada qof ee dhiiri-gelinayay dadka kacdoonka Masar?", "options": { "a": "Kaliibar iyo Diibwii", "b": "Cumar Makram iyo Axmed Maxruuqi", "c": "Suleymaan Xalabi iyo asxaabtiisa", "d": "Cabdullaahi bin Xaamid iyo Cusmaan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Taariikhdee ayay dhacday dhimashadii Janaraalkii Qaahira ee Diibwii?", "options": { "a": "Kacdoonkii 1aad ee Qaahira", "b": "Dagaalkii 1931", "c": "Dhalashadii ANC", "d": "Kacdoonkii Koonfur Afrika" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 21, "question": "Dagaalkee ayuu Cumar Mukhtaar ku jiray intii u dhaxeysay 1913-1915?", "options": { "a": "Dagaalkii Faransiiska", "b": "Dagaalkii Talyaaniga", "c": "Dagaalkii Ingiriiska", "d": "Dagaalkii Jaad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Waa maxay magaca Golaha waddaniga ee Koonfur Afrika markii la asaasay?", "options": { "a": "ANC", "b": "Warankii Ummadda", "c": "Kacdoonka Madoowga", "d": "Golaha Xuquuqda" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 23, "question": "Goormee ayuu bilowday halgankii Cumar Mukhtaar ee Bingazi?", "options": { "a": "1900", "b": "1911", "c": "1915", "d": "1862" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 24, "question": "Waa maxay xaaladda siyaasadeed ee gumeysiga Faransiisku ka tagay Masar?", "options": { "a": "Xurriyad la'aan iyo dagaalo badan", "b": "Nabad iyo barwaaqo", "c": "Midab takoor", "d": "Hantigoosi" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 25, "question": "Muxuu Cumar Mukhtaar ku sheegay inuu ka xoog badan yahay hubka cadawga?", "options": { "a": "Maalka", "b": "Iimaanka", "c": "Ciidanka badan", "d": "Caawinaada dibadda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 26, "question": "Maxaa xiriir ah oo ka dhexeeya cilmiga iyo ilaalinta dalka sida uu qabo cutubkan?", "options": { "a": "Cilmigu wuxuu keenaa lacag badan", "b": "In dadku bartaan xuquuqdooda, taasna ay dhaliso ilaalinta dalka", "c": "Cilmigu wuxuu dadka ka dhigaa fulayaal", "d": "Cilmigu ma laha wax xiriir ah oo ku saabsan dalka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Sharax doorkii uu Suleymaan Xalabi ka qaatay halgankii Azhar?", "options": { "a": "Wuxuu ahaa madaxa culimada", "b": "Wuxuu ahaa arday dilay hoggaamiyihii Faransiiska ee Kiliibar", "c": "Wuxuu hagi jiray ciidanka Suudaan", "d": "Wuxuu keenay kutubada Masjidka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Muxuu Cumar Mukhtaar ula jeeday markuu yiri 'Nolosheeydu waxay ka dheertahay midka i daldalaya'?", "options": { "a": "Inuu noolaan doono boqol sano kale", "b": "In fikirkiisa iyo halgankiisu ay jiri doonaan geeridiisa ka dib", "c": "Inuu ka da' weyn yahay ninka daldalaya", "d": "Inuu ka baxsan doono daldalaadda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Waa maxay farqiga u dhexeeya 'dulmiga' iyo 'dembiga' sida uu sheegay Cumar Mukhtaar?", "options": { "a": "Dulmigu wuxuu qofka ka dhigaa halyeey, dembiguna wuxuu qofka ka dhigaa fulay wadnihiisu gariirayo", "b": "Dulmigu waa wanaagsan yahay, dembiguna waa xun yahay", "c": "Dulmigu wuxuu keenaa lacag, dembiguna wuxuu keenaa xabsi", "d": "Ma jiro wax farqi ah oo u dhaxeeya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Maxay ahayd saameyntii Janaraal Kaliibar uu kala kulmay kacdoonkii 2aad ee Qaahira?", "options": { "a": "Wuxuu dareemay guul weyn", "b": "Wuxuu ka niyad-jabay joogitaanka Qaahira", "c": "Wuxuu go'aansaday inuu dalkaas dego", "d": "Wuxuu noqday madaxweynaha Masar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Sidee bay 'midoobidda' u keentay guusha Mahdiga ee Suudaan?", "options": { "a": "Waxay keentay in hub badan la helo", "b": "Midnimadii hoggaamiyaasha (bin Xaamid iyo Cusmaan) ayaa dhalisay in laga guuleysto Ingiriiska", "c": "Waxay keentay in Ingiriisku iska baxo isaga oo aan lala dagaalamin", "d": "Waxay keentay in Ruushka laga helo ciidan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Maxay ahayd sababta ururka ANC loogu tilmaamay urur 'Afrikaan ah' oo guuleystay?", "options": { "a": "Sababtoo ah waxay haysteen lacag badan", "b": "Sababtoo ah dhabar-adaygga hoggaamiyaasha iyo xubnaha madowga ah ee midaysnaa", "c": "Sababtoo ah Talyaaniga ayaa caawiyay", "d": "Sababtoo ah waxay ahaayeen dad aqoon yar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Fasir macnaha 'Warankii Ummadda' ee uu sameeyay ANC 1961?", "options": { "a": "Waa urur waxbarasho", "b": "Waa garab militari oo loogu talagalay in lagu difaaco xuquuqda madowga", "c": "Waa magaca lacagta Koonfur Afrika", "d": "Waa goob caafimaad" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay ahayd ujeeddada Cumar Mukhtaar ee ka dhigashada Saldhigga Biniin?", "options": { "a": "Inuu halkaas ku nasto", "b": "Inuu si joogta ah kaga duulo (weeraro) Talyaaniga", "c": "Inuu halkaas beer ku sameysto", "d": "Inuu kula kulmo Faransiiska" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Maxaa lagu sifeeyay dhacdooyinkii dhaqdhaqaaqa Mahdiga ee Suudaan?", "options": { "a": "Kacdoonadii ugu caansanaa taariikhda Suudaan iyo Afrika", "b": "Kacdoon yar oo aan waxba beddelin", "c": "Dagaal qabiil oo ka dhacay Suudaan", "d": "Ma jirin wax dhaqdhaqaaq ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Muxuu ahaa xiriirka ka dhexeeya ardayda reer Gaza iyo Suleymaan Xalabi?", "options": { "a": "Waxay ahaayeen ganacsato", "b": "Waxay ahaayeen ardaydii Azhar ee ka qayb qaatay halgankii ka dhanka ahaa Faransiiska", "c": "Waxay ahaayeen macalimiin Talyaani ah", "d": "Ma jirin wax xiriir ah oo ka dhaxeeyay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Muxuu Cumar Mukhtaar ka yiri iimaanka qofka xorta ah?", "options": { "a": "In iimaanku yahay mid daciif ah", "b": "In iimaanka qofka xaq u leh inuu dalkiisa si xor ah ugu noolaado uu ka xoog badan yahay hubka", "c": "In hubka uu ka muhiimsan yahay iimaanka", "d": "Inaan la dagaalamin" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Saameynta gumeysigu ku yeeshay dadka reer Masar ee cutubkan lagu xusay waa maxay?", "options": { "a": "Gudubyo iyo dhibaatooyin kala duwan oo loo gaystay shacabka", "b": "Inay ka dhigeen kuwa ugu qanisan aduunka", "c": "Inay u dhis canshuur dhaaf", "d": "Ma jirin wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Muxuu Cumar Mukhtaar aaminsanaa inuu yahay xukunka dhabta ah?", "options": { "a": "Xukunka Talyaaniga", "b": "Xukunka Eebbe (Illaahay)", "c": "Xukunka isaga u gaarka ah", "d": "Xukunka dhalanteedka ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxay ahayd sababtii Cumar Mukhtaar uu degdeg ugu soo laabtay Bingazi markuu maqlay Talyaaniga?", "options": { "a": "Inuu dalka ka cararo", "b": "Inuu abaabulo ciidan difaaca dalka", "c": "Inuu Talyaaniga soo dhoweeyo", "d": "Inuu kula kulmo reerkiisa" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Muxuu ANC u adeegsaday kontomeeyadii qarnigii 20aad?", "options": { "a": "Qaabab dhawr ah oo lagu hirgelinayo halgankooda waddaninimo", "b": "Inay dalka oo dhan gubaan", "c": "Inay dalka u dhiibaan Ingiriiska", "d": "Waxba ma ay samayn" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Muxuu Cumar Mukhtaar kaga duwanaa shakhsiyaadka kale ee taariikhda Liibiya?", "options": { "a": "Wuxuu dhashay xilli dambe", "b": "Wuxuu ahaa shakhsi taariikhda galay oo ka dhex muuqday dadkiisa, isagoo u istaagay la dagaalanka gumeystaha", "c": "Wuxuu ahaa qof Talyaaniga raacay", "d": "Ma jirin wax uu kaga duwanaa" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 43, "question": "Maxaa dhashay markii ay dadka reer Masar arkeen Janaraal Diibwii iyo ciidankiisa?", "options": { "a": "Way u sacabiyeen", "b": "Waxay ku qaadeen weerar, wayna dileen isaga iyo ciidankiisii", "c": "Way ka carareen Qaahira", "d": "Waxay codsadeen nabad" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Xagga bulshada, maxaa ka dhashay gumeysigii Faransiiska ee Masar?", "options": { "a": "Kacdoono badan oo gumeysi-diid ah iyo in in badan oo reer Masar ah naftooda waayeen", "b": "In dadku midoobaan oo ay faraxshaan", "c": "In qof kastaa helo guri bilaash ah", "d": "Ma jirin wax isbeddel bulsho ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Waa maxay dardaarankii Cumar Mukhtaar ee ku saabsanaa jiilka soo socda?", "options": { "a": "Inay nabad la galaan cadawga", "b": "Inay la dagaalami doonaan cadawga illaa ay ka xoroobaan", "c": "Inay dalka isaga baxaan", "d": "Inay gumeysiga raacaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxaa xiriir ah oo ka dhexeeya iimaanka iyo guusha halganka?", "options": { "a": "Iimaanku wuxuu yareeyaa baqdinta, wuxuuna qofka ka dhigaa mid ku kalsoon xaqa uu u leeyahay xornimada", "b": "Iimaanku wuxuu daciifiyaa xoogga ciidanka", "c": "Iimaanku waa dhalanteed", "d": "Iimaanku wuxuu keenaa hubka ugu casrisan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 47, "question": "Falanqee sida ay u kala duwanyihiin natiijada 'dulmiga' ee labada dhinac: qofka la dulmiyay iyo dembiilaha?", "options": { "a": "Qofka la dulmiyay wuxuu noqdaa halyeey, dembiiluhuna wuxuu noqdaa fulay wadnihiisu gariirayo", "b": "Labada dhinacba waxay noqdaan fulayaal", "c": "Dembiilaha ayaa guuleysta had iyo jeer", "d": "Dulmigu ma laha wax natiijo ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 48, "question": "Maxay ahayd ujeeddada dhabta ah ee ciidankii Faransiisku u boobeen kutubtii Azhar una burburiyeen masaaxifta?", "options": { "a": "Sababtoo ah way u baahnaayeen warqad", "b": "Inay ku jabiyaan niyadda iyo caqiidada shacabka Masar, maadaama Azhar ahayd halka laga soo bilaabo halganka", "c": "Sababtoo ah kutubtu waxay ahaayeen kuwo gaboobay", "d": "Ma jirin ujeeddo cad" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 49, "question": "Sidee bay 'mideynta' labada hoggaamiye (Cabdullaahi bin Xaamid iyo Cusmaan) u beddeshay mustaqbalka Suudaan?", "options": { "a": "Waxay keentay in Ingiriisku dalka maamulo muddo dheer", "b": "Waxay dhalisay xukuumaddii ugu horreysay ee xor ah oo Afrikaan ah, taasna ay hadda ku naaloonayaan xornimo", "c": "Waxay keentay in Suudaan loo qaybiyo laba qaybood", "d": "Ma ay beddelin mustaqbalka Suudaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 50, "question": "Maxaa caddeyn u ah in nolosha Cumar Mukhtaar ay ka dheer tahay midka daldalaya?", "options": { "a": "Sababtoo ah weli taariikhdiisa iyo halgankiisa ayaa la bartaa loona arkaa tusaale xornimo", "b": "Sababtoo ah wuxuu dhashay 1862", "c": "Sababtoo ah daldalihii ayaa isla markiiba dhintay", "d": "Caddayn ma jirto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Qiimeey doorka 'Cilmiga' ee xornimo u doonista dalka sida ku xusan halganka Cumar Mukhtaar?", "options": { "a": "Cilmigu wuxuu furaa indhaha dadka, wuxuuna u horseedaa inay dalkooda ka difaacdaan gumeystaha", "b": "Cilmigu ma aha muhiim xilliga dagaalka", "c": "Cilmigu wuxuu yimaadaa xornimada ka dib", "d": "Cilmigu wuxuu keenaa in lala heshiiyo cadawga" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Sidee ayuu 'Gumeysiga' iyo 'Xuquuq la'aantu' isugu xiran yihiin xilligii Koonfur Afrika?", "options": { "a": "Gumeysigu wuxuu ku dhisnaa midab takoor iyo in dadka madowga ah laga xajiyo xuquuqdooda", "b": "Gumeysigu wuxuu siiyay dadka madowga ah xuquuq dheeraad ah", "c": "Ma jirin wax xiriir ah", "d": "Gumeysigu wuxuu rabay in qof kasta siman yahay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Maxay ahayd ujeeddada Janaraal Kaliibar ka niyad-jabkiisa Qaahira maarso 1800?", "options": { "a": "In shacabka Masar ay ahaayeen kuwa daciif ah", "b": "In dhabar-adaygga iyo halganka joogtada ah ee reer Masar ay ka xoog badnaayeen ciidankiisa", "c": "Sababtoo ah wuxuu rabay inuu guryo dhisat", "d": "Sababtoo ah lacag ayaa ka dhammaatay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Maxay ka dhigan tahay 'Innaa Lillaahi wa innaa Ilayhi Raajicuun' oo uu yiri Cumar Mukhtaar xilligii xukunka?", "options": { "a": "Inuu aqbalay geerida isagoo aaminsan xukunka Ilaahay iyo in loo laabanayo", "b": "Inuu ka baqay geerida", "c": "Inuu u duceynayo cadawga", "d": "Waa hadal caadi ah oo aan micno lahayn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Falanqee siday Suleymaan Xalabi iyo ardaydii reer Gaza u ahaayeen tusaale dhiirranaan?", "options": { "a": "Waxay dileen hogaamiyihii cadawga iyagoo aan haysan ciidan weyn, taasna waxay muujisay in qof kasta wax qaban karo", "b": "Waxay ahaayeen kuwa ugu fiican xagga waxbarashada", "c": "Waxay caawisay Faransiiska si ay dalka u joogaan", "d": "Ma jirin wax dhiirranaan ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Sidee ayuu u saameeyay dhaqdhaqaaqii Mahdiga Suudaan taariikhda guud ee Afrika?", "options": { "a": "Wuxuu noqday tusaale halgan oo dhiiri-geliyay dhaqdhaqaaqyadii kale ee Afrika si ay u raadiyaan xornimo", "b": "Wuxuu sababay in Afrika oo dhan gumeysi lagu daro", "c": "Ma uusan saameyn Afrika inteeda kale", "d": "Wuxuu u horseeday Afrika inay raacaan Ingiriiska" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Muxuu ahaa farqiga u dhaxeeya dagaalkii 1913 iyo kii 1931 ee Cumar Mukhtaar?", "options": { "a": "1913 wuxuu ahaa guulo halgan, 1931-na wuxuu ahaa markii gacanta lagu dhigay lana daldalay", "b": "1913 wuxuu ahaa mid nabad ah, 1931-na waa mid dagaal", "c": "Labaduba waa isku mid", "d": "Dagaalkii 1913 ayaa ka dhib badnaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Maxaa keeni kara 'Niyad-jab' marka loo eego hadalkii Cumar Mukhtaar ee ahaa 'Way na jebin karaan haddii ay na niyad-jebiyaan'?", "options": { "a": "In qofku waayo iimaanka iyo rajada xornimada, taasna ay keento inuu is-dhiibo", "b": "In hubku kaa dhamaado", "c": "In saaxiibadaadu kaa cararaan", "d": "Niyad-jabku muhiim ma ahan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Qiimeey saamaynta dhinaca 'Siyaasadda' ee halgankii Masar ee ka dhanka ahaa Faransiiska?", "options": { "a": "Waxay keentay in shacabku fahmaan muhiimadda madax-banaanida, ugu dambeyntiina ka xoroobaan gumeysiga", "b": "Waxay keentay in dalka laga dhigo boqortooyo Faransiis ah", "c": "Waxay keentay in shacabku isku dilaan gudaha", "d": "Ma jirin wax saamayn siyaasadeed ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Sidee ayay midab-takoorku u curyaamisay Koonfur Afrika ka hor inta uusan ANC guuleysan?", "options": { "a": "Waxay dadka u qaybisay dad cad oo wax walba leh iyo dad madow oo xuquuq la'aan ah", "b": "Waxay dadka ka dhigtay kuwa siman", "c": "Waxay keentay in dhaqaaluhu kordho", "d": "Midab-takoorku ma jirin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sharax doorkii ururka ANC ee sanadihii kontomeeyadii xagga waddanimada?", "options": { "a": "Waxay wadeen halgan wacyigelin ah iyo mudaaharaadyo nabadeed ka hor intaysan hubka qaadan", "b": "Waxay caawinayeen dowladda midab takoorka", "c": "Waxay ka qaxeen dalka", "d": "Ma jirin wax door ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Maxaa xiriir ah oo ka dhexeeya 'dulmiga' iyo 'halyeeynimada'?", "options": { "a": "Dulmigu wuxuu qofka ku kiciyaa inuu difaaco xaqiisa, markaas ayuu noqdaa halyeey taariikhda gala", "b": "Halyeeynimadu waxay u baahan tahay lacag", "c": "Dulmigu wuxuu burburiyaa halyeeyada", "d": "Ma jiro wax xiriir ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Muxuu Suleymaan Xalabi u noqday mid ka dhex muuqda taariikhda Azhar?", "options": { "a": "Sababtoo ah wuxuu fuliyay fal geesinimo leh oo wax weyn ka beddelay habkii gumeysiga Faransiisku u arkayay shacabka", "b": "Sababtoo ah wuxuu ahaa kii ugu weynaa ardayda", "c": "Sababtoo ah wuxuu Faransiiska baray carabi", "d": "Sababtoo ah wuxuu ahaa qof nabad jecel" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Sidee bay 'Saldhiggyada' sida Biniin u xoojiyeen halgankii Cumar Mukhtaar?", "options": { "a": "Waxay u ahaayeen goobo uu ciidanku kaga soo duulo cadawga, halkaasna ay ku helaan ammaan iyo abaabul", "b": "Waxay ahaayeen goobo lagu tijaabiyo hubka", "c": "Waxay ahaayeen xabsiyo lagu xiro Talyaaniga", "d": "Saldhigyadu ma ahayn muhiim" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Maxay ahayd sababtii dhalisay kacdoonkii 2aad ee Qaahira maarso 1800?", "options": { "a": "Sababtoo ah dhibaatooyinkii gumeysiga ee joogtada ahaa iyo rabitaanka madax-banaanida", "b": "Sababtoo ah lacagta ayaa yaraatay", "c": "Sababtoo ah Janaraal Kaliibar ayaa dadka u yeeray", "d": "Ma jirin sabab cad" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Qiimeey hadalkii Cumar Mukhtaar: 'Xukun waa kii Eebbe ee ma aha kiina dhalanteedka ah'?", "options": { "a": "Wuxuu muujinayaa in awoodda gumeystuhu tahay mid kumeel gaar ah, awoodda rabaaniga ahna ay tahay midda dhabta ah", "b": "Wuxuu doonayay inuu noqdo hoggaamiye diimeed oo keliya", "c": "Wuxuu ka dhalan rabaa inuu noqdo madaxweyne", "d": "Hadalku micno siyaasadeed ma lahayn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee bay 'mideynta' shucuubta u beddeshaa natiijada halganka gumeysi-diidka?", "options": { "a": "Midnimadu waxay keentaa cudud dhab ah oo adkeyneysa halganka, kana dhigaysa mid guuleysta", "b": "Midnimadu waxay daciifisaa talada hoggaanka", "c": "Midnimadu muhiim ma ahan", "d": "Midnimadu waxay u roon tahay gumeystaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Muxuu xiriirka ka dhexeeya 'iimaanka' iyo 'hubka' u ahaa mid xooggan xilligii Cumar Mukhtaar?", "options": { "a": "Sababtoo ah iimaanka ayaa qofka siiya dhiirigelinta uu ku isticmaalo hubka si geesinimo leh", "b": "Iimaanka iyo hubka wax xiriir ah ma laha", "c": "Hubka ayaa ka muhiimsanaa iimaanka mar kasta", "d": "Iimaanku waa wax lagu beddelo hubka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Maxaa keeni kara in 'nolosha qof halyeey ah' ay ka dheeraato midka daldalaya?", "options": { "a": "Dhaxalka fikirka iyo halganka oo ay raacaan jiilalka dambe", "b": "Sababtoo ah wuxuu leeyahay dawooyin", "c": "Sababtoo ah wuxuu ahaa qof xoog badan", "d": "Ma dheeraan karto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Saameynta 'boobka kutubta' ee Azhar ku yeeshay aqoonta Masar xilligaas?", "options": { "a": "Waxay curyaamisay dhaxalkii aqooneed ee yaallay Masjidka, waxayna muujisay naxariis darrada gumeysiga", "b": "Waxay keentay in aqoon cusub la barto", "c": "Ma saameyn wax aqoon ah", "d": "Way kordhisay aqoonta Masar" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Maxay ahayd sababtii uu u guuleystay dhaqdhaqaaqa Koonfur Afrika ugu dambeyntii?", "options": { "a": "Sababtoo ah dhabar-adaygii hoggaamiyeyaasha sida Mandela iyo taageerada ballaran ee dadka madowga ah", "b": "Sababtoo ah cadawgii ayaa isaga baxay is-kood", "c": "Sababtoo ah hub casri ah ayaa la siiyay", "d": "Sababtoo ah midab-takoorkii ayaa is-baabi'iyay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Falanqee 'isku-xirka halganka Suudaan iyo halganka Afrikaan' ee xogta ku jira?", "options": { "a": "Halganka Suudaan wuxuu tusaale u ahaa kacdoonnadii ugu caansanaa ee dhiiri-geliyay Afrika oo dhan", "b": "Suudaan iyo Afrika wax xiriir ah ma lahayn", "c": "Halganka Suudaan wuxuu ka duwanaa halganka kale ee Afrika", "d": "Afrika oo dhan ayaa Suudaan u soo gurmatay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Muxuu ahaa doorka 'Ardayda Azhar' ee kacdoonadii ka dhanka ahaa Faransiiska?", "options": { "a": "Waxay ahaayeen horseedka iyo udub-dhexaadka halganka, iyagoo naftooda u huray dalka", "b": "Waxay ahaayeen arday wax uun barata oo aan siyaasadda gelin", "c": "Waxay caawinayeen Janaraal Diibwii", "d": "Waxay ka qaxeen Masjidka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Sidee bay 'mudooyinka kala duwan' ee dagaallada Cumar Mukhtaar u muujindayaan dhabar-adayg?", "options": { "a": "Dagaallada socday in ka badan 20 sano waxay muujindayaan go'aan adayg iyo halgan aan marna is-dhiibayn", "b": "Waxay muujindayaan in ciidankiisu ahaa mid daciif ah", "c": "Waxay muujindayaan in Talyaanigu ahaa mid naxariis badan", "d": "Mudooyinku muhiim ma ahan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Maxay ahayd sababtii Suleymaan Xalabi loogu dilay dil gaar ah (daldalaad ama toogasho)?", "options": { "a": "Sababtoo ah wuxuu dilay Janaraalkii ugu sareeyay Faransiiska Kiliibar", "b": "Sababtoo ah wuxuu ahaa qariib", "c": "Sababtoo ah wuxuu xaday kutub", "d": "Ma jirin sabab cad" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Qiimeey doorka 'Hoggaaminta' ee dhaqdhaqaaqii Mahdiga ee Suudaan?", "options": { "a": "Hoggaaminta mideysan waxay ahayd furihii guusha iyo dhismaha dowlad xor ah", "b": "Hoggaamintu ma ahayn mid muhiim ah", "c": "Hoggaaminta Suudaan waxay ahayd mid u shaqaysa Ingiriiska", "d": "Hoggaamintu waxay ahayd mid kumeel-gaar ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Sidee buu 'Gumeysigu' u saameeyay dhalinyarada reer Masar ee cutubkan?", "options": { "a": "Wuxuu ku kiciyay inay noqdaan kacaaniyiin iyo halyeeyo naftooda u hura dalka", "b": "Wuxuu ka dhigay kuwa ganacsi jecel", "c": "Wuxuu ka dhigay kuwo Faransiis ah", "d": "Ma saameyn dhalinyarada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 78, "question": "Sharax siday 'is-dhiibid la'aantu' u tahay tiirka guusha halganka sida Cumar Mukhtaar?", "options": { "a": "Waa go'aan qofka ka hor istaagaya inuu cadawga u hoggaansamo, taasna ay keentu guul dambe ama geeri sharaf leh", "b": "Waa in la dhimado isla markiiba", "c": "Waa in dalka laga baxo", "d": "Is-dhiibid la'aantu ma keentu guul" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch4_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch4',
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
    
    # Remove existing his_ch4 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch4']
    
    # Check if his_ch4 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch4' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 4aad: Halgankii iyo Kacdoonnada Afrika",
            "id": "his_ch4"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch4':
                c['title'] = "Cutubka 4aad: Halgankii iyo Kacdoonnada Afrika"
                break
    
    # Add new his_ch4 questions
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

    # Remove existing his_ch4 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch4']
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
