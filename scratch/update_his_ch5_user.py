import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Goormuu dhammaaday Dagaalkii 2aad ee Adduunka?", "options": { "a": "1939", "b": "1942", "c": "1945", "d": "1948" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa kuwee labadii hogaamiye ee ugu muhiimsanaa Kacaanka Ruushka?", "options": { "a": "Hitler iyo Mussolini", "b": "Trotsky iyo Vladimir Lenin", "c": "Stalin iyo Roosevelt", "d": "Churchill iyo Truman" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Dagaalkii Qaboobaa wuxihu u dhexeeyay labadii quwadood ee:", "options": { "a": "Jarmalka iyo Talyaaniga", "b": "Ingiriiska iyo Faransiiska", "c": "Mareykanka iyo Midowgii Soofiyeeti", "d": "Ruushka iyo Jabbaan" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa maxay nidaamka siyaasadeed ee dunidu ka dhaxashay Kacaanka Ruushka?", "options": { "a": "Demuqraadiyad", "b": "Fashistanimo", "c": "Shuucinimada (Communism)", "d": "Boqortooyo" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 5, "question": "Taariikhdee ayaa lagu dhawaaqay dhismaha dawladda Israa'iil?", "options": { "a": "May 15, 1948", "b": "October 6, 1973", "c": "September 1, 1939", "d": "January 1, 1945" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 6, "question": "Dagaalkii 6-da Oktoobar wuxuu dhacay sanadkii:", "options": { "a": "1948", "b": "1956", "c": "1967", "d": "1973" }, "correctAnswer": "d", "difficultyLevel": "easy" },
  { "id": 7, "question": "Hogaamiyihii Fashistaha ee Talyaaniga wuxuu ahaa:", "options": { "a": "Adolf Hitler", "b": "Benito Mussolini", "c": "Francisco Franco", "d": "Joseph Stalin" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Ururkee la aasaasay Dagaalkii 2aad ka dib si nabadda loo ilaaliyo?", "options": { "a": "Ururka Midowga Afrika", "b": "Qaramada Midoobay (UN)", "c": "Jaamacadda Carabta", "d": "NATO" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Dagaalkii u dhexeeyay Ruushka iyo Jabbaan wuxuu dhacay sanadihii:", "options": { "a": "1914-1918", "b": "1939-1945", "c": "1904-1905", "d": "1948-1949" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 10, "question": "Qorshaha Mareykanka ee lagu dhisayay Yurubta burburtay waxaa loo yaqaan:", "options": { "a": "Qorshaha Truman", "b": "Qorshaha Marshall", "c": "Qorshaha NATO", "d": "Qorshaha Roosevelt" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Immisa qof ayaa qiyaastii ku dhimatay Dagaalkii 2aad ee Adduunka?", "options": { "a": "10 Milyan", "b": "35 Milyan", "c": "62 Milyan", "d": "100 Milyan" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 12, "question": "Hogaamiyihii xisbiga Naaziga ee Jarmalka wuxuu ahaa:", "options": { "a": "Lenin", "b": "Mussolini", "c": "Hitler", "d": "Franco" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 13, "question": "Dagaalkii 2aad wuxuu bilowday markii lagu duulay dalka:", "options": { "a": "Faransiiska", "b": "Booland (Poland)", "c": "Ruushka", "d": "Masar" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Magaalooyinkee ayay Jarmalka iyo Talyaanigu ku kala saxiixdeen heshiiska milatari?", "options": { "a": "London iyo Paris", "b": "Moscow iyo Washington", "c": "Room iyo Baarliin", "d": "Qaahira iyo Dimishiq" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 15, "question": "Waa kuma hogaamiyihii Fashistaha ee dalka Isbayn?", "options": { "a": "Mussolini", "b": "Franco", "c": "Hitler", "d": "Stalin" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Sanadkee ayuu Hitler qabsaday dalka Austriya?", "options": { "a": "1935", "b": "1938", "c": "1940", "d": "1945" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Dagaalkii Qaboobaa wuxuu bilaabmay goorma?", "options": { "a": "Dagaalkii 1aad ka dib", "b": "Dagaalkii 2aad ka dib", "c": "Kacaankii Ruushka ka hor", "d": "Dagaalkii 1973 ka dib" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Dalka Jarmalka waxaa loo qaybiyay laba dawladood xilligii:", "options": { "a": "Dagaalkii 1aad", "b": "Dagaalkii Qaboobaa", "c": "Kacaankii Ruushka", "d": "Dagaalkii 1967" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Immisa reer Falastiin ah ayaa guryahooda ka qaxay 1948?", "options": { "a": "100 kun", "b": "200 kun", "c": "400 kun", "d": "1 milyan" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 20, "question": "Waa maxay ujeedadii Jarmalka ee 1938 ee dalka Austriya?", "options": { "a": "Inuu burburiyo", "b": "Inuu xoreeyo", "c": "Inuu ku daro Jarmalka", "d": "Inuu ka ganacsado" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 21, "question": "Hogaamiyihii Soofiyeetiga ee dhintay 1953 wuxuu ahaa:", "options": { "a": "Lenin", "b": "Stalin", "c": "Gorbachev", "d": "Trotsky" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Waa maxay sababta ugu weyn ee dhalashada Kacaanka Ruushka?", "options": { "a": "Dagaalka Jabbaan kaliya", "b": "Dhibaatooyinka beeraha", "c": "Dhismaha warshadaha", "d": "Xiriirka Mareykanka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Dagaalkii labaad ee adduunka dalkee ayuu Jarmalku qabsaday 1939?", "options": { "a": "Talyaaniga", "b": "Yugoslaafiya", "c": "Faransiiska", "d": "Ruushka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 24, "question": "Waa kuwee labada magaalo ee heshiiska milatari saxiixday?", "options": { "a": "Baarliin iyo London", "b": "Room iyo Baarliin", "c": "Paris iyo Room", "d": "Moscow iyo Baarliin" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 25, "question": "Sharax ujeedkii Ruushka ee dagaalkii 1904-1905 uu la galay Jabbaan?", "options": { "a": "Inuu xoreeyo Jabbaan", "b": "Qabsashada dhul cusub, adkeynta awoodda iyo joojinta kacaanka", "c": "Si uu u caawiyo Mareykanka", "d": "Inuu tijaabiyo hub cusub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Maxaa dhacay bishii Sibtember 1939 oo hurisay Dagaalkii 2aad?", "options": { "a": "Jabbaan oo weerartay Shiinaha", "b": "Ciidamada Jarmalka oo ka tallaabay soohdinta Booland", "c": "Dhismaha Qaramada Midoobay", "d": "Dhimashadii Stalin" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Maxay ahayd natiijada Dagaalkii 1948 ee Carabta iyo Israa'iil?", "options": { "a": "Guul u soo hoyatay Carabta", "b": "Asaasidda Israa'iil iyo dhibaatada dadka reer Falastiin", "c": "Burburka labada dhinacba", "d": "Heshiis nabadeed oo rasmi ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Maxaa xiriir ah oo ka dhexeeya Sahyuuniyadda iyo gumeysiga cusub?", "options": { "a": "Ganacsi wadajir ah", "b": "Islaam naceyb", "c": "Dhismaha warshadaha", "d": "Ilaalinta deegaanka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Waa maxay sababta ugu weyn ee dilaaca Dagaalkii Qaboobaa?", "options": { "a": "Dagaalkii Jarmalka iyo Talyaaniga", "b": "Aragtiyaha is diidan iyo loolanka danaha Mareykanka iyo Soofiyeetiga", "c": "Kacaankii Ruushka oo fashilmay", "d": "Burburkii warshadaha Yurub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Maxaa dhacay markii uu dhamaaday Dagaalkii Qaboobaa?", "options": { "a": "Ruushka ayaa adduunka xukumay", "b": "Adduunka waxaa hoggaaminayay hal isbahaysi oo ah Mareykanka", "c": "Dagaalkii 3aad ayaa bilowday", "d": "Dhammaan hubka ayaa la baabi'iyay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Waa maxay 'Qorshaha Marshall'?", "options": { "a": "Qorshe lagu weerarayo Ruushka", "b": "Qorshe Mareykanku ku dhisayo Yurubta burburtay", "c": "Qorshe lagu qaybinayo Jarmalka", "d": "Qorshe hubka looga dhigayo Jabbaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Sidee buu u isbeddelay sawirka dagaalkii 2aad ka hor dhamaadkii 1942?", "options": { "a": "Waa uu istaagay", "b": "Sawirka dagaalka wuu is beddelay (isbeddel xagga awoodda)", "c": "Jarmalka ayaa guulaystay", "d": "Talyaaniga ayaa is dhiibay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Waa maxay saddexda heer ee Dagaalkii 2aad ee Adduunka soo maray?", "options": { "a": "Bilaaw, Dhexe, iyo Dhammaad", "b": "Istiraatiiji, Howlgal, iyo Taatiko", "c": "Badda, Bariga, iyo Cirka", "d": "Dhaqaale, Siyaasad, iyo Bulsho" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxaa lagu heshiiyay xiriirkii Room iyo Baarliin?", "options": { "a": "Inaan la dagaalamin", "b": "Gacansiinta midba midka kale haddii uu dagaal galo", "c": "In Booland la siiyo Ingiriiska", "d": "In la baabi'iyo xisbiga Naaziga" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Maxay ahayd natiijada Dagaalkii 1973 ee Carabta iyo Israa'iil?", "options": { "a": "Israa'iil oo qabsatay dhowr dal", "b": "Argagax milatari oo aan horay loo arag oo gudaha Israa'iil ah", "c": "In Qaramada Midoobay la kala diiro", "d": "Asaasidda dawladda Masar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxay Yurub isu aragtay xilligii Dagaalkii Qaboobaa?", "options": { "a": "Dawlad weyn oo midaysan", "b": "In ay u kala qaybsantahay laba isbahaysi oo waaweyn", "c": "In ay ka madax-banaantahay Mareykanka", "d": "In ay tahay xarunta shuucinimada" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Maxaa xiriir ah oo ka dhexeeya Dagaalkii 2aad iyo dhismaha Israa'iil?", "options": { "a": "Ma jiro wax xiriir ah", "b": "Duruufaha caalamiga ah ee ka dhashay dagaalkaas ayaa keenay dhismaha Israa'iil", "c": "Israa'iil ayaa soo afjartay dagaalkii 2aad", "d": "Hitler ayaa saxiixay dhismaha Israa'iil" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxay ahayd saameynta dhaqaale ee Dagaalkii 2aad ku yeeshay Yurub?", "options": { "a": "Dhaqaalaha ayaa kor u kacay", "b": "Burbur warshado, joogsi wax soo saar, iyo shaqo la'aan korortay", "c": "Warshado cusub ayaa la dhisay xilligii dagaalka", "d": "Ma jirin wax saameyn ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Dagaalkii 1967 maxay ahayd natiijadiisa ugu muhiimsan?", "options": { "a": "Dhammaadka dhibaatada Falastiin", "b": "Fiditaanka baaxadda dagaalka Carabta iyo Israa'iil", "c": "In Jarmalku caawiyo Carabta", "d": "Burburkii Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Waa maxay mabaadii’da ka dambaysa Kacaanka Ruushka?", "options": { "a": "In la dhismo nidaam dimuqraadi ah", "b": "Isku dayga qabsashada dhul cusub iyo fashilka kaligii-talisnimada", "c": "In la xoojiyo xiriirka Jabbaan", "d": "In la taageero Hitler" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Maxaa dhacay sanadkee 1948 ee dalka Jugoslofaakiya?", "options": { "a": "Dagaal sokeeye", "b": "Afgembigii hantiwadaagga (Socialist coup)", "c": "Waxaa qabsaday Mareykanka", "d": "Waxaa loo qaybiyay laba qaybood" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Maxaa lagu tilmaamaa xiriirka Is-ballaarinta Jabbaan iyo Dagaalkii 2aad?", "options": { "a": "Inay Jabbaan joojisay dagaalka", "b": "Inay ahayd mid ka mid ah sababihii dhaliyay dagaalkii 2aad", "c": "In Jabbaan ay dhex-dhexaad ahayd", "d": "Inay ka hortagtay Naaziga" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 43, "question": "Sidee bay awooddii Mareykanka iyo Soofiyeetigu u saameeyeen adduunka dagaalka ka dib?", "options": { "a": "Way daciifeen", "b": "Waxay noqdeen labada awoodood oo dunida ugu sareeyo", "c": "Waxay ku biireen hal dawlad", "d": "Waxay u dhiibeen awoodda Ingiriiska" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Waa maxay micnaha 'Dabeecadda adag' ee dhibaatada Falastiin?", "options": { "a": "Inay tahay mid si fudud lagu xalin karo", "b": "Inay tahay mid dhib badan oo aanay wali dhammaan", "c": "Inay tahay mid xuduudaha lagu heshiiyay", "d": "Inay tahay mid dhaqaale kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 45, "question": "Maxay ahayd sababta Talyaanigu u qabsaday Albaaniya?", "options": { "a": "Inuu caawiyo dadka Albaaniya", "b": "Is-ballaarin iyo xoojinta awoodda Fashistaha", "c": "Inuu ka hortago Ruushka", "d": "Inuu helo saliid" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxay dhibaatooyinka beeraha u noqdeen sabab weyn oo kacaanka Ruushka ah?", "options": { "a": "Maadaama beeruhu ay yaraadeen", "b": "Maadaama ay ahaayeen laf-dhabarta nolosha ee markaas dhibaataysneyd", "c": "Sababtoo ah Lenin ayaa nebaa beeralayda", "d": "In Jabbaan ay qaadatay badarka Ruushka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 47, "question": "Waa maxay ujeedadii laga lahaa dhismaha Qaramada Midoobay?", "options": { "a": "In la bilaabo dagaal cusub", "b": "In la ilaaliyo nabadda iyo amniga caalamiga ah", "c": "In la caawiyo Jarmalka", "d": "In la xukumo Midowgii Soofiyeeti" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 48, "question": "Sidee bay u kala duwanaayeen dagaalkii 1948 iyo kii 1956?", "options": { "a": "Labaduba way isku mid ahaayeen", "b": "1948 wuxuu ahaa mid dhammaystiran, 1956 wuxuu ahaa mid xaddidan", "c": "1956 ayaa ka weynaa", "d": "Ma jirin wax farqi ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 49, "question": "Maxay ahayd dhibaatada ugu weyn ee haysatay dadka rayidka ah dagaalkii 2aad ka dib?", "options": { "a": "Ma jirin dhibaato", "b": "Dhimasho badan, burbur guryo, iyo shaqo la'aan", "c": "In ay helaan lacag badan", "d": "In ay u guuraan Amerika" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 50, "question": "Waa maxay dabeecadda 'Is-ballaarinta' ee dawladaha Fashistaha?", "options": { "a": "In ay nabad ku raadiyaan dunida", "b": "In ay qabsadaan dhulal cusub si ay u weyneeyaan awoodooda", "c": "In ay dhisaan ururo caalami ah", "d": "In ay taageeraan dhibbanayaasha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 51, "question": "Maxay ahayd saameynta 'Is-ballaarinta Jabbaan' ee bariga fog ka dib dagaalkii Ruushka?", "options": { "a": "Waxay keentay in Ruushku guulaysto", "b": "Waxay xoojisay awoodda Jabbaan, kuna dhiirigelisay loolan weyn", "c": "Waxay dhalisay xiriir saaxiibtinimo", "d": "Waxay soo afjartay boqortooyadii Jabbaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 52, "question": "Falanqee xaaladda Ruushka xilligii u dhaxeysay 1904-1905, sidee bayna u saameysay dhalashada kacaanka?", "options": { "a": "Waxaa jiray horumar dhaqaale oo weyn", "b": "Guuldarradii dagaalka Jabbaan waxay dhalisay niyad jab iyo dardar-gelinta dhaqdhaqaaqa kacaanka", "c": "Ruushka ayaa qabsaday dhamaan bariga fog", "d": "Kacaanka ayaa iskiis u istaagay ka dib guushii Jabbaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Sidee buu nidaamka kaligii talisnimada ee Ruushka u saameeyay fashilka ka adkaanshaha cadawga gudaha?", "options": { "a": "Wuxuu mideeyay dadka", "b": "Wuxuu daciifiyay kalsoonida shacabka, isagoo awoodi waayay inuu xaliyo dhibaatooyinka gudaha", "c": "Wuxuu keenay in Jabbaan laga adkaado", "d": "Wuxuu dhameeyay dhibaatooyinka beeraha" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Qiimeey saameynta siyaasadeed ee adduunku ka dhaxlay Kacaankii Ruushka marka laga hadlayo 'Shuucinimada'?", "options": { "a": "Waxay keentay in adduunku nabad noqdo", "b": "Waxay abuurtay nidaam cusub oo loolan la galay hanti-goosadka, soona saaray Midowgii Soofiyeeti", "c": "Waxay keentay in Mareykanku burburo", "d": "Waxay baabi'isay dhamaan ciidamada Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxay ahayd doorka 'Xisbiga Naaziga' ee burburinta xasiloonida adduunka ee ka dambeysay Dagaalkii 1aad?", "options": { "a": "Waxay dhiseen Qaramada Midoobay", "b": "Waxay jebiyeen heshiisyadii caalamiga ahaa, iyagoo bilaabay is-ballaarin milatari", "c": "Waxay caawiyeen dadka reer Falastiin", "d": "Waxay nabad ka dhigeen dalka Jarmalka kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Sharax xiriirka ka dhexeeya Heshiiskii Fersaylis ee bilowga Dagaalkii 2aad ee Adduunka?", "options": { "a": "Wuxuu ahaa heshiis nabad lagu gaaray", "b": "Wuxuu Jarmalka saaray shuruudo adag oo dhaliyay carada iyo aargoosiga Naaziga", "c": "Wuxuu mideeyay Yurub iyo Mareykanka", "d": "Wuxuu horseeday Kacaankii Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sidee bay 'Dhaqaale xumadii weyneyd' u saameysay kor u kaca keli-taliyaasha Yurub?", "options": { "a": "Dadka ayaa lacag badan helay", "b": "Burburka dhaqaale wuxuu fududeeyay in dadku taageeraan hogaamiyayaal adag oo ballanqaaday badbaado", "c": "Waxay joojisay dagaalkii 2aad", "d": "Waxay keentay in Jabbaan ay caawiso Jarmalka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Falanqee ujeedada ka dambaysay heshiiskii 'Room iyo Baarliin' ee u dhexeeyay Hitler iyo Mussolini?", "options": { "a": "Inay iska kaashadaan ganacsiga badda", "b": "Inay abuuraan isbahaysi milatari oo ka dhan ah quwadaha kale ee Yurub", "c": "Inay joojiyaan Dagaalkii Qaboobaa", "d": "Inay dalka Isbayn nabad ka dhigaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay ahayd muhiimadda siyaasadeed ee ballan-qaadkii Ingiriiska ee ku aaddan madax-banaanida Booland?", "options": { "a": "Ma lahayn wax muhiimad ah", "b": "Waxay ahayd xariiq cas oo Jarmalka looga digay inuu weeraro dalkaas, taasoo dhalisay dagaalka", "c": "Waxay Booland ka dhigtay qayb ka mid ah Ingiriiska", "d": "Waxay joojisay weerarkii Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Qiimeey isbeddelka istiraatiijiga ah ee dagaalkii 2aad ee dhacay ka hor dhamaadkii 1942?", "options": { "a": "Awooddii Jarmalka ayaa kor u kacay si aan caadi ahayn", "b": "Miisaanka awoodda ayaa u wareegay dhinaca isbahaysiga ka soo horjeeda Jarmalka", "c": "Dagaalka ayaa u guuray bariga fog kaliya", "d": "Dhammaan dalalkii dagaalamayay ayaa heshiiyay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sharax saameynta 'Qorshaha Marshall' ku yeeshay xasiloonida siyaasadeed ee Yurubta Galbeed?", "options": { "a": "Wuxuu keenay in Yurub ay ku biirto Soofiyeetiga", "b": "Wuxuu ka hortagay fiditaanka shuucinimada isagoo dib u dhisay dhaqaalaha Yurub", "c": "Wuxuu bilaabay Dagaalkii 1aad ee adduunka", "d": "Wuxuu burburiyay warshadihii Mareykanka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 62, "question": "Maxay ahayd natiijadii istiraatiijiga ahayd ee ka dhalatay Dagaalkii 1948 ee Falastiin?", "options": { "a": "In reer Falastiin ay dib u helaan dhulkooda", "b": "Asaasidda dawladda Israa'iil iyo abuurista dhibaato qaxooti oo muddo dheer jirta", "c": "In Carabtu ay qabsato Tel Aviv", "d": "In Ingiriisku uu sii joogo Falastiin" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 63, "question": "Sidee buu Dagaalkii 1973 u saameeyay niyadda milatari ee gudaha Israa'iil?", "options": { "a": "Wuxuu kordhiyay kalsoonidooda", "b": "Wuxuu dhaliyay argagax iyo dareen nugulnimo milatari oo aan horay loo arag", "c": "Wuxuu keenay inay qabsadaan Masar oo dhan", "d": "Ma jirin wax saameyn ah oo uu ku yeeshay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Falanqee xiriirka ka dhexeeya 'Islaam naceybka' iyo isbahaysiga Sahyuuniyadda iyo gumeysiga cusub?", "options": { "a": "Waa xiriir ganacsi oo kaliya", "b": "Waa aasaaska ideoolajiga ah ee ay ku midoobeen si ay u wiiqaan awoodda dalalka Islaamka", "c": "Wuxuu horseeday nabadda Bariga Dhexe", "d": "Wuxuu caawiyay horumarka reer Falastiin" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sharax duruufaha caalamiga ah ee Dagaalkii 2aad ka dib ee fududeeyay dhismaha Israa'iil?", "options": { "a": "Daciifnimada Carabta oo kaliya", "b": "Isku-dheelitirka awoodaha cusub iyo saameynta xasuuqii Yuhuudda ee Yurub (Holocaust)", "c": "Taageerada Midowgii Soofiyeeti ee ku aaddan boqortooyooyinka Carabta", "d": "In Jarmalku uu saxiixay heshiiska 1948" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxay ahayd saameynta dhimashadii Istaalin (1953) ku yeelatay jawiga Dagaalkii Qaboobaa?", "options": { "a": "Dagaalka ayaa isla markiiba dhammaaday", "b": "Waxay keentay xilli isbeddel ah iyo isku dayo 'wada-noolaansho' oo dhex maray labada isbahaysi", "c": "Ruushka ayaa u dhiibay awoodda Mareykanka", "d": "Mareykanka ayaa weeraray Moscow" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee buu afgembigii hantiwadaagga ee Jugoslofaakiya (1948) u sii huriyay Dagaalkii Qaboobaa?", "options": { "a": "Wuxuu keenay nabad dhex marta Yurub", "b": "Wuxuu u muujiyay reer Galbeedka khatarta fiditaanka Soofiyeetiga, taasoo keentay adkeynta xuduudaha", "c": "Wuxuu joojiyay Qorshaha Marshall", "d": "Wuxuu mideeyay dhamaan dalalka hanti-goosadka ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 68, "question": "Qiimeey heerka 'Istiraatiijiga ah' ee Dagaalkii 2aad marka la barbardhigo heerka 'Taatikada ah'?", "options": { "a": "Ma jiro wax farqi ah oo u dhexeeya", "b": "Istiraatiijiyadda waa qorshaha guud iyo ujeedooyinka fog, halka taatikada ay tahay fulinta dagaalka ee goobta", "c": "Taatikada ayaa ka muhiimsan istiraatiijiyadda", "d": "Labaduba waxay ku koobnaayeen badda kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 69, "question": "Falanqee tilmaamaha guud ee dagaalladii Carabta iyo Israa'iil ee u dhexeeyay 1948 ilaa 1982?", "options": { "a": "Dhammaantood waxay ahaayeen kuwo guul u horseeday Carabta", "b": "Dagaalkii 1948 wuxuu ahaa mid dhammaystiran, halka kuwii kale ay ahaayeen kuwo xaddidan xagga himilooyinka", "c": "Labaduba waxay ahaayeen dagaallo dhaqaale oo kaliya", "d": "Dagaalladaas ma lahayn wax natiujo istiraatiiji ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 70, "question": "Sidee bay awoodda Mareykanku u noqotay mid 'keli-ah' (Unipolar) ka dib dhammaadkii Dagaalkii Qaboobaa?", "options": { "a": "Sababtoo ah Mareykanka ayaa qabsaday Ruushka", "b": "Burburkii nidaamkii Soofiyeetiga ayaa ka tagay Mareykanka oo ah quwadda kaliya ee dunida hoggaaminaysa", "c": "Sababtoo ah Mareykanka ayaa xubin ka noqday Soofiyeetiga", "d": "Qaramada Midoobay ayaa Mareykanka u dooratay hogaanka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 71, "question": "Maxay ahayd saameynta 62 milyan ee dhimashada ah ku yeelatay dib u dhiska bulshooyinka Yurub?", "options": { "a": "Waxay keentay in dadku badnaadaan ka dib dagaalka", "b": "Waxay horseedday burbur dhanka shaqaalaha, aqoonta, iyo hoos u dhac weyn oo ku yimid dadka wax soo saari kara", "c": "Waxay sahashay in warshado cusub la dhiso", "d": "Dhimashadu waxay ku koobneyd ciidamada kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sharax micnaha 'Is-ballaarin' ee Jabbaan u adeegsatay xilligii ka horreeyay Dagaalkii 2aad?", "options": { "a": "Waa dhismaha xiriir nabad ah", "b": "Waa siyaasad ku dhisneyd qabsashada dhulalka deriska ah si loo helo kheyraad iyo awood milatari", "c": "Waa inay Jabbaan isaga baxdo bariga fog", "d": "Waa inay Jabbaan caawiso Ruushka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 73, "question": "Qiimeey doorka 'Dhibaatooyinka beeraha' ee dhiirigelinta shacabka Ruushka inay ku biiraan kacaanka?", "options": { "a": "Beeralayda waxay ahaayeen kuwa ugu qanisan Ruushka", "b": "Dhibaatada nolosha iyo gaajada ka dhalatay beeraha waxay dadka ku riixday inay nidaamka ridi karaan", "c": "Beeraha ma lahayn wax saameyn ah", "d": "Lenin ayaa dadka ku amray inay beertaan badar badan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 74, "question": "Maxay ahayd saameynta 'Aragtiyaha is-diidan' ee Dagaalkii Qaboobaa ku yeelatay nolosha dadka ku nool bariga iyo galbeedka Jarmalka?", "options": { "a": "Waxay ku noolaayeen isku nidaam", "b": "Waxay u qaybiyeen dadka laba nidaam oo kala duwan (Hanti-wadaag and Hanti-goosad) iyo nolol aad u kala fog", "c": "Ma jirin wax farqi ah oo u dhexeeyay labada dhinac", "d": "Waxay keentay in Jarmalku u guuro Mareykanka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 75, "question": "Sidee bay u kala duwanaayeen ujeedooyinka 'Heerka howlgalka' iyo 'Heerka taatikada' ee Dagaalkii 2aad?", "options": { "a": "Way isku mid ahaayeen", "b": "Howlgalku wuxuu khuseeyaa dhaqdhaqaaqa ciidanka ee gobolada, taatikaduna waa dagaalka dhabta ah ee fool-ka-foolka ah", "c": "Taatikada ayaa ah midda dhacda dagaalka ka hor", "d": "Howlgalku waa midka dhaca dagaalka ka dib kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 76, "question": "Falanqee saameynta qaxootiga reer Falastiin (400,000+) ee dagaalkii 1948 ku yeelatay xasilloonida gobolka?", "options": { "a": "Waxay keentay in Bariga Dhexe uu nabad noqdo", "b": "Waxay abuurtay dhibaato bini'aadanimo iyo mid siyaasadeed oo haysata gobolka ilaa maanta", "c": "Reer Falastiin waxay isla markiiba ku laabteen guryahooda", "d": "Dawladaha Carabta ayaa Falastiiniyiinta u dhisay magaalooyin cusub" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 77, "question": "Qiimeey kaalinta 'Is-ballaarinta awoodda' ee dalka Ruushka intii u dhaxeysay 1904-1905?", "options": { "a": "Waxay horseedday guul weyn", "b": "Waxay dhalisay dagaal aan looga dhabeyn ujeedooyinkii laga lahaa, fashilkiisuna wuxuu horseeday kacdoon gudaha ah", "c": "Waxay baabi'isay dhamaan kacaannadii Ruushka", "d": "Waxay dalka Ruushka ka dhigtay mid dimuqraadi ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 78, "question": "Maxay ahayd muhiimadda xidhiidhkii 'Sahyuuniyadda iyo gumeysiga cusub' ee isbeddelka khariidadda Carabta?", "options": { "a": "Waxay ka hortagtay in khariidadda la beddelo", "b": "Waxay dhalisay khariidado cusub iyo gobollo ay maamusho Sahyuuniyadda oo ku dhex yaalla wadnaha Carabta", "c": "Waxay Carabta ka dhigtay hal dawlad", "d": "Waxay dhameeyay xiriirkii gumeysiga ee Yurub" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 79, "question": "Sharax saameynta 'Hoos u dhaca dhaqaale' ee ka dhashay Dagaalkii 2aad ee ku yimid wadamada guulaystay (sida Ingiriiska iyo Faransiiska)?", "options": { "a": "Dhaqaalahooda ayaa aad u kordhay", "b": "In kasta oo ay guulaysteen, haddana waxay la kulmeen burbur dhaqaale iyo baahi weyn oo dib u dhis ah", "c": "Waxay noqdeen quwadaha ugu qanisan dunida", "d": "Ma jirin wax dhaqaale ah oo kaga baxay dagaalka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 80, "question": "Sidee bay 'Aragtiyaha is-diidan' u saameeyeen samayska ururka Qaramada Midoobay bilowgiisii?", "options": { "a": "Ma jirin wax saameyn ah", "b": "Waxay abuurtay kala qaybsanaan iyo adeegsiga codka diidmada qayaxan (Veto) ee labada quwadood", "c": "Waxay keentay in hal madaxweyne la doorto", "d": "Waxay mideysay dhamaan mabaadii'da Mareykanka iyo Soofiyeetiga" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 81, "question": "Qiimeey doorka 'Hitler iyo xisbiga Naaziga' ee u diyaar garowga Dagaalkii 2aad marka laga eego dhanka ciidanka?", "options": { "a": "Waxay yareeyeen tirada ciidanka", "b": "Waxay dhiseen ciidan xooggan oo ku qalabaysan hub casri ah, iyagoo jebiyay dhamaan xannibaadihii hubka", "c": "Waxay ciidanka u isticmaaleen nabad kaliya", "d": "Ma jirin wax diyaargarow ah oo ay sameeyeen" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 82, "question": "Falanqee micnaha 'Heer cusub' ee adduunku galay ka dib dhamaadkii Dagaalkii Qaboobaa?", "options": { "a": "Waa xilli adduunku nabad wada noqday", "b": "Waa xilli uu hal hogaan (Mareykanka) go'aamiyo jihada siyaasadda iyo dhaqaalaha caalamka", "c": "Waa xilli Ruushku uu dib u soo noolaaday", "d": "Waa xilli aan loo baahnayn Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch5_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch5',
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
    
    # Remove existing his_ch5 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch5']
    
    # Check if his_ch5 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch5' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 5aad: Isbeddellada Caalamiga ah ee Qarnigii 20aad",
            "id": "his_ch5"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch5':
                c['title'] = "Cutubka 5aad: Isbeddellada Caalamiga ah ee Qarnigii 20aad"
                break
    
    # Add new his_ch5 questions
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

    # Remove existing his_ch5 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch5']
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
