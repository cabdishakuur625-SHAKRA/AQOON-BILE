import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Halkee ayay ku taal xarunta ugu weyn ee Qaramada Midoobay?", "options": { "a": "Geneva", "b": "Nairobi", "c": "New York", "d": "London" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa ku weey labada wadan oo xarumo ku leh Qaramada Midoobay?", "options": { "a": "Kenya iyo Switzerland", "b": "Somalia iyo Djibouti", "c": "Egypt iyo Sudan", "d": "Italy iyo Spain" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 3, "question": "Halkee ayay ku taal xarunta Ururka Jaamacadda Carabta?", "options": { "a": "Riyadh", "b": "Mogadishu", "c": "Cairo", "d": "Baghdad" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 4, "question": "Halkee ayay ku taal xarunta Ururka Midowga Afrika?", "options": { "a": "Nairobi", "b": "Addis Ababa", "c": "Johannesburg", "d": "Cairo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Sanadkee ayay Soomaaliya ku biirtay Ururka Jaamacadda Carabta?", "options": { "a": "1960", "b": "1974", "c": "1991", "d": "2000" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa kuwee wadamo ka mid ah asaasayaashii Jaamacadda Carabta 1945?", "options": { "a": "Somalia iyo Djibouti", "b": "Egypt, Iraq iyo Syria", "c": "Libya iyo Sudan", "d": "Qatar iyo UAE" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Magaaladee ayaa xarun ku meel gaar ah u ah Ururka Iskaashiga Islaamka (OIC)?", "options": { "a": "Mecca", "b": "Medina", "c": "Jeddah", "d": "Riyadh" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay ujeedada ugu weyn ee Qaramada Midoobay?", "options": { "a": "Inay dagaal huriso", "b": "Inay nabad ka dhex dhaliso caalamka", "c": "Inay xukunto wadammada oo dhan", "d": "Inay lacag ururiso" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Maxkamadda Caalamiga ah ee Caddaaladda (ICJ) waxay ku taal magaalada:", "options": { "a": "Vienna", "b": "The Hague (Laahaay)", "c": "Paris", "d": "Rome" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Sanadkee ayaa la aasaasay Ururka Iskaashiga Islaamka (OIC)?", "options": { "a": "1945", "b": "1963", "c": "1969", "d": "1974" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 11, "question": "Wadankee ayay Soomaaliya kaga biirtay Ururka Midowga Afrika?", "options": { "a": "Waa xubin asaase ah", "b": "1974", "c": "1993", "d": "2002" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 12, "question": "Ururkee ayaa fashilmay ka hor intaan la aasaasin Qaramada Midoobay?", "options": { "a": "Ururka Midowga Afrika", "b": "Ururkii Ummadaha (League of Nations)", "c": "Jaamacadda Carabta", "d": "NATO" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Waa maxay magaca hadda loo yaqaan Ururkii Shirweynaha Islaamka?", "options": { "a": "Ururka Midnimada Islaamka", "b": "Ururka Iskaashiga Islaamka", "c": "Midowga Islaamka", "d": "Jaamacadda Islaamka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Immisa xubnood ayuu ka kooban yahay Ururka Iskaashiga Islaamka?", "options": { "a": "22", "b": "54", "c": "57", "d": "193" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 15, "question": "Ururka Midowga Afrika waxaa lagu beddelay ururkii loo yaqaanay:", "options": { "a": "Ururka Ganacsiga Afrika", "b": "Ururka Midnimada Afrika (OAU)", "c": "Ecowas", "d": "IGAD" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Xoghaynta Guud waa laan ka mid ah ururkee?", "options": { "a": "Jaamacadda Carabta", "b": "Qaramada Midoobay", "c": "Midowga Afrika", "d": "Dhammaan ururrada sare" }, "correctAnswer": "d", "difficultyLevel": "easy" },
  { "id": 17, "question": "Goorma ayaa la beddelay magaca Ururka Iskaashiga Islaamka (OIC)?", "options": { "a": "1969", "b": "1991", "c": "2011", "d": "2020" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 18, "question": "Wadankee ayay ku taal magaalada Jidda (Jeddah)?", "options": { "a": "Somalia", "b": "Egypt", "c": "Saudi Arabia", "d": "Jordan" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 19, "question": "Maxkamadda Caalamiga ah waxay ku taal dalka:", "options": { "a": "Holland (Netherlands)", "b": "Austria", "c": "Switzerland", "d": "USA" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 20, "question": "Waa maxay ujeedada Bangiga Horumarinta Islaamka?", "options": { "a": "Inuu hub soo iabiyo", "b": "Inuu amaah siiyo dalalka Islaamka ee saboolka ah", "c": "Inuu xukumo Bangiyada adduunka", "d": "Ma jiro bangi saas ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Goorma ayay Jabuuti ku biirtay Jaamacadda Carabta?", "options": { "a": "1974", "b": "1977", "c": "1960", "d": "1993" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Ururkee ayaa ka shaqeeya horumarinta bulshada iyo dhaqaalaha (UNDP)?", "options": { "a": "Jaamacadda Carabta", "b": "Qaramada Midoobay", "c": "Midowga Afrika", "d": "EAC" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Qudus waxaa loo qoondeeyay inay noqoto xarunta joogtada ah ee ururkee?", "options": { "a": "Jaamacadda Carabta", "b": "Qaramada Midoobay", "c": "Ururka Iskaashiga Islaamka", "d": "Midowga Afrika" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 24, "question": "Dagaalkee ka dib ayaa la aasaasay Qaramada Midoobay?", "options": { "a": "Dagaalkii 1aad", "b": "Dagaalkii 2aad", "c": "Dagaalkii Sokeeye", "d": "Dagaalkii Qaboobaa" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 25, "question": "Sharax sababta Ururkii Ummadaha (League of Nations) loogu beddelay Qaramada Midoobay?", "options": { "a": "Sababtoo ah wuxuu ahaa urur aad u weyn", "b": "Wuxuu ku guul darreystay inuu nabad ka dhex dhaliyo dunida iyo inuu ka baaqsado Dagaalkii 2aad", "c": "Sababtoo ah Mareykanka ayaan xubin ka ahayn", "d": "Ma jiro wax isbeddel ah oo dhacay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Waa maxay farqiga u dhexeeya xubinnimada Jaamacadda Carabta iyo tan Qaramada Midoobay?", "options": { "a": "Ma jiro wax farqi ah", "b": "Jaamacadda Carabta waa dalal carbeed oo xubinnimadoodu ku xiran tahay ogolaansho, halka UN ay u furan tahay wadan kasta oo nabad jecel", "c": "UN waxaa xubin ka noqon kara dalalka carabta kaliya", "d": "Jaamacadda Carabta waxay xubin ka tahay UN-ka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Maxay ahayd ujeedadii Suldaan Cabdul Xamiidka 2aad ee fikirka Jaamacadda Islaamka?", "options": { "a": "Inuu gumaysto dalalka kale", "b": "Inuu mideeyo Muslimiinta hoos yimaada boqortooyadiisa si ay uga hortagaan gumeysiga", "c": "Inuu dhiso warshado cusub", "d": "Inuu saaxiib la noqdo reer Yurub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Waa maxay mas'uuliyadda gaarka ah ee Golaha Ammaanka (Security Council)?", "options": { "a": "Ilaalinta dhaqaalaha adduunka", "b": "Ilaalinta nabadda iyo nabadgelyada caalamka", "c": "Dhismaha iskuullada", "d": "Qaybinta cuntada" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Maxaa dhacay sanadkii 2002 oo ku saabsan Midowga Afrika?", "options": { "a": "Waxaa la aasaasay Ururka Midnimada Afrika", "b": "Ururka Midowga Afrika ayaa si rasmi ah u beddelay Ururka Midnimada Afrika (OAU)", "c": "Dhammaan dalalka Afrika ayaa midoobay", "d": "Dagaalladii Afrika ayaa dhammaaday" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Waa maxay hindisaha 'Hishiiskii Abuuja' ee 1991?", "options": { "a": "In la dhiso ciidan Afrikan ah", "b": "In la aasaaso Ururka Dhaqaalaha Afrika", "c": "In la xoreeyo Koonfur Afrika", "d": "In la joojiyo abaaraha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Maxay ahayd soo jeedintii Madaxweynihii Soomaaliya Aadan Cabdulle Cusmaan ee 1967?", "options": { "a": "In la dhiso Jaamacadda Carabta", "b": "In la aasaaso Ururka Shirweynaha Islaamka", "c": "In Soomaaliya la xoreeyo", "d": "In la dhiso Midowga Afrika" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Waa maxay ujeeddooyinka bulshada ee Ururka Iskaashiga Islaamka?", "options": { "a": "Samaynta bangiyo", "b": "Cirib-tirka midab takoorka iyo gumeysiga", "c": "Dagaal ka dhan ah reer Galbeedka", "d": "Samaynta khariidado cusub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Maxay ku kala duwan yihiin fikradaha Nikruuma iyo Niyareeri ee ku aaddan midnimada Afrika?", "options": { "a": "Ma jirin wax ay isku khilaafeen", "b": "Nikruuma wuxuu rabay midnimo degdeg ah, halka Niyareeri uu rabay in marka hore qaranimada la adkeeyo", "c": "Nikruuma wuxuu rabay hanti-wadaag, Niyareeri-na hanti-goosad", "d": "Labaduba waxay rabeen in Yurub dib loogu laabto" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Waa maxay sababta Jidda loogu doortay xarunta ku meel gaarka ah ee OIC?", "options": { "a": "Sababtoo ah waa magaalada ugu weyn dalalka Islaamka", "b": "Sababtoo ah xarunta joogtada ah (Qudus) ayaa weli gumeysi ku jirta", "c": "Sababtoo ah Boqorka Sacuudiga ayaa saas rabay", "d": "Waa xarun ganacsi oo kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Maxaa lagu go'aamiyay shirkii Kaazakhistaan ee sanadkii 2011 (OIC)?", "options": { "a": "In magaca loo beddelo Ururka Iskaashiga Islaamka, shirarkana la qabto labadii sanaba mar", "b": "In magaca loo beddelo Midowga Islaamka", "c": "In Soomaaliya laga saaro ururka", "d": "In Jidda laga guuro" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Waa maxay kaalinta Golaha Guud (General Assembly) ee miisaaniyadda UN-ka?", "options": { "a": "Wuxuu bixiyaa lacagta oo dhan", "b": "Wuxuu tixgeliyaa oo ansixiyaa miisaaniyadda ururka", "c": "Ma laha wax shaqo ah oo ku saabsan lacagta", "d": "Wuxuu u qaybiyaa lacagta dalalka saboolka ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Maxay yihiin caqabadaha gudaha ee haysta Midowga Afrika?", "options": { "a": "Midab kala sooca kaliya", "b": "Xallinta khilaafaadka, af-gembiyada, iyo dhaqaalaha daciifka ah", "c": "Dagaalkii qaboobaa", "d": "Gumeysiga reer Yurub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Sidee buu Ururka Iskaashiga Islaamka u caawiyaa dalalka saboolka ah?", "options": { "a": "Inuu hub u diro", "b": "Inuu siiyo amaah dhaqaale iyo samaynta Bangiga Horumarinta Islaamka", "c": "Inuu u dhiso warshado hubka ah", "d": "Ma caawiyo gabi ahaanba" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Maxaa loola jeedaa 'Dardar gelinta ka qeyb galka Afrika ee Ururadda caalamiga'?", "options": { "a": "In Afrika ay ka baxdo UN-ka", "b": "In Afrika ay cod xoog leh ku yeelato go'aannada caalamiga ah", "c": "In Afrika ay samaysato urur u gaar ah", "d": "In Afrika ay Yurub ku biirto" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Shaqada Golaha Guud ee UN-ka sidee bay u saamaysaa xubnaha?", "options": { "a": "Go'aannadoodu waa qasab", "b": "Go'aannada Golaha Guud kuma xirna xubnaha (ma ahan kuwo qasab ah)", "c": "Golaha Guud ma gaaro go'aan", "d": "Golaha Guud wuxuu xukumaa madaxda adduunka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Waa maxay ujeedada 'Qorshe howleedka Lagoos' ee 1980?", "options": { "a": "In la bilaabo dagaal ka dhan ah gumeysiga", "b": "In la hirgeliyo barnaamijyo horumarineed si looga hortago dhibaatooyinka", "c": "In magaca ururka la beddelo", "d": "In Addis Ababa xarunta laga dhigo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Maxay ahayd ujeeddadii laga lahaa 'Baaqii Manaroofiya' ee 1979?", "options": { "a": "In la helo isku filnaansho heer sare ah oo dhinaca Afrika ah", "b": "In la eryo gumeystayaasha", "c": "In la dhiso ciidan Afrikan ah", "d": "In la mideeyo diimaha Afrika" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Sidee bay Qaramada Midoobay u horumarisaa dhaqaalaha dalalka?", "options": { "a": "Inay canshuur ka qaaddo", "b": "Iyada oo loo marayo Barnaamijkeeda Horumarinta (UNDP)", "c": "Inay siiso hub", "d": "Ma jirto waxqabad dhaqaale oo ay leedahay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Waa maxay mas'uuliyadda Xoghaynta Guud ee Jaamacadda Carabta?", "options": { "a": "Inay ciidamada amarto", "b": "Inay maamusho hawlaha maalinlaha ah ee ururka", "c": "Inay xuduudaha beddesho", "d": "Shaqo ma laha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 45, "question": "Maxay ururrada goboleed (sida OAU) u asaasmeen intii u dhaxeysay 1958-1963?", "options": { "a": "Inay Yurub ku daydaan", "b": "Si ay isugu keenaan Afrika oo ay u mideeyaan halganka madax-bannaanida", "c": "Si ay u bilaaboan ganacsiga hubka", "d": "Si ay Mareykanka u taageeraan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxaa xiriir ah oo ka dhexeeya sayniska, teknoolojiyada iyo OIC?", "options": { "a": "OIC waxay mamnuucday sayniska", "b": "Sayniska iyo teknoolojiyadu waxay ka mid yihiin waxqabadyada ururku muhiimadda siiyo", "c": "Waa urur diimeed oo kaliya", "d": "Sayniska waxaa loogu talagalay dalalka reer Galbeedka kaliya" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 47, "question": "Xaaladda 'Filnaansho la’aan xoogga dadka' ee Afrika maxay ka dhigan tahay?", "options": { "a": "In dadku ay aad u badan yihiin", "b": "In xoogga dadka iyo aqoontooda aan si buuxda looga faa'iideysan karin", "c": "In dadku ay wada shaqeynayaan", "d": "In Afrika aysan dad lahayn" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 48, "question": "Waa maxay 'Dhexdhexaadnimada' lagu xusay waxqabadyada OIC?", "options": { "a": "Inaan la dhex galin khilaafaadka", "b": "In la dhiirigeliyo fikirka dhexdhexaadka ah ee Islaamka, lagana fogaado xagjirnimada", "c": "Inaan cidna la caawin", "d": "Waa fikir dhinaca dhaqaalaha ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 49, "question": "Maxay ahayd ujeeddada shirkii Durban ee sanadkii 2000?", "options": { "a": "In laga baxo Midowga Afrika", "b": "In lagu saxiixo sharciga asaasiga ah ee lagu dhisayo Midowga Afrika", "c": "In la xoreeyo Falastiin", "d": "In magaalada Durban xarun laga dhigo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 50, "question": "Sidee bay xubnaha Qaramada Midoobay u aqbalaan waajibaadka axdiga?", "options": { "a": "Iyagoo bixinaya lacag kaliya", "b": "Iyagoo aqbalaya nabadda iyo fulinta tallaabooyinka ku xusan axdiga", "c": "Iyagoo hubkooda dhiibaya", "d": "Iyagoo beddelaya calankooda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 51, "question": "Maxay dalalka Carabta u aasaaseen Jaamacadda Carabta 1945?", "options": { "a": "Si ay nabad ugu raadiyaan Yurub", "b": "Si ay isugu duwaan aragtidooda siyaasadeed, ugana gudbaan caqabadaha dhaqaale iyo bulsho", "c": "Si ay u qabsadaan Afrika", "d": "Ma jirin sabab cad oo loo aasaasay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 52, "question": "Falanqee sababta ururrada goboleed iyo kuwa caalamiga ah ay u noqdeen lagama maarmaan ka dib Dagaalkii 2aad?", "options": { "a": "Maadaama dalalku isku filnaan waayeen", "b": "Burburkii dagaalka ayaa keenay baahi loo qabo nidaam iskaashi oo ilaaliya nabadda, xaliya khilaafaadka, dibna u dhiska dhaqaalaha", "c": "Sababtoo ah Mareykanka ayaa ku qasbay dalalka kale", "d": "Si loo bilaabo Dagaalkii Qaboobaa" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Qiimeey doorka 'Golaha Ammaanka' ee Qaramada Midoobay marka la eego madax-bannaanida dalalka xubnaha ka ah?", "options": { "a": "Ma laha wax saameyn ah", "b": "Goluhu wuxuu awood u leeyahay inuu qaado tallaabooyin qasab ah (sira cunaqabateyn ama milatari) haddii nabadgelyada caalamka la khatar geliyo", "c": "Wuxuu dalalka ku amraa inay beddelaan madaxdooda", "d": "Wuxuu xubin kasta siiyaa awoodda Veto" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Sidee bay u kala duwan yihiin caqabadaha 'Gudaha' iyo kuwa 'Dibadda' ee haysata Midowga Afrika?", "options": { "a": "Caqabadaha gudaha waa kuwa dhaqaale, kuwa dibaddana waa kuwa bulsho", "b": "Guduhu waa dhismaha hay'ado xasilloon iyo khilaafaadka gudaha, dibadduna waa raadadkii gumeysiga iyo midab-kala-sooca", "c": "Labaduba waa isku mid oo ma kala duwana", "d": "Dibadda waa gumeysiga, gudahana waa is-ballaarinta Jabbaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Sharax xiriirka ka dhexeeya fikirka Jamaal Al-Diin Al-Afgaani iyo aasaaskii OIC ee 1969?", "options": { "a": "Ma jiro wax xiriir ah oo ka dhexeeya", "b": "Fikirka Al-Afgaani ee ahaa 'Jaamacadda Islaamka' wuxuu ahaa abuurka horseeday midnimada Muslimiinta, taasoo dhabowday markii OIC la dhisay", "c": "Al-Afgaani ayaa ahaa xoghayihii ugu horreeyay ee OIC", "d": "OIC waxay diidday fikradihii Al-Afgaani" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Qiimeey saameynta ay Qaramada Midoobay ku leedahay go'aannada dalalka ka dib markii lagu taliyey Golaha Ammaanka?", "options": { "a": "Go'aannadu waxay noqdaan kuwo aan la fulin karin", "b": "Go'aanka kama dambaysta ah ee xubinnimada ama qaraashka wuxuu saameeyaa aqoonsiga caalamiga ah iyo xilka saaran wadanka", "c": "UN waxay maamushaa lacagta wadammada oo dhan", "d": "UN ma laha awood go'aan gaarid" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sidee bay u kala duwan yihiin 'Hindisaha 1aad' (Nikruuma vs Niyareeri) ee midnimada Afrika?", "options": { "a": "Waxay ku heshiiyeen in Afrika hal magaalo laga dhigo", "b": "Nikruuma wuxuu u arkay midnimada siyaasadeed inay tahay badbaadada kaliya, halka Niyareeri uu rabo in marka hore dalalka daciifka ah ay xoogaystaan", "c": "Nikruuma wuxuu u hiiliyay gumeysiga", "d": "Niyareeri wuxuu rabay in Midowga Afrika laga saaro UN-ka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Falanqee ujeedooyinka siyaasadeed ee OIC marka laga hadlayo 'Caddaaladda iyo Nabadda'?", "options": { "a": "Waa inay Muslimiinta oo dhan ka dhigaan hal wadan", "b": "Waa adkeynta midnimada iyo taageeridda nabadda caalamiga ah iyadoo lagu saleynayo caddaalad iyo xushmad dhex marta xubnaha", "c": "Inay nabad ka dhex dhaliso Mareykanka iyo Ruushka", "d": "Inay caddaaladda ku koobto dalalka carabta kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Waa maxay muhiimadda 'Hishiiskii Abuuja' (1991) ee masiirka dhaqaale ee Afrika?", "options": { "a": "In Afrika ay lacag ka amaahato OIC", "b": "Wuxuu dhigay aasaaska suuq ka dhex dhasha Afrika si loo gaaro madax-bannaani dhaqaale iyo is-kaashi", "c": "Wuxuu mamnuucay ganacsiga dibadda", "d": "Wuxuu Afrika ka dhigay qayb ka mid ah dhaqaalaha Yurub" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Maxay xarunta OIC u tahay 'Ku-meel-gaar' (Temporary) tan iyo markii la aasaasay?", "options": { "a": "Sababtoo ah Jidda ma ahan meel ku habboon", "b": "Maadaama ururku go'aamiyay in xarunta joogtada ah ay noqoto Qudus marka laga xoreeyo gumeysiga Israa'iil", "c": "Sababtoo ah ururka ayaa dhowaan dumi doona", "d": "Ma jiro heshiis laga gaaray xarunta joogtada ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sharax saameynta 'Dhexdhexaadnimada' (Moderation) ee laga rabo dalalka xubnaha ka ah OIC?", "options": { "a": "Inaan la dhex galin siyaasadda UN-ka", "b": "In la dhiirigeliyo wada-hadalka diimaha iyo ka fogaanshaha xagjirnimada si loo muujiyo wejiga nabadda ee Islaamka", "c": "In dalalku aysan ciidan yeelan", "d": "In la dhexdhexaadiyo Mareykanka iyo Shiinaha" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 62, "question": "Qiimeey doorka 'Golaha Nabadda iyo Nabadgelyada Afrika' (PSC) ee ku dhex jira Midowga Afrika?", "options": { "a": "Wuxuu go'aamiyaa sicirka macishadda", "b": "Waa hay'adda mas'uulka ka ah ka hortagga khilaafaadka, nabad-ilaalinta, iyo xasilinta dalalka Afrika ee dhibataysan", "c": "Wuxuu maamulaa doorashooyinka adduunka", "d": "Wuxuu Afrika ka ilaaliyaa saameynta OIC" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 63, "question": "Sidee bay Qaramada Midoobay ula tacaashaa 'Fashilka' ururradii ka horreeyay (League of Nations)?", "options": { "a": "Iyadoo lacag badan ururinaysa", "b": "Iyadoo abuurtay hay'ado awood badan leh (sida Golaha Ammaanka) iyo ka qayb-gelinta quwadaha waaweyn", "c": "Iyadoo xarunta New York ka dhigtay", "d": "Iyadoo aan wax xiriir ah la lahaan dalalka guuldareystay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Falanqee xiriirka u dhexeeya 'Horumarka Joogtada ah' (Sustainable Development) iyo waxqabadyada OIC?", "options": { "a": "OIC ma taageerto horumarka joogtada ah", "b": "Waa mid ka mid ah tiirarka waxqabadka ururka si loo hubiyo in kheyraadka dalalka Islaamka loo isticmaalo mustaqbalka fog", "c": "Waa horumar dhinaca milatariga ah oo kaliya", "d": "Waa horumar laga soo minguuriyay Jaamacadda Carabta" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sharax doorka Soomaaliya ee aasaaskii OIC sanadkii 1969?", "options": { "a": "Soomaaliya waxay ahayd dalkii ugu dambeeyay ee ku biiray", "b": "Soomaaliya waxay ahayd dalkii soo jeediyay fikradda aasaaska (iyadoo loo marayo Aadan Cadde), waana xubin asaase ah", "c": "Soomaaliya waxay diidday inay ka qayb gasho shirkii u horreeyay", "d": "Soomaaliya waxay bixisay miisaaniyadda ururka oo dhan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 66, "question": "Qiimeey saameynta 'Ka-hortagga Af-gembiyada' ee ku jirta ujeedooyinka Midowga Afrika?", "options": { "a": "Ma laha wax saameyn ah", "b": "Waxay muhiim u tahay xasiloonida siyaasadeed, iyadoo ururku cunaqabateyn saaro dawladaha xoogga ku yimaada", "c": "Midowga Afrika wuxuu dhiirigeliyaa af-gembiyada", "d": "Waa ujeeddo loogu talagalay dalalka carabta" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee buu u isbeddelay jawiga 'Shirweynaha OIC' ka dib kalfadhigii 38aad ee 2011?", "options": { "a": "Shirarkii ayaa la joojiyay", "b": "Waxaa la kordhiyay tirada shirarka (labadii sanaba mar) si loola socdo isbeddelada degdegga ah ee adduunka", "c": "Shirarka waxaa lagu qabtaa Mareykanka kaliya", "d": "Shirarku waxay noqdeen kuwo qarsoodi ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 68, "question": "Maxay 'Xalinta khilaafaadka' u tahay tiir muhiim u ah Jaamacadda Carabta?", "options": { "a": "Si looga hortago fara-gelinta shisheeye iyo in la ilaaliyo midnimada dalalka Carabta", "b": "Si loo bilaabo dagaal ka dhan ah Afrika", "c": "Si loo daciifiyo xubnaha qaar", "d": "Si looga farxiyo Qaramada Midoobay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Falanqee ujeedada 'Iskaashiga cusub ee Horumarinta Afrika' (NEPAD) ee 2001?", "options": { "a": "Waa in Afrika ay deyn ka cafiso Yurub", "b": "Waa barnaamij istiraatiiji ah oo lagu cirib-tirayo faqriga laguna gaarayo kuraas joogto ah oo UN-ka ah", "c": "Waa hindise lagu dhisayo ciidanka badda ee Afrika", "d": "Ma jiro hindise caynkaas ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 70, "question": "Qiimeey saameynta 'Midab-kala-sooca' (Apartheid) ee ay la tacaalaysay OAU/AU?", "options": { "a": "Waxay ahayd caqabad hortaagnayd sharafta iyo xorriyadda Afrika, ururka ayaana horseeday in meesha laga saaro", "b": "Ururku wuxuu taageeray midab-kala-sooca", "c": "Midab-kala-sooca wuxuu ka jiray dalalka carabta kaliya", "d": "Ma lahayn wax saameyn ah oo muuqda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Sharax saameynta 'Badqabka Cunnada' (Food Security) ee ku jirta qorshaha OIC?", "options": { "a": "In dalalka Islaamku ay cunta ka iibsadaan Yurub", "b": "Waa qorshe lagu hubinayo in dalalka xubnaha ka ah ay isku fillaadaan xagga wax-soo-saarka beeraha iyo kaydka cuntada", "c": "In cuntada la yareeyo si loo keydiyo lacag", "d": "Waa qorshe loogu talagalay dalalka hodanka ah kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sidee bay 'Ujeeddooyinka Dhaqaale' ee OIC u saameeyaan xiriirka dalalka hodanka ah iyo kuwa saboolka ah?", "options": { "a": "Waxay sii kordhiyaan farqiga u dhexeeya", "b": "Waxay dhiirigeliyaan in dalalka hodanka ah ay maalgashi iyo amaah siiyaan kuwa saboolka ah si loo simo horumarka", "c": "Dalalka saboolka ah waa inay canshuur siiyaan kuwa hodanka ah", "d": "Xiriirka dhaqaale ma khuseeyo OIC" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 73, "question": "Falanqee xaaladda Afrika ka hor bartamihii qarnigii 20aad sida ku xusan casharka?", "options": { "a": "Waxay ahayd qaarad aad u horumarsan", "b": "Waxay ahayd goob ay ku hardamaan gumeystayaashii reer Yurub si ay gacanta ugu dhigaan kheyraadkeeda", "c": "Waxay ahayd goob nabad ah oo aan gumeysi arkin", "d": "Waxay ahayd xarunta adduunka ee ganacsiga" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 74, "question": "Maxay ahayd muhiimadda shirkii 'Qaahira' ee 1995 ee Midowga Afrika?", "options": { "a": "In Addis Ababa laga guuro", "b": "Wuxuu dejiyay qodobo muhiim u ah dardar-gelinta iskaashiga dhaqaalaha iyo bulshada Afrika", "c": "Wuxuu bilaabay dagaalka ka dhanka ah argagixisada", "d": "Wuxuu joojiyay xiriirkii UN-ka iyo Afrika" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 75, "question": "Qiimeey xiriirka ka dhexeeya 'Golaha Baarlamaanka Afrika' iyo qaranimada dalalka xubnaha ka ah?", "options": { "a": "Baarlamaanku wuxuu baabi'iyaa baarlamaannada qaranka", "b": "Waa gole wadatashi iyo isku-duwidda sharciyada si loo gaaro midaynta Afrika mustaqbalka", "c": "Ma laha wax shaqo ah", "d": "Wuxuu hoos yimaadaa baarlamaanka Yurub" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 76, "question": "Sharax micnaha 'Tixgelinta mabaadii’da guud ee nabadeynta' ee ay qabato UN-ka?", "options": { "a": "In la dhiso ciidamo badan", "b": "In la dejiyo xeerar iyo talooyin caalami ah oo looga baaqsan karo iska hor-imaadyada mustaqbalka", "c": "In la baabi'iyo xuduudaha dalalka", "d": "In la taageero hal dhinac oo dagaalamaya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 77, "question": "Sidee bay Ururka Iskaashiga Islaamku uga shaqeeyaa 'Qadiyadda Falastiin'?", "options": { "a": "Inuu hub u diro Israa'iil", "b": "Inuu taageero buuxda siiyo xuquuqda reer Falastiin iyo madax-bannaanida Qudus", "c": "Inuu ka aamuso dhibaatada ka jirta halkaas", "d": "Inuu dhaho Falastiin waa inay ka baxdaa dhulkeeda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 78, "question": "Falanqee caqabadda 'Ka-hortagga raadadkii Dagaalkii Qaboobaa' ee Midowga Afrika?", "options": { "a": "In Afrika ay laba isbahaysi u qaybsanto", "b": "In laga fogeeyo Afrika inay noqoto goob lagu loolamo, laguna ilaaliyo dhexdhexaadnimada", "c": "In Afrika ay Ruushka raacdo kaliya", "d": "In la baabi'iyo xiriirka Mareykanka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 79, "question": "Maxay ahayd ujeeddada ka dambaysay dhismaha 'Guddiga Wakiillada' ee Midowga Afrika?", "options": { "a": "Inay go'aan ka gaaraan miisaaniyadda", "b": "Inay u diyaariyaan shirarka Golaha Madaxda iyo inay fududeeyaan xiriirka hay'adaha ururka", "c": "Inay matalaan dalalka Yurub", "d": "Inay qoraan taariikhda Afrika" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 80, "question": "Qiimeey muhiimadda 'Ladagaalanka Argagixisada' ee ku jirta waxqabadyada OIC?", "options": { "a": "Si loo ilaaliyo amniga dalalka Islaamka iyo in dunida loo muujiyo in Islaamku ka soo horjeedo rabshadda", "b": "Si loo weeraro dalalka kale", "c": "In argagixisada lacag la siiyo", "d": "Argagixisadu ma khuseeyo OIC" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Sidee bay 'Ujeeddooyinka Siyaasadeed' ee OIC u saameeyaan nabadda caalamka?", "options": { "a": "Waxay kordhiyaan colaadda", "b": "Waxay dhiirigeliyaan is-afgaradka xubnaha iyo dalalka kale si loo gaaro nabad ku dhisneyn caddaalad", "c": "OIC ma laha saameyn siyaasadeed", "d": "Waxay u hiiliyaan hal quwad oo kaliya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 82, "question": "Falanqee xiriirka ka dhexeeya 'Isbeddelka Cimilada' iyo dalalka Islaamka sida ku xusan OIC?", "options": { "a": "Cimiladu ma saameeyo dalalka Islaamka", "b": "OIC waxay ku dartay qorshaheeda sidii looga wada shaqeyn lahaa saameynta deegaanka iyo cimilada ee dalalka xubnaha ah", "c": "Isbeddelka cimiladu waa been", "d": "Dalalka Islaamka ayaa mas'uul ka ah isbeddelka cimilada" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 83, "question": "Qiimeey doorka 'Xoghayaha Guud' ee OIC ee fulinta go'aannada?", "options": { "a": "Isaga ayaa iska leh go'aanka ugu dambeeya", "b": "Wuxuu mas'uul ka yahay dabagalka iyo fulinta go'aannadii ka soo baxay shirarka madaxda iyo wasiirrada", "c": "Xoghayuhu ma fuliyo go'aanno", "d": "Xoghayuhu wuxuu u shaqeeyaa UN-ka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 84, "question": "Sharax muhiimadda 'Maal-gashiga iyo Maal-gelinta' ee OIC ee mustaqbalka dalalka xubnaha ka ah?", "options": { "a": "In lacagta la dhigo bangiyada reer Galbeedka", "b": "Waa dariiq lagu kordhinayo wax-soo-saarka gudaha laguna yareynayo ku tiirsanaanta gumeysiga cusub", "c": "In lacag lagu iibsado hub", "d": "Ma jiro maal-gashi uu ururku sameeyo" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 85, "question": "Sidee bay 'Hormarin Joogto ah' (Sustainable Development) iyo 'Cirib-tirka Faqriga' isugu xiran yihiin qorshaha Midowga Afrika?", "options": { "a": "Ma isku xirna", "b": "Faqri la'aantu waa tiirka koowaad ee lagu gaari karo horumar isku kalsoon oo waara oo Afrika ah", "c": "Horumarku wuxuu yimaadaa faqriga ka dambeeyo", "d": "Waa qorshe ay UN-ka u dejiyeen Afrika" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 86, "question": "Qiimeey saameynta 'Xalinta Khilaafaadka' ee PSC ay ku leedahay hoos u dhaca af-gembiyada Afrika?", "options": { "a": "Af-gembiyada waa ay kordheen", "b": "Dadaallada PSC waxay yareeyeen fursadaha af-gembiyada iyadoo la dhiirigelinayo dimuqraadiyadda iyo xasiloonida", "c": "PSC ma gasho arimaha af-gembiyada", "d": "Waa hay'ad daciif ah oo aan waxba qaban" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 87, "question": "Maxay ahayd ujeeddada dhabta ah ee 'Hindisaha 6aad' (NEPAD) ee la bilaabay 2001?", "options": { "a": "In Afrika lagu mideeyo hal lacag", "b": "In la dhiso iskaashi cusub oo caalami ah si loo dardar-geliyo horumarka dhaqaalaha Afrika", "c": "In la weeraro gumeystayaashii hore", "d": "In la baabi'iyo xuduudaha dalalka" }, "correctAnswer": "b", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch6_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch6',
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
    
    # Remove existing his_ch6 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch6']
    
    # Check if his_ch6 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch6' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 6aad: Ururrada Caalamiga ah iyo kuwa Goboleed",
            "id": "his_ch6"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch6':
                c['title'] = "Cutubka 6aad: Ururrada Caalamiga ah iyo kuwa Goboleed"
                break
    
    # Add new his_ch6 questions
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

    # Remove existing his_ch6 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch6']
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
