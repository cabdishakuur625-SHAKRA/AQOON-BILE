import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa kuwee isirka dadka Cusmaaniyiinta?", "options": { "a": "Qabiil ka mid ah Carabta", "b": "Qabiil ka mid ah Turkiga", "c": "Qabiil ka mid ah Faarisiga", "d": "Qabiil ka mid ah Kurdida" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Yaa ahaa aasaasihii Dawladda Cusmaaniyiinta?", "options": { "a": "Ardhagural", "b": "Cusmaan binu Ardhagural", "c": "Orkhaan Al-Gaazi", "d": "Muxammad Al-Faatix" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Sanadkee buu dhintay Ardhagural?", "options": { "a": "1288-dii", "b": "1300-dii", "c": "1250-dii", "d": "1299-dii" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa maxay magaca hadda loo yaqaan magaalada Konistantinoobal?", "options": { "a": "Ankara", "b": "Istanbuul", "c": "Buursa", "d": "Izmir" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Yaa furtay magaalada Istanbuul sanadkii 1453?", "options": { "a": "Suldaan Muraad 1-aad", "b": "Suldaan Muxammad Al-Faatix", "c": "Suleymaan Qaanuuni", "d": "Suldaan Saliim 1-aad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa kuma madaxweynihii ugu horreeyay ee Jamhuuriyadda Turkiga?", "options": { "a": "Ismet Inonu", "b": "Mustafa Kamaal Ataatuk", "c": "Suldaan Cabdulxamiid", "d": "Cusmaan 3-aad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Sanadkee bay dowladdii Cusmaaniyiintu si rasmi ah u burburtay?", "options": { "a": "1914-tii", "b": "1924-tii", "c": "1945-tii", "d": "1899-kii" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Dawladda Cusmaaniyiinta waxay dhul ku lahayd inta qaaradood?", "options": { "a": "Laba qaaradood", "b": "Saddex qaaradood", "c": "Afar qaaradood", "d": "Hal qaarad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Halkee bay ku yaallaan buuraha Anatooliya oo dowladda ay ka dhalatay?", "options": { "a": "Masar", "b": "Turkiga", "c": "Sacuudiga", "d": "Ciraaq" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa kuma suldaankii 2-aad ee dowladda Cusmaaniyiinta?", "options": { "a": "Suldaan Orkhaan Al-Gaazi", "b": "Suldaan Muraad 1-aad", "c": "Bayazid 1-aad", "d": "Ardhagural" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 11, "question": "Magaaladii ugu horreysay ee Ardhagural uu furtay waxay ahayd?", "options": { "a": "Konistantinoobal", "b": "Askii Shahar", "c": "Adraana", "d": "Qudus" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa kuma suldaankii furtay magaalada Adraana sanadkii 1361?", "options": { "a": "Suldaan Orkhaan", "b": "Suldaan Muraad 1-aad", "c": "Suldaan Muxammad 1-aad", "d": "Suldaan Cusmaan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Sanadkee bay Buursa noqotay magaalo madaxdii Cusmaaniyiinta?", "options": { "a": "1302-dii", "b": "1453-dii", "c": "1288-dii", "d": "1326-dii" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa kuma suldaankii 3-aad ee reer Cusmaan?", "options": { "a": "Suldaan Muraad 1-aad", "b": "Suldaan Muraad 2-aad", "c": "Suldaan Orkhaan", "d": "Suldaan Bayazid" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 15, "question": "Qarnigee bay dowladda soo gashay Aasiyada yar?", "options": { "a": "Qarnigii 10-aad", "b": "Qarnigii 13-aad", "c": "Qarnigii 15-aad", "d": "Qarnigii 18-aad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Muxuu qabtay Suldaan Orkhaan sanadkii 1326?", "options": { "a": "Wuxuu furtay Ankara", "b": "Wuxuu qabtay awoodda dhimashadii aabbihiis kadib", "c": "Wuxuu furtay badda Cas", "d": "Wuxuu dhisay Istanbuul" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Intee sano ayuu xilka hayay Muxammad Al-Faatix?", "options": { "a": "10 sano", "b": "31 sano", "c": "50 sano", "d": "20 sano" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Maxaa lagu beddelay dowladda Cusmaaniyiinta markii ay dhacday?", "options": { "a": "Imaraadka Carabta", "b": "Jamhuuriyadda Turkiga", "c": "Dowladdii Seljuuqa", "d": "Boqortooyada Ingiriiska" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Waa kuwee qaaradaha ay dowladda xukumaysay?", "options": { "a": "Aasiya, Afrika, iyo Yurub", "b": "Aasiya, Yurub, iyo Ameerika", "c": "Afrika, Yurub, iyo Awstaraaliya", "d": "Aasiya iyo Afrika kaliya" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 20, "question": "Yaa ahaa aasaasihii dowladda militariga ee Cusmaaniyiinta?", "options": { "a": "Cusmaan 1-aad", "b": "Orkhaan Al-Gaazi", "c": "Ardhagural", "d": "Suldaan Saliim" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Sharax soo ifbaxa dawladda Cusmaaniyiinta?", "options": { "a": "Waxay ka dhasheen dhexdeeda Turkiga", "b": "Waxay ka soo barakeceen bartamaha Aasiya iyagoo u soo guuray Anatooliya", "c": "Waxay ahaayeen ganacsato ka timid Masar", "d": "Waxay ahaayeen ciidan ka goostay Biizantiinka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 22, "question": "Muxuu ahaa dardaarankii Cusmaan ee ku socday saaxiibadiis?", "options": { "a": "Inay dhistaan qalcadaha badda", "b": "Inay sii wadaan sarreeynta diinta Islaamka iyo jihaadka", "c": "Inay heshiis la galaan Biizantiinka", "d": "Inay dib ugu laabtaan Aasiyada dhexe" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 23, "question": "Maxay ahayd muhiimadda qabsashadii qalcadda Tarnab?", "options": { "a": "Waxay soo afjartay dowladdii Seljuuqa", "b": "Waxay fududaysay qabsashadii dambe ee Konistantinoobal", "c": "Waxay ahayd markii u horeysay ee badda la galo", "d": "Waxay u gogol xaartay qabsashadii Masar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 24, "question": "Waa maxay nidaamka 'Sanjaq' ee dawladda ka jiray?", "options": { "a": "Waa nidaamka lagu qaybinayo lacagta", "b": "Waa qaybinta dalka loo qaybiyay gobollo tiradoodu tahay 32", "c": "Waa magaca ciidanka fardooleyda", "d": "Waa magaca dowladda dhexdeeda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Muxuu ahaa doorka Suldaan ku-xigeenka?", "options": { "a": "Inuu ahaado madaxa Sheekha Islaamka", "b": "Inuu u matalo Suldaanka gobollada (Sanjaqyada)", "c": "Inuu ururiyo canshuurta badda", "d": "Inuu hoggaamiyo ciidanka fardooleyda kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Muxuu Suldaan Muraad 1-aad isku magacaabay markii u horeysay?", "options": { "a": "Boqorka Yurub", "b": "Khaliifka Muslimiinta", "c": "Hoggaamiyaha Seljuuqa", "d": "Amiirka Anatooliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Nidaamka maaliyadeed ee dowladda maxaa ugu muhiimsanaa?", "options": { "a": "Ganacsiga dharka", "b": "Xisaabta dakhliga, kharashka, iyo qaybinta dhulka", "c": "Canshuurta maraakiibta badda kaliya", "d": "Maalgelinta dibadda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Waa kuma qofka labaad ee awoodda dalka ku xigay Suldaanka?", "options": { "a": "Taliyaha Ciidanka", "b": "Sheekha Islaamka", "c": "Wasiirka Arrimaha Dibadda", "d": "Guddoomiyaha Sanjaq" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Intee sano ayuu socday khilaafkii walaalihii Muxammad 1-aad?", "options": { "a": "5 sano", "b": "11 sano", "c": "2 sano", "d": "20 sano" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Muhiimadda juqraafiyeed ee Konistantinoobal maxay ahayd?", "options": { "a": "Waxay ku tiilay bartamaha saxaraha", "b": "Waxay u dhaxaysay laba qaaradood waxayna ku tiilay meel ganacsi iIyo difaac ah", "c": "Waxay ahayd meel beeraha ku fiican", "d": "Waxay ahayd dekedda kaliya ee dowladda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Waa maxay waxqabadkii ugu muhiimsanaa ee Suldaan Muxammad 1-aad?", "options": { "a": "Wuxuu furtay Masar", "b": "Wuxuu soo celiyay haybaddii dowladda iIyo sharciyeynta ciidanka badda", "c": "Wuxuu dhisay Istanbuul", "d": "Wuxuu riday dowladdii Biizantiinka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Saldhigga ciidanka Cusmaaniyiinta maxaa u ahaa aaladda xukunka?", "options": { "a": "Ciidanka Lugta", "b": "Fardooleyda fadhiisinka ku leh soohdimaha", "c": "Maraakiibta quusa", "d": "Hubka culculus ee casriga ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Dhaqdhaqaaqa cilmiga ee dalka sidee buu u bilowday?", "options": { "a": "Wuxuu bilowday dhammadkii dowladda", "b": "Waxaa la dhisay laba dugsi intii u dhaxaysay 1331-1335", "c": "Waxaa laga soo minguuriyay Yurub", "d": "Waxaa lagu bilaabay kulyadda Sulaymaaniya kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Immisa maraakiib ayuu lahaa Suleymaan Qaanuuni?", "options": { "a": "10 markab", "b": "300 oo markab", "c": "1000 markab", "d": "50 markab" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Waa maxay Kulyadda Sulaymaaniya?", "options": { "a": "Waa qalcadda dagaalka", "b": "Waa xarun cilmiyeed oo la dhammaystiray 1557-dii", "c": "Waa masaajidka Istanbuul ugu weyn", "d": "Waa nidaamka canshuuraha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 36, "question": "Halkee buu Suldaan Muraad 1-aad ku shahiiday?", "options": { "a": "Buursa", "b": "Goobta dagaalka ee magaalada Quusuu (Kosovo)", "c": "Istanbuul dhexdeeda", "d": "Masar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Maxaa keentay in dowladda loo bixiyo 'Cusmaaniyiinta'?", "options": { "a": "Maaddaama ay qabiil ka yimaadeen", "b": "Waxaa loogu magac daray Suldaankii kuxunka dhisay ee Cusmaan", "c": "Maaddaama ay magaalada Buursa degeen", "d": "Maaddaama ay Seljuuqa ka go'een" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxay dowladda u noqotay mid 'caalami ah'?", "options": { "a": "Maaddaama ay lacag badan haysatay", "b": "Maaddaama ay dhul ku lahayd saddexda qaaradood ee dunidii hore", "c": "Maaddaama ay dad badan oo Yurubiyaan ah u shaqaynayeen", "d": "Maaddaama ay caalamka oo dhan ay xukumaysay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Waa maxay sababta Muxammad 1-aad loogu tixgeliyo inuu dowladda badbaadiyay?", "options": { "a": "Maaddaama uu furtay Yurub", "b": "Maaddaama uu soo afjaray khilaafkii walaalihii dowladdana mideeyay", "c": "Maaddaama uu dhisay ciidanka fardooleyda", "d": "Maaddaama uu riday Biizantiinka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Nidaamka xukunka maxaa iska beddelay markii uu dalku fiday?", "options": { "a": "Waxa uuu noqday mid fowdo ah", "b": "Dalka waxaa loo qaybiyay 32 gobol (Sanjaq) si loo maamulo", "c": "Waxa uuu noqday boqortooyo ka madax-bannaan diinta", "d": "Suldaanku wuxuu iska casilay xilka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Muxuu Cusmaan xaqiijiyay sanadkii 1308-dii?", "options": { "a": "Wuxuu furtay magaalada Istanbuul", "b": "Wuxuu xaqiijiyay himilooyinkiisii madax-bannaanida dowladda", "c": "Wuxuu dhisay ciidanka badda", "d": "Wuxuu dhintay isaga oo dagaallamaya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Maxaa dhacay Agoosto 21, 1326-dii?", "options": { "a": "Waxaa la dhisay Istanbuul", "b": "Waxaa geeriyooday Cusmaan Al-Gaazi", "c": "Waxaa la furtay Adraana", "d": "Dagaalkii 1aad ee adduunka ayaa bilaabmay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 43, "question": "Masjidka weyn ee Azniiq goormee la dhisay?", "options": { "a": "1300-dii", "b": "1331-dii", "c": "1453-dii", "d": "1557-dii" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Hoggaamiyihii riday dowladda Cusmaaniyiinta wuxuu ahaa?", "options": { "a": "Suleymaan Qaanuuni", "b": "Mustafa Kamaal Ataatuk", "c": "Suldaan Cabdulxamiid", "d": "Mustafa 1-aad" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 45, "question": "Falanqee sababihii gudaha ee u horseeday dhicidii Dawladda Cusmaaniyiinta?", "options": { "a": "Ciidanka oo yaraaday iyo hubka oo gabaabsi noqday", "b": "Heshiis la'aan dadka dhexdiisa ah, ka fogaanshaha shareecada, iIyo keligii talisnimo", "c": "Biyo la'aan baahsan iIyo cudurro dalka ku faafay", "d": "Suldaanka oo ka guuray magaalada madaxda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 46, "question": "Maxay ahayd saameynta 'Xuquuqda iyo mudnaanta' la siiyay dalalka reer Yurub?", "options": { "a": "Waxay keentay in Yurub ay Islaamto", "b": "Waxay daciifisay madax-bannaanida dowladda iIyo dhaqaalaheeda", "c": "Waxay keentay in ganacsiga dowladda uuu aad u kordho", "d": "Waxay dhashay in ciidanka Cusmaaniyiinta ay Yurub ka taliyaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 47, "question": "Falanqee nidaamka xukunka ee dowladda ee dhammadkii noqday 'keligii talisnimo'?", "options": { "a": "Awoodda oo loo qaybiyay dadka shacabka ah", "b": "Awoodda oo dhan oo gacanta u gashay hal qof (Suldaanka) oo aan xadidnayn", "c": "In golaha wasiirrada ay xilka la wareegeen", "d": "In dowladda ay noqotay mid dimuqraadi ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 48, "question": "Maxay ahayd kaalinta hay'adda islaamiga ah ee xukunka dhexdiisa?", "options": { "a": "Waxay ahayd mid sawir ah kaliya", "b": "Waxay ahayd udub-dhexaadka dowladda maaddaama xukunku shareecada ku dhisnaa", "c": "Waxay ahayd mid dhanka ciidanka kaliya qaabilsan", "d": "Waxay ahayd mid hoos timaada maamulka gobollada" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 49, "question": "Sidee bay u kala duwanaayeen maamulka gobollada weyn sida Masar iyo Yaman?", "options": { "a": "Ma lahayn canshuur gabi ahaanba", "b": "Ma lahayn qaybinta 'Sanjaq' ee gobollada kale caadiga u ahayd", "c": "Ma hoos imaan jirin Suldaanka", "d": "Ciidan fardooley ah ma fadhiyi jirin" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 50, "question": "Dhibaatada taariikhiga ah ee haysta bulshada Islaamka ee dhulkan maxaa ka mid ah?", "options": { "a": "Jahliga iyo aqoon la'aanta", "b": "Xasuuq, gabood-falo, midab-takoorid iIyo barakicin", "c": "In diinta laga baxay gabi ahaanba", "d": "Inaan la dhisin masaajidda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 51, "question": "Falanqee saameynta 'ka fogaanshaha shareecada' ay ku yeelatay burburka dowladda?", "options": { "a": "Waxay keentay in reer Yurub ay ka baqdaan dowladda", "b": "Waxay daciifisay cadaaladdii iIyo qiyamkii mideynayay bulshada dhexdeeda", "c": "Waxay keentay in dakhliga dowladda uuu kordho", "d": "Waxay keentay in ciidanka badda ay awood yeeshaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 52, "question": "Muxuu ahaa farqiga u dhexeeya Ardhagural iIyo Cusmaan ee dhanka madax-bannaanida?", "options": { "a": "Ardhagural wuxuu ahaa boqor, Cusmaan wuxuu ahaa amiir", "b": "Ardhagural wuxuu hoos joogay Seljuuqa, halka Cusmaan uu ku dhawaaqay madax-bannaani", "c": "Cusmaan wuxuu ka yimid Aasiya, Ardhagural wuxuu ku dhashay Anatooliya", "d": "Ma jirin wax farqi ah oo u dhexeeyay labadooda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Sidee bay dowladda ugu guulaysatay inay xukunto saddex qaaradood oo kala duwan?", "options": { "a": "Iyadoo adeegsanaysa nidaamka maamulka Sanjaq iIyo awood ciidan oo isku xiran", "b": "Iyadoo qaarad walba siisay madax-bannaani buuxda", "c": "Iyadoo adeegsanaysa maraakiib quusa oo kaliya", "d": "Ma jirin maamul rasmi ah oo qaaradahaas ka jiray" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Waa maxay sababta dhabta ah ee 'Dagaalkii 1aad ee Dunida' loogu xiriiriyo dhicidii dowladda?", "options": { "a": "Maaddaama dowladda ay ka guulaysatay reer Yurub", "b": "Maaddaama dowladda ay ka qaybgashay lagana adkaaday, taas oo daciifisay awooddeeda kama dambaysta ah", "c": "Maaddaama dowladda ay iska diiday inay ka qaybgasho", "d": "Maaddaama dhulka Turkiga uu noqday mid barwaaqo ah dagaalka kadib" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Xilligii dowladda ay dhacaysay, maxay ahayd kaalinta 'dhaqdhaqaaqyada gooni u goosadka ah'?", "options": { "a": "Waxay xoojiyeen midnimada dowladda", "b": "Waxay keeneen in gobollo badan ay ka go'aan dowladda dhexdeeda, daciifiyeenna awoodda", "c": "Waxay dhisneen xarumo cilmi oo cusub", "d": "Waxay Suldaanka ka caawiyeen maamulka Sanjaqyada" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Maxay ahayd qiimaha uu lahaa dardaarankii Cusmaan ee ahaa 'ku socda Tawxiidka'?", "options": { "a": "In dowladda ay noqoto mid hanti raac ah", "b": "In dowladda ay lahaato ujeeddo diimeed oo midaysan oo jihaad ku jiro", "c": "In dadka oo dhan laga dhigo Turkiga", "d": "In la baabi'iyo gobollada Sanjaq" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 57, "question": "Kaalinta Sheekha Islaamka maxay ku dhisneyd markii la eego dhanka awoodda?", "options": { "a": "Wuxuu ahaa qofka ugu hooseeya dowladda", "b": "Wuxuu ahaa midka kuxiga Suldaanka dhanka awoodda iIyo saameynta shareecada", "c": "Wuxuu ahaa taliyaha ciidanka badda", "d": "Wuxuu ahaa wasiirka maaliyadda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Muxuu Muxammad 1-aad u sharciyeeyay 'ciidanka badda'?", "options": { "a": "Si loo xoojiyo ganacsiga dowladda ee Yurub iIyo badda", "b": "Si dowladda ay u la tartanto awoodaha badda ee xilligaas jiray", "c": "Maaddaama ciidanka fardooleyda ay shaqadii joojiyeen", "d": "Si uu u baabi'iyo dowladdii Biizantiinka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Falanqee isku magacaabistii Muraad 1-aad ee 'Khaliifka Muslimiinta'?", "options": { "a": "Waxay ahayd magac sharaf ah oo kaliya", "b": "Waxay ahayd hoggaanka ruuxiga ah iIyo kan siyaasadeed ee dhammaan muslimiinta", "c": "Waxay ahayd inuu ku cabsi geliyo reer Yurub", "d": "Waxay ahayd inuu ka madax-bannaanaado walaalihii" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Sababaha dibadda ee burburka maxaa u horreeyay?", "options": { "a": "Cimilada oo isbeddeshay", "b": "Duulaankii Gumaystaha iIyo soo bixitaankii awoodda Ruushka", "c": "In dalkii laga dhacay dhuxusha", "d": "Ganacsiga reer Yurub oo gabi ahaanba joogsaday" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 61, "question": "Goorma ayay Buursa noqotay saldhigga dhabta ah ee xukunka?", "options": { "a": "1288-dii", "b": "1302-dii, waxayna noqotay magaala madaxdii koowaad", "c": "1453-dii", "d": "1326-dii" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 62, "question": "Sidee bay dowladda ugu guulaysatay inay ka mid noqoto boqortooyooyinka ugu waa weyn taariikhda Islaamka?", "options": { "a": "Maaddaama ay lacag badan soo daabaceen", "b": "Mudadii dheerayd ee ay jirtay iIyo sidii ay u difaacday dunida Islaamka", "c": "Maaddaama qof walba oo dowladda u dhashay uu Turkiga ahaa", "d": "Sababtoo ah ma jirin dowlado kale oo la tartamayay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 63, "question": "Muxuu ahaa ujeedka laga lahaa 'qaybinta dhulka' ee nidaamka maaliyadda?", "options": { "a": "In dhulka loo qaybiyo reer Yurub", "b": "In la dhiirigeliyo beeraha iIyo in ciidanka laga bixiyo kharashaadka dhulka", "c": "In Suldaanka uu dhulka oo dhan iska leeyahay", "d": "Si looga fogaado maamulka gobollada" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxaa dhacay markii la riday dowladda loona beddelay Jamhuuriyad?", "options": { "a": "Dalku wuxuu u guuray shareecada Islaamka", "b": "Nidaamkii Khilaafada ayaa la baabi'iyay, dalkuna wuxuu noqday cilmaani (Secular)", "c": "Suldaan kale ayaa la doortay", "d": "Turkiga wuxuu dib u qabsaday Istanbuul" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 65, "question": "Dhibaatada nidaamka 'Sanjaq' ee dhammadkii maxay ahayd?", "options": { "a": "Ma jirin dhibaato dhab ah", "b": "Musuqmaasuq iIyo maamul-xumo ka dhalatay madaxdii gobollada u matalaysay Suldaanka", "c": "In Sanjaqyada ay dhamaantood Masar ku yaalleen", "d": "Inaysan jirin wax maamul ah gabi ahaanba" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 66, "question": "Falanqee doorka 'Askii Shahar' ee dhalashada dowladda?", "options": { "a": "Waxay ahayd magaaladii ay ku heshiiyeen Biizantiinka iIyo Cusmaaniyiinta", "b": "Waxay ahayd magaaladii ugu horreysay ee lagu aasaasay cududda dowladda Cusmaaniyiinta", "c": "Waxay ahayd halkii looga dhawaaqay burburka dowladda", "d": "Waa magaaladii uuu ku dhashay Ardhagural" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 67, "question": "Maxaa keenay in Istanbuul loo bixiyo 'Muxammad Al-Faatix' (magaca buundada)?", "options": { "a": "Maaddaama uuu isagu dhisay buundada", "b": "Si loo sharfo loona xusuusto guushii taariikhiga ahayd ee uuu furtay magaaladaas", "c": "Maaddaama buundada ay ku tiilay qalcaddiisa", "d": "Ma jiro sabab cad oo loo bixiyay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 68, "question": "Falanqee xaaladda dhaqaale ee dowladda ee qarnigii 19-aad?", "options": { "a": "Waxay ahayd barwaaqo weyn", "b": "Jahwareer dhaqaale, musuqmaasuq iIyo daymo lagu yeeshay dowladda", "c": "Waxay dowladda joojisay isticmaalka lacagta", "d": "Ganacsiga maraakiibta badda ayaa kor u kacay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 69, "question": "Sidee bay dowladda u kobcisay dhaqanka Islaamka gobollada Yurub?", "options": { "a": "Iyadoo qof kasta ku qasabtay inuu Islaamo", "b": "Iyadoo dhistay masaajidda, dugsiyada, iIyo dhiirigelinta dacwada Islaamka", "c": "Ma jirin wax dhaqan Islaam ah oo Yurub ka faafay", "d": "Iyadoo dadka Yurub u dirtay bartamaha Aasiya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 70, "question": "Muhiimadda ay 'shareecada Islaamka' u lahayd jiritaanka dowladda maxay ahayd?", "options": { "a": "Inay dowladda ka dhigto mid reer Yurub u dhow", "b": "Waxay ahayd nidaamka mideeya bulshooyinka kala duwan cadaaladdana saldhig u ah", "c": "Waxay ahayd nidaam militariga kaliya lagu xukumo", "d": "Waxay ka dhigtay dowladda mid aad u taajir ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 71, "question": "Muxuu ahaa ujeedada ka dambaysay dhismaha 'Kulyadda Sulaymaaniya'?", "options": { "a": "In la dhisno ciidan cusub", "b": "In la abuuro xarun cilmi oo weyn oo aqoonta dhinac walba ah u horseedda dowladda", "c": "In la canshuuro dadka cilmiga leh", "d": "In lagu tartamo dowladda Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 72, "question": "Maxaa lagu tilmaami karaa doorka 'Mustafa Kamaal Ataatuk' ee taariikhda Turkiga?", "options": { "a": "Wuxuu ahaa kii ugu dambeeyay khulafada", "b": "Wuxuu ahaa ninkii u beddelay dowladda nidaamka cilmaaniga iIyo Jamhuuriyadda Turkiga", "c": "Wuxuu ahaa aasaasihii ciidanka badda", "d": "Wuxuu ahaa midka dhisay Kulyadda Sulaymaaniya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 73, "question": "Guul darooyinka ciidanka dhammadkii maxaa ugu weynaa?", "options": { "a": "Hubkii fardooleyda oo dhammaaday", "b": "Iska caabbinta reer Yurub ee xoogga badneyd iIyo daciifnimada hoggaanka militariga", "c": "In dowladda ay ka baxday Anatooliya", "d": "In ciidanka ay goosteen dhanka Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 74, "question": "Waa maxay muhiimadda ay 'bishaarada Nabiga (NNKH)' u lahayd qabsashadii Istanbuul?", "options": { "a": "Waxay ahayd mid dhiirigelisa ciidanka si ay u fuliyaan ballanqaadkaas rabaaniga ah", "b": "Waxay ahayd mid reer Yurub looga dhigayay inay is dhiibaan", "c": "Waxay ahayd mid qof kasta oo Istanbuul joogay ka dhigaysay muslim", "d": "Ma jirin wax saameyn ah oo ay ku lahayd furashada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Nidaamka maamulka ee gobollada Sanjaq, sidee buu u fududeeyay fiditaanka dowladda?", "options": { "a": "Ma uusan fududayn ee wuxuu keenay burbur", "b": "Wuxuu ogolaaday in gobol kasta si madax-bannaan balse dowladda dhexdeeda ah loo maamulo", "c": "Wuxuu keenay in gobollada ay lacag u diraan reer Yurub", "d": "Suldaanku ma uusan awoodin inuu arko gobolladaas" }, "correctAnswer": "b", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch1_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch1',
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
    
    # Remove existing his_ch1 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch1']
    
    # Check if his_ch1 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch1' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 1aad: Dawladda Cusmaaniyiinta",
            "id": "his_ch1"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch1':
                c['title'] = "Cutubka 1aad: Dawladda Cusmaaniyiinta"
                break
    
    # Add new his_ch1 questions
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

    # Remove existing his_ch1 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch1']
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
