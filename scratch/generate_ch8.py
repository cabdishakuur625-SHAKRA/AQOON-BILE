import json
import random
import os

questions = []
id_counter = 1

def add_q(q_text, correct, w1, w2, w3, difficulty):
    global id_counter
    opts = [correct, w1, w2, w3]
    random.shuffle(opts)
    
    correct_key = ''
    options_dict = {}
    for i, opt in enumerate(opts):
        key = chr(97 + i) # a, b, c, d
        options_dict[key] = opt
        if opt == correct:
            correct_key = key
            
    q = {
        "id": f"Som_Ch8_Q{id_counter:02d}",
        "question": q_text,
        "options": options_dict,
        "correctAnswer": correct_key,
        "difficultyLevel": difficulty,
        "subjectId": "somali",
        "chapterId": "somali_ch8"
    }
    questions.append(q)
    id_counter += 1

# Easy Questions (25)
easy_data = [
    ("Waa maxay Sahan?", "Hanaan lagu uruuriyo xog", "Ciyaar hiddo ah", "Gabay soomaaliyeed", "Cunto dhaqameed"),
    ("Yaa curiyey heesta 'Soomaali baan ahay'?", "C/qaadir Xirsi YamYam", "Xasan Ganeey", "Hadraawi", "Cali Sugulle"),
    ("Xagee ayuu ku dhashay abwaan Xasan Ganeey?", "Duleedka Bullaxaar", "Hargeysa", "Muqdisho", "Kismaayo"),
    ("Goorma ayuu Xasan Ganeey ku biiray ciidamadii kumaandooska?", "1967 kii", "1970 kii", "1960 kii", "1980 kii"),
    ("Goorma ayuu Xasan Ganeey ku biiray kooxdii baanbayda?", "1970 kii", "1967 kii", "1980 kii", "1960 kii"),
    ("Maxaa loola jeedaa 'barkhadaystayaal'?", "Dadka rajo fiican kunoolka ah", "Dadka xoola dhaqatada ah", "Dadka xunxun", "Dadka beeraleyda ah"),
    ("Maxaa loola jeedaa 'baasaystayaal'?", "Dadka rajo xun kunoolka ah", "Dadka rajo fiican kunoolka ah", "Dadka caqliga badan", "Dadka dagaalyahanada ah"),
    ("Yaa curiyey maansada 'Dhaqan'?", "Xasan Xaaji C/laahi (Xasan Ganeey)", "C/qaadir Xirsi YamYam", "Hadraawi", "Cali Xuseen"),
    ("Waa kuma cidda keliya ee ay soomaalidu u taqaanay sokeeye?", "Carabta muslimiinta ah", "Reer galbeedka", "Aasiyaanka", "Afrikaanka kale"),
    ("Maxaa kamid ah waxyaabaha bulshada ka leexiya danta guud?", "Anshax xumada", "Waxbarashada", "Wadashaqeynta", "Run sheegida"),
    ("Maxay ka dhigan tahay 'adigu ma istaqaan'?", "In qofku is qiimeeyo oo fahmo qofka uu yahay", "In qofku dadka kale barto", "In qofku xoolo raadiyo", "In qofku safro"),
    ("Waa maxay danta guud?", "Dhawrista iyo ilaalinta waxyaabaha bulshada ka dhexeeya", "In qof kasta danihiisa gaarka ah raadsado", "In sharciga la jebiyo", "In la dagaalamo"),
    ("Waa maxay Anshax?", "Xeerarka kala garata waxa wanaagsan iyo xun", "Cunto fudud", "Nooc kamid ah dharka", "Qalab dagaal"),
    ("Yaa xil ka saaran yahay ilaalinta waxyaabaha inaga dhexeeya?", "Dhammaan xilbaa naga wada saaran", "Madaxda oo kaliya", "Odayaasha oo kaliya", "Dhalinyarada oo kaliya"),
    ("Waa maxay qumanayaal?", "Waxyaabaha qofnimada ka sameysan tahay", "Buuro dhaadheer", "Magaalooyin qadiimi ah", "Cudurro khatar ah"),
    ("Fikrada ah in dadka isku mid noqdaan goorma ayey soo ifbaxday?", "Qarnigii 20aad", "Qarnigii 19aad", "Qarnigii 18aad", "Qarnigii 21aad"),
    ("Sidee ku ogaan kartaa qofnimada cid kasta ay leedahay?", "Jid inaad la marto, jabad inaad la degto, ama cunto inuu idin dhexmaro", "Inaad wejigiisa eegto oo kaliya", "Inaad magiciisa weydiiso", "Inaad xoolahiisa tiriso"),
    ("Maxaa loola jeedaa deegaanka qofka?", "Qoyskaaga, wadaayadaada, gurigaaga, rugaha waxbarashada, bulshadaada", "Dhirta iyo ugaarta oo kaliya", "Xoolaha iyo beelaha oo kaliya", "Cimilada iyo buuraha oo kaliya"),
    ("Waa maxay aanooyinka qofka?", "Waayo aragnimada iyo waxyaabaha deegaanku ku kordhiyay qofnimadiisa", "Cudurada qofka ku dhaca", "Dhaqaalaha qofka", "Taariikhda qoyskiisa"),
    ("Maxaa loola jeedaa 'waano abuuris baa ka horeysay'?", "Qof dabeecad xun waano waxba kama tarto", "Qofka waa in la waaniyo markasta", "Abuurista dadka isku mid maaha", "Waano waa furaha guusha"),
    ("Muxuu kahadlayaa casharka Q8?", "Ilaalinta danta guud", "Barashada xiddigaha", "Dhaqashada xoolaha", "Sameynta doomo"),
    ("Sahan waa hanaan lagu uruuriyo maxay?", "Xog, war iyo wacaal", "Biyo", "Geedo", "Qalab"),
    ("Maxay soomaalidu ka aaminsan tahay sooyaalkeeda?", "Ma taqaan", "Si fiican ayey u taqaan", "Way qortay", "Way u heestaa"),
    ("Maxaa inagu kalifaaya in aynu wax wada ilaashano?", "Dal, calan, af iyo diin baa inaga dhexeeya", "Cagajugleyn shisheeye", "Dhaqaale raadis", "Cabsida cudurada"),
    ("Qofnimada qofka sidee loo qiimeeyaa?", "Siduu isu haysto/arko iyo xogta dadka kale bixiyaan", "Dhererkiisa", "Midabkiisa", "Hantidiisa")
]

