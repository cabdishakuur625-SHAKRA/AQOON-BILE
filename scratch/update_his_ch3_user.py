import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay hindisaha calanka Soomaaliya?", "options": { "a": "Maxamed Siyaad Barre", "b": "Maxamed Cawaale Liibaan", "c": "Cabdullaahi Ciise", "d": "Aadan Cabdulle Cusmaan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Sanadkee ayay Soomaaliya qaadatay madax-banaanideeda?", "options": { "a": "1941", "b": "1960", "c": "1950", "d": "1969" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Yaa ahaa taliyihii ugu horreeyay ee ciidanka xoogga dalka Soomaaliyeed?", "options": { "a": "Maxamed Siyaad Barre", "b": "Jeneral Daa'uud Cabdulle Xirsi", "c": "Cabdullaahi Yuusuf", "d": "Salaad Gabayre" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Sanadkee ayaa la qoray Af-soomaaliga?", "options": { "a": "1960", "b": "1972", "c": "1969", "d": "1974" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Waa kuma gudoomiyihii golaha sare ee kacaanka?", "options": { "a": "Cabdirashiid Cali Sharma'arke", "b": "Jeneraal Maxamed Siyaad Barre", "c": "Aadan Cabdulle", "d": "Maxamed Cawaale" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Sanadkee ayay dhacday abaartii Daba-dheer?", "options": { "a": "1960", "b": "1974", "c": "1991", "d": "1950" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Halkee lagu dilay Madaxweyne Cabdirashiid Cali Sharma'arke?", "options": { "a": "Muqdisho", "b": "Laas-Caanood", "c": "Hargeysa", "d": "Kismaayo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Immisa sano ayaa loo qabtay muddada dawladnimo gaarsiinta Soomaaliya?", "options": { "a": "5 sano", "b": "10 sano", "c": "20 sano", "d": "1 sano" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Muddadii u dhaxeysay 1941-1950 yaa maamulayay koonfurta Soomaaliya?", "options": { "a": "Talyaaniga", "b": "Ingiriiska", "c": "Faransiiska", "d": "Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa kuwee labadii dawladood ee ku loolamay dawladnimo gaarsiinta Soomaaliya?", "options": { "a": "Ingiriiska iyo Talyaaniga", "b": "Ruushka iyo Maraykanka", "c": "Jarmalka iyo Faransiiska", "d": "Shiinaha iyo Hindiya" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 11, "question": "Goormee ayuu Talyaanigu si rasmi ah ula wareegay maamulka dawladnimo gaarsiinta?", "options": { "a": "Oktoobar 1969", "b": "Abriil 1950", "c": "Luuliyo 1960", "d": "Janaayo 1941" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa maxay xisbigii muujiyay inay diyaar u yihiin kala wareegidda talada dalka?", "options": { "a": "USP", "b": "SYL", "c": "SNC", "d": "MSB" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Waa maxay nidaamka dhaqaale ee uu qaatay maamulkii ciidanka?", "options": { "a": "Hantigoosi", "b": "Hantiwadaag", "c": "Iskaashi", "d": "Maamul-baahsan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa maxay dawladnimo gaarsiin?", "options": { "a": "Waa gumeysi toos ah", "b": "Hab dadka loogu diyaarinayo is-maamul iyo madax-banaani", "c": "Waa in dalka la iibiyo", "d": "Waa dagaal dhexmara labo qabiil" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Sanadkee ayaa la dilay Kamaaludiin Saalax (Safiirkii Masar)?", "options": { "a": "1950", "b": "1960", "c": "1967", "d": "1969" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Yaa ku guuleystay doorashadii madaxweynenimo ee Luuliyo 1967?", "options": { "a": "Aadan Cabdulle", "b": "Cabdirashiid Cali Sharma'arke", "c": "Maxamed Siyaad Barre", "d": "Cabdullaahi Ciise" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Maamulkii rayidka ahaa wuxuu dalka ka jiray inta u dhaxeysay?", "options": { "a": "1950-1960", "b": "1960-1969", "c": "1969-1991", "d": "1941-1950" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Xilligii dawladnimo gaarsiinta (AFIS) waxay ahayd sanadihii?", "options": { "a": "1941-1950", "b": "1950-1960", "c": "1960-1969", "d": "1972-1980" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Waa maxay ujeeddada laga lahaa in bulshada laga qayb geliyo maamulka dawladnimo gaarsiinta?", "options": { "a": "Si loo canshuro", "b": "Si loogu diyaariyo is-maamul", "c": "Si ay Talyaaniga u raacaan", "d": "Si ay dagaal u galaan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Maxaa dhacay markii gobollada qaarkood ay ka baxeen gacanta golaha dawladnimo gaarsiinta?", "options": { "a": "Dagaal ayaa qaraxay", "b": "Waxa ay noqdeen kuwa xor ah ama gobollo kale ku biiray", "c": "Ingiriiska ayaa dib u qabsaday", "d": "Qaramada Midoobay ayaa diidday" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Maxay Qaramada Midoobay u hakisay hawlihii golaha dawladnimo gaarsiinta?", "options": { "a": "Sababtoo ah lacag ayaa ka dhammaatay", "b": "Sababtoo ah ma jirin gobollo ku haray gacantooda", "c": "Sababtoo ah Talyaaniga ayaa diiday", "d": "Sababtoo ah Ruushka ayaa ka horyimid" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Maxay ahayd sababtii loo sameeyay nidaamka dawladnimo gaarsiinta?", "options": { "a": "Si loo kordhiyo gumeysiga", "b": "Si looga beddelo habkii hore ee hoosgeynta (colonialism)", "c": "Si loo baabi'iyo xisbiyada", "d": "Si loo dhiso ciidan xooggan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Sidee bay golayaashii la-tashiga gacan uga geysteen madax-banaanida?", "options": { "a": "Waxay keeneen hub", "b": "Waxay suurto-geliyeen dhisidda xisbiyo iyo doorashooyin", "c": "Waxay eryeen Talyaaniga", "d": "Waxay heshiis la galeen Itoobiya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 24, "question": "Sharax kaalintii uu ku lahaa Jeneral Daa'uud Cabdulle Xirsi madax-banaanida?", "options": { "a": "Wuxuu hindisay calanka", "b": "Wuxuu suurto-geliyay in xukuumaddu awood u yeelato fulinta go'aamadeeda", "c": "Wuxuu ahaa madaxweynihii ugu horreeyay", "d": "Wuxuu ahaa hogaamiyaha SYL" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Muxuu ahaa go'aankii Qaramada Midoobay ee loolankii Ingiriiska iyo Talyaaniga?", "options": { "a": "In Ingiriisku sii maamulo", "b": "In Talyaanigu maamulo muddada dawladnimo gaarsiinta", "c": "In dalka la qaybiyo", "d": "In dalka si degdeg ah xornimo loo siiyo 1950" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Maxay ahayd sababta 'diiniyan' loogu gaabiyay maamulkii ciidanka?", "options": { "a": "Waxay dhisteen masaajido badan", "b": "Ma ay dhegeysan culumada, qaarna waa la toogtay", "c": "Waxay amreen in diinta la barto", "d": "Waxay raaceen shareecada Islaamka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Xilligii rayidka (1960-1969) qaabkee ayay bulshadu wax u dooranaysay?", "options": { "a": "Hab keli-talis ah", "b": "Habka baarlamaaniga ah iyo xisbiyo badan", "c": "Habka qabiilka oo keliya", "d": "Ma jirin wax doorasho ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Muxuu ahaa ujeeddada kacaanku u galay afgembiga sida ay iyagu sheegteen?", "options": { "a": "In dalka la burburiyo", "b": "La dagaalanka musuq-maasuqa iyo dulmiga", "c": "In Talyaaniga dib loo soo celiyo", "d": "In calanka la beddelo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Maxay ahayd guushii ugu weynayd ee xagga aqoonta ee maamulkii ciidanka?", "options": { "a": "In jaamacado badan la furay", "b": "Qorista iyo horumarinta Af-soomaaliga", "c": "In Ingiriisida lagu qasbay dadka", "d": "In waxbarashada la lacag gareeyay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Muxuu xambaarsanaa go'aankii dawladnimo gaarsiinta ee dhinaca dhaqaalaha?", "options": { "a": "In la canshuro dadka masaakiinta ah", "b": "In la kobciyo dhaqaalaha gobolka lana dhowro xuquuqda", "c": "In dhaqaalaha loo dhoofiyo Talyaaniga", "d": "In la mamnuuco ganacsiga xorta ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Midnimada dalku maxay muhiim ugu tahay nabadgalyada?", "options": { "a": "Waxay keenaysaa in qabiiladu is-dilaan", "b": "Waxaa hal meel looga soo wada jeesanayaa cadowga", "c": "Waxay daciifisaa ciidanka", "d": "Waxay keentaa in dadku dalka ka qaxaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Muxuu ahaa gaabiskii dhinaca siyaasadda ee maamulkii ciidanka (MSB)?", "options": { "a": "Wuxuu dhiirigeliyay xisbiyada badan", "b": "Wuxuu baabi'iyay hay'adihii dastuuriga ahaa iyo nidaamka xisbiyada", "c": "Wuxuu dhisay baarlamaan xooggan", "d": "Wuxuu aqbalay talada shacabka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sidee bay Soomaaliya u hoos gashay maamulka Talyaaniga 1950-kii?", "options": { "a": "Dagaal ayay ku qabsadeen", "b": "Qaramada Midoobay ayaa u dhiibtay muddada dawladnimo gaarsiinta", "c": "Ingiriiska ayaa hadiyad u siiyay", "d": "Shacabka Soomaaliyeed ayaa doortay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxaa dhacay 12-kii Abriil 1960?", "options": { "a": "Waxaa dhashay SYL", "b": "Waxaa la dilay safiirkii Masar Kamaaludiin Saalax", "c": "Waxaa la qoray Af-soomaaliga", "d": "Waxaa la doortay Aadan Cabdulle" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Maxay ahayd ujeeddada laga lahaa horumarinta adeegga guud xilligii dawladnimo gaarsiinta?", "options": { "a": "In dadka lagu dhibo", "b": "Si loo diyaariyo kaabayaasha dowladda madax-bannaan", "c": "Si Talyaaniga loogu shaqeeyo", "d": "Si loo dhiso xabsiyo badan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 36, "question": "Muxuu ahaa dhibka ugu weyn ee 'Aragti-wadaagga' lagu beddelay xilligii ciidanka?", "options": { "a": "Waxaa lagu beddelay xornimo buuxda", "b": "Waxaa lagu beddelay cabburis bulsho", "c": "Waxaa lagu beddelay doorashooyin", "d": "Waxaa lagu beddelay canshuur dhaaf" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Dhinaca bulshada, maxay ahaayeen guulihii uu gaaray maamulkii ciidanka?", "options": { "a": "Cabburis iyo xabsi", "b": "Horumarka waxbarashada iyo caafimaadka", "c": "In dadka dalka laga eryo", "d": "In la diido qorista afka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxay ka dhigan tahay 'dalku waa dhaxal awoowe' marka loo eego difaaca dalka?", "options": { "a": "In la iibiyo dhulka", "b": "In loo diyaar noqdo difaaca dalka iyo ka horyimidda gumeysiga kasta", "c": "In qof kasta iska fariisto", "d": "In dalka loo dhiibo shisheeye" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Maxay ahayd sababta uu Ingiriisku gacanta ugu hayay Soomaaliya 1941-1950?", "options": { "a": "Wuxuu ahaa gumeystaha rasmiga ah", "b": "Wuxuu ahaa maamul ciidan oo kumeel-gaar ah dagaalkii kadib", "c": "Soomaaliya ayaa iska dhiibtay", "d": "Ma jirin cid kale oo jirtay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxaa loola jeedaa 'Guri la dhisay haddana la dumiyay' ee ku saabsan maamulkii ciidanka?", "options": { "a": "In dhismihii dowladda la gubay", "b": "In dalku gaaray horumar sare balse ku dambeeyay burbur weyn", "c": "In MSB uu guri dhisay kadibna ka guuray", "d": "Ma jiro wax macno ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Doorashadii 1967 maxay kaga duwanayd xilliyadii kale?", "options": { "a": "Waxaa doortay ciidanka", "b": "Waxay ahayd doorasho rayid ah oo xisbiyo ku tartameen", "c": "Ma jirin wax doorasho ah", "d": "Waxaa soo magacaabay Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Muxuu ahaa kaalinta SYL ee madax-banaanida ka sokow xisbinimada?", "options": { "a": "Waxay muujiyeen in Soomaalidu karto is-maamulka", "b": "Waxay taageereen gumeysiga", "c": "Waxay dalka ka qaxeen", "d": "Waxay diideen calanka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Maxaa dhacay markii go'aanka dawladnimo gaarsiinta Soomaaliya la soo bandhigay?", "options": { "a": "Shacabka ayaa diiday", "b": "Loolan adag ayaa dhex maray Ingiriiska iyo Talyaaniga", "c": "Talyaaniga ayaa dalka isaga baxay", "d": "Qaramada Midoobay ayaa burburtay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Maxay ahayd sababta ay midnimadu u keenayso 'isku-filnaan'?", "options": { "a": "Sababtoo ah dadka ayaa is-caawinaya wax-soosaarkuna kordhayo", "b": "Sababtoo ah lacag shisheeye ayaa la helayaa", "c": "Sababtoo ah ciidanka ayaa dadka qasbaya", "d": "Midnimadu isku-filnaan ma keento" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Maxaa lagu tilmaamay xaaladda siyaasadeed ee Soomaaliya xilligii dawladnimo gaarsiinta?", "options": { "a": "Dagaal sokeeye", "b": "La-tashi gole iyo maamul Qaramada Midoobay hoos taga", "c": "Keli-talisnimo", "d": "Boqortooyo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxay ahayd sababtii loo toogtay culumada xilligii kacaanka?", "options": { "a": "Sababtoo ah waxay doonayeen inay dalka qabsadaan", "b": "Sababtoo ah waxay ka horyimaadeen go'aamadii kacaanka (gaar ahaan xeerka qoyska)", "c": "Sababtoo ah waxay ahaayeen jaasiusiin", "d": "Ma jirin culumo la toogtay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 47, "question": "Falanqee farqiga u dhexeeya hab-maamulkii rayidka iyo kii dawladnimo gaarsiinta?", "options": { "a": "Ma jirin wax farqi ah", "b": "Rayidku wuxuu ahaa madax-banaani xisbiyo leh, dawladnimo gaarsiintuna waxay ahayd u diyaargarow madax-banaani", "c": "Dawladnimo gaarsiinta ayaa ka horumarsanayd", "d": "Rayidka waxaa maamulaysay Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 48, "question": "Maxay ujeeddada Qaramada Midoobay ka lahayd in Talyaaniga loo dhiibo Soomaaliya halkii Ingiriiska laga deyn lahaa?", "options": { "a": "Sababtoo ah Talyaaniga ayaa lacag badan bixiyay", "b": "Si loo fuliyo nidaamka dawladnimo gaarsiinta ee heshiiskii qaramada midoobay ee go'aamiyay in gumeystihii hore u diyaariyo dalka xornimo", "c": "Sababtoo ah Ingiriiska ayaa rabay inuu dalka qaato", "d": "Sababtoo ah Soomaalida ayaa Talyaaniga jeclayd" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 49, "question": "Sharax siday midnimadu u ilaalinayso danaha umadda ka dhexeeya?", "options": { "a": "Iyadoo qof kasta hantidiisa la wareegayo", "b": "Iyadoo loo siman yahay khayraadka iyo go'aamada dalka, loona midoobayo horumarka", "c": "Iyadoo shisheeye lala heshiinayo", "d": "Ma jiro wax dano ah oo ka dhexeeya umadda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 50, "question": "Qiimeey saamaynta uu ku yeeshay Jeneral Daa'uud dhismihii hay'adaha fulinta ee Soomaaliya?", "options": { "a": "Wuxuu dhisay ciidan xooggan oo suurto-geliyay in go'aamada dowladda la fuliyo laguna ixtiraamo", "b": "Wuxuu baabi'iyay dhamaan hay'adihii rayidka ahaa", "c": "Wuxuu dhiirigeliyay musuq-maasuqa", "d": "Wuxuu xoogga saaray dhinaca waxbarashada oo keliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Muxuu ahaa qopsaha fog ee 'Habka dawladnimo gaarsiinta' marka laga hadlayo horumarinta siyaasadda?", "options": { "a": "In dadka la baro luqadda Talyaaniga oo keliya", "b": "In bulshada loo tababaro hoggaaminta dalka si ay madax-banaani u gaaraan", "c": "In dalka laga dhigo mid hoostaga Talyaaniga weligiis", "d": "In la dhiso hal xisbi oo keliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 52, "question": "Maxay ahayd sababta ay Qaramada Midoobay u go'aamisay in Talyaanigu xilka wareejiyo 10 sano ka dib?", "options": { "a": "Sababtoo ah waqtigaas ayaa ku filnaa in dalka la dhiso", "b": "Waa waqtigii loo qabtay in Soomaaliya ay ku gaarto madax-banaani buuxda", "c": "Sababtoo ah Talyaaniga ayaa dalbaday", "d": "Sababtoo ah shacabka ayaa ka hor yimid" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Falanqee doorka Maxamed Cawaale Liibaan ee xagga aqoonsiga qaranimada?", "options": { "a": "Wuxuu dhisay ciidanka xoogga dalka", "b": "Wuxuu hindisay calanka oo ah astaanta ugu weyn ee aqoonsiga iyo madax-banaanida qaran", "c": "Wuxuu ahaa wasiirkii ugu horreeyay", "d": "Wuxuu qoray taariikhda Soomaaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Sidee bay 'kaabayaasha dhaqaalaha' u caawiyeen maamulkii ciidanka?", "options": { "a": "Ma ay caawin, dalka ayay burburiyeen", "b": "Waxay kor u qaadeen wax-soosaarka iyo nolosha bulshada xilligii hore ee kacaanka", "c": "Waxay keeneen canshuur badan oo MSB qaatay", "d": "Waxay u dhiibeen shisheeye" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxaa keeni kara 'Gumeysi fikir' marka loo eego xogta aad akhrisay?", "options": { "a": "Marka dadka laga xado dhulkooda", "b": "Marka bulshada laga xukumo dhanka fikirka iyo dhaqanka, laguna beddelo mid shisheeye", "c": "Marka la diido in wax la barto", "d": "Gumeysi fikir ma jiro" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Sharax dhibaatada ka dhalata 'Baabi'inta hay'adaha dastuuriga ah'?", "options": { "a": "Waxay keentaa xukun keli-talis ah, cabburis, iyo ugu dambeyntii burbur qaran", "b": "Waxay keentaa horumar degdeg ah", "c": "Waxay keentaa in dadku is-jecelaadaan", "d": "Ma laha wax dhib ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sidee buu maamulkii rayidka ahaa u dhiirigeliyay 'Hannaanka Baarlamaaniga ah'?", "options": { "a": "Iyadoo ciidanka laga dhigay xubno baarlamaan", "b": "Iyadoo loo oggolaaday xisbiyo badan inay tartamaan shacabkuna doortaan wakiilladooda", "c": "Iyadoo Talyaanigu soo magacaabay xubnaha", "d": "Iyadoo hal xisbi oo keliya la aqoonsaday" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Maxay ahayd saamaynta dilkii Kamaaludiin Saalax ku yeeshay madax-banaanida Soomaaliya?", "options": { "a": "Waxay dib u dhigtay xornimada", "b": "Waxay muujisay loolanka u dhexeeyay awoodaha shisheeye iyo dhibka loo soo maray madax-banaanida", "c": "Waxay keentay in Talyaanigu dalka ka baxo isla markiiba", "d": "Ma lahayn wax saameyn ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Qiimee xiriirka ka dhexeeya musuq-maasuqa iyo dhicidda kacaanka 1969?", "options": { "a": "Musuq-maasuqu wuxuu ahaa sababta rasmiga ah ee ciidanku u isticmaaleen inay ku xaqiijiyaan afgembigooda", "b": "Ma jirin wax musuq-maasuq ah", "c": "Musuq-maasuqu wuxuu yimid kacaanka kadib", "d": "MSB ayaa bilaabay musuq-maasuqa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Muxuu ahaa ujeeddada maamulkii ciidanka ka lahaa 'Horumarinta adeegga bulshada'?", "options": { "a": "Inay dadka uun u adeegaan", "b": "Inay helaan taageerada shacabka iyo inay muujiyaan inay ka fiican yihiin maamulkii rayidka", "c": "Inay lacag ka helaan hay'adaha caalamiga ah", "d": "Ma jirin qopshe cad" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sharax farqiga u dhexeeya 'Gumeysi toos ah' iyo 'Dawladnimo gaarsiin'?", "options": { "a": "Gumeysigu waa hoos-geyn weligeed ah, dawladnimo gaarsiintuna waa muddayn iyo u diyaarin xornimo", "b": "Labaduba waa isku mid", "c": "Dawladnimo gaarsiinta ayaa ka daran", "d": "Gumeysiga waxaa maamusha Qaramada Midoobay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Maxay midnimadu ugu tahay dalka 'Awood difaac'?", "options": { "a": "Sababtoo ah qof kasta wuxuu helayaa hub", "b": "Sababtoo ah cududda iyo talada oo midowda ayaa ka hortagi karta duullaan kasta", "c": "Sababtoo ah midnimada waxaa lagu helaa lacag shisheeye", "d": "Midnimadu difaac ma noqon karto" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 63, "question": "Waa maxay micnaha 'Xil-ka-gaabinta hannaanka aragti-wadaagga'?", "options": { "a": "In dadka loo oggolaaday inay doortan wax kasta", "b": "In talada dalka lagu soo koobay hal qof ama koox, bulshadana laga hor istaagay inay aragtiyadooda dhiibtaan", "c": "In la dhisay jaamacado", "d": "In la xoojiyay xisbiyada" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Falanqee xiriirka u dhexeeya 'Abaartii Daba-dheer' iyo maamulkii ciidanka?", "options": { "a": "Maamulku wuxuu awood u yeeshay inuu dadka gurmad u sameeyo una raro gobollada kale si loo badbaadiyo", "b": "Maamulku wuxuu amray in abaarta la iska dhaafo", "c": "Abaartu waxay keentay in MSB la rido", "d": "Abaartu waxay dalka ka saartay Talyaaniga" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sidee bay 'Qorista Af-soomaaliga' u ahayd horumar xagga madax-banaanida ah?", "options": { "a": "Waxay meesha ka saartay ku tiirsanaantii luqadaha shisheeye waxayna mideysay isgaarsiinta dalka", "b": "Waxay keentay in dadku dalka ka qaxaan", "c": "Waxay ahayd amarka Talyaaniga", "d": "Ma lahayn wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxay ahayd sababta maamulkii ciidanka Ingiriiska looga soo bilaabo 1941?", "options": { "a": "Sababtoo ah waxay jabiyeen Talyaanigii haystay dalka xilligii dagaalkii 2aad ee adduunka", "b": "Sababtoo ah Soomaalida ayaa u yeeratay", "c": "Sababtoo ah Qaramada Midoobay ayaa u dhiibtay bilowgii", "d": "Sababtoo ah Talyaaniga ayaa hadiyad u siiyay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Muxuu ahaa doorka 'Golayaashii la-tashiga' ee ku aaddan dhismaha xukuumadda?", "options": { "a": "Waxay ahaayeen kuwa go'aamiya xilliga dagaalka la galayo", "b": "Waxay gacan ka geysteen dhismihii hay'adaha maamulka iyo in sharciga dalka la dejiyo", "c": "Waxay u shaqeynayeen si qarsoodi ah", "d": "Ma jirin wax goleyaal ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 68, "question": "Sharax sababta maamulka dawladnimo gaarsiinta Soomaaliya loogu dhowrayay xuquuqda aadanaha?", "options": { "a": "Si loo tuso dunida in Talyaanigu isbeddelay", "b": "Si bulshada loogu diyaariyo nidaam dowladeed oo ku dhisan caddaalad iyo xuquuq xor ah", "c": "Sababtoo ah sharciga Qaramada Midoobay ayaa sidaas qabay", "d": "Labaduba b iyo c" }, "correctAnswer": "d", "difficultyLevel": "hard" },
  { "id": 69, "question": "Sidee bay 'doorashooyinkii' xilligii rayidka u muujiyeen bisayl siyaasadeed?", "options": { "a": "Iyadoo awoodda si nabad ah loola kala wareegay xisbiyada dhexdooda", "b": "Iyadoo ciidanku ay dadka qasbeen", "c": "Iyadoo hal xisbi oo keliya uu guuleystay weligiis", "d": "Ma jirin wax bisayl ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Maxaa keena 'is-xilqaan' marka midnimadu jirto?", "options": { "a": "Sababtoo ah dadka ayaa dareemaya inay masuul ka yihiin dalkooda iyo horumarkiisa", "b": "Sababtoo ah waxaa la bixinayaa lacag", "c": "Sababtoo ah xabsiga ayaa laga baqayaa", "d": "Is-xilqaan ma jiro" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Falanqee 'Burburkii weynaa' ee laga dhaxlay maamulkii ciidanka?", "options": { "a": "Wuxuu ka dhashay xukunka kelitaliska ah iyo baabi'inta dimuqraadiyadda oo horseeday dagaal sokeeye", "b": "Wuxuu ka dhashay abaarta", "c": "Wuxuu ka dhashay faragelin shisheeye oo keliya", "d": "Ma jiro wax burbur ah oo dhacay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sidee bay Soomaaliya u gaadhay horumarkii ugu sareeyay xilligii kacaanka?", "options": { "a": "Iyadoo la dhisay warshado, ciidan xooggan, lana qoray afka loona adeegay bulshada bilowgii", "b": "Iyadoo lacag badan laga soo amaahday dibadda", "c": "Iyadoo dadka la wada xiray", "d": "Iyadoo la gubay dhulkii hore" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Sharax doorka Kamaaludiin Saalax uu ku lahaa dhismaha dowladnimada Soomaaliya?", "options": { "a": "Wuxuu ahaa safiir gacan ka geysanayay hagidda iyo talada Soomaaliya ee ku aaddan madax-banaanida", "b": "Wuxuu ahaa wasiirkii waxbarashada", "c": "Wuxuu hindisay calanka", "d": "Wuxuu ahaa taliyaha ciidanka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Maxay ahayd sababta uu maamulkii ciidanka u baabi'iyay 'nidaamka xisbiyada badan'?", "options": { "a": "Si uu u xoojiyo xukunka hal qof uuna meesha uga saaro mucaaradka", "b": "Si dadku u midoobaan", "c": "Si doorashooyinku u sahlanaadaan", "d": "Sababtoo ah xisbiyadu ma shaqeynayn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Falanqee 'Dhaqaalaha hantiwadaagga' ee Soomaaliya xilligii MSB?", "options": { "a": "Wuxuu ahaa nidaam dowladda ay gacanta ku hayso ganacsiga iyo wax-soosaarka si bulshadu u simnaato", "b": "Wuxuu ahaa nidaam ganacsiga xorta ah", "c": "Wuxuu ahaa nidaam diineed", "d": "Ma lahayn wax nidaam dhaqaale ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Saamaynta 'Xeeladaha ciidanka Ingiriiska' ee 1941-1950 ee ku aaddan koonfurta Soomaaliya?", "options": { "a": "Waxay gogol-xaar u ahaayeen in dalku isbeddel siyaasadeed galo lana soo bandhigo nidaamyo cusub", "b": "Waxay gabi ahaanba tirtireen dhaqanka Soomaalida", "c": "Waxay dhisteen caasimadda Muqdisho", "d": "Waxay gacan siiyeen Talyaaniga markii ugu horreysay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Maxaa keeni kara in 'Dowlad xor ah' ay ku biirto gobol kale sida ku xusan dawladnimo gaarsiinta?", "options": { "a": "Sababtoo ah ma rabaan madax-banaani", "b": "Si loo gaaro midnimo weyn iyo xoojinta cududda qaranka (sida koonfur iyo waqooyi)", "c": "Sababtoo ah waa laga qasbay", "d": "Ma jiro wax midnimo ah oo dhacay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 78, "question": "Sharax siday 'kaalinta dadka qaar' u dhiirigelisay dadka kale inay u halgamaan dalka?", "options": { "a": "Iyadoo dadkaas ay tusaale u noqdeen dhabar-adaygga iyo hal-abuurka qaran", "b": "Iyadoo dadka lacag la siiyay", "c": "Iyadoo ciidanku ay amreen", "d": "Ma jirin wax tusaale ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Sidee bay u kala duwanaayeen 'Muddada dawladnimo gaarsiinta' iyo 'Muddada maamulkii ciidanka Ingiriiska'?", "options": { "a": "Ingiriisku wuxuu ahaa maamul dagaal, dawladnimo gaarsiintuna waxay ahayd maamul rayid-ku-meel-gaar ah", "b": "Talyaaniga ayaa ka daran ahaa Ingiriiska", "c": "Labaduba waxay ahaayeen hal maamul", "d": "Ingiriisku wuxuu dalka haystay 10 sano" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 80, "question": "Maxay ahayd sababta kacaanka loo yaqaan 'Afgambi' marka laga hadlayo sharciga?", "options": { "a": "Sababtoo ah wuxuu ku yimid awood ciidan isagoo dumiyay dowladdii sharciga ku dhisnayd", "b": "Sababtoo ah shacabka ayaa codeeyay", "c": "Sababtoo ah Talyaaniga ayaa amray", "d": "Ma ahan afgambi ee waa kacaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Qiimeey doorka 'Xisbiyada Siyaasadeed' ee xilligii 1950-1960?", "options": { "a": "Waxay ahaayeen udub-dhexaadka wacyigelinta dadka iyo u diyaargarowga xornimada", "b": "Waxay ahaayeen kuwa dalka burburiyay", "c": "Waxay u shaqeynayeen gumeystaha", "d": "Ma jirin wax xisbiyo ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 82, "question": "Maxay ka dhigan tahay in dawladnimo gaarsiintu tahay 'Hab cusub oo ka duwan hoosgeynta'?", "options": { "a": "In la tirtiray gumeysigii hore lana keenay nidaam xisaabtan leh oo madax-banaani horseedaya", "b": "In dalka la siiyay lacag", "c": "In dalka la qaybiyo", "d": "In Talyaanigu dalka iskaga baxay 1941" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch3_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch3',
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
    
    # Remove existing his_ch3 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch3']
    
    # Check if his_ch3 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch3' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 3aad: Taariikhda Soomaaliya (1941-1991)",
            "id": "his_ch3"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch3':
                c['title'] = "Cutubka 3aad: Taariikhda Soomaaliya (1941-1991)"
                break
    
    # Add new his_ch3 questions
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

    # Remove existing his_ch3 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch3']
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
