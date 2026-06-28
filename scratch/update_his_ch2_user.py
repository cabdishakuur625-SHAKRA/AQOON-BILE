import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Halkee bay ku taallaa Falastiin?", "options": { "a": "Waqooyiga Afrika", "b": "Koonfur bari ee badda dhexe", "c": "Bartamaha Aasiya", "d": "Galbeedka Yurub" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Waa kuwee dadkii ugu horreeyay ee degay dhulka Falastiin?", "options": { "a": "Yuhuudda", "b": "Kancaaniyiinta", "c": "Faarisiyiinta", "d": "Ingiriiska" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 3, "question": "Maxaa loola jeedaa magaca 'Kalcaan'?", "options": { "a": "Buuraha", "b": "Dhulka hooseeya", "c": "Badda", "d": "Webiga" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa maxay bedka guud ee dhulka Falastiin?", "options": { "a": "10 kun km2", "b": "27 kun km2", "c": "50 kun km2", "d": "100 kun km2" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 5, "question": "Sanadkee ayaa lagu dhawaaqay dawladnimada Israa'iil?", "options": { "a": "1917", "b": "1948", "c": "1967", "d": "1937" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa maxay isirka Muslimiinta laga tirada badan yahay ee Barma?", "options": { "a": "Kurdida", "b": "Ruhinga", "c": "Oromada", "d": "Berberka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Magaala madaxda dalka Miyanmaar waa maxay?", "options": { "a": "Dhaka", "b": "Raanguun", "c": "Istanbuul", "d": "Karachi" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Waa maxay tirada dadka ku nool dalka Miyanmaar?", "options": { "a": "12 Milyan", "b": "60 Milyan", "c": "27 Milyan", "d": "100 Milyan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 9, "question": "Immisa boqolkiiba dadka Kashmiir ayaa Muslimiin ah?", "options": { "a": "50%", "b": "80%", "c": "20%", "d": "95%" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa kuwee caruurtii uu ka tagay Nabi Ibraahim (NNKH)?", "options": { "a": "Ismaaciil, Isxaaq iyo Yacquub", "b": "Muuse iyo Haaruun", "c": "Yuusuf iyo Benyamiin", "d": "Nuur iyo Saalax" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 11, "question": "Sanadkee ayaa la soo saaray ballanqaadkii Belfoor?", "options": { "a": "1948", "b": "1917", "c": "1846", "d": "1999" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 12, "question": "Maxaa loola jeedaa magaca 'Aarmaan'?", "options": { "a": "Dhulka siman", "b": "Buuraha", "c": "Xeebta", "d": "Boholo" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Halkee buu ku geeriyooday Nabi Ibraahim (NNKH)?", "options": { "a": "Qudus", "b": "Al-Khaliil", "c": "Makka", "d": "Madiina" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 14, "question": "Waa maxay bedka gobolka Kashmiir?", "options": { "a": "27 kun km2", "b": "240 kun km2", "c": "680 kun km2", "d": "100 kun km2" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Goormee ayay Miyanmaar ka go'day maamulkii Ingiriiska?", "options": { "a": "1947", "b": "1937", "c": "1848", "d": "1999" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 16, "question": "Muslimiinta Barma diintee ayaa lagu cadaadiyaa?", "options": { "a": "Kiristanka", "b": "Buudistaha", "c": "Hinduuska", "d": "Yuhuudda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 17, "question": "Waa kuwee dalalka ay xadka la leedahay Kashmiir?", "options": { "a": "Soomaaliya iyo Itoobiya", "b": "Hindiya, Bakistaan, Afgaanistaan iyo Shiinaha", "c": "Masar iyo Suudaan", "d": "Iiraan iyo Ciraaq" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 18, "question": "Maxaa keena in Muslimiinta Ruhinga aan loo aqoonsan dhalasho?", "options": { "a": "Ma haystaan aqoonsi diimeed", "b": "Laguma darin 135-ta koox ee rasmiga ah", "c": "Ma rabaan inay shaqeeyaan", "d": "Waa dad soo galooti ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Xilligii ugu fiicnaa ee Falastiin soo martay waagii hore yaa talinayay?", "options": { "a": "Faarisiyiinta", "b": "Daa'uud iyo Suleeymaan", "c": "Aashuuriyiinta", "d": "Baabiliyiinta" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Sanadkee ayuu Ingiriisku qabsaday Miyanmaar?", "options": { "a": "1937", "b": "1848", "c": "1917", "d": "1819" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 21, "question": "Sidee buu u kala baxaa qaabka dhulka Falastiin?", "options": { "a": "Dhul wada buura ah", "b": "Dhul xeebeed siman, buuraley iyo dhul boholo ah", "c": "Dhul wada saxare ah", "d": "Jasiirado yaryar" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 22, "question": "Maxay Falastiin ugu weyn tahay Muslimiinta?", "options": { "a": "Waa dhul saliid badan", "b": "Waa qibladii hore iyo dhul barakeysan", "c": "Waa meel ganacsi", "d": "Waa halka ay dowladda Cusmaaniyiintu ka dhalatay" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 23, "question": "Yaa qabsaday boqortooyadii Waqooyiga Falastiin sanadkii 721 NCH?", "options": { "a": "Baabiliyiinta", "b": "Aashuuriyiinta", "c": "Faarisiyiinta", "d": "Yuhuudda" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 24, "question": "Kancaaniyiintu goormee ayay soo degeen Falastiin?", "options": { "a": "1900 NCH", "b": "3000-2500 NCH", "c": "539 NCH", "d": "1453 MI" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Maxay aaminsan yihiin mad-habta Barootestanka ee Yurub ka soo baxday?", "options": { "a": "In Falastiin tahay dhul Muslim", "b": "In Israa'iil ay leeyihiin Falastiin (Kitaabka Israa'iil)", "c": "In Falastiin ay tahay dhul caalami ah", "d": "In Falastiin lagu celiyo Turkiga" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 26, "question": "Muxuu ahaa ballanqaadkii Ingiriisku u sameeyay Yuhuudda?", "options": { "a": "In lacag la siiyo", "b": "In dal looga sameeyo dhulka Falastiin", "c": "In hub la siiyo", "d": "In laga difaaco Jarmalka" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 27, "question": "Muxuu Ingiriisku ka yeelay Kashmiir sanadkii 1846-dii?", "options": { "a": "Wuxuu siiyay Pakistaan", "b": "Wuxuu ka kireeyay nin Hinduus ah muddo 100 sano ah", "c": "Wuxuu ka dhigay magaalo xor ah", "d": "Wuxuu u dhiibay Shiinaha" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Sidee looga xallin karaa qadiyadda Kashmiir sida uu qabo qoraalku?", "options": { "a": "In Hindiya la siiyo", "b": "In la raaco halka ay Muslimiintu u badan yihiin (Pakistaan)", "c": "In dalka la qaybiyo badh badh", "d": "In Shiinaha loo dhiibo" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 29, "question": "Goormee ayuu Islaamku soo gaaray Miyanmaar markii ugu horreysay?", "options": { "a": "Qarnigii 10-aad MI", "b": "Qarnigii labaad ee hijriyada (Haaruun Rashiid)", "c": "1948", "d": "1784" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 30, "question": "Maxaa dhacay sanadkii 1784 ee gobolka Aarakaan?", "options": { "a": "Islaamka ayaa ku faafay", "b": "Boqorka Buudabaay ayaa qabsaday kuna daray Barma", "c": "Ingiriiska ayaa qabsaday", "d": "Xornimo ayay heleen" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 31, "question": "Waa maxay ururka 969 ee laga dhisay Miyanmaar?", "options": { "a": "Urur gargaar", "b": "Urur diimeed Buudiste xagjir ah oo Islaamka ka horjeeda", "c": "Xisbi siyaasadeed", "d": "Ururka ganacsatada" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 32, "question": "Intee in le'eg oo ka mid ah Kashmiir ayay Hindiya haysataa?", "options": { "a": "30%", "b": "65%", "c": "5%", "d": "100%" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 33, "question": "Goormee ayuu Islaamku gaaray Kashmiir markii ugu horreysay?", "options": { "a": "Sanadkii 90 hijriyada", "b": "1819", "c": "1947", "d": "539 NCH" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Maxay Kashmiir u tahay halbowle u ah nolosha Bakistaan?", "options": { "a": "Saliid ayaa laga soo saaraa", "b": "Waxaa ka soo baxa saddex wabi oo muhiim ah", "c": "Waa halka ay warshaduhu ku yaallaan", "d": "Waa suuq weyn oo ganacsi" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 35, "question": "Waa maxay luuqadda ay ku hadlaan Muslimiinta Ruhinga?", "options": { "a": "Ingiriis", "b": "Ruhinga ha", "c": "Urdu", "d": "Hindi" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 36, "question": "Sanadkee ayay Falastiin oo idili gacanta u gashay Faarisiyiinta?", "options": { "a": "721 NCH", "b": "539 NCH", "c": "1917 MI", "d": "1948 MI" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 37, "question": "Nabi Ibraahim (NNKH) goormee ayuu yimid dhulka Falastiin?", "options": { "a": "3000 NCH", "b": "1900 NCH", "c": "539 NCH", "d": "1917 MI" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 38, "question": "Halkee laga keenay magaca 'Falastiin' sida ku xusan qoraalka?", "options": { "a": "Magaca Kalcaaniyiinta", "b": "Badda lija ama jaziiradda Takriit", "c": "Magaca webiga Urdun", "d": "Luqadda Ingiriiska" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 39, "question": "Intee in le'eg ayay Bakistaan ka haysataa dhulka Kashmiir?", "options": { "a": "5%", "b": "30%", "c": "65%", "d": "80%" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 40, "question": "Waa maxay bedka guud ee dalka Miyanmaar?", "options": { "a": "240 kun km2", "b": "680 kun km2", "c": "27 kun km2", "d": "60 kun km2" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 41, "question": "Maxaa weheliyay Kancaaniyiinta markii ay soo degayeen Falastiin?", "options": { "a": "Ingiriiska", "b": "Aaraamiyiinta iyo Finiiqiyiinta", "c": "Yuhuudda", "d": "Faarisiyiinta" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 42, "question": "Intee in le'eg ayay Shiinaha ka haysataa dhulka Kashmiir?", "options": { "a": "30%", "b": "5%", "c": "65%", "d": "0%" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 43, "question": "Sanadkee ayuu Ingiriisku qabsaday Hindiya?", "options": { "a": "1947", "b": "1819", "c": "1848", "d": "1917" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 44, "question": "Goormee ayuu Suleeymaan (CS) geeriyooday ka dibna boqortooyadii kala jabtay?", "options": { "a": "Ka hor 1900 NCH", "b": "Xilligii qadiimka", "c": "Xilligii Cusmaaniyiinta", "d": "Ma jiro taariikh sugan" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 45, "question": "Falanqee istiraatiijiyada deegaanka Kashmiir iyo muhiimadda ay u leedahay dalalka gobolka?", "options": { "a": "Waa dhul aan muhiim ahayn oo cidla ah", "b": "Waa goob muhiimad difaac iyo amni u leh Hindiya, Bakistaan iyo Shiinaha", "c": "Waa meel kaliya loo dalxiis tago", "d": "Waa marin u dhexeeya Afrika iyo Aasiya" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 46, "question": "Maxay qaddiyadda Falastiin u soo if baxday casrigan dambe marka loo eego kaalinta Yurub?", "options": { "a": "Maaddaama ay tahay dhul dalxiis", "b": "Taageerada reer Yurub iyo ballanqaadkii Ingiriiska ee ahaa deegaan Yuhuudeed", "c": "Dhaqaalaha laga helay Falastiin darteed", "d": "Maaddaama ay kutaallo meel biyo la'aan ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 47, "question": "Waa maxay xalka ugu habboon ee qadiyadda Falastiin sida ku xusan qoraalka?", "options": { "a": "In dhulka loo daayo Israa'iil", "b": "In Muslimiintu midoobaan, hal mowqifna ka istaagaan taageerada Falastiin", "c": "In Qaramada Midoobay ay xukunto dhulka", "d": "In dadka Falastiiniyiinta ah laga raro dhulka" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 48, "question": "Sharax doorka Qaramada Midoobay ka ciyaartay xasuuqa Muslimiinta Ruhinga?", "options": { "a": "Waxay qaadatay go'aano adag oo lagu joojiyay xasuuqa", "b": "Ilaa hadda waxay ka indha laabaneysaa xasuuqa iyo barakicinta qasabka ah", "c": "Waxay ciidamo u dirtay Miyanmaar", "d": "Waxay dhalasho siisay dadka Ruhinga" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 49, "question": "Falanqee muhiimadda ay Kashmiir u leedahay Hindiya dhanka falsafadda xukunka?", "options": { "a": "Waxay rabaan inay diinta Islaamka ku faafiyaan", "b": "Inay xoojiso falsafadda xukunkeeda calmaaniga ah iyo xannibaadda Bakistaan", "c": "Waxay rabaan inay dadka Kashmiir canshuur badan ka qaadaan", "d": "Inay dhistaan warshado waa weyn" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 50, "question": "Sidee bay dowladda Miyanmaar u cadaadisaa Muslimiinta Ruhindiga dhanka dhaqaalaha iyo sharciga?", "options": { "a": "Waxay u oggolaadaan inay ganacsadaan", "b": "Barakicin, ka ceyrinta shaqooyinka, iyo la wareegidda hantidooda", "c": "Waxay siiyaan dhalasho buuxda", "d": "Ma jiraan wax cadaadis ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 51, "question": "Sharax ujeeddada uu boqorka Buudabaay u qabsaday Aarakaan sanadkii 1784?", "options": { "a": "Si uu u caawiyo Muslimiinta", "b": "Maaddaama uu ka baqayay in Islaamku uu dalkiisa ku faafo", "c": "Si uu ganacsiga u horumariyo", "d": "Si uu u eryo Ingiriiska" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 52, "question": "Falanqee sheegashada diineed ee Yuhuudda iyo sida Muslimiintu u arkaan?", "options": { "a": "Muslimiintu waxay u arkaan inay Yuhuuddu xaq u leedahay", "b": "Muslimiintu waxay u arkaan dhulkii nabiyada oo ay iyagu leeyihiin, Yuhuudduna ku marmarsiyooto madhabta Barootestanka", "c": "Ma jirto cid sheegata dhulkaas", "d": "Labaduba waxay ku heshiiyeen inay qaybsadaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 53, "question": "Sidee buu ahaa heshiiskii Ingiriisku markii uu qaybinayay Hindiya iyo Bakistaan sanadkii 1947?", "options": { "a": "In gobol kasta uu noqdo dal madax-bannaan", "b": "Gobolkii Muslimiintu u badnaayeen laraaciyo Pakistaan, kii Hinduusku ubadnaayeenna Hindiya", "c": "In Ingiriisku sii maamulo gobolladaas", "d": "In la gubaa dhulkaas oo dhan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 54, "question": "Maxaa keena in Muslimiinta Ruhinga loo tixgeliyo 'dad aan wadan lahayn'?", "options": { "a": "Ma haystaan luuqad gaar ah", "b": "Maadaama aan loo aqoonsanayn inay ka tirsan yihiin 135-ta koox ee dalkaas deggan", "c": "Maadaama ay yihiin dad aad u tiro yar", "d": "Maadaama ay rabaan inay dalka ka baxaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 55, "question": "Falanqee xiriirka ka dhexeeya ururka 969 iyo xaaladda Muslimiinta Miyanmaar?", "options": { "a": "Waxay ka shaqeeyaan nabadeynta dalka", "b": "Waa xagjiriin Buudiste ah oo loo sameeyay inay hor istaagaan fiditaanka Islaamka", "c": "Waa urur dhalinyaro oo ciyaaraha ka shaqeeya", "d": "Waa xisbi muxaafid ah oo Muslimiinta taageera" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 56, "question": "Maxay Kashmiir muhiim ugu tahay difaaca Pakistaan?", "options": { "a": "Maaddaama ay ku yaallaan buuro batrool leh", "b": "Waa saldhig difaac u ah waqooyiga Pakistaan iyo xoog dadeed oo Muslimiin ah", "c": "Waa halka ay ka soo go'aan dhammaan raashinka dalka", "d": "Waa meel ay ku tababartaan ciidanka badda" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 57, "question": "Sharax siday boqortooyada Falastiin ugu kala jabtay labo dhimashadii Suleeymaan (CS) ka dib?", "options": { "a": "Midna dadka ayaa qaatay midna boqorka", "b": "Waqooyiga (Aashuuriyiinta qabsadeen) iyo Qudus (Baabiliyiinta qabsadeen)", "c": "Waxay u kala jabtay dalal yaryar oo xor ah", "d": "Cidna ma qabsan ee iyaga ayaa isku dhex dhimaday" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 58, "question": "Sidee bay ganacsatada Muslimiintu kaalin uga qaateen faafinta Islaamka Miyanmaar?", "options": { "a": "Iyadoo ciidamo ay kaxaysteen", "b": "Iyadoo koox ganacsato ah oo martay Aarakaan ay diinta gaarsiiyeen xilligii Haaruun Rashiid", "c": "Ma jiraan ganacsato Islaamka geeyay", "d": "Iyadoo boqorka Barma ay lacag siiyeen" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay tahay sababta dhabta ah ee looga soo horjeedo Muslimiinta Ruhinga sida ku xusan taariikhda boqorka Buudabaay?", "options": { "a": "Inay dhul badan qaateen", "b": "In laga baqayo in Islaamku uu dalka ku faafo", "c": "Inay la shaqeeyaan Ingiriiska", "d": "Inay luqad kale ku hadlaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 60, "question": "Falanqee xalka qadiyadda Ruhindiga sida uu qoraalku soo jeedinayo?", "options": { "a": "In dadkaas laga saaro dalka Miyanmaar", "b": "In la dhigo gogol nabadeed, lana joojiyo xasuuqa iyo isir goynta", "c": "In lagu daro dalka Bangladesh", "d": "In loo qaybiyo hub si ay isu difaacaan" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 61, "question": "Muxuu ahaa magaca gobolkii lagu daray Barma sanadkii 1784?", "options": { "a": "Kashmiir", "b": "Aarakaan", "c": "Raanguun", "d": "Qudus" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 62, "question": "Maxay Hindiya u aragtaa xornimada Kashmiir mid khatar ku ah?", "options": { "a": "Waxay u aragtaa inay furayso albaab xiran oo aan la xakameyn karin", "b": "Waxay ka baqaysaa inay Shiinaha raacaan", "c": "Ma rabaan inay weeyaan biyo", "d": "Inay dadkaas noqdaan kuwo taajir ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Sharax xilligii Nabi Ibraahim (NNKH) uu yimid Falastiin iyo caruurtii uu kaga tagay?", "options": { "a": "1900 MI, caruurtiisuna waxay ahaayeen Ismaaciil iyo Isxaaq", "b": "1900 NCH, caruurtiisuna waxay ahaayeen Ismaaciil, Yacquub iyo Isxaaq", "c": "3000 NCH, caruurtiisuna waxay ahaayeen Kancaaniyiin", "d": "1917 MI, caruurtiisuna waxay ahaayeen Yuhuud" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 64, "question": "Maxay ku kala duwan yihiin 'Kancaaniyiinta' iyo 'Aaraamiyiinta' dhanka deegaanka?", "options": { "a": "Kancaaniyiintu xeebta ayay degeen, Aaraamiyiintuna buuraha", "b": "Kancaaniyiintu waa dad taajir ah, Aaraamiyiintuna waa masaakiin", "c": "Labaduba isku meel ayay wada degeen oo waa xeebta", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Muxuu xalku noqon karaa haddii Muslimiintu u midoobi lahaayeen Falastiin?", "options": { "a": "In Yuhuudda lala heshiiyo oo dhulka la siiyo", "b": "In hal mowqif la qaato lana bilaabo wada hadal xooggan oo lagu taageerayo Muslimiinta Falastiin", "c": "In Qaramada Midoobay la baryo", "d": "In dalka laga haajiro" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 66, "question": "Waa maxay ujeeddada ka dambeysa xasuuqa joogtada ah ee Muslimiinta Barma?", "options": { "a": "In dalku nabad noqdo", "b": "In Islaamka dalka laga dabar gooyo lana barakiciyo dadka Ruhinga", "c": "Si dadka looga dhigo kuwo shaqeeya", "d": "Ma jiro xasuuq joogto ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 67, "question": "Falanqee saameynta siyaasadeed ee kireyntii Kashmiir (1846)?", "options": { "a": "Waxay keentay in dadku xor noqdaan", "b": "Waxay gogol xaar u ahayd 100 sano oo cadaadis ah oo Hinduusku ku hayo Muslimiinta", "c": "Waxay keentay in Ingiriisku dalka ka baxo", "d": "Waxay keentay in Shiinuhu qabsado Kashmiir" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 68, "question": "Intee in le'eg ayay Kashmiir muhiim u tahay webiyada Pakistaan?", "options": { "a": "Ma laha wax wabiyaal ah", "b": "Waxay ka soo baxaan saddexda wabi ee halbowle u ah nolosha Bakistaan", "c": "Webiyada Pakistaan waxay ka yimaadaan Hindiya", "d": "Webiyada Kashmiir waxay aadaan dhanka Shiinaha" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 69, "question": "Sharax siday u wada degeen Kancaaniyiinta iyo Finiiqiyiinta?", "options": { "a": "Waxay soo degeen intii u dhexeysay 3000-2500 NCH", "b": "Waxay soo degeen sanadkii 1917", "c": "Waxay yimaadeen dhimashadii Suleeymaan ka dib", "d": "Waxay ka yimaadeen dhanka Yurub" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Muxuu ahaa qorshihii Ingiriiska ee gobolka Bunjaab?", "options": { "a": "In laga dhigo dal madax-bannaan", "b": "Kashmiir waxay u tahay xoog dadeed oo Muslimiin ah oo taageeraya gobolkaas", "c": "In dadka laga dhigo Hinduus", "d": "In Ingiriisku sii maamulo" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 71, "question": "Falanqee bedka dalka Miyanmaar marka loo eego tirada dadka Ruhinga?", "options": { "a": "Bedkeedu waa 680 kun km2, Ruhingana waa dad laga tirada badan yahay oo la dhibo", "b": "Bedkeedu waa 27 kun km2, Ruhingana waa dadka ugu badan", "c": "Ma jiro wax xiriir ah", "d": "Bedkeedu waa mid aad u yar" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Maxaa keena in Muslimiinta Ruhinga ay ku hadlaan af ka geddisan kan gobollada kale ee Miyanmaar?", "options": { "a": "Maaddaama ay yihiin dad ka yimid Yurub", "b": "Maaddaama ay yihiin isir iyo koox gaar ah (Ruhinga ha)", "c": "Maaddaama ay doonayaan inay is qariyaan", "d": "Ma hadlaan af gaar ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 73, "question": "Maxay ahayd sababta uu Ingiriisku uga kireeyay Kashmiir ninkii Hinduuska ahaa?", "options": { "a": "Si uu Muslimiinta u caawiyo", "b": "Maaddaama uu 27 sano la dagaallamayay uuna u suurta geli weyday qabsasho toos ah", "c": "Sababtoo ah Hinduuska ayaa lacag badan siiyay", "d": "Ma jirin sabab gaar ah" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 74, "question": "Falanqee ujeeddada laga leeyahay barakicinta qasabka ah ee Muslimiinta Barma?", "options": { "a": "In dhulalkooda lala wareego lana isir gooyo", "b": "In dadka loo raadiyo meel ka fiican", "c": "Si dalka looga dhigo mid barwaaqo ah", "d": "In la baro dhaqanka Buudistaha" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Sharax doorka Haaruun Rashiid ee taariikhda Islaamka Miyanmaar?", "options": { "a": "Isaga ayaa qabsaday dalkaas", "b": "Xilligiisii ayaa ganacsato Muslimiin ahi ay Islaamka geeyeen dalkaas", "c": "Wuxuu dhisay masaajidkii ugu weynaa Barma", "d": "Wuxuu xiriir la lahaa boqorka Buudabaay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 76, "question": "Muxuu ahaa go'aankii Ingiriiska ee bixitaankii Hindiya sanadkee 1947?", "options": { "a": "Inuu dhulka gabi ahaanba isaga baxo isagoo cidna u dhiibin", "b": "Inuu dalka u qaybiyo labo dowladood oo ku salaysan diinta (Hindiya iyo Pakistaan)", "c": "Inuu dalka u dhiibo Shiinaha", "d": "Inuu dalka u dhiibo Qaramada Midoobay" }, "correctAnswer": "b", "difficultyLevel": "hard" },
  { "id": 77, "question": "Maxay Falastiin ugu dhex jirtaa 'dhulka barakeysan' ee Qur'aanka lagu sheegay?", "options": { "a": "Maaddaama ay tahay dhul ku yaalla badda dhexe", "b": "Maaddaama ay tahay dhulkii nabiyada iyo qibladii hore", "c": "Maaddaama ay tahay dhul dalxiis", "d": "Ma jiro wax barako ah oo ku dhex jirta" }, "correctAnswer": "b", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"His_Ch2_Q{i+1:02d}",
        'subjectId': 'his',
        'chapterId': 'his_ch2',
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
    
    # Remove existing his_ch2 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'his_ch2']
    
    # Check if his_ch2 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'his_ch2' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "his",
            "title": "Cutubka 2aad: Dunida Islaamka iyo Qadiyadaha Casriga ah",
            "id": "his_ch2"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'his_ch2':
                c['title'] = "Cutubka 2aad: Dunida Islaamka iyo Qadiyadaha Casriga ah"
                break
    
    # Add new his_ch2 questions
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

    # Remove existing his_ch2 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'his_ch2']
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