# Medium Questions (27)
medium_data = [
    ("Imisa qodob ayaa loo baahan yahay si loo diyaariyo sahan?", "In ka badan 5 qodob", "2 qodob", "1 qodob", "3 qodob"),
    ("Qodobadan kee baa ka mid ah ciwaanada sahanka?", "Talo bixinta sahanka", "Dhaqaalaha sahanka", "Da'da sahanka", "Magaca sahanka"),
    ("Maxaa loola jeedaa 'soomaalidu ma istaqaan' marka laga hadlayo casharka?", "Sooyaalkeeda, sokeeyaheeda, soohdinteeda ma taqaan", "Ma taqaan luqado kale", "Ma taqaan dalal kale", "Ma taqaan cuntooyinka qalaad"),
    ("Sida ay aaminsan yihiin sahamiyayaashii reer galbeedka, Soomaalidu maxay u fiicnaayeen?", "Sooyaalka", "Dhismaha buundooyinka", "Sameynta gawaarida", "Barashada sayniska"),
    ("Tilmaamaha reer galbeedku isku raaceen ee Soomaalida leedahay waxaa ka mid ah:", "Dad martisoor wacan", "Dad gaagaaban", "Dad xishood badan", "Dad aan safin"),
    ("Tilmaam kale oo reer galbeedku Soomaalida ku tilmaameen waa?", "Dhul yaqaan ayey ahaayeen", "Badmareeno ayey ahaayeen", "Beeraley waaweyn ayey ahaayeen", "Ganacsato kaliya ayey ahaayeen"),
    ("Isbedelada nolosha qofka imisa ayey u qaybsamaan?", "Saddex (3)", "Laba (2)", "Afar (4)", "Shan (5)"),
    ("Isbedelada qaar waxba lagama bedeli karo, tusaale ahaan:", "Muuqaalka iyo Hidaha", "Ilig kaa dhacay", "Nabar ku gaaray", "Caqiidada"),
    ("Isbedelada wax laga bedeli karo waxaa tusaale u ah:", "Ilig kaa dhacay ama nabar", "Muuqaalka asalka ah", "Hidde sidayaasha (DNA)", "Dhererka qofka"),
    ("Isbedel adag in la bedelo laakiin suuragal ah waa:", "Caqiidada", "Muuqaalka", "Hidaha", "Da'da qofka"),
    ("Qumanayaasha qofka waxaa ka mid ah:", "Siduu isu arko, hab dhaqankiisa, dareenkiisa, fekerkiisa", "Cuntada uu cuno", "Dharka uu xirto", "Guriga uu degan yahay"),
    ("Qumanayaasha hidaysiga ah ee waalidka laga dhaxlo waxaa ka mid ah:", "Jismiga, dabeecada, muuqaalka, midabka", "Caqiidada iyo luqada", "Dhaqaalaha iyo hantida", "Waxbarashada iyo xirfada"),
    ("Maxaa loola jeedaa 'basar xun' ama 'basar fiican'?", "Dabeecad xun ama dabeecad wanaagsan", "Cunto xun ama cunto fiican", "Muuqaal xun ama muuqaal fiican", "Dhul xun ama dhul fiican"),
    ("Abwaan Xasan Ganeey, muxuu tusaale ahaan usoo qaatay maansadiisii Dhaqan?", "Dhul kayn iyo buuro qurux badan leh oo roob fiican helay", "Magaalooyin casri ah", "Bado waaweyn iyo jasiirado", "Xoolo aad u farabadan"),
    ("Arrimaha sahanka loo baahan yahay marka la diyaarinayo waxaa ka mid ah:", "In natiijada kasoo baxda la abla-ableeyo", "In sheeko la iska allifo", "In aan xogta cidna lala wadaagin", "In xogta oo dhan la iska tuuro"),
    ("Marka laga reebo Carabta muslimiinta ah, Soomaalidu ma u taqaanay sokeeye ummado kale xilligii hore?", "Maya", "Haa, reer yurub", "Haa, Aasiyaanka", "Haa, dhammaan dadka madow"),
    ("Dhinaca soohdinta, tilmaamaha reer galbeedku ee Soomaalida waxay sheegayaan:", "Soohdinta way ilaashan jireen", "Soohdinta ma aqoon", "Soohdinta cadowga ayey u dhiibeen", "Soohdintu muhiim uma ahayn"),
    ("Qaabka qofka loo qiimeeyo waxaa tiir u ah:", "Xogta ay dadku isaga ka bixiyaan iyo sida ay u arkaan", "Lacagtiisa bankiga ku jirta", "Nooca baabuurka uu wato", "Tirada xoolihiisa"),
    ("Waa maxay qaybta ugu dambeysa ee warbixinta sahanka?", "Talo bixinta sahanka", "Tixraaca", "Ararta", "Hilinka"),
    ("Maxaa inagu kalifa in aan si wadajir ah u ilaashano danta guud?", "Hal soohdin, hal af iyo hal diin baynu wada haysanaa", "Cabsida abaaraha", "Mushaar inaan ku helno", "Inaan dalal kale qabsano"),
    ("Waxyaabaha danta guud leexiya ee ummada dhibaatada ku ah waa maxay?", "Anshax xumo kasta", "Ganacsiga xorta ah", "Waxbarashada casriga ah", "Qabyaalad la'aanta"),
    ("Ereyga 'baasaystayaal' wuxuu inta badan tilmaamayaa dadka:", "Wax kasta dhanka xun ka arka", "Wax kasta dhanka fiican ka arka", "Xoolaha badan", "Safarka badan"),
    ("Cidda diyaarinaysa weydiimaha sahanka waa inay:", "Abla-ableeyaan natiijada kasoo baxda", "Qariyaan xogta dhabta ah", "Jawaabaha sii qiyaasaan iska bedelaan", "Buunbuuniyaan warbixinta"),
    ("Tixraaca sahanka macnaheedu waa maxay?", "Halka laga soo xigtay xogta iyo macluumaadka", "Gunaanadka warbixinta", "Waqtiga la bilaabay sahanka", "Ujeedada sahanka"),
    ("Waa maxay ujeedka laga leeyahay 'sooyaalkeeda ma taqaan'?", "Ummada oo aan aqoon u lahayn taariikhdeedii hore", "Dadka oo aad u yaqaan taariikhda", "in taariikhda la bedelay", "In la diiday taariikhda"),
    ("Reer galbeedku waxay Soomaalida ku tilmaameen dad dhuudhuuban oo:", "Dhaadheer", "Gaagaaban", "Cayilan", "Madow"),
    ("Curiyaha maansada Dhaqan waa:", "Xasan Xaaji C/laahi", "Cabdi Qays", "Maxamed Ibraahim Warsame", "Cali Sugulle")
]

