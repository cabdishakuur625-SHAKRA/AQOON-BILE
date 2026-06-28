import json

questions = [
    # EASY (25 questions)
    {"q": "Waa maxay Aar?", "opts": {"a": "Libaax weyn oo lab ah", "b": "Libaaxa yar ee dhedig", "c": "Shabeel weyn", "d": "Aar aan shaash yeelan"}, "ans": "a", "diff": "easy"},
    {"q": "Waa maxay Baranbarqo?", "opts": {"a": "Libaax weyn", "b": "Libaaxa yar ee dhedig", "c": "Libaax lab ah", "d": "Shabeel yar"}, "ans": "b", "diff": "easy"},
    {"q": "Waa maxay Gaani?", "opts": {"a": "Libaaxa yar", "b": "Libaax weyn oo lab ah", "c": "Aarka aan shaash yeelan weli ama gar", "d": "Haramcad"}, "ans": "c", "diff": "easy"},
    {"q": "Yaa tiriyey maansada (Adigoon cirka ubixin)?", "opts": {"a": "Xaaji Aadam", "b": "Maxamed Ibraahim Warsame (Hadraawi)", "c": "Cabdullaahi Suldaan (Timacadde)", "d": "Xasan Sheekh Muumin"}, "ans": "b", "diff": "easy"},
    {"q": "Xaggee ayuu ku yaalaa dhulka Soomaaliya?", "opts": {"a": "Koonfurta Afrika", "b": "Waqooyi-bari ee Qaarada Afrika", "c": "Galbeedka Afrika", "d": "Bartamaha Afrika"}, "ans": "b", "diff": "easy"},
    {"q": "Dhererka xeebta Soomaaliya waa imisa?", "opts": {"a": "2000 km", "b": "3333 km", "c": "4000 km", "d": "1500 km"}, "ans": "b", "diff": "easy"},
    {"q": "Soohdinta waqooyi ee badda Soomaaliya maxay ku egtahay?", "opts": {"a": "Badweynta Hindiya", "b": "Badda Cas ama Baabal mandab", "c": "Gacanka Cadmeed", "d": "Raaskambooni"}, "ans": "b", "diff": "easy"},
    {"q": "Xaggee ayay isaga darsamaan Badweynta Hindiya iyo Badda Cas?", "opts": {"a": "Raaskambooni", "b": "Raas Caseyr", "c": "Saylac", "d": "Hobyo"}, "ans": "b", "diff": "easy"},
    {"q": "Waa maxay laagta markii koonfur laga joogo qabowga ah, waqooyina diiran?", "opts": {"a": "Lafogure", "b": "Nugaal", "c": "Daroor", "d": "Karkaaro"}, "ans": "a", "diff": "easy"},
    {"q": "Berriga Soomaaliya muxuu ku wanaagsan yahay?", "opts": {"a": "Macdanta oo qura", "b": "Daaqa xoolaha iyo beerashada", "c": "Kalluumeysiga", "d": "Warshadaha"}, "ans": "b", "diff": "easy"},
    {"q": "Dhulka Soomaaliya boqolkiiba imisa ayaa ku wanaagsan beerashada?", "opts": {"a": "50%", "b": "80%", "c": "30%", "d": "100%"}, "ans": "b", "diff": "easy"},
    {"q": "Imisa webi ayaa marta dalka Soomaaliya?", "opts": {"a": "Hal webi", "b": "Labo webi", "c": "Saddex webi", "d": "Afar webi"}, "ans": "b", "diff": "easy"},
    {"q": "Magacyada webiyada mara Soomaaliya waa kuwee?", "opts": {"a": "Nugaal iyo Daroor", "b": "Jubba iyo Shabeelle", "c": "Niil iyo Yufraad", "d": "Tana iyo Galana"}, "ans": "b", "diff": "easy"},
    {"q": "Keebaa biyo badan webiga Jubba iyo Shabeelle?", "opts": {"a": "Shabeelle", "b": "Jubba", "c": "Waa isku mid", "d": "Midna"}, "ans": "b", "diff": "easy"},
    {"q": "Buuraha teelteelka ah ee Soomaaliya waxaa ka mid ah?", "opts": {"a": "Golis", "b": "Surrad", "c": "Buur Hakabo iyo Buur Heybe", "d": "Daallo"}, "ans": "c", "diff": "easy"},
    {"q": "Buurta ugu dheer Soomaaliya waa tee?", "opts": {"a": "Gacan libaax", "b": "Surrad", "c": "Daallo", "d": "Naaso hablood"}, "ans": "b", "diff": "easy"},
    {"q": "Waa maxay Xeeb?", "opts": {"a": "Dhul buuraley ah", "b": "Diilinta badda qarkeeda ah ilaa 20 km berriga", "c": "Dhul kayn ah", "d": "Dhul dooxo ah"}, "ans": "b", "diff": "easy"},
    {"q": "Magaalooyinka dhul xeebeedka ah waxaa ka mid ah?", "opts": {"a": "Baydhabo", "b": "Hargeysa", "c": "Muqdisho, Kismaayo, iyo Boosaaso", "d": "Garoowe"}, "ans": "c", "diff": "easy"},
    {"q": "Dhulka Gubanka ah xaggee ayuu dhacaa?", "opts": {"a": "Koonfurta fog", "b": "U dhaxeeya Buuraha Golis iyo dhulka xeebta", "c": "Xadka Itoobiya", "d": "Gobolka Banaadir"}, "ans": "b", "diff": "easy"},
    {"q": "Maxaa lagu gartaa dhulka dooxada ah?", "opts": {"a": "Buuro waaweyn", "b": "Togag badan ayaa mara", "c": "Biyo yari", "d": "Baraf ayaa ka da'a"}, "ans": "b", "diff": "easy"},
    {"q": "Dhulka Dooyga ah muxuu ku wanaagsan yahay?", "opts": {"a": "Beerashada meseggada iyo xoolaha", "b": "Kalluumeysiga", "c": "Dhismaha warshadaha", "d": "Dhuxusha"}, "ans": "a", "diff": "easy"},
    {"q": "Gobolkee ayuu u badan yahay dhulka Adablaha ah?", "opts": {"a": "Bari", "b": "Sanaag", "c": "Baay", "d": "Awdal"}, "ans": "c", "diff": "easy"},
    {"q": "Khayraadka badda ma dabooli karaan baahiyaha berriga?", "opts": {"a": "Maya", "b": "Haa", "c": "Waqti kooban kaliya", "d": "Qeyb ahaan"}, "ans": "b", "diff": "easy"},
    {"q": "Muxuu ahaa magaca buurta eylo?", "opts": {"a": "Buur hakabo", "b": "Buur haybe", "c": "Buur golis", "d": "Buur surrad"}, "ans": "b", "diff": "easy"},
    {"q": "Dhulkee u fiican dhaqashada Geela iyo Riyaha?", "opts": {"a": "Dooyga", "b": "Dhoobeyda", "c": "Xeebta", "d": "Deexda"}, "ans": "a", "diff": "easy"},

    # MEDIUM (27 questions)
    {"q": "Libaaxa weyn ee lab ah maxaa loo yaqaanaa?", "opts": {"a": "Gaani", "b": "Baranbarqo", "c": "Aar", "d": "Shabeel"}, "ans": "c", "diff": "medium"},
    {"q": "Libaaxa yar ee dhedig magaceed?", "opts": {"a": "Aar", "b": "Baranbarqo", "c": "Gaani", "d": "Haramcad"}, "ans": "b", "diff": "medium"},
    {"q": "Sanadkee la tiriyey maansada (Adigoon cirka ubixin)?", "opts": {"a": "1960", "b": "1972", "c": "1980", "d": "1990"}, "ans": "b", "diff": "medium"},
    {"q": "Qaaraddee ayuu dhacaa dhulka Soomaaliya?", "opts": {"a": "Aasiya", "b": "Yurub", "c": "Afrika", "d": "Koonfur Ameerika"}, "ans": "c", "diff": "medium"},
    {"q": "Masaafada lagu qiyaaso dhererka xeebaha Soomaaliya waa?", "opts": {"a": "1000 km", "b": "2000 km", "c": "3333 km", "d": "4000 km"}, "ans": "c", "diff": "medium"},
    {"q": "Dhanka koonfureed, badda Soomaaliya xaggee ayay ku egtahay?", "opts": {"a": "Raaskambooni", "b": "Raas Caseyr", "c": "Kismaayo", "d": "Hobyo"}, "ans": "a", "diff": "medium"},
    {"q": "Biyaha Badda Cas iyo Badweynta Hindiya barta ay isugu yimaadaan waxaa la yiraahdaa?", "opts": {"a": "Raaskambooni", "b": "Raas Caseyr", "c": "Saylac", "d": "Berbera"}, "ans": "b", "diff": "medium"},
    {"q": "Qiyaastii inta boqolkiiba ee dhulka Soomaaliya uu ku fiican yahay tacbashada beeraha waa?", "opts": {"a": "50%", "b": "60%", "c": "80%", "d": "90%"}, "ans": "c", "diff": "medium"},
    {"q": "Berriga Soomaaliya ma beerashada mise xoolaha ayuu aad ugu wanaagsan yahay?", "opts": {"a": "Beerashada oo kaliya", "b": "Daaqsinka xoolaha iyo ugaarta", "c": "Macdanta", "d": "Warshadaha"}, "ans": "b", "diff": "medium"},
    {"q": "Xaggee ayay ka soo burqadaan webiyada Jubba iyo Shabeelle?", "opts": {"a": "Buuraha Kiinya", "b": "Buuraha Itoobiya", "c": "Buuraha Soomaaliya", "d": "Badweynta Hindiya"}, "ans": "b", "diff": "medium"},
    {"q": "Webiga ugu baaxadda iyo biyaha badan Soomaaliya waa kee?", "opts": {"a": "Shabeelle", "b": "Jubba", "c": "Nugaal", "d": "Daroor"}, "ans": "b", "diff": "medium"},
    {"q": "Keebaa dheef badan webiga Jubba iyo Shabeelle?", "opts": {"a": "Jubba", "b": "Shabeelle", "c": "Labaduba way siman yihiin", "d": "Midna"}, "ans": "b", "diff": "medium"},
    {"q": "Tuulada Dhaay Tubaako ee uu ku dhammaado Webiga Shabeelle degmadee ayay u dhow dahay?", "opts": {"a": "Marka", "b": "Afgooye", "c": "Sablaale", "d": "Baraawe"}, "ans": "c", "diff": "medium"},
    {"q": "Noocyada buuraha ee Soomaaliya ku yaal waa imisa nooc?", "opts": {"a": "Laba nooc (teelteel iyo silsilad)", "b": "Saddex nooc", "c": "Hal nooc", "d": "Afar nooc"}, "ans": "a", "diff": "medium"},
    {"q": "Buur Eylo xaggee ayay ku taalaa?", "opts": {"a": "Shabeellaha Hoose", "b": "Gobolka Baay", "c": "Gedo", "d": "Hiiraan"}, "ans": "b", "diff": "medium"},
    {"q": "Waa maxay buuro fiiqfiiqan?", "opts": {"a": "Buuro leh doog iyo dhir badan", "b": "Buuro leh qarar iyo dhagxaan madow oo aan doog lahayn", "c": "Buuro yar yar oo ciid ah", "d": "Buuro baraf leh"}, "ans": "b", "diff": "medium"},
    {"q": "Dhererka Buurta Surrad waa imisa mitir qiyaastii?", "opts": {"a": "5,000 oo mitir", "b": "6,000 oo mitir", "c": "8,000 oo mitir", "d": "10,000 oo mitir"}, "ans": "c", "diff": "medium"},
    {"q": "Buuraha 'Naaso Hablood' waxay ka mid yihiin?", "opts": {"a": "Buuraha cagaarka leh", "b": "Buuraha fiiqfiiqan", "c": "Buuraha ciidda ah", "d": "Buuraha barafka leh"}, "ans": "a", "diff": "medium"},
    {"q": "Dhul xeebeedka tigaad waxtar leh maka baxdaa?", "opts": {"a": "Haa, aad ayey ugu baxdaa", "b": "Maya, cusbada ayaa ku badan", "c": "Haa, xilliga roobka", "d": "Maya, biyo la'aan awgeed"}, "ans": "b", "diff": "medium"},
    {"q": "Xoolaha noocee ah ayaa ku dhaqma dhulka Deexda?", "opts": {"a": "Geela", "b": "Xoolaha nugul sida idaha iyo lo'da", "c": "Fardaha", "d": "Dameeraha"}, "ans": "b", "diff": "medium"},
    {"q": "Xoolaha ku dhaqma dhulka Gubanka waxaa u badan?", "opts": {"a": "Geela", "b": "Lo'da", "c": "Riyaha", "d": "Fardaha"}, "ans": "c", "diff": "medium"},
    {"q": "Waa maxay Dhulka Oogada ah?", "opts": {"a": "Dhul hoose oo kulul", "b": "Dhul taag sare ah oo cimilo fiican leh", "c": "Dhul xeeb ah", "d": "Dhul lamadegaan ah"}, "ans": "b", "diff": "medium"},
    {"q": "Waa kuwee dooxooyinka ugu caansan Soomaaliya?", "opts": {"a": "Nugaal iyo Daroor", "b": "Jubba iyo Shabeelle", "c": "Golis iyo Surrad", "d": "Hawd iyo Dooy"}, "ans": "a", "diff": "medium"},
    {"q": "Ceyayaanka xoolaha cuna (dullinka) dhulkee ayuu ku badan yahay?", "opts": {"a": "Dhulka Hawdka ah", "b": "Dhulka Oogada", "c": "Dhulka Xeebta", "d": "Dhulka Guban"}, "ans": "a", "diff": "medium"},
    {"q": "Sifooyinka Dhulka Dooyga waxaa ka mid ah?", "opts": {"a": "Dhul baraf ah", "b": "Dhul ciid cas oo kaymo badan leh", "c": "Dhul dhagax ah", "d": "Dhul cusbo leh"}, "ans": "b", "diff": "medium"},
    {"q": "Xaggee ayuu u badan yahay dhulka dhoobeyda ah?", "opts": {"a": "Dhulka buuraleyda", "b": "Webiyada jiinkooda", "c": "Dhulka lamadegaanka", "d": "Xeebaha"}, "ans": "b", "diff": "medium"},
    {"q": "Waa maxay sifooyinka Dhulka Ciidda?", "opts": {"a": "Carro dhoobo ah", "b": "Carro aad u guduudan oo furfuran", "c": "Carro madow", "d": "Carro dhagax ah"}, "ans": "b", "diff": "medium"},

    # HARD (29 questions)
    {"q": "Aarka aan shaash yeelan weli ama gar maxaa lagu magacaabaa?", "opts": {"a": "Gaani", "b": "Baranbarqo", "c": "Aar", "d": "Shabeel"}, "ans": "a", "diff": "hard"},
    {"q": "Saddexda libaax ee kala ah Aar, Baranbarqo iyo Gaani, keebaa ah aarka aan shaash yeelan?", "opts": {"a": "Aar", "b": "Baranbarqo", "c": "Gaani", "d": "Dhammaantood"}, "ans": "c", "diff": "hard"},
    {"q": "Waa tuma maansada uu tiriyey Maxamed Ibraahim Warsame (Hadraawi) sanadkii 1972?", "opts": {"a": "Sirta Nolosha", "b": "Adigoon cirka ubixin, ama boodin leexada", "c": "Gudgude", "d": "Dabahuwan"}, "ans": "b", "diff": "hard"},
    {"q": "Dhulka Soomaaliya wuxuu dhacaa geeska Afrika, gaar ahaan xaggee?", "opts": {"a": "Waqooyi-galbeed", "b": "Waqooyi-bari ee qaaradda Afrika", "c": "Koonfur-bari", "d": "Bartamaha"}, "ans": "b", "diff": "hard"},
    {"q": "Xeebta Soomaaliya oo ah tan ugu dheer qaaradda Afrika, dhererkeedu waa imisa kiiloomitir?", "opts": {"a": "2500 km", "b": "3000 km", "c": "3333 km", "d": "3500 km"}, "ans": "c", "diff": "hard"},
    {"q": "Labada daraf ee ay ku egtahay badda Soomaaliya (Waqooyi iyo Koonfur) waa kuwee?", "opts": {"a": "Zayla iyo Kismaayo", "b": "Baabal mandab iyo Raaskambooni", "c": "Boosaaso iyo Hobyo", "d": "Berbera iyo Marka"}, "ans": "b", "diff": "hard"},
    {"q": "Laagta Lafogure sifooyinkeeda waxaa ka mid ah?", "opts": {"a": "Mar walba waa kulul tahay", "b": "Koonfur qabow ah, waqooyi kulul", "c": "Mar walba waa qabow", "d": "Biyo badan ayay leedahay"}, "ans": "b", "diff": "hard"},
    {"q": "Cimilada berriga Soomaaliya sidee u badan tahay?", "opts": {"a": "Aad u kulul", "b": "Aad u qabow", "c": "Waa dhexdhexaad", "d": "Isbedbedesha maalin kasta"}, "ans": "c", "diff": "hard"},
    {"q": "Maxaa aad ugu habboon berriga Soomaaliya in laga faa'iideysto?", "opts": {"a": "Daaqsinka xoolaha iyo ugaarta", "b": "Warshadaynta", "c": "Dalxiiska barafka", "d": "Qodista dhuxusha"}, "ans": "a", "diff": "hard"},
    {"q": "Webiga Jubba xaggee ayuu kaga darsamaa Badweynta Hindiya?", "opts": {"a": "Mogadishu", "b": "Tuulada Goobweyn", "c": "Baraawe", "d": "Kismaayo"}, "ans": "b", "diff": "hard"},
    {"q": "Maxaa sababay in webiga Jubba dheeftiisu yaraato?", "opts": {"a": "Wuxuu maraa dhul dhagax ah", "b": "Wuxuu maraa dhul cusbooley ah", "c": "Wuxuu maraa kayn cufan", "d": "Wuxuu maraa lamadegaan"}, "ans": "b", "diff": "hard"},
    {"q": "Waa maxay sababta uu u dheef batay webiga Shabeelle?", "opts": {"a": "Wuxuu maraa dhul dhoobeey ah", "b": "Wuxuu maraa dhul buuraley ah", "c": "Biyihiisa oo yar", "d": "Kalluunka ku badan"}, "ans": "a", "diff": "hard"},
    {"q": "Xaggee ayuu ku dhammaadaa webiga Shabeelle?", "opts": {"a": "Badweynta Hindiya", "b": "Tuulada Dhaay Tubaako", "c": "Webiga Jubba", "d": "Dhulka Hawdka"}, "ans": "b", "diff": "hard"},
    {"q": "Qaabkee ayuu u dhammaadaa webiga Shabeelle?", "opts": {"a": "Qaab toosan", "b": "Qaab faafsan ah", "c": "Qaab goobaaban", "d": "Biya-dhac weyn"}, "ans": "b", "diff": "hard"},
    {"q": "Buuraha silsiladda ah ee Soomaaliya waxaa tusaale u ah?", "opts": {"a": "Buuraha Golis", "b": "Buur Hakabo", "c": "Buur Heybe", "d": "Buur Eylo"}, "ans": "a", "diff": "hard"},
    {"q": "Xaggee ayay ku yaaliin Buuraha Golis?", "opts": {"a": "Koonfurta Soomaaliya", "b": "Waqooyi-bari iyo waqooyi-galbeed ee Soomaaliya", "c": "Bartamaha Soomaaliya", "d": "Gobolka Banaadir"}, "ans": "b", "diff": "hard"},
    {"q": "Waa kuwee buuraha cagaarka leh ee ku yaal gobolka Sanaag?", "opts": {"a": "Golis iyo Hakabo", "b": "Surrad, Daallo iyo Shimbiris", "c": "Heybe iyo Eylo", "d": "Karkaaro oo keliya"}, "ans": "b", "diff": "hard"},
    {"q": "Waa imisa nooc oo dhul ah oo ay Soomaalidu degto marka loo eego qaab-dhismeedka?", "opts": {"a": "Labo nooc oo kaliya", "b": "Shan nooc", "c": "In ka badan 10 nooc sida Xeeb, Deex, Guban iwm", "d": "Saddex nooc"}, "ans": "c", "diff": "hard"},
    {"q": "Waa maxay sifooyinka Dhulka Deexda?", "opts": {"a": "Dhul qabow oo buuraley ah", "b": "Dhul kulul oo cusbada dhexdhexaad tahay, roobkuna badan yahay", "c": "Dhul lamadegaan ah", "d": "Dhul dhoobo ah"}, "ans": "b", "diff": "hard"},
    {"q": "Maxaa ka mid ah dhirta geed-gaabka ah ee ka baxda Deexda?", "opts": {"a": "Qaboox iyo garas", "b": "Daranta, jillabka iyo caday deexeedka", "c": "Geed-qori iyo baxar-saaf", "d": "Qurac iyo qansax"}, "ans": "b", "diff": "hard"},
    {"q": "Heerkulka dhulka Gubanka ah muxuu yahay?", "opts": {"a": "Aad ayuu u qabow yahay", "b": "Aad ayuu u sarreeyaa oo waa dhul kulul", "c": "Waa dhexdhexaad", "d": "Baraf ayaa ka da'a"}, "ans": "b", "diff": "hard"},
    {"q": "Dhulka Oogada ah xoolaha kee baa lagu dhaqdaa?", "opts": {"a": "Lo'da oo keliya", "b": "Geela, idaha iyo riyaha", "c": "Digaagga", "d": "Fardaha"}, "ans": "b", "diff": "hard"},
    {"q": "Maxaa lagu gartaa dhulka Hawdka ah?", "opts": {"a": "Ciid cad iyo buuro", "b": "Ciid cas iyo boor guduudan oo roobkiisu badan yahay", "c": "Dhoobo madow", "d": "Dhagxaan iyo caro madow"}, "ans": "b", "diff": "hard"},
    {"q": "Miraha la cuno ee ka baxa dhulka Hawdka waxaa ka mid ah?", "opts": {"a": "Mooska iyo cambaha", "b": "Hohobta, mareerka iyo xagarka", "c": "Liinta iyo babaayga", "d": "Sareenka iyo galleeyda"}, "ans": "b", "diff": "hard"},
    {"q": "Waa maxay noocyada dullinka xoolaha cuna?", "opts": {"a": "Kudkudaha, shillinta, dhuuga, iyo gendiga", "b": "Digaagga iyo shimbiraha", "c": "Aboorka iyo qudhaanjada", "d": "Abeesada iyo jilbiska"}, "ans": "a", "diff": "hard"},
    {"q": "Waa maxay sababta dhulka dhoobeyda ahi uusan ugu habboonayn taranka iyo caafimaadka xoolaha?", "opts": {"a": "Cunto la'aan awgeed", "b": "Dullinka, qaniinyada iyo cudurrada ayaa ku badan", "c": "Biyo la'aan awgeed", "d": "Cimilo qabow awgeed"}, "ans": "b", "diff": "hard"},
    {"q": "Gobolladee ayuu u badan yahay dhulka Cadduunka ah?", "opts": {"a": "Banaadir iyo Shabeellaha Hoose", "b": "Mudug, Galgaduud iyo Hiiraan", "c": "Bari iyo Nugaal", "d": "Awdal iyo Waqooyi Galbeed"}, "ans": "b", "diff": "hard"},
    {"q": "Waa maxay macdanta aadka uga buuxda dhulka Cadduunka ah?", "opts": {"a": "Dahabka", "b": "Macdanta Yuuraaniyamka", "c": "Qalinka", "d": "Naxaasta"}, "ans": "b", "diff": "hard"},
    {"q": "Dhulka Ciidda magaalooyinka ku yaal waxaa ka mid ah?", "opts": {"a": "Hargeysa iyo Boorama", "b": "Caabudwaaq, Galdogob iyo Buuhoodle", "c": "Marka iyo Baraawe", "d": "Kismaayo iyo Jilib"}, "ans": "b", "diff": "hard"}
]

formatted_questions = []
for i, q in enumerate(questions):
    formatted_questions.append({
        "id": f"Som_Ch6_Q{i+1:02d}",
        "question": q["q"],
        "options": q["opts"],
        "correctAnswer": q["ans"],
        "difficultyLevel": q["diff"],
        "subjectId": "somali",
        "chapterId": "somali_ch6"
    })

with open(r'C:\flutterApp\Aqoon_Bile\scratch\somali_ch6.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(formatted_questions)} questions.")
counts = {"easy":0, "medium":0, "hard":0}
for q in questions:
    counts[q["diff"]] += 1
print(f"Counts: {counts}")
