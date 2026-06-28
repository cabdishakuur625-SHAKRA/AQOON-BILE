import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay qeexidda aasaasiga ah ee Dastuurka?", "options": { "a": "Waa xeerar lagu maamulo ganacsiga", "b": "Waa mabaadi’da aasaasiga ah ee habeeya awoodaha dawladda iyo xuquuqda dadka", "c": "Waa heshiis dhex mara laba dal", "d": "Waa qawaaniin lagu maamulo waddooyinka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa maxay ujeeddada koowaad ee Sharcigu?", "options": { "a": "In la canshuurow dadka", "b": "In la ciqaabo dadka oo dhan", "c": "Guul-gaarista amniga dadka iyo xaqiijinta cadaaladda", "d": "In la dhiso xisbiyo badan" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 3, "question": "Halkee ayay asal ahaan ka timid ereyga 'Dimuqraadiyad'?", "options": { "a": "Carabta", "b": "Ingiriiska", "c": "Giriigga", "d": "Roomaanka" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 4, "question": "Maxaa loola jeedaa ereyga 'Demos'?", "options": { "a": "Xukun", "b": "Dad ama Bulsho", "c": "Sharci", "d": "Doorasho" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Maxaa loola jeedaa ereyga 'Cratic'?", "options": { "a": "Xukun", "b": "Nabad", "c": "Talo", "d": "Dad" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa maxay Shuuradu?", "options": { "a": "Waa xukun qasab ah", "b": "Waa raadinta ra’yiga iyo talada laga raadiyo cidda ehelka u ah", "c": "Waa go'aan uu hal qof gaaro", "d": "Waa magaca xisbi siyaasadeed" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Wadankee ayaa caan ku ah in uusan lahayn dastuur qoran?", "options": { "a": "Soomaaliya", "b": "Hindiya", "c": "Ingiriiska", "d": "Mareykanka" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay nooca dastuurka ee Soomaaliya hadda leedahay?", "options": { "a": "Dastuur adag", "b": "Dastuur kumeel-gaar ah", "c": "Dastuur aan qorneyn", "d": "Dastuurka Boqortooyo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Goorma ayay dunida si rasmi ah uga bilowdeen xisbiyada siyaasadeed (marka laga reebo Mareykanka)?", "options": { "a": "1800", "b": "1850", "c": "1900", "d": "1960" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Maxay tahay Maxkamadda Dastuuriga ah?", "options": { "a": "Maxkamadda sare ee garsoorka", "b": "Maxkamadda ciidanka", "c": "Maxkamadda gobolka", "d": "Maxkamadda ganacsiga" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 11, "question": "Immisa qaybood ayaa loo qaybiyaa ka qaybgalka siyaasadda ee qofka?", "options": { "a": "Hal siyaabood", "b": "Laba siyaabood (Musharraxnimo iyo Cod-bixin)", "c": "Saddex siyaabood", "d": "Ma laha qaybo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Waa kuwee sifooyinka ka qaybgalka siyaasadda?", "options": { "a": "Dagaal iyo is-qabqabsi", "b": "Waxqabad, tabarucid, iyo xulasho", "c": "Lacag bixin iyo amardiido", "d": "Ma jiro wax sifo ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Maxaa lagu gartaa Dastuurka Hindiya?", "options": { "a": "Waa dastuur aan qorneyn", "b": "Waa dastuur aad u faah-faahsan", "c": "Waa dastuur kumeel-gaar ah", "d": "Waa dastuur adag oo aan isbeddelayn" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa maxay Shuuradu marka loo eego shareecada Islaamka?", "options": { "a": "Waa doorasho", "b": "Waa xaqiiqo xukunkeedu yahay xukun Eebbe", "c": "Waa xukun shacabka ay dejiyaan", "d": "Waa nidaam Giriig ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Magaaladee ayay dimuqraadiyaddu si rasmi ah uga bilaabatay qarnigii 5aad NCH?", "options": { "a": "Rome", "b": "Mogadishu", "c": "Athens", "d": "Cairo" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 16, "question": "Waa maxay 'Shuuradu' marka loo eego xadiiska 'Al-mustashaaru mu'taman'?", "options": { "a": "In qofka lala tashanayo la aamino", "b": "In qofka la doorto", "c": "In sharciga la jebiyo", "d": "In talada la qariyo" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 17, "question": "Waa maxay nidaamka xisbiyada ee dalku yeelan karo xisbiyo badan?", "options": { "a": "Nidaamka xisbiga awoodda badan", "b": "Nidaamka labada xisbi", "c": "Nidaamka xisbiyada badan", "d": "Nidaamka xisbi la'aanta" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 18, "question": "Maxaa reebban in xisbi siyaasadeed uu yeesho?", "options": { "a": "Barnaamij siyaasadeed", "b": "Qaab-dhismeed ciidan", "c": "Xafiisyo gobollada ah", "d": "Mabaadi' cad" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Goorma ayaa ciidamada Soomaaliya talada dalka la wareegeen?", "options": { "a": "1960", "b": "1969", "c": "1991", "d": "2000" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Waa maxay masdarka Dimuqraadiyadda?", "options": { "a": "Waa xukun Eebbe", "b": "Waa xukunka shacabka ee uu dejiyo shacabku", "c": "Waa xukunka boqortooyada", "d": "Waa xukunka ciidanka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Xisbiyada Soomaaliya waxay ka soo baxeen ururro kala duwan, maxaa ka mid ahaa?", "options": { "a": "Ururka Shaqaalaha xeebta iyo ururrada samafalka", "b": "Ururrada diimeed oo kaliya", "c": "Ururka ganacsato caalami ah", "d": "Ururka ciyaaraha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 22, "question": "Waa maxay sarraynta sharcigu?", "options": { "a": "In qofka ladan la tixgeliyo", "b": "In qof kasta oo bulshada ka mid ah uu u hoggaansamo sharciga si siman", "c": "In sharciga la beddelo maalin kasta", "d": "In sharcigu xukumo dalalka dariska ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Waa maxay faa'iidada koowaad ee Shuurada?", "options": { "a": "In la helo lacag", "b": "In laga hortago tafarruqa iyo khilaafka", "c": "In hal qof uu xukumo", "d": "In la dhiso xisbi cusub" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 24, "question": "Waa maxay nidaamka 'Labada Xisbi'?", "options": { "a": "Marka dalku hal xisbi leeyahay", "b": "Marka dalku leeyahay laba xisbi oo ugu xoog badan oo talada ku tartama", "c": "Marka dalku xisbi la'aan yahay", "d": "Marka dalku leeyahay 100 xisbi" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 25, "question": "Maxaa loola jeedaa 'Baahinta Xukunka'?", "options": { "a": "In xukunka hal meel lagu ururiyo", "b": "In xukunka loo qaybiyo heerar kala duwan (tusaale: Federaal iyo Gobol)", "c": "In xukunka la siiyo ciidanka", "d": "In xukunka la joojiyo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 26, "question": "Sharax xiriirka ka dhexeeya sharciga iyo bulshada?", "options": { "a": "Sharciga iyo bulshadu xiriir ma laha", "b": "Waa xiriir adag; ma jiri karo sharci bulsho la'aan, bulshona ma jiri karto sharci la'aan", "c": "Bulshada ayaa ka sarraysa sharciga", "d": "Sharciga ayaa kaliya saameeya dawladda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Maxay ku kala duwan yihiin Dastuurka adag iyo kan la beddeli karo?", "options": { "a": "Dastuurka adag waa kan kumeel-gaarka ah", "b": "Dastuurka adag wax-ka-beddelkiisu wuxuu u baahan yahay nidaam adag, kan la beddeli karona waa sidii sharciga caadiga ah", "c": "Ma jiraan wax farqi ah", "d": "Dastuurka adag waa kan aan qorneyn" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Waa maxay ujeeddada laga leeyahay 'Ilaalinta lunsashada hantida guud'?", "options": { "a": "In la kordhiyo hantida gaarka ah", "b": "In la habeeyo nolosha dadka iyo in la ilaaliyo xuquuqda qaranka", "c": "In hantida la siiyo xisbiyada", "d": "In hantida la gubo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Sidee ayay Dimuqraadiyadda iyo Shuuradu u kala duwan yihiin dhinaca xukunka (Masdarka)?", "options": { "a": "Dimuqraadiyaddu waa xukunka dadka, Shuuraduna waa xukun Eebbe oo ku saleysan caqiido", "b": "Shuuradu waa nidaam Giriig ah, Dimuqraadiyadduna waa mid Islaami ah", "c": "Labaduba waa isku mid", "d": "Labaduba waxay ka yimaadeen Ingiriiska" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Maxay ahayd taladii Cumar bin Khadhaab markii uu dhaawacmay?", "options": { "a": "Wuxuu magacaabay wiilkiisa", "b": "Wuxuu soo xulay lix saxaabi si ay dhexdooda iska doortaan", "c": "Wuxuu yiri qofna ha dooranina", "d": "Wuxuu u dhiibay xukunka Cali bin Abii Dhaalib" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Waa maxay faa'iidada laga helayo 'In Shuuradu dhaliyo ra'yi laysla ogolyahay'?", "options": { "a": "Waxay keenaysaa in dadku ay u hoggaansamaan amarka si fudud", "b": "Waxay keenaysaa in doorasho laga baaqdo", "c": "Waxay dhalisaa tafarruq", "d": "Ma laha wax faa'iido ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Maxaa dhacaya haddii xisbi siyaasadeed uu leeyahay magac u eg mid jira?", "options": { "a": "Waa laga aqbalayaa", "b": "Waa ka mid shuruudaha in uusan lahayn magac u eg xisbi jira si aan wareer loo abuurin", "c": "Waa in uu lacag bixiyaa", "d": "Dawladda ayaa u magac bixinaysa" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Sharax heerarka uu soo maro ka qaybgalka siyaasadda?", "options": { "a": "Wuxiu ka bilowdaa doorasho wuxuuna ku dhamaadaa xafiis", "b": "Wuxuu ku bilowdaa tixgelinta arrimaha guud, wuxuu u gudbaa hawlgal, ugu dambayna waa dhaqdhaqaaq siyaasadeed", "c": "Wuxuu ku bilaabmaa dagaal", "d": "Ma laha wax heerar ah" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay ahayd sababta ciidamadu u baabi'iyeen nidaamkii baarlamaanka 1969?", "options": { "a": "Dalku wuxuu ahaa mid aad u qani ah", "b": "Musuqmaasuq baahsan iyo xad-gudubyo ka jiray maamulladii rayidka", "c": "Si ay dalka u gumeystaan", "d": "Ma jirin sabab cad" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Waa maxay farqiga u dhexeeya 'Dastuurka qoran' iyo kan 'Aan qorneyn'?", "options": { "a": "Dastuurka qoran waa mid ku urursan hal dukumiinti, kan aan qorneyna waa caadooyin iyo qawaaniin kala duwan", "b": "Dastuurka aan qorneyn ma jiro", "c": "Dastuurka qoran waa mid kumeel-gaar ah", "d": "Dastuurka aan qorneyn waa mid adag" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Maxaa looga baahan yahay xisbi in mabaadii'diisu aysan ka hor imaanin midnimada qaranka?", "options": { "a": "Si loo ilaaliyo nabadgelyada iyo nabadda bulshada", "b": "Si xisbiga lacag loo siiyo", "c": "Si doorashada loo guuleysto", "d": "Ma jirto sabab muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Waa maxay doorka Bulshada Rayidka ee dimuqraadiyadda?", "options": { "a": "Inay dawladda la dagaalamaan", "b": "Inay u adeegaan danaha shacabka oo ay miisaamaan awoodda dawladda", "c": "Inay xisbi siyaasadeed noqdaan oo kaliya", "d": "Inay dadka canshuur ka qaadaan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Maxaa loola jeedaa 'Dulqaadashada Siyaasadeed'?", "options": { "a": "In la ogolaado ra'yiga dadka kale iyo tartanka xalaasha ah", "b": "In la tirtiro xisbiyada mucaaradka", "c": "In hal ra'yi oo kaliya la qaato", "d": "In doorashada dib loo dhigo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Waa maxay micnaha 'La xisaabtanka iyo Daah-furnaanta'?", "options": { "a": "In dadka lagu yiri ma la xisaabtami kartaan", "b": "In madaxdu ay u sharaxaan shacabka go'aamadooda iyo sida ay hantida u maamulaan", "c": "In hantida la qariyo", "d": "In doorashada la musuq-maasuqo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxay 'Shuuradu' u tahay mid ka hortagta tafarruqa?", "options": { "a": "Maxaa yeelay waxay isku keentaa fikradaha kala duwan", "b": "Maxaa yeelay waxay qasabtaa hal go'aan", "c": "Ma hortagto tafarruqa", "d": "Waxay abuurtaa xisbiyo badan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Sidee buu sharcigu u habeeyaa xuquuqda iyo waajibaadka?", "options": { "a": "Wuxuu caddeeyaa waxa qofka laga rabo iyo waxa uu xaqa u leeyahay", "b": "Wuxuu siiyaa xuquuq dadka qaar oo kaliya", "c": "Ma habeeyo xuquuqda", "d": "Wuxuu dhimaa waajibaadka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Waa maxay farqiga u dhexeeya 'Nidaamka xisbiyada badan' iyo 'Nidaamka labada xisbi'?", "options": { "a": "Xisbiyada badan waxay u furan yihiin kooxo badan, halka labada xisbi ay laba awoodood ku tartamaan", "b": "Ma jiro farqi weyn", "c": "Xisbiyada badan waa kuwa ciidan", "d": "Labada xisbi waa kuwa kumeel-gaar ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Goorma ayay xisbiyada Soomaaliya bilaabeen inay soo shaac baxaan si xoog leh?", "options": { "a": "Dagaalkii 1aad ka hor", "b": "Dagaalkii 2aad ka dib (dhamaadkii 40-meeyadii)", "c": "Sannadkii 2000", "d": "1969 ka dib" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Maxay Dimuqraadiyaddu ugu baahan tahay 'Xorriyadda Fikirka'?", "options": { "a": "Si dadku ay u cabbiri karaan aragtidooda iyagoon cabsi qabin", "b": "Si dadku ay u caayaan dawladda", "c": "Si doorashada loo joojiyo", "d": "Si hal xisbi loo dhiso" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Waa maxay dhibaatada ugu weyn ee haysatay maamulladii rayidka ee Soomaaliya (1960-1969)?", "options": { "a": "Dhaqaale la'aan", "b": "Musuqmaasuq baahsan oo maamulka iyo dhaqaalaha ah", "c": "Dagaal sokeeye", "d": "Gumeysi cusub" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 46, "question": "Maxaa loola jeedaa 'Xisbiyada tartama iyo kuwa aan tartamin'?", "options": { "a": "Kuwa tartama waa kuwa talada raba, kuwa aan tartaminna waa kuwa taageerada uun bixiya", "b": "Ma jiraan xisbiyo aan tartamin", "c": "Kuwa tartama waa kuwa ciidanka ah", "d": "Waa xisbiyo dibadda ka yimid" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 47, "question": "Waa maxay micnaha 'Xaqiijinta ujeedooyinka dhaqaalaha' ee sharciga?", "options": { "a": "In sharcigu habeeyo ganacsiga iyo kobaca dhaqaalaha", "b": "In sharcigu dadka lacag siiyo", "c": "In sharcigu canshuurta tirtiro", "d": "In sharcigu joojiyo suuqa xorta ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 48, "question": "Maxay muhiim u tahay in xisbigu si cad u soo bandhigo barnaamijyadiisa?", "options": { "a": "Si shacabku u ogaadaan waxa uu doonayo inuu qabto haddii uu guuleysto", "b": "Si uu u helo lacag badan", "c": "Si uu magac u yeesho uun", "d": "Ma ahan muhiim" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 49, "question": "Sidee bay 'Shuuradu' iyo 'Dimuqraadiyaddu' isugu shabbahaan (isku mid ugu yihiin)?", "options": { "a": "Labaduba waxay ku saleysan yihiin raadinta ra'yiga iyo in laga fogaado xukun-maroorsi", "b": "Labaduba waxay ka yimaadeen Giriigga", "c": "Labaduba waa xukun Eebbe", "d": "Ma jiraan wax ay isaga mid yihiin" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 50, "question": "Waa maxay ka qaybgalka 'Tabaruc' ee siyaasadda?", "options": { "a": "In qofku uu iskiis u go'aansado inuu qayb ka noqdo dhaqdhaqaaq isagoon lagu qasbin", "b": "In lacag lagu siiyo ka qaybgalka", "c": "In lagu qasbo qofka", "d": "Waa mushahar" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 51, "question": "Maxaa loola jeedaa 'Dastuurka Faah-faahsan' sida kan Hindiya?", "options": { "a": "Waa dastuur aad u dheer oo qeexaya wax kasta oo dalka khuseeya", "b": "Waa dastuur aan waxba qeexin", "c": "Waa dastuur kumeel-gaar ah", "d": "Waa dastuur gaaban" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 52, "question": "Waa maxay nidaamka 'Xisbiga awoodda badan'?", "options": { "a": "Marka xisbiyo badan jiraan laakiin hal xisbi uu had iyo jeer guuleysto", "b": "Marka ciidanku xisbi yahay", "c": "Marka xisbiga sharciga ah la mamnuuco", "d": "Marka dalku xisbi la'aan yahay" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 53, "question": "Maxay ku kala duwan yihiin Sharciga iyo Dastuurka marka loo eego sarraynta?", "options": { "a": "Dastuurka ayaa ka sarreeya sharciga, sharciguna waa in uusan ka hor imaan dastuurka", "b": "Sharciga ayaa ka sarreeya dastuurka", "c": "Labaduba waa isku mid", "d": "Ma laha wax sarrayn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 54, "question": "Waa maxay micnaha 'Xulasho' ee ka qaybgalka siyaasadda?", "options": { "a": "In muwaadinku uu isagu doorto cidda u matalaysa golayaasha", "b": "In dawladdu u doorato muwaadinka", "c": "In xisbiga la qasbo", "d": "In doorasho la'aan lagu yimaado" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 55, "question": "Falanqee xiriirka ka dhexeeya sharciga iyo xasilloonida bulshada?", "options": { "a": "Sharcigu wuxuu abuuraa xeerar xaddidaya khilaafaadka, taas oo horseedda nabad iyo xasillooni", "b": "Sharcigu wuxuu kordhiyaa colaadda", "c": "Xasilloonidu waxay ku timaadaa xoog ciidan kaliya", "d": "Sharciga iyo xasilloonidu isma khuseeyaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Maxay tahay muhiimadda 'Maxkamadda Dastuuriga ah' ee ilaalinta nidaamka dimuqraadiga?", "options": { "a": "Inay xaqiijiso in dhammaan qawaaniinta la soo saaro ay waafaqsan yihiin mabaadii'da dastuurka", "b": "Inay xukunto dambiilayaasha caadiga ah", "c": "Inay magacawdo madaxweynaha", "d": "Inay canshuurta ururiso" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Qiimeey saameynta 'Shuurada' ee dhismaha go'aan-qaadashada dawlad Islaami ah?", "options": { "a": "Waxay dammaanad qaadaysaa in talada aan hal qof lagu koobin, lagana fogaado dulmiga", "b": "Waxay ka dhigaysaa dawladda mid daciif ah", "c": "Waxay keentaa in dadka oo dhan ay is-khilaafaan", "d": "Ma laha wax saameyn ah oo muuqda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Isbarbardhig Dimuqraadiyadda Giriigga iyo tan casriga ah?", "options": { "a": "Giriiggu waxay isticmaali jireen dimuqraadiyad toos ah, halka tan casriga ah ay tahay mid matalaad (Indirect)", "b": "Giriiggu waxay lahaayeen xisbiyo badan", "c": "Dimuqraadiyadda casriga ah ma laha doorasho", "d": "Ma jiro wax farqi ah oo u dhexeeya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay tahay sababta sharcigu muhiim ugu yahay ilaalinta hantida guud?", "options": { "a": "Si looga hortago musuqmaasuqa iyo lunsashada kheyraadka qaranka ee u dhexeeya dadka oo dhan", "b": "Si hantida loogu qaybiyo madaxda uun", "c": "Si hantida loo qariyo", "d": "Ma jirto sabab sharci ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Sidee buu dastuurka Ingiriisku u shaqeeyaa isagoon ahayn dukumiinti qoran oo kaliya?", "options": { "a": "Wuxuu ku dhisanyahay caadooyin (Conventions), go'aanno maxkamadeed, iyo qawaaniin muddo dheer soo jiray", "b": "Ingiriisku dastuur ma laha", "c": "Wuxuu ku dhisanyahay amarka boqortooyada uun", "d": "Waa dastuur kumeel-gaar ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Falanqee doorka lixdii saxaabi ee Cumar bin Khadhaab soo xulay xilligii geeridiisa?", "options": { "a": "Waxay ahaayeen tusaale nool oo ku saabsan sida shuuradu u shaqeyso si loo helo hoggaamiye laysku raacsan yahay", "b": "Waxay ahaayeen kuwo is-dagaalay", "c": "Waxay diideen inay talada qabtaan", "d": "Cumar ayaa mid ka mid ah magacaabay isaga" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Waa maxay caqabadaha hortaagan ka qaybgalka siyaasadda ee dalalka musuqmaasuqu baahanyahay?", "options": { "a": "Dadka oo lumiya kalsoonida nidaamka doorashada iyo caddaaladda", "b": "Dadka oo aan aqoon u lahayn siyaasadda", "c": "Xisbiyada oo aad u badan", "d": "Sharciga oo aad u adag" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Maxaa loola jeedaa 'Sarraynta Qaanuunka' ee tiirarka dimuqraadiyadda?", "options": { "a": "In qof kasta (madax iyo shacab) uu u hoggaansamo sharciga oo uusan jirin qof sharciga ka sarreeya", "b": "In sharciga laga dhigo mid adag", "c": "In sharciga lagu xukumo dadka saboolka ah uun", "d": "In sharciga la jebiyo marka loo baahdo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Qiimeey sababta ay ciidanka Soomaaliya u laaleen dastuurkii 1960-kii?", "options": { "a": "Waxay u arkeen inuu ku fashilmay xaqiijinta cadaaladda iyo horumarka dhaqaalaha ee xilligaas", "b": "Maxaa yeelay dastuurku wuxuu ahaa mid qaldan", "c": "Si ay dalka ugu xukumaan rabitaankooda", "d": "Maxaa yeelay dastuurku wuxuu ahaa mid Giriig ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Sidee bay u kala duwan yihiin mabaadii'da xisbi tartama iyo mid aan tartamin marka loo eego talada dalka?", "options": { "a": "Xisbiga tartama wuxuu hiigsadaa awoodda, halka kan kale uu diiradda saaro saameynta bulshada ama fikirka uun", "b": "Xisbiga aan tartamin ma jiro", "c": "Xisbiga tartama waa mid ciidan", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Maxay tahay muhiimadda 'Baahinta Xukunka' ee ilaalinta midnimada dal federaal ah?", "options": { "a": "Waxay suurtagal ka dhigaysaa in gobol kasta uu maamulo arrimihiisa gudaha, taasoo yaraysa khilaafka awoodda", "b": "Waxay daciifisaa dawladda dhexe", "c": "Waxay keentaa in dalku qayb-qaybsamo", "d": "Waxay kordhisaa canshuurta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Falanqee shuruudda ah 'Xisbigu in uusan lahayn qaab-dhismeed ciidan'?", "options": { "a": "Si looga fogaado in tartanka siyaasadeed uu isu beddelo dagaal iyo cabsi-gelin hubaysan", "b": "Maxaa yeelay ciidanku xisbi ma noqon karaan", "c": "Si looga fogaado in xisbigu uu noqdo mid dawladdu leedahay", "d": "Ma ahan shuruud muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Qiimeey xiriirka u dhexeeya 'Xorriyadda Fikirka' iyo 'Dulqaadashada Siyaasadeed'?", "options": { "a": "Xorriyadda fikirku ma jiri karto haddii aan la helin dulqaad loo hayo ra'yiga dadka kale", "b": "Labaduba isma khuseeyaan", "c": "Xorriyadda fikirku waxay keenaysaa dagaal", "d": "Dulqaadashadu waa mid daciifnimo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Maxay tahay sababta Shuuradu u tahay 'Asaaska Caqiidada' ee Islaamka marka loo eego xukunka?", "options": { "a": "Sababtoo ah waa amarka Eebbe ee lagu soo dejiyay Qur'aanka iyo Sunnada", "b": "Sababtoo ah waa nidaam dadku dejiyeen", "c": "Sababtoo ah waa dimuqraadiyad", "d": "Ma ahan asaas caqiido" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Sidee bay xisbiyada siyaasadeed ee Soomaaliya u saameeyeen halgankii madax-bannaanida?", "options": { "a": "Waxay mideeyeen codkii shacabka waxayna abuureen dhaqdhaqaaqyo siyaasadeed oo diidanaa gumeysiga", "b": "Waxay taageereen gumeysiga", "c": "Waxay ahaayeen ururro ganacsi uun", "d": "Ma lahayn wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Qiimeey doorka 'Baaritaanka ra'yiga' ee Shuurada marka la barbardhigo 'Doorashada' Dimuqraadiyadda?", "options": { "a": "Labaduba waxay ujeedadoodu tahay in la gaaro go'aan matalaya dadka", "b": "Shuuradu waa qasab, doorashaduna waa ikhtiyaar", "c": "Doorashadu ma khuseyso ra'yiga", "d": "Shuuradu waxay khuseysaa dadka diinta aqoon u leh oo kaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Sharax sababta 'Dastuurka kumeel-gaarka ah' looga isticmaalo dalalka soo kabanaya sida Soomaaliya?", "options": { "a": "Si loogu maareeyo xilliga kala guurka ah inta laga gaarayo heshiis siyaasadeed oo sugan", "b": "Maxaa yeelay dastuur joogto ah lama heli karo", "c": "Si qolo walba ay u beddesho", "d": "Waa amarka Qaramada Midoobay" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Falanqee sifooyinka ka qaybgalka siyaasadda ee dhinaca 'Waxqabadka' (Activity)?", "options": { "a": "In qofku uusan fadhiyin uun balse uu dhab ahaan u qayb qaato go'aamada dawladnimada", "b": "In qofku iska dhex muuqdo uun", "c": "Waa in qofku lacag bixiyo", "d": "Waa in qofku ciidan noqdo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Maxay tahay ujeeddada ka dambaysa 'Xaqiijinta ujeedooyinka siyaasadeed' ee sharciga?", "options": { "a": "In la habeeyo nidaamka talada dalka iyo in la qeexo xiriirka ka dhexeeya laamaha dawladda", "b": "In hal xisbi uun la siiyo awoodda", "c": "In doorashada mar kasta dib loo dhigo", "d": "Ma laha ujeeddo siyaasadeed" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Qiimeey saameynta 'La xisaabtanka' ku leeyahay kalsoonida muwaadinka ee dawladda?", "options": { "a": "Markay dawladdu tahay mid furan, muwaadinku wuxuu dareemayaa in canshuurtiisii iyo xuquuqdiisii ay nabad qabto", "b": "Waxay keentaa in dawladdu dunto", "c": "La xisaabtanku wuxuu daciifiyaa madaxda", "d": "Muwaadinku ma rabo inuu xisbiga la xisaabtamo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Sharax farqiga u dhexeeya 'Shuurada' iyo 'Dimuqraadiyadda' ee dhinaca Mabaadi'da?", "options": { "a": "Shuuradu waxay ku saleysan tahay shareecada, Dimuqraadiyadduna waxay ku saleysan tahay rabitaanka bini'aadamka uun", "b": "Labaduba waa isku mabaadi' uun", "c": "Dimuqraadiyaddu waa mid shareecada waafaqsan mar kasta", "d": "Shuuradu ma laha mabaadi' sugan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Falanqee muhiimadda 'Xiriirka adag ee u dhexeeya sharciga iyo bulshada'?", "options": { "a": "Sharcigu wuxuu ka tarjumayaa qiyamka bulshada, bulshaduna waxay ku dhisataa nidaamkeeda sharciga", "b": "Bulshada ayaa ka sarraysa sharciga mar kasta", "c": "Sharciga iyo bulshadu mar kasta way is-khilaafaan", "d": "Xiriirku waa mid gumeysi uun" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 78, "question": "Maxay tahay caqabadda 'Nidaamka xisbiga awoodda badan' ee ka qaybgalka siyaasadda xalaasha ah?", "options": { "a": "Waxay dhalin kartaa in xisbiyada yar-yar ay waayaan fursad ay talada dalka ku gaaraan", "b": "Ma jirto wax caqabad ah", "c": "Waxay keentaa dimuqraadiyad badan", "d": "Waxay xisbiga ka dhigtaa mid daciif ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Qiimeey saameynta 'Xorriyadda Fikirka' ee ku saabsan horumarka bulshada?", "options": { "a": "Waxay suurtogal ka dhigaysaa in fikrado cusub iyo hal-abuurnimo ay soo baxaan, taasoo horumar horseeda", "b": "Waxay keentaa tafarruq iyo dagaal uun", "c": "Ma laha wax saameyn ah", "d": "Waxay ka dhigaysaa dadka kuwo caajis ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 80, "question": "Waa maxay micnaha 'In mabaadii'da xisbiga aysan ka hor imaanin mabaadii'da dastuuriga ah'?", "options": { "a": "Si loo hubiyo in xisbigu uusan dumin nidaamka guud ee dawladnimada iyo amniga qaranka", "b": "In xisbigu uu noqdo mid dastuurka uun ka hadla", "c": "In dawladdu u qorto mabaadi'da xisbiga", "d": "Ma laha micno weyn" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Falanqee 'Daliilka Shuurada' ee Sunnada: 'Al-mustashaaru mu'taman'?", "options": { "a": "Wuxuu muujinayaa mas'uuliyadda weyn ee saaran qofka lala tashanayo inuu talo hufan bixiyo", "b": "Wuxuu muujinayaa in talada la iska diidi karo", "c": "Wuxuu muujinayaa in shuuradu tahay mid aan qasab ahayn", "d": "Wuxuu khuseeyaa doorashooyinka uun" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 82, "question": "Qiimeey doorka 'Xallinta Khilaafaadka' ee sharciga marka ay is-khilaafaan hay'adaha dawladda?", "options": { "a": "Sharcigu wuxuu qeexayaa awood kasta meesha ay ku joogto si looga fogaado xukun-maroorsi", "b": "Sharcigu wuxuu u hiiliyaa fulinta uun", "c": "Sharcigu wuxuu keenaa in hay'aduhu is-dilaan", "d": "Ma habeeyo khilaafaadka hay'adaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 83, "question": "Maxay tahay muhiimadda 'Mabaadi'da aasaasiga ah' ee dastuurka ee dhinaca caddeynta xuquuqda?", "options": { "a": "Waxay u adeegaan silsilad dammaanad-qaadaysa in muwaadin kasta uu helo xuquuqdiisa aasaasiga ah", "b": "Waxay u adeegaan in lagu canshuuraysto dadka", "c": "Ma jiraan wax xuquuq ah oo la caddeeyay", "d": "Waxay dhowraan xuquuqda madaxda uun" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 84, "question": "Falanqee sababta 'Dastuurada adag' ay ugu baahan yihiin nidaam gaar ah si loo beddelo?", "options": { "a": "Si loo ilaaliyo xasiloonida nidaamka dalka loogana fogaado in mar kasta dano siyaasadeed loo beddelo", "b": "Si dadka loogu diido inay wax beddelaan", "c": "Sababtoo ah madaxda ayaa raba inay kursiga ku negaadaan", "d": "Maxaa yeelay waa dastuur qadiimi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 85, "question": "Qiimeey saameynta 'Heerarka ka qaybgalka siyaasadda' ee dhismaha muwaadin firfircoon?", "options": { "a": "Waxay ka dhigtaa muwaadinka mid tixgeliya arrimaha guud, kuna lug yeesha go'aan-qaadashada dalkiisa", "b": "Waxay ka dhigtaa muwaadinka mid dawladda neceb", "c": "Ma laha wax saameyn ah", "d": "Waxay keentaa in qofku uu doonayo lacag uun" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 86, "question": "Sharax micnaha 'Xaqiijinta ujeedooyinka bulsho' ee sharciga ee dhinaca tacliinta iyo caafimaadka?", "options": { "a": "Wuxuu habeeyaa helidda adeegyada aasaasiga ah ee muwaadinka", "b": "Wuxuu ka dhigaa kuwo qaali ah", "c": "Ma khuseeyo adeegyada bulshada", "d": "Wuxuu joojiyaa isbitaallada gaarka ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 87, "question": "Qiimeey doorka 'Ururrada Ardayda iyo Shaqaalaha' ee dhalashada xisbiyadii ugu horreeyay ee Soomaaliya?", "options": { "a": "Waxay ahaayeen unugyadii ugu horreeyay ee laga dhex helay dad wax-bartay oo dareen waddaninimo leh", "b": "Ma lahayn wax door ah", "c": "Waxay ahaayeen kuwo u shaqeeya gumeystaha", "d": "Waxay ahaayeen ururro ciyaaro uun" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 88, "question": "Waa maxay micnaha 'Dimuqraadiyaddu waa xukunka inta badan' (Majority rule)?", "options": { "a": "In go'aanka ay gaaraan tirada ugu badan ee dadka lagu shaqeeyo", "b": "In qof kasta go'aan leeyahay", "c": "In dadka laga tirada badanyahay la dhibo", "d": "In doorasho la'aan lagu yimaado" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 89, "question": "Falanqee 'Xaqiijinta ujeedooyinka siyaasadeed' ee sharciga Soomaaliya (1960)?", "options": { "a": "Wuxuu ahaa kii habeeyay nidaamkii baarlamaanka iyo doorashooyinkii ugu horreeyay", "b": "Wuxuu ahaa kii ciidanka keenay", "c": "Ma jirin ujeeddo siyaasadeed", "d": "Wuxuu ahaa mid gumeysi" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 90, "question": "Qiimeey xiriirka u dhexeeya 'Shuurada' iyo 'Midnimada Muslimiinta'?", "options": { "a": "Shuuradu waxay meesha ka saartaa is-maandhaafka waxayna mideysaa ra'yiga Muslimiinta", "b": "Shuuradu waxay keentaa kala qaybsanaan", "c": "Midnimadu kuma timaaddo shuuro", "d": "Waa nidaam aan hadda shaqeyn karin" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 91, "question": "Falanqee 'Baahinta Xukunka' (Decentralization) marka loo eego cadaaladda gobollada?", "options": { "a": "Waxay xaqiijinaysaa in kheyraadka iyo awoodda si siman loo gaarsiiyo meelaha fog-fog", "b": "Waxay awoodda ku koobaysaa caasimadda", "c": "Waxay daciifisaa amniga", "d": "Waa nidaam gumeysi" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch7_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch7',
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
    
    # Remove existing his_ch7 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch7']
    
    # Check if his_ch7 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch7' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 7aad: Dawladnimada, Sharciga iyo Qayb-galka Siyaasadda",
            "id": "his_ch7"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch7':
                c['title'] = "Cutubka 7aad: Dawladnimada, Sharciga iyo Qayb-galka Siyaasadda"
                break
    
    # Add new his_ch7 questions
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

    # Remove existing his_ch7 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch7']
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
