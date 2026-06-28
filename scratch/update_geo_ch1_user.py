import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha kelmada 'Jiyoolooji'?", "options": { "a": "Barashada xiddigaha", "b": "Barashada dhulka iyo isbeddelladiisa", "c": "Barashada badaha kaliya", "d": "Barashada dhirta" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa ku bama laanta ku takhasusta saliidda iyo dhaqaalaha?", "options": { "a": "Jiyooloojiga bay’ada", "b": "Jiyooloojiga saliidda iyo dhaqaalaha", "c": "Jiyooloojiga waxbarashada", "d": "Jiyooloojiga handasada" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Imisa sano ayaa lagu qiyaasaa da'da qolofta dhulka?", "options": { "a": "1500 milyan sano", "b": "2000 milyan sano", "c": "5000 milyan sano", "d": "1000 milyan sano" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa ku bama waaga ugu waqtiga gaaban dhammaan waayada jiyooloojiga?", "options": { "a": "Waaga koowaad", "b": "Waaga cusub", "c": "Waaga labaad", "d": "Waaga saddexaad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Macaadiinta dahabka iyo qalinka, waagee baa la helaa?", "options": { "a": "Waaga cusub", "b": "Kambiriyan ka horreeye", "c": "Waaga labaad", "d": "Waaga saddexaad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Da'da dhulka guud ahaan waxaa lagu qiyaasaa?", "options": { "a": "2000 milyan sano", "b": "3000 milyan sano", "c": "1500 milyan sano", "d": "4000 milyan sano" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 7, "question": "Waa ku bama waaga loo yaqaano 'Waagii nolosha dhexe'?", "options": { "a": "Baaliyosooik", "b": "Mesosooik", "c": "Kinozoik", "d": "Kambiriyan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Saliidda inta badan waagee bay sameysantay?", "options": { "a": "Kambiriyan ka horreeye", "b": "Waaga labaad (Mesosooik)", "c": "Waaga koowaad", "d": "Waaga koowaad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Culimada Muslimiinta maxay cabbireen sanadkii 210 Hijriga?", "options": { "a": "Dhexroorka iyo wareegga dhulka", "b": "Dhererka buuraha", "c": "Qoto dheerka badda", "d": "Miisaanka dhagaxyada" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 10, "question": "Qaab dhismeedka dhulka Soomaaliya wuxuu ka yimid sagxaddii hore ee?", "options": { "a": "Aasiya", "b": "Afrika", "c": "Yurub", "d": "Ameerika" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Sagxadda hore ee Soomaaliya waxay qeyb ka ahayd qaaraddii qadiimiga ahayd ee?", "options": { "a": "Laaraasiya", "b": "Junduwanaland", "c": "Atilaantis", "d": "Baajiya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa ku bama mid ka mid ah noocyada carrada Soomaaliya?", "options": { "a": "Carro dhoobo madow", "b": "Carro baraf leh", "c": "Carro dhuxul ah", "d": "Carro dahab ah" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 13, "question": "Maxay dadka Soomaaliyeed u jaraan dhirta?", "options": { "a": "Si ay u helaan dhuxul", "b": "Si ay u helaan biyo", "c": "Si ay u helaan dahab", "d": "Si ay u helaan hilib" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 14, "question": "Jiyooloojigu wuxuu darsaa saddexda qeyb ee dhulka oo kala ah: Adkaha, Dareeraha iyo?", "options": { "a": "Cuntada", "b": "Hawada", "c": "Dabka", "d": "Barafka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Waagee baa la helaa dhagaxa nuuriyadda ee sibidhka loo adeegsado?", "options": { "a": "Waaga koowaad", "b": "Waaga saddexaad (Kinozoi)", "c": "Kambiriyan ka horreeye", "d": "Waaga cusub" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Dherer ahaan, waaga labaad ma ka gaaban yahay waaga koowaad?", "options": { "a": "Haa", "b": "Maya", "c": "Waa isku mid", "d": "Laba jeer ayuu ka dheer yahay" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 17, "question": "Waa ku bama waaga loogu adeegsado faarkiisa simidda waddooyinka?", "options": { "a": "Waaga koowaad", "b": "Waaga cusub", "c": "Waaga labaad", "d": "Kambiriyan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Xilligii Juraasik wuxuu ka tirsan yahay waagee?", "options": { "a": "Waaga koowaad", "b": "Waaga labaad", "c": "Waaga saddexaad", "d": "Waaga afaraad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Waa maxay dhibaatada ugu weyn ee haysata carrada Soomaaliya?", "options": { "a": "Carro guur (Erosion)", "b": "Biyo badan", "c": "Baraf", "d": "Dhulgariir maalinle ah" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 20, "question": "Waa ku bama waaga ugu dheer waayada Jiyooloojiga?", "options": { "a": "Waaga koowaad (Baaliyosooik)", "b": "Waaga labaad", "c": "Waaga saddexaad", "d": "Waaga cusub" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 21, "question": "Maxay tahay sababta waaga koowaad looga waayo dhulka Soomaaliya inta badan?", "options": { "a": "Sababtoo ah marna ma jirin", "b": "Wuxuu ku baaba'ay carro guurkii dhacay waagii labaad ama wuu ku qarsoon yahay dhul ka da' yar", "c": "Sababtoo ah badda ayaa qaadday", "d": "Sababtoo ah foolkaano ayaa gubtay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 22, "question": "Jiyooloojiga handasadu muxuu darsaa?", "options": { "a": "Dhismaha waddooyinka iyo guryaha", "b": "Barashada dhirta", "c": "Saliidda dhulka", "d": "Cimilada" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 23, "question": "Waa maxay farqiga u dhexeeya 'solid earth' iyo 'liquid earth'?", "options": { "a": "Solid waa adke (dhagax), liquid waa dareere (biyo/magma)", "b": "Solid waa hawo, liquid waa dhagax", "c": "Solid waa biyo, liquid waa hawo", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 24, "question": "Xilliga 'Kiritaasiga' (Chalk) maxay tahay ahmiyaddiisa dhaqaale?", "options": { "a": "Waa isha ugu muhiimsan saliidda iyo tamarta maanta", "b": "Waxaa laga helaa dahab kaliya", "c": "Waxaa laga helaa dhuxul dhagax", "d": "Waa carrada beeraha kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 25, "question": "Muxuu ahaa saamaynta 'Badda Ayuusiin' ku yeelatay Soomaaliya waagii saddexaad?", "options": { "a": "Waxay keentaa in badda ay gudaha u soo gasho waqooyi galbeed", "b": "Waxay qalajisay webiyada", "c": "Waxay abuurtay buuro dhaadheer", "d": "Waxay keentaa in dhulku kordho" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 26, "question": "Maxaa keena carro guurka dhulka Soomaaliya?", "options": { "a": "Dabaylaha iyo biyaha", "b": "Dhirta badan", "c": "Barafka dhalaalaya", "d": "Dayaxa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 27, "question": "Dhaqdhaqaaqa Gacanka Cadmeed iyo Badda Cas maxay ku soo kordhiyeen Soomaaliya?", "options": { "a": "Waxay saameeyeen qaab dhismeedka dhulka (jeexyo)", "b": "Waxay keeneen carro madow", "c": "Waxay abuureen dhir cusub", "d": "Ma jiro wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 28, "question": "Xilliga 'Juraasik' dhadhaabyadiisa halkee baa laga helaa Soomaaliya?", "options": { "a": "Galbeedka (Boorama) iyo bartamaha", "b": "Koonfurta fog kaliya", "c": "Xeebaha Muqdisho kaliya", "d": "Puntland kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Maxay culimada Muslimiinta uga natiijo dhowaadeen saynisyahanada casriga ah?", "options": { "a": "Cabbiraadda wareegga iyo dhexroorka dhulka", "b": "Magacaabista waayada", "c": "Soo saarista sibidhka", "d": "Barashada xiddigaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Waa ku bama waaga lagu tilmaamo 'Nolosha hore'?", "options": { "a": "Mesosooik", "b": "Baaliyosooik", "c": "Kinozoik", "d": "Waaga cusub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Macaadiinta 'shucaaca bixisa' waagee baa la helaa?", "options": { "a": "Kambiriyan ka horreeye", "b": "Waaga labaad", "c": "Waaga saddexaad", "d": "Waaga cusub" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Carrada 'foolkaano' maxay ka timid?", "options": { "a": "Dhaqdhaqaaqa volcano-yada", "b": "Webiyada", "c": "Badda", "d": "Dhirta qudhuntay" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 33, "question": "Faarka wabiga maxaa loo adeegsadaa?", "options": { "a": "Carrada beeraha oo aad u nafaqo badan", "b": "Dhisidda buundooyinka", "c": "Samaynta quraaradaha", "d": "Soo saarista dahabka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay Soomaaliya u leedahay 'Dhadhaab shiileedyo' (Metamorphic rocks)?", "options": { "a": "Sababtoo ah rogrogan dhulka ah iyo kuleylka bannaanka u soo baxay", "b": "Sababtoo ah barafka ayaa u dhalan rogay", "c": "Sababtoo ah dadka ayaa shiilay", "d": "Ma lahan wax dhadhaab shiileed ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Xagga dhererka, qeex silsiladda waayada jiyooloojiga laga bilaabo kan ugu dheer?", "options": { "a": "Koowaad > Labaad > Saddexaad > Cusub", "b": "Cusub > Saddexaad > Labaad > Koowaad", "c": "Labaad > Koowaad > Cusub > Saddexaad", "d": "Saddexaad > Labaad > Koowaad > Cusub" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Xilliga 'Baaliyoosiin' waa waagee?", "options": { "a": "Waaga koowaad", "b": "Waaga afaraad", "c": "Waaga labaad", "d": "Kambiriyan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Maxaa lagu gartaa dhadhaabyada 'wiriq ah' ee Soomaaliya xilligan?", "options": { "a": "Waxay ka maran yihiin foosilis (fossils)", "b": "Waxay leeyihiin foosilis badan", "c": "Waa dhagaxyo jilicsan", "d": "Dhagaxyadaas badda ayaa laga helaa" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 38, "question": "Macaadinta 'Manganese' waagee baa la helaa?", "options": { "a": "Waaga koowaad (Baaliyosooik)", "b": "Waaga labaad", "c": "Waaga saddexaad", "d": "Waaga cusub" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Waa maxay ujeeddada 'Jiyooloojiga Bay'ada'?", "options": { "a": "Ilaalinta deegaanka", "b": "Soo saarista saliidda", "c": "Barashada xoolaha", "d": "Dhismaha maraakiibta" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 40, "question": "Carro 'lakabeedka' Soomaaliya maxay ka kooban tahay?", "options": { "a": "Nuurad iyo bataax", "b": "Dahab iyo qalin", "c": "Saliid kaliya", "d": "Biyo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Sidee ayay Soomaaliya qeyb uga ahayd 'Junduwanaland'?", "options": { "a": "Waxay ka mid ahayd sagxadda hore ee Afrika ee qaaraddaas weyn ka tirsanayd", "b": "Waxay ahayd qaarad gooni ah", "c": "Badda ayay ku jirtay markaas", "d": "Ma jirin waagaas Soomaaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Xilliga 'Ayuusiin' maxaa ku daboolan Soomaaliya?", "options": { "a": "Dhadhaabyo waawayn", "b": "Biyo baraf ah", "c": "Dhir badan", "d": "Saliid kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Waa maxay dhexroorka dhulka oo ay cabbireen Muslimiintu?", "options": { "a": "Xarriiqda dhex marta badhtamaha goobada dhulka", "b": "Wareegga bannaanka", "c": "Dhererka dhulka", "d": "Balaca badda" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 44, "question": "Muxuu ahaa magaca qaaraddii hore ee Afrika ka mid ahayd?", "options": { "a": "Pangea", "b": "Junduwanaland", "c": "Gondwana", "d": "B iyo C waa sax" }, "correctAnswer": "d", "difficultyLevel": "medium" },
  { "id": 45, "question": "Salfarka (Sulphur) waagee baa la helaa?", "options": { "a": "Waaga saddexaad (Kinozoi)", "b": "Kambiriyan", "c": "Waaga koowaad", "d": "Waaga cusub" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 46, "question": "Falanqee sababta Jiyooloojiga loogu tixgeliyo cilmi 'diinaamik' ah?", "options": { "a": "Sababtoo am wuxuu darsaa dhaqdhaqaaqa iyo isbeddellada joogtada ah ee dhulka", "b": "Sababtoo ah dhulku ma dhaqaaqo", "c": "Sababtoo ah waa cilmi qadiimi ah kaliya", "d": "Sababtoo ah waa cilmi koronto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 47, "question": "Maxay Soomaaliya u leedahay dhadhaabyo 'Dhalan rogan' (Metamorphic) xilligan?", "options": { "a": "Sababtoo ah kuleylka iyo cadaadiska ka dhashay rogrogan dhulka (tectonic movements)", "b": "Sababtoo ah biyaha ayaa badalay", "c": "Ma lahan dhadhaabyo dhalan rogan", "d": "Sababtoo ah waa dhadhaabyo gumeystihii keenay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 48, "question": "Isbarbar dhig ahmiyadda dhaqaale ee waaga Kambiriyan iyo waaga Labaad?", "options": { "a": "Kambiriyan waa macaadin qaali ah (Dahab), waaga labaadna waa tamar (Saliid)", "b": "Kambiriyan waa saliid, waaga labaadna waa dahab", "c": "Labaduba waa isku mid", "d": "Kambiriyan ma lahan wax dhaqaale ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 49, "question": "Muxuu ahaa saamaynta jeexa Badda Cas ku yeelatay jihada dhulka Soomaaliya?", "options": { "a": "Waxay u jeexday jihada Waqooyi Galbeed ilaa Koonfur Bari", "b": "Waxay u jeexday Bari ilaa Galbeed", "c": "Waxay u jeexday Waqooyi ilaa Koonfur kaliya", "d": "Ma jiro jeex ka dhashay Badda Cas" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 50, "question": "Sidee bay sagxadda 'Arakiga' (Archean) u saameysay qaab dhismeedka Soomaaliya?", "options": { "a": "Waa dhadhaabyada ugu horreeyay ee qolofta dhulka oo sagxad u ah kuwa kale", "b": "Waa dhagaxyo jilicsan oo dhowaan dhashay", "c": "Waa dhagaxyo badda dhexdeeda laga sameeyay", "d": "Waa carra beeris kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 51, "question": "Falanqee xiriirka ka dhexeeya dhir la'aanta iyo carro guurka Soomaaliya?", "options": { "a": "Dhir la'aantu waxay keentaa in dabaysha iyo biyuhu si fudud u qaadaan carrada", "b": "Dhir la'aantu waxay kordhisaa nafaqada carrada", "c": "Dhirta iyo carrada xiriir ma lahan", "d": "Dhirta oo la jaro waxay joojisaa carro guurka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Maxay tahay sababta natiijadii Muslimiinta ee wareegga dhulka loogu tilmaamay inay 'aad ugu dhowdahay' tan casriga ah?", "options": { "a": "Sababtoo ah waxay isticmaaleen xisaab maangal ah iyo indho-indheyn sax ah", "b": "Sababtoo ah qalab casri ah bay lahaayeen", "c": "Sababtoo ah way qiyaaseen kaliya", "d": "Sababtoo ah saynisyahanada casriga ah ayaa ka soo xigtay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Waa maxay ujeeddada 'Jiyooloojiga Waxbarashada'?", "options": { "a": "In cilmiga loo gudbiyo jiilalka cusub qaab aqoon academic ah", "b": "In dugsiyada laga dhisayo buuro", "c": "In macalimiinta la siiyo saliid", "d": "Ma lahan ujeeddo cad" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Falanqee xiriirka u dhexeeya 'Foosfaytka' iyo waaga 'Mesosooik'?", "options": { "a": "Waa macdan muhiim ah oo sameysantay xilligii nolosha dhexe", "b": "Foosfaytka waaga cusub ayuu sameysmay", "c": "Foosfaytka ma ahan macdan", "d": "Foosfaytka Soomaaliya lagama helo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Maxay tahay sababta 'Gacanka Cadmeed' loogu tilmaamay inuu saameyn ku leeyahay Jiyooloojiga Soomaaliya?", "options": { "a": "Sababtoo ah dhaqdhaqaaqa dhulka ee furay gacanka wuxuu qeyb ka yahay tectonic-ka gobolka", "b": "Sababtoo ah biyo badan ayuu keenaa", "c": "Sababtoo ah kaluunka ayaa saameeya dhagaxa", "d": "Gacanka Cadmeed xiriir ma lahan dhulka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Isbarbar dhig carrada 'Bannaan xeebeedka' iyo carrada 'Dhoobada madow'?", "options": { "a": "Bannaan xeebeedku waa bataax, dhoobada madowse waa carro beeris nafaqo leh", "b": "Labaduba waa isku mid", "c": "Dhoobada madow waa xeebta kaliya", "d": "Bannaan xeebeedka ayaa ka nafaqo badan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Muxuu qabaa aragtida ah in 'Waaga koowaad uu ku qarsoon yahay' dhul ka da' yar Soomaaliya?", "options": { "a": "In lakabyada dhulka ee ka dambeeyay ay ku dul dhasheen kuwaas oo daboolay", "b": "In dhulku uu hoos u liqay", "c": "In la gubay", "d": "In gumeystuhu qariyay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Falanqee ahmiyadda 'Sibsibka' (Silt) iyo 'Quruuruxa' ee waaga cusub?", "options": { "a": "Waxay muhiim u yihiin dhismaha kaabayaasha dhaqaalaha sida waddooyinka", "b": "Waxay muhiim u yihiin soo saarista dahabka", "c": "Ma lahan wax faa'iido ah", "d": "Waa dhadhaabyo qaali ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Sidee ayay culimada Muslimiinta u saameeyeen jiyooloojiga casriga ah?", "options": { "a": "Waxay degeen aasaaska cabbiraadda dhulka iyo hab maangal ah", "b": "Waxay ikhtiraaceen kombuyuutarka", "c": "Waxay magacaabeen dhammaan waayada", "d": "Ma jirin wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Waa maxay doorka 'Foosiliska' (Fossils) ee lagu garto da'da dhadhaabyada?", "options": { "a": "Waxay ka caawiyaan jiyoolojiistaha inuu ogaado xilliga uu dhagaxu dhashay", "b": "Waxay ka dhigaan dhagaxa mid jilicsan", "c": "Waxay bedelaan midabka dhagaxa", "d": "Foosilisku waa wax aan loo baahneyn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Maxay tahay sababta Soomaaliya u leedahay carro nuurad (Limestone soil)?", "options": { "a": "Sababtoo ah dhadhaabyada hoose ee nuuradda ah oo burburay", "b": "Sababtoo ah roobka ayaa keenay", "c": "Sababtoo ah dadka ayaa ku shubay", "d": "Sababtoo ah dahab ayaa ku jira" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Falanqee ahmiyadda 'Xilliga Tirisik' ee Soomaaliya?", "options": { "a": "Wuxuu calaamad u yahay bilowga waaga koowaad ee sameysanka dhulkeena", "b": "Waa xilliga ay dadku yimaadeen", "c": "Waa xilliga saliiddu dhamaatay", "d": "Xilligan Soomaaliya kama jirin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Muxuu qabaa fikradka 'Pre-Cambrian' ee xagga macaadiinta?", "options": { "a": "Waa xilliga ay sameysmeen inta badan macaadiinta adag iyo kuwa qaaliga ah", "b": "Waa xilliga saliidda kaliya", "c": "Waa xilliga nolosha aadanaha", "d": "Xilligan dhulku ma jirin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Sidee buu dhexroorka dhulku u caawiyaa fahamka jiyooloojiga?", "options": { "a": "Wuxuu suurtageliyaa in la ogaado baaxadda iyo qaabka meeraha", "b": "Wuxuu sheegaa halka saliiddu ku jirto", "c": "Wuxuu bedelaa cimilada", "d": "Ma lahan wax faa'iido ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Maxaa loola jeedaa 'Dhadhaab wiriq ah'?", "options": { "a": "Waa dhadhaab adag oo badanaa ka yimaada foolkaanooyinka ama metamorphics", "b": "Waa dhadhaab jilicsan sida dhoobada", "c": "Waa dhadhaab biyo ka sameysan", "d": "Waa dhadhaab hawada ku jira" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Falanqee dhibaatada 'Carro Burburka' ee ka dhashay jarista dhirta?", "options": { "a": "Waxay saameysaa wax soo saarka beeraha iyo nolosha duur-joogta", "b": "Waxay kordhisaa biyaha webiyada", "c": "Waxay keentaa in dhagaxyadu kordhaan", "d": "Ma lahan wax saamayn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Waa maxay doorka 'Magniiska' (Manganese) ee laga helay waagii koowaad?", "options": { "a": "Waa macdan muhiim u ah warshadaha birta", "b": "Waxaa loo adeegsadaa cuntada", "c": "Waxaa loo adeegsadaa shidaalka diyaaradaha", "d": "Ma lahan wax faa'iido ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Falanqee 'Dynamic changes' ee dhulka?", "options": { "a": "Isbeddellada kuleylka, cadaadiska iyo dhaqdhaqaaqa qolofta dhulka", "b": "Isbeddelka midabka carrada kaliya", "c": "Isbeddelka xilliyada sanadka", "d": "Ma lahan wax micno ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Maxay tahay sababta Jiyooloojiga loogu qaybiyay laamo badan?", "options": { "a": "Si si qoto dheer loogu darsado dhinac walba oo dhulka iyo dhaqaalaha khuseeya", "b": "Si dadka loogu jahwareeriyo", "c": "Sababtoo ah mid kaliya kuma riimi karo", "d": "Ma jiro wax sabab ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Sidee loo kala saaraa waaga Mesosooik iyo waaga Kinozoi?", "options": { "a": "Mesosooik waa nolosha dhexe (saliid), Kinozoi waa nolosha dambe (sibidh/nuurad)", "b": "Ma jiro wax farqi ah", "c": "Kinozoi ayaa ka horreeyay Mesosooik", "d": "Mesosooik ayaa ka waqti gaaban Kinozoi" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Muxuu qabaa nuxurka ah in 'Soomaaliya ay ka timid sagxaddii hore ee Afrika'?", "options": { "a": "In dhulkeenu leeyahay aasaas qadiimi ah oo kuxiran qaabdhismeedka qaaradda oo dhan", "b": "In Soomaaliya dhowaan la dhisay", "c": "In ay badda ka soo baxday shalay", "d": "Ma lahan wax micno ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Waa maxay ahmiyadda macaadiinta shucaaca bixisa (Radioactive minerals)?", "options": { "a": "Waxaa loo adeegsadaa tamarta nukliyeerka iyo cilmibaarista", "b": "Waxaa loo adeegsadaa samaynta dahabka", "c": "Waa macaadin la cuno", "d": "Ma lahan wax faa'iido ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Sidee bay dabayshu u saameysaa carro guurka Soomaaliya?", "options": { "a": "Waxay qaaddaa lakabka kore ee carrada nafaqada leh (topsoil)", "b": "Waxay keentaa roob badan", "c": "Waxay dabooshaa webiyada", "d": "Dabayshu carro guur ma keento" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Falanqee 'Archaeology' iyo 'Geology' xiriirka ka dhexeeya?", "options": { "a": "Geology wuxuu diyaariyaa dhulka iyo dhadhaabyada ay archaeology wax ka baarto", "b": "Waa isku mid", "c": "Xiriir ma lahan", "d": "Archaeology ayaa ka horreeyay Geology" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Muxuu qabaa gunaanadka nuxurka casharka ee ku saabsan barashada Jiyooloojiga?", "options": { "a": "Waa lagama maarmaan si loo fahmo kheyraadka, deegaanka iyo taariikhda meeraha aan ku noolnahay", "b": "Waa wax la iska barto kaliya", "c": "Waqti lumis ayuu u yahay ardayda", "d": "Kaliya dadka saliidda raba ayuu khuseeyaa" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    # Some questions might have images or weird structures, but we map them correctly
    formatted_q = {
        'id': f"Geo_Ch1_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch1',
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
    
    # Remove existing geo_ch1 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch1']
    
    # Check if geo_ch1 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch1' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 1aad: Hordhaca Jiyooloojiga",
            "id": "geo_ch1"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch1':
                c['title'] = "Cutubka 1aad: Hordhaca Jiyooloojiga"
                break
    
    # Add new geo_ch1 questions
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

    # Remove existing geo_ch1 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch1']
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