# Hard Questions (29)
hard_data = [
    ("Marka la diyaarinayo warbixin sahan, waa in si cad loo xuso:", "Cidda codsatay iyo amminta kama dambeysta ah", "Kharashka baxay oo kaliya", "Magacyada dhamaan dadka la wareystay", "Halka laga soo iibsaday qalabka"),
    ("Waa maxay ujeedada ugu weyn ee loo diyaariyo weydiimaha sahanka?", "In si nidaamsan loogu uruuriyo xog iyo wacaal si warbixin loo dhammaystiro", "In dadka la isku diro", "In waqtiga la iska lumiyo", "In lacag lagu raadiyo"),
    ("Ararta guud ee sahanka maxay ka tarjumaysaa?", "Waa hordhaca muujinaya nuxurka iyo ujeedada warbixinta", "Waa qodobada u dambeeya warbixinta", "Waa liiska dadka sahanka fuliyay", "Waa magaca mashruuca"),
    ("Hilinka xog uruurinta maxaa loola jeedaa?", "Wadada ama habka loo maray si loo helo xogta sahanka", "Halka laga bilaabay safarka", "Qalabka sahanka", "Natiijada ugu dambaysa"),
    ("Abla-ableynta natiijada kasoo baxda sahanku waa:", "Kala hufidda iyo lafo-gurka xogta si go'aan looga gaaro", "Akhrinta warbixinta oo kaliya", "Gubida xogaha aan loo baahnayn", "Kaydinta xogta qarsoon"),
    ("Sidee bay 'adigu ma istaqaan' ula xiriirtaa is-qiimeynta qofka?", "Waxay qofka ku dhiirigelinaysaa inuu si dhab ah u fahmo awoodihiisa iyo daciifnimooyinkiisa", "Waxay ku guubaabinaysaa inuu dadka kale eedeeyo", "Waxay u sheegaysaa inuu ka aamuso xaqiisa", "Waxay tusinaysaa inuusan muhiim ahayn"),
    ("Sababta isbedelada caqiidada ay u adag tahay in la bedelo laakiin macquul ay u tahay ayaa ah:", "In ay ku saleysan tahay rumaysi qoto dheer oo waqti badan qaatay", "In la iibsan karo rumaysiga", "In hidde ahaan la isku gudbiyo", "In dadku aysan waxba akhrin"),
    ("Sida casharku qabo, qumanayaasha qofnimada ee ku saleysan 'fekerkiisa' iyo 'dareenkiisa' waa kuwa:", "Laga bedeli karo iyadoo la eegayo deegaanka iyo waxbarashada", "Aan weligood la bedeli karin", "La mid ah hidda sidayaasha muuqaalka", "Qofka iskiis ugu soo dhasho"),
    ("Goorma ayey ahayd markii ugu horraysay ee si weyn loo falanqeeyo in dadku isku mid noqon karaan adduunka?", "Qarnigii 20aad iyadoo is-dhexgal ballaaran yimid", "Qarnigii 15aad", "Xilligii casrigii dhagaxa", "Qarnigii 21aad kaligiis"),
    ("Tijaabinta qofnimada dadka iyadoo la marayo jid, jabad, iyo cunto maxay tusinaysaa?", "In dhaqanka soomaalidu aaminsan yahay in dabeecadda qofka lagu barto safarka iyo wax-wada-qaybsiga", "In qofka aan lagu aamini karin cunto", "In socdaalku khatar yahay", "In qof kasta oo cunto lala cuno uu yahay qof xun"),
    ("Muxuu ula jeedaa qoraagu marka uu yiraahdo 'waano abuuris baa ka horeysay'?", "Haddii dabeecadda aasaasiga ah ee qofku xun tahay, wacyigelin iyo waano saameyn kuma yeeshaan", "Waano waa in la bixiyaa ka hor inta aan la dhalan", "Abuurista dadka ayaa la waaniyaa", "Qof walba wuu qaataa waanada"),
    ("Sida loo qeexo 'Aanooyinka qofka' waxay muujinaysaa:", "Saamaynta culus ee deegaanka, waayo-aragnimada, iyo waxa uu rumeysan yahay ay ku leeyihiin shakhsiyaddiisa", "In qofku leeyahay aanooyin uusan iska gudi karin", "In qofka qoyskiisa uun laga aarguto", "Taariikhda dhiigga ee qoyska"),
    ("Ereyga 'danta guud' kuma koobna oo kaliya hantida dawladda, balse wuxuu ku qotomaa:", "Dhawrista iyo ilaalinta dhammaan waxyaabaha masiiriga ah ee bulshada ka dhexeeya", "Uruurinta canshuuraha", "Ilaalinta amniga madaxda", "Nadiifinta waddooyinka oo kaliya"),
    ("Xasan Ganeey kumaandooska buu ku biiray 1967, baanbaydana 1970, maxay tani ina tuseysaa taariikhdiisa?", "Inuu lahaa waayo-aragnimo ciidan iyo mid farshaxan/muusig isku dhafan", "Inuu isaga baxay ciidamada dhaqso", "Inuusan weligii ciidan noqon", "Inuu asaasay kumaandooska"),
    ("Tilmaanta ay reer galbeedku ku sifeeyeen Soomaalida ee 'sooyaalka way ku fiicnaayeen' waxay liddi ku tahay:", "Weeraha ah in Soomaalidu uusan 'sooyaalkeeda aqoon'", "Fikradda ah in Soomaalidu badmareeno ahaayeen", "Taariikhdii gumeysiga ee Afrika", "Xiriirkii Soomaalida iyo Carabta"),
    ("Xilka ilaalinta waxa naga dhexeeya ee 'dhammaan naga wada saaran' wuxuu la micno yahay:", "Waajib wadareed dusha ka saaran muwaadin kasta oo Soomaaliyeed", "In dawladda oo kaliya lagu eedeeyo dib-u-dhaca", "In odayaasha dhaqanka ay qaadaan mas'uuliyadda fashilka", "In qof walba iska aamuso"),
    ("Muxuu Xasan Ganeey u soo qaatay 'dhul kayn iyo buuro qurux badan oo roob fiican da'ay' maansadiisa Dhaqan?", "Waa tusaale bilicsan oo sawiraya hufnaanta, kheyraadka iyo qiimaha dalka iyo dhaqanka", "Wuxuu doonayey inuu beero iibsado", "Waa tusaale muujinaya abaarta", "Wuxuu dadka ugu yeerayay xaalufinta"),
    ("Marka la leeyahay qumanayaasha qofka waxa kamid ah 'hab dhaqankiisa', tan macnaheedu waa:", "Sida uu ula falgalo deegaanka, dadka, iyo xaaladaha kala duwan", "Dharka uu jecel yahay inuu xirto uun", "Nooca shaqada uu qabto oo kaliya", "Sida uu u hadlo kaliya"),
    ("Isbedelada aan wax laga bedeli karin ee 'Muuqaalka iyo Hidaha' waxay tilmaamayaan:", "Nidaamka dabiiciga ah ee Eebbe qofka ku abuuray, hidde-sideyaashiisa, iyo isirkiisa", "Midabka dharka uu xirto qofka", "Dabeecadaha uu deegaanka ka barto", "Fikirada siyaasadeed ee uu qaato"),
    ("Sidee 'Anshax xumada' ay ugu tahay khatar ilaalinta danta guud?", "Waxay wiiqdaa kalsoonida bulshada, xeerarkii wanaagsanaa, iyo masuuliyadii wadajirka ahayd", "Waxay kordhisaa dhaqaalaha dalka balse dhaqanka ayay yareyneysaa", "Khatar kuma aha ilaalinta danta guud", "Waxay dadka barta u oggolaataa inay kaligood noolaadaan"),
    ("Ereyga 'sokeeyaheeda ma taqaan' wuxuu xambaarsan yahay fekerka ah in:", "Ummaddu aysan aqoon dhab ah u lahayn cidda ay is-xigaan ee danta wadaaga", "Soomaalidu dhammaan caalamka nacab la tahay", "Qof kasta oo shisheeye ah uu sokeeye yahay", "Dawladaha jaarka ah ay yihiin sokeeyaha kaliya"),
    ("Arrimaha sahanka ku saabsan ee la weydiiyo cidda codsatay iyo ujeedada warbixinta waxay muujinayaan:", "In sahanku leeyahay hanaan cilmiyeysan, qorsheysan, oo jawaab u raadinaya su'aal gaar ah", "In sahanku yahay olole aan ujeedo lahayn", "In natiijada sahanka mar hore la sii ogaa", "In qof kasta iska codsan karo sahan aan la fahmin"),
    ("Muxuu yahay xiriirka ka dhexeeya 'barkhadaystayaal' iyo horumarka qofka?", "Rajada wanaagsan waxay horseedaa himilo sare, dhiirigelin joogto ah, iyo horumar", "Rajadu kuma xirna horumarka qofka", "Rajada fiican waxay qofka ka dhigtaa mid caajis ah", "Qofka rajo xun uun baa guuleysta"),
    ("Qiimeynta qofka oo lagu saleeyo xogta ay dadku ka bixiyaan waxay tusinaysaa:", "In qofnimadu aysan ku ekeyn aragtida isaga uun balse ay tahay mid bulshadu ka marqaati kacdo", "In qofku xaq u lahayn inuu is-qiimeeyo", "In dadka kale had iyo jeer ku qaldan yihiin qofka", "In qofku qariyo dabeecaddiisa rasmiga ah"),
    ("Maxay tahay sababta dabeecada, muuqaalka iyo midabka loogu tixgeliyo qumanayaasha hidaysiga ee laga dhaxlo waalidka?", "Waa arrimo hidde-sideyaasha waalidku toos ugu gudbiyaan carruurta dhalasho ahaan", "Waayo waa wax iskuulka lagu barto", "Sababtoo ah bulshada ayaa go'aamisa dhaxalkaas", "Waa arrimo ay dawladdu qeybiso"),
    ("Deegaanka qofka oo ay ka mid yihiin rugaha waxbarashada iyo wadaayadaada sidee bay saameyn ugu yeeshaan?", "Waxay qaabeeyaan fikirkiisa, dabeecaddiisa, iyo dhaqankiisa bulsho", "Waxba kuma kordhiyaan qofnimadiisa asalka ah", "Waxay wax ka bedelaan muuqaalkiisa jireed (hidaysiga)", "Waxay yareeyaan fahamkiisa sooyaalka"),
    ("Sida casharku caddeeyay, haddii hal af, hal diin, iyo hal soohdin inaga dhexeeyaan, waa maxay natiijada waajibka ah?", "Inay nagu qasab tahay inaan danteena guud si adag u wada ilaashano", "Inaan ku faanno oo kaliya iyadoon fal la socon", "Inaan u oggolaano dadka kale inay maamulaan", "In la kala qeybiyo si loo maamulo"),
    ("Waa maxay macnaha fog ee 'waano abuuris baa ka horeysay' marka la eego anshaxa bulshada?", "In isbedelada asaasiga ah ee dabeecadda aadanaha ay ka adag yihiin tababar ama naseexo dambe", "In waano kasta ay si iskeed ah u shaqeyso haddii la badiyo", "In aadanuhu uusan lahayn dabeecad dabiici ah", "In abuuristu aysan lahayn muhiimad"),
    ("Baanbayda uu Xasan Ganeey ku biiray 1970-kii waxay ahayd:", "Koox faneed/muusig oo ciidamada ka tirsan oo soo bandhigtay suugaantiisa iyo kartidiisa faneed", "Koox siyaasadeed oo dowladda diidanayd", "Koox isboorti oo caalami ah", "Urur iskaa-wax-u-qabso ah oo bulshada caawiya")
]

for q in easy_data:
    add_q(*q, "easy")
    
for q in medium_data:
    add_q(*q, "medium")
    
for q in hard_data:
    add_q(*q, "hard")

out_dir = r"C:\flutterApp\Aqoon_Bile\scratch"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "somali_ch8.json")

with open(out_path, "w", encoding="utf-8") as f:
    json.append_str = json.dumps(questions, ensure_ascii=False, indent=2)
    f.write(json.append_str)

print(f"Generated {len(questions)} questions successfully.")
