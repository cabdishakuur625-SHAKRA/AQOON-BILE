import json

questions_data = [
    {"q": "Maxaa kamid ah tiirarka maansada soomaaliyeed?", "a": "Qaafiyada", "b": "Tuduca", "c": "Alanka", "d": "Xarafka"},
    {"q": "Maansadu maxay ka koobantahay?", "a": "Meerisyo isku qaafiyad ah", "b": "Tuducyo kala qaafiyad ah", "c": "Ereyo aan xiriir lahayn", "d": "Lugood aan miisaan lahayn"},
    {"q": "Codka habdhaca leh maxaa sameeya?", "a": "Xarafka qaafiyada", "b": "Tuduca", "c": "Hakadka", "d": "Shaqalka dheer"},
    {"q": "Waa maxay qaafiyad?", "a": "Adeegsiga iyo soo celcelinta xaraf isku mid ah", "b": "Xubnaha dhawaaqa yaryar ee meeriska", "c": "Dhowr meeris ama sadar", "d": "Erey lagu suubistay maansada"},
    {"q": "Hal xaraf qaafiyadeed iyo hal lug maxay ku kala duwanyihiin?", "a": "Waa isku mid", "b": "Xarafka ayaa ka weyn", "c": "Lugta ayaa ka weyn", "d": "Waa labo shay oo kala duwan dhamaantood"},
    {"q": "Maxaa loola jeedaa meerisjab ama deelqaaf?", "a": "Erey lagu suubistay xarafka qaafiyada ee gabaygu kusocdo", "b": "Habdhaca sargoan ee meeriska", "c": "Shaqal gaab oo meeriska ku jira", "d": "Lugta hore ee gabayga"},
    {"q": "Waa maxay tuduc?", "a": "Dhowr meeris ama sadar", "b": "Hal erey oo maansada kamid ah", "c": "Xarafka ugu dambeeya meeriska", "d": "Codka habdhaca leh ee maansada"},
    {"q": "Maxaa loola jeedaa miisaanka maansada?", "a": "Habdhaca sargoan ee meeriska", "b": "Adeegsiga xaraf isku mid ah", "c": "Kala qaybinta lugaha maansada", "d": "Tirada ereyada ku jira maansada"},
    {"q": "Hab alan shaqal waa maxay?", "a": "Miisaanka maansada", "b": "Meerisjab", "c": "Qaafiyad", "d": "Tuduc"},
    {"q": "Miisaanka maansada muxuu qeexayaa?", "a": "Wuxuu qeexayaa xeerarka ay ku fadhido maansada", "b": "Wuxuu qeexayaa magaca abwaanka", "c": "Wuxuu qeexayaa xilliga la tiriyey", "d": "Wuxuu qeexayaa dhererka maansada oo dhan"},
    {"q": "Maxaa kamid ah godadka maansada?", "a": "Gabayga, guurowga, geeraarka, jiiftada, buranburka, saarka", "b": "Guban, oogo, dooxo", "c": "Saddexda libaax ee kala ah aar, baranbarqo iyo gaani", "d": "Dhambalan iyo hooris"},
    {"q": "Maansada maxaa lagu miisaamaa?", "a": "Inta alan ay ka koobantahay", "b": "Inta erey ay ka koobantahay", "c": "Inta tuduc ay leedahay", "d": "Inta xaraf ay ka koobantahay"},
    {"q": "Waa maxay alan?", "a": "Xubnaha dhawaaqa yaryar ee meerisku ka koobanyahay", "b": "Dhowr meeris ama sadar oo is raacsan", "c": "Lugta dambe ee gabayga", "d": "Ereyada shisheeye ee maansada ku jira"},
    {"q": "Alanka imisa shibane ayaa raaci kara?", "a": "Hal ama labo shibane", "b": "Afar shibane", "c": "Saddex shibane", "d": "Xitaa hal shibane ma raaci karo"},
    {"q": "Waa maxay alan gaab?", "a": "Waa shaqal gaab", "b": "Waa shaqal dheer", "c": "Waa labo shibane", "d": "Waa xarafka qaafiyada"},
    {"q": "Waa maxay alan dheer?", "a": "Waa shaqal dheer", "b": "Waa shaqal gaab", "c": "Waa erey ka kooban dhowr shibane", "d": "Waa meeris dhameystiran"},
    {"q": "Maxaa loo dhaxeysiiyaa labada lugood ee meeriska?", "a": "Hakad", "b": "Shaqal dheer", "c": "Erey cusub", "d": "Xaraf qaafiyadeed kale"},
    {"q": "Lugta hore maxaa loo yaqaanaa?", "a": "Hojis / horaad", "b": "Hooris / dambeed", "c": "Dhambalan", "d": "Deelqaaf"},
    {"q": "Lugta dambe maxaa loo yaqaanaa?", "a": "Hooris / dambeed", "b": "Hojis / horaad", "c": "Dhambalan", "d": "Meerisjab"},
    {"q": "Waa maxay dhambalan?", "a": "Lugta hore ee hojiska oo ku dhamaada shaqal dheer oo kala jabaya", "b": "Waa dhowr meeris oo hal tuduc noqday", "c": "Waa qaafiyad isbedeshay", "d": "Waa meerisjab ama deelqaaf"},
    {"q": "Meeriska salsalka kabdaha iyo gabayada qaar waa imisa lugood?", "a": "3 luggood", "b": "Labo lugood", "c": "Hal lug keliya", "d": "Afar lugood"},
    {"q": "Meerisyada gabayga, buraanburka iyo guurowga waa imisa lugood?", "a": "Labo lugood", "b": "Hal lug keliya", "c": "3 luggood", "d": "Lug ma laha"},
    {"q": "Meerisyada geeraarka, saarka, iyo jiiftada waa imisa lug?", "a": "Hal lug keliya", "b": "Labo lugood", "c": "3 luggood", "d": "Lugoodkoodu waa isbedbedelaa"},
    {"q": "Labada xaraf marna shaqalka noqda marna shibanaha waa kuwee?", "a": "w iyo y", "b": "m iyo n", "c": "b iyo t", "d": "k iyo q"},
    {"q": "Xarfaha (w/y) goorma ayey hab dhaqanka shaqalka qaataan?", "a": "Kolka ay ugu dambeeyaan alan shaqal gaab ah", "b": "Marka ay ugu horreeyaan meeriska", "c": "Marka ay isxigaan", "d": "Marka ay ku dhex jiraan shaqal dheer"},
    {"q": "Gabayga waa imisa alan ugu badnaan?", "a": "21 alan", "b": "19 alan", "c": "20 alan", "d": "18 alan"},
    {"q": "Gabayga waa imisa alan ugu yaraan?", "a": "19 alan", "b": "18 alan", "c": "20 alan", "d": "21 alan"},
    {"q": "Gabayga waa imisa alan inta badan (caadiyan)?", "a": "20 alan", "b": "19 alan", "c": "18 alan", "d": "21 alan"},
    {"q": "Lugta hore ee gabayga had iyo goor imisa alan ayey ka koobantahay?", "a": "12 alan", "b": "10 alan", "c": "8 alan", "d": "14 alan"},
    {"q": "Lugta dambe ee gabayga imisa alan ayey ka koobantahay?", "a": "8 alan", "b": "6 alan", "c": "10 alan", "d": "12 alan"},
    {"q": "Gabayga buraanburka waa imisa alan?", "a": "18 alan", "b": "20 alan", "c": "25 alan", "d": "9 alan"},
    {"q": "Gabayga geeraarka waa imisa alan?", "a": "9 alan", "b": "8 alan", "c": "10 alan", "d": "12 alan"},
    {"q": "Gabayga jiiftada waa imisa alan?", "a": "9 alan", "b": "8 alan", "c": "10 alan", "d": "18 alan"},
    {"q": "Gabayga saarka waa imisa alan?", "a": "10 alan", "b": "9 alan", "c": "8 alan", "d": "12 alan"},
    {"q": "Gabayga salsalka kabdaha waa imisa alan?", "a": "27-25 alan", "b": "20-22 alan", "c": "18-20 alan", "d": "30-35 alan"},
    {"q": "Meerisyada guurowga waa imisa lugood?", "a": "Labo lugood", "b": "Hal lug", "c": "Saddex lugood", "d": "Afar lugood"},
    {"q": "Meerisyada heesaha waa imisa lug?", "a": "Hal lug keliya", "b": "Labo lugood", "c": "Saddex lugood", "d": "Wax lug ah ma laha"},
    {"q": "Gabayada qaar waa imisa lugood meeriskoodu?", "a": "3 luggood", "b": "2 lugood", "c": "1 lug", "d": "4 lugood"},
    {"q": "Salsalka kabdaha labada lugood ee hore maxaa loo yaqaanaa?", "a": "Hojis", "b": "Hooris", "c": "Dhambalan", "d": "Tuduc"},
    {"q": "Salsalka kabdaha lugta dambe maxaa loo yaqaanaa?", "a": "Hooris", "b": "Hojis", "c": "Alan gaab", "d": "Deelqaaf"},
    {"q": "Maxaa qayb kamid ah raacaya hojiska qaybna hooriska marka dhambalan dhaco?", "a": "Dhawaaqii shaqalka dheeraa ee kala jabay", "b": "Xarafka qaafiyada", "c": "Ereyga ugu dambeeya meeriska", "d": "Hakadka u dhexeeya lugaha"},
    {"q": "Xubnaha dhawaaqa yaryar ee meeriska maxaa la yiraahdaa?", "a": "Alan", "b": "Lug", "c": "Tuduc", "d": "Qaafiyad"},
    {"q": "Adeegsiga iyo soo celcelinta xaraf isku mid ah maansada maxaa la yiraahdaa?", "a": "Qaafiyad", "b": "Lug", "c": "Meeris", "d": "Alan"},
    {"q": "Dhowr meeris ama sadar oo isku xiga maxaa loo yaqaanaa?", "a": "Tuduc", "b": "Alan", "c": "Lug", "d": "Dhambalan"},
    {"q": "Ereyga lagu suubistay xarafka qaafiyada ee gabaygu ku socdo waa maxay?", "a": "Meerisjab ama deelqaaf", "b": "Hooris", "c": "Hojis", "d": "Alan dheer"},
    {"q": "Xeerarka ay ku fadhido maansada maxaa qeexa?", "a": "Miisaanka maansada", "b": "Godadka maansada", "c": "Xarafka qaafiyada", "d": "Tirada tuducyada"},
    {"q": "Maansada maxaa lagu qiyaasaa inta ay le'eg tahay dhanka miisaanka?", "a": "Inta alan ee ay ka koobantahay", "b": "Inta erey ee ku jirta", "c": "Inta abwaan ee tiriyey", "d": "Inta xaraf ee shaqalka ah"},
    {"q": "Maxaa isku mid ah dhanka maansada?", "a": "Hal xaraf qaafiyadeed iyo hal lug", "b": "Gabayga iyo geeraarka", "c": "Alan dheer iyo alan gaab", "d": "Hojis iyo hooris"},
    {"q": "Codka habdhaca leh ee maansada maxaa sameeya?", "a": "Xarafka qaafiyada", "b": "Abwaanka", "c": "Codka qofka tirinaya", "d": "Dhererka meeriska"},
    {"q": "Tiirka ugu muhiimsan maansada Soomaaliyeed maxaa kamid ah?", "a": "Qaafiyada", "b": "Laxanka", "c": "Da'da abwaanka", "d": "Xilliga la tiriyey"},
    {"q": "Hojis iyo Hooris maxay kala yihiin?", "a": "Lugta hore iyo lugta dambe", "b": "Alan dheer iyo alan gaab", "c": "Gabay iyo jiifto", "d": "Qaafiyad iyo meeris"},
    {"q": "Maxaa loo dhaxeysiiyaa hakad?", "a": "Labada lugood ee meeriska", "b": "Labada tuduc ee gabayga", "c": "Labada abwaan ee doodaya", "d": "Shaqalka iyo shibanaha"},
    {"q": "Haddii gabaygu leeyahay 20 alan, imisa ayaa lugta hore ah inta badan?", "a": "12 alan", "b": "10 alan", "c": "8 alan", "d": "14 alan"},
    {"q": "Haddii gabaygu leeyahay 20 alan, imisa ayaa lugta dambe ah?", "a": "8 alan", "b": "10 alan", "c": "12 alan", "d": "14 alan"},
    {"q": "Maxay ku kala duwan yihiin Geeraarka iyo Jiiftada dhanka alanka?", "a": "Labaduba waa isku mid oo waa 9 alan", "b": "Geeraarku waa 10, jiiftaduna waa 9", "c": "Jiiftada ayaa ka alan badan", "d": "Labaduba waa min labo lugood"},
    {"q": "Alanka maansada muxuu ka samaysmaa?", "a": "Shaqal oo uu ku laranyahay hal ama labo shibane", "b": "Saddex shibane oo isku xiga", "c": "Keliya shaqalo isku xiga", "d": "Xarfo aan la dhawaaqin"},
    {"q": "Intee in le'eg ayuu qaafiyada meerisku isbedeli karaa gabayga dhexdiisa?", "a": "Maba isbedeli karo, gabaygu waa hal qaafiyad", "b": "Tuduc kasta wuu isbedeli karaa", "c": "Lug kasta wuu isbedeli karaa", "d": "Abwaanka ayaa go'aan ka gaaraya mar walba"},
    {"q": "Waa maxay sababta (w) iyo (y) ay shaqal u noqdaan mararka qaar?", "a": "Kolka ay ugu dambeeyaan alan shaqal gaab ah", "b": "Marka ay xarafka qaafiyada yihiin", "c": "Marka ay meeriska ugu horreeyaan", "d": "Sabab la'aan ayey isku bedelaan"},
    {"q": "Waa maxay faraqa u dhexeeya Buraanburka iyo Gabayga dhanka alanka?", "a": "Gabaygu waa 20 alan, Buraanburkuna waa 18 alan", "b": "Gabaygu waa 18 alan, Buraanburkuna waa 20 alan", "c": "Labaduba waa 20 alan", "d": "Buraanburku waa 27 alan"},
    {"q": "Waa maxay maansada ugu alanka badan ee la xusay?", "a": "Salsalka kabdaha oo ah 27-25 alan", "b": "Gabayga", "c": "Buraanburka", "d": "Guurowga"},
    {"q": "Waa maxay maansada alankeedu ugu yaryahay ee godadka la xusay?", "a": "Geeraarka iyo Jiiftada oo ah 9 alan", "b": "Gabayga iyo Guurowga", "c": "Saarka oo ah 10 alan", "d": "Buraanburka"},
    {"q": "Sidee buu u dhacaa \"dhambalan\"?", "a": "Marka lugta hore ku dhamaato shaqal dheer oo kala jabaya labada lugood dhexdooda", "b": "Marka ereygu uusan ku jirin afsoomaaliga", "c": "Marka xarafka qaafiyada la waayo", "d": "Marka abwaanku illaawo meeriska"},
    {"q": "Muxuu yahay shaqalka gaaban marka loo eego alanka?", "a": "Waa alan gaab", "b": "Waa alan dheer", "c": "Waa lug dambeed", "d": "Waa meerisjab"},
    {"q": "Muxuu yahay shaqalka dheer marka loo eego alanka?", "a": "Waa alan dheer", "b": "Waa alan gaab", "c": "Waa lug horaad", "d": "Waa hakad"},
    {"q": "Waa imisa tirada shaqallada ee alanku qaadan karo?", "a": "Hal shaqal gaab ama hal shaqal dheer", "b": "Saddex shaqal", "c": "Afar shaqal", "d": "Tiro aan xad lahayn"},
    {"q": "Salsalka kabdaha imisa hojis ayuu leeyahay?", "a": "Labo hojis", "b": "Hal hojis", "c": "Saddex hojis", "d": "Hojis ma leeyahay"},
    {"q": "Salsalka kabdaha imisa hooris ayuu leeyahay?", "a": "Hal hooris", "b": "Labo hooris", "c": "Saddex hooris", "d": "Hooris ma leeyahay"},
    {"q": "Muxuu sargooyaa habdhaca miisaanka maansada?", "a": "Meeriska", "b": "Magaca maansada", "c": "Xilliga guga", "d": "Dareenka abwaanka"},
    {"q": "Maansada \"Saarka\" imisa lugood ayey ka kooban tahay meeriskiisu?", "a": "Hal lug keliya", "b": "Labo lugood", "c": "Saddex lugood", "d": "Afar lugood"},
    {"q": "Maansada \"Guurowga\" imisa lugood ayey ka kooban tahay meeriskiisu?", "a": "Labo lugood", "b": "Hal lug keliya", "c": "Saddex lugood", "d": "Afar lugood"},
    {"q": "Haddii meeriska gabaygu ka kooban yahay labo lugood, maxaa kala qaybiya?", "a": "Hakad", "b": "Xaraf weyn", "c": "Tuduc", "d": "Qaafiyad cusub"},
    {"q": "Meerisjabku goormuu dhacaa?", "a": "Marka erey lagu suubiyo xarafka qaafiyada oo uusan la jaanqaadayn gabayga haray", "b": "Marka luguhu bataan", "c": "Marka gabaygu dhammaado", "d": "Marka abwaanku daalo"},
    {"q": "Maansadu waa maxay ugu dambayn?", "a": "Meerisyo isku qaafiyad ah oo miisaaman", "b": "Ereyo iska daba qoran", "c": "Sheeko faneed dheer", "d": "Maahmaahyo la isku geeyey"},
    {"q": "Godadka maansada miyey ka mid tahay heestu?", "a": "Haa, lugta heesaha ayaa casharka lagu xusay oo ah hal lug", "b": "Maya, heestu maansada kuma jirto", "c": "Haa, laakiin waa 4 lugood", "d": "Maya, heestu waa buraanbur"},
    {"q": "Waa maxay tirada ugu badan ee alan ee gabay yeelan karo sida casharka ku xusan?", "a": "21 alan", "b": "20 alan", "c": "19 alan", "d": "22 alan"},
    {"q": "Xarfaha W iyo Y maxay yihiin asal ahaan?", "a": "Shibane, balse marna shaqal ayey noqdaan", "b": "Shaqal, balse marna shibane ayey noqdaan", "c": "Had iyo jeer waa shaqal", "d": "Had iyo jeer waa shibane"},
    {"q": "Waa maxay lugta dambeed ee meeriska?", "a": "Hooris", "b": "Hojis", "c": "Dhambalan", "d": "Alan gaab"},
    {"q": "Waa maxay lugta horaad ee meeriska?", "a": "Hojis", "b": "Hooris", "c": "Deelqaaf", "d": "Alan dheer"},
    {"q": "Maansada Salsalka Kabdaha tirada alankeedu waay isbedbedeshaa, intee u dhaxaysaa?", "a": "25 ilaa 27 alan", "b": "18 ilaa 20 alan", "c": "10 ilaa 15 alan", "d": "30 ilaa 35 alan"},
    {"q": "Gabayga, Guurowga iyo Buraanburka maxay wadaagaan dhanka lugaha?", "a": "Dhammaantood waa min labo lugood", "b": "Dhammaantood waa min hal lug", "c": "Dhammaantood waa min saddex lugood", "d": "Lugohoodu waa kala duwan yihiin"},
    {"q": "Geeraarka, Jiiftada iyo Saarka maxay wadaagaan dhanka lugaha?", "a": "Dhammaantood waa min hal lug keliya", "b": "Dhammaantood waa min labo lugood", "c": "Dhammaantood waa isku qaafiyad", "d": "Dhammaantood waa min 20 alan"}
]

out = []
for i, d in enumerate(questions_data):
    if i < 25:
        diff = "easy"
    elif i < 52:
        diff = "medium"
    else:
        diff = "hard"
    
    out.append({
        "id": f"Som_Ch3_Q{i+1:02d}",
        "question": d["q"],
        "options": {
            "a": d["a"],
            "b": d["b"],
            "c": d["c"],
            "d": d["d"]
        },
        "correctAnswer": "a",
        "difficultyLevel": diff,
        "subjectId": "somali",
        "chapterId": "somali_ch3"
    })

with open(r"C:\flutterApp\Aqoon_Bile\scratch\somali_ch3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Generated 81 questions.")
