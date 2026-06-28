const String fullSeedJson = r'''
{
  "subjects": [
    {
      "id": "bio",
      "name": "Biology"
    },
    {
      "id": "chem",
      "name": "Chemistry"
    },
    {
      "id": "phy",
      "name": "Physics"
    },
    {
      "id": "som",
      "name": "Somali"
    },
    {
      "id": "his",
      "name": "History"
    },
    {
      "id": "geo",
      "name": "Geography"
    },
    {
      "id": "islam",
      "name": "Islamic Studies"
    }
  ],
  "chapters": [
    {
      "id": "Chapter 1",
      "subjectId": "his",
      "title": "Cutubka 1: Dawladda Cusmaaniyiinta"
    },
    {
      "id": "Chapter 2",
      "subjectId": "his",
      "title": "Cutubka 2: Qadiyadda Falastiin, Kashmiir & Barma"
    },
    {
      "id": "Chapter 3",
      "subjectId": "his",
      "title": "Cutubka 3aad: Dawladnimo Gaarsiinta Soomaaliya"
    },
    {
      "id": "Chapter 4",
      "subjectId": "his",
      "title": "Cutubka 4aad: Dhaqdhaqaaqyada Xoraynta (Mahdiga, Cumar Mukhtaar, Azhar, Koonfur Afrika)"
    },
    {
      "id": "Chapter 5",
      "subjectId": "his",
      "title": "Cutubka 5aad: Kacaankii Ruushka, Dagaalkii 2aad ee Dunida & Dagaalkii Qaboobaa"
    },
    {
      "id": "Chapter 6",
      "subjectId": "his",
      "title": "Cutubka 6aad: Uruurada Caalamiga ah (QM, Jaamacadda Carabta, AU, OIC)"
    },
    {
      "id": "Chapter 7",
      "subjectId": "his",
      "title": "Cutubka 7aad: Dastuurka, Sharciga, Dimuqraadiyadda iyo Xisbiyada"
    },
    {
      "id": "geo_ch1",
      "subjectId": "geo",
      "title": "Cutubka 1: Cilmiga Jiyooloojiga (macalin xasan)"
    },
    {
      "id": "geo_ch2",
      "subjectId": "geo",
      "title": "Cutubka 2: Nololey (macalin xasan)"
    },
    {
      "id": "geo_ch3",
      "subjectId": "geo",
      "title": "Cutubka 3: Dadka iyo Deegaanka (macalin xasan)"
    },
    {
      "id": "geo_ch4",
      "subjectId": "geo",
      "title": "Cutubka 4: Juqraafiga Soomaaliya (macalin xasan)"
    },
    {
      "id": "geo_ch5",
      "subjectId": "geo",
      "title": "Cutubka 5: Juqraafiga Dadka (macalin xasan)"
    },
    {
      "id": "geo_ch6",
      "subjectId": "geo",
      "title": "Cutubka 6: Deegaannada Magaalooyinka (macalin xasan)"
    },
    {
      "id": "geo_ch7",
      "subjectId": "geo",
      "title": "Cutubka 7: Ilaha Dhaqaale (macalin xasan)"
    },
    {
      "id": "geo_ch8",
      "subjectId": "geo",
      "title": "Cutubka 8: Juqraafiga Siyaasadda (macalin xasan)"
    },
    {
      "id": "islam_ch1",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch2",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch3",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch4",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch5",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch6",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch7",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch8",
      "subjectId": "islam",
      "title": "عزديا ِٜٛكت"
    },
    {
      "id": "islam_ch9",
      "subjectId": "islam",
      "title": "لاٚأ"
    },
    {
      "id": "islam_ch10",
      "subjectId": "islam",
      "title": "١ٝتلآا ١ً٦ضلأا ٔع بٝمد :لاٚأ"
    },
    {
      "id": "bio_ch1",
      "subjectId": "bio",
      "title": "General Biology"
    },
    {
      "id": "chem_ch1",
      "subjectId": "chem",
      "title": "General Chemistry"
    },
    {
      "id": "phy_ch1",
      "subjectId": "phy",
      "title": "General Physics"
    },
    {
      "id": "som_ch1",
      "subjectId": "som",
      "title": "General Somali"
    }
  ],
  "questions": [
    {
      "id": "Chap1_Q1_01",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Isirka dadka Cusmaaniyiinta waa?",
      "options": {
        "a": "Qabiil Turki ah",
        "b": "Carab",
        "c": "Faarisi",
        "d": "Mongol"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_02",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Dawladda Cusmaaniyiintu waxay soo if baxday xilligii?",
      "options": {
        "a": "Qarnigii 10aad",
        "b": "Qarnigii 13aad dabayaaqadiisa",
        "c": "Qarnigii 15aad",
        "d": "Qarnigii 18aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_03",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Aasaasihii magaca Cusmaaniyiinta laga keenay waa?",
      "options": {
        "a": "Cusmaan binu Ardhagural",
        "b": "Orkhaan",
        "c": "Muraad",
        "d": "Suleymaan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_04",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu ka dhalatay burburkii dawladdii?",
      "options": {
        "a": "Rome",
        "b": "Seljuuq",
        "c": "Persia",
        "d": "Mamluk"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_05",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay gaartay saddex qaaradood oo kala ah?",
      "options": {
        "a": "Afrika, Aasiya, Yurub",
        "b": "Afrika iyo Aasiya",
        "c": "Yurub iyo Ameerika",
        "d": "Aasiya iyo Australia"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_06",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Dardaaranka Cusmaan wuxuu ku saabsanaa?",
      "options": {
        "a": "Ganacsi",
        "b": "Jihaad iyo diinta Islaamka",
        "c": "Cilmiga kaliya",
        "d": "Beeraha"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_07",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Dawladdii Cusmaaniyiintu waxay u qaybsantay?",
      "options": {
        "a": "32 gobol",
        "b": "10 gobol",
        "c": "5 gobol",
        "d": "50 gobol"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_08",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Suldaanka Cusmaaniyiinta wuxuu ahaa?",
      "options": {
        "a": "Awoodda ugu sarreysa",
        "b": "Madaxweynaha kaliya",
        "c": "Ganacsade",
        "d": "Qareen"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_09",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Ciidanka Cusmaaniyiintu waxay ku saleysnaayeen?",
      "options": {
        "a": "Fardooley iyo ciidanka dhulka",
        "b": "Badda kaliya",
        "c": "Diyaarado",
        "d": "Taangiyo"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_10",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Nidaamka maaliyadeed wuxuu ka koobnaa?",
      "options": {
        "a": "Canshuur iyo kharash",
        "b": "Kaliya ganacsi",
        "c": "Kaliya dagaal",
        "d": "Kaliya beeraha"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_11",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Hay’adda Islaamiga ah waxay ku saleysneyd?",
      "options": {
        "a": "Shareecada Islaamka",
        "b": "Sharciga Yurub",
        "c": "Dastuur cusub",
        "d": "Xeer qabiil"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_12",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Suldaankii ugu caansanaa Cusmaaniyiinta waa?",
      "options": {
        "a": "Cusmaan 1",
        "b": "Orkhaan",
        "c": "Muraad",
        "d": "Selim"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap1_Q1_13",
      "subjectId": "his",
      "chapterId": "Chapter 1",
      "question": "Conistantinople maanta waxaa loo yaqaan?",
      "options": {
        "a": "Istanbul",
        "b": "Ankara",
        "c": "Izmir",
        "d": "Bursa"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Sheeg deegaanka falastiin iyo qaabka dhulkeeda?",
      "options": {
        "a": "Dhul xeebeed, buuraley iyo boholo",
        "b": "Kaliya buuro",
        "c": "Kaliya saxare",
        "d": "Jasiirado"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Qadiyadda Falastiin maxay ugu weyn tahay Muslimiinta?",
      "options": {
        "a": "Waa dal ganacsi",
        "b": "Waa qibladii hore iyo dhul barakeysan",
        "c": "Waa dal yar",
        "d": "Waa jasiirad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kuwa soo koobay taariikhda Falastiin waxay sheegeen xilligii ugu fiicnaa inuu ahaa?",
      "options": {
        "a": "Daa’uud iyo Suleymaan",
        "b": "Rooma",
        "c": "Ingiriis",
        "d": "Cusmaaniyiin"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Dadkii ugu horeeyay ee Falastiin degay waa?",
      "options": {
        "a": "Kancaaniyiinta",
        "b": "Rooma",
        "c": "Turki",
        "d": "Faaris"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Maxaa keenay qadiyadda Falastiin inay soo if baxdo casriga?",
      "options": {
        "a": "Dagaal ganacsi",
        "b": "Taageero Yurub iyo Balfour",
        "c": "Cimilada",
        "d": "Beeraha"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Xalka Falastiin waa?",
      "options": {
        "a": "Dagaal kaliya",
        "b": "Midnimo Muslimiin iyo wada hadal",
        "c": "Kala go’",
        "d": "Qax"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kashmiir waa goob?",
      "options": {
        "a": "Ganacsi",
        "b": "Istiraatiiji ah",
        "c": "Saxare",
        "d": "Badda"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Ingiriisku wuxuu Kashmiir ku sameeyay?",
      "options": {
        "a": "Magaalo",
        "b": "Nidaam gumeysi",
        "c": "Deked",
        "d": "Buundo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Isirka Muslimiinta Barma waa?",
      "options": {
        "a": "Rohinga",
        "b": "Arab",
        "c": "Turk",
        "d": "Hindi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Muslimiinta Barma waxay la kulmaan?",
      "options": {
        "a": "Horumar",
        "b": "Barakicin iyo xasuuq",
        "c": "Ganacsi",
        "d": "Ciyaaro"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap2_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Falastiin waxa laga helay magaca?",
      "options": {
        "a": "Badda Mediterranean",
        "b": "Buuraha",
        "c": "Saxare",
        "d": "Webi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Nabi Ibraahim Falastiin wuxuu yimid sanadkii?",
      "options": {
        "a": "1900 NCH",
        "b": "1000 NCH",
        "c": "500 NCH",
        "d": "2000 NCH"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Aashuuriyiintu waxay qabsadeen Waqooyiga Falastiin sanadkii?",
      "options": {
        "a": "721 NCH",
        "b": "800 NCH",
        "c": "600 NCH",
        "d": "500 NCH"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Israa’iil waxaa lagu dhawaaqay?",
      "options": {
        "a": "1945",
        "b": "1948",
        "c": "1950",
        "d": "1939"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kashmiir Muslimiintu waa boqolkiiba?",
      "options": {
        "a": "50%",
        "b": "60%",
        "c": "80%",
        "d": "90%"
      },
      "correctAnswer": "c",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Ingiriisku Hindiya wuxuu qabsaday?",
      "options": {
        "a": "1819",
        "b": "1850",
        "c": "1900",
        "d": "1800"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Miyanmaar waxay ka go’day Ingiriiska sanadkii?",
      "options": {
        "a": "1937",
        "b": "1947",
        "c": "1957",
        "d": "1920"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Balfour Declaration wuxuu dhacay?",
      "options": {
        "a": "1917",
        "b": "1920",
        "c": "1930",
        "d": "1900"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kashmiir dhulkeedu waa?",
      "options": {
        "a": "240k km²",
        "b": "100k km²",
        "c": "300k km²",
        "d": "500k km²"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Miyanmaar dadka ku nool waa?",
      "options": {
        "a": "30M",
        "b": "60M",
        "c": "90M",
        "d": "120M"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kancaaniyiinta waxay ka dhigan tahay?",
      "options": {
        "a": "Qabiil",
        "b": "Dhul hooseeya",
        "c": "Buur",
        "d": "Webi"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q22",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Aarmaan micnaheedu waa?",
      "options": {
        "a": "Buuraha",
        "b": "Badda",
        "c": "Dhul hoose",
        "d": "Saxare"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q23",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Falastiin Faarisiyiintu qabsadeen sanadkii?",
      "options": {
        "a": "539 NCH",
        "b": "600 NCH",
        "c": "700 NCH",
        "d": "800 NCH"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q24",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kashmiir waxaa la qeybsaday sanadkii?",
      "options": {
        "a": "1947",
        "b": "1930",
        "c": "1950",
        "d": "1920"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q25",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Falastiin muhiimaddeedu waa?",
      "options": {
        "a": "Dhaqaale",
        "b": "Diini iyo taariikhi",
        "c": "Warshado",
        "d": "Saxare"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap2_Q26",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Cusmaan bin Ardhagaral wuxuu dhintay sanadkii?",
      "options": {
        "a": "1326",
        "b": "1300",
        "c": "1288",
        "d": "1350"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q27",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Buursa caasimad noqotay sanadkii?",
      "options": {
        "a": "1302",
        "b": "1326",
        "c": "1400",
        "d": "1280"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q28",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Orkhaan wuxuu xukunka qabtay?",
      "options": {
        "a": "1326",
        "b": "1300",
        "c": "1400",
        "d": "1250"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q29",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Muxammad Al-Faatix wuxuu qabsaday Constantinople?",
      "options": {
        "a": "1453",
        "b": "1400",
        "c": "1500",
        "d": "1600"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q30",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Cusmaaniyiintu waxay burbureen kadib?",
      "options": {
        "a": "WW1",
        "b": "WW2",
        "c": "Kacdoon",
        "d": "Heshiis"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q31",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Janissaries waxay ahaayeen?",
      "options": {
        "a": "Ciidan gaar ah",
        "b": "Ganacsato",
        "c": "Farmers",
        "d": "Diblomaasiyiin"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q32",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Cusmaaniyiinta nidaamkoodu wuxuu ahaa?",
      "options": {
        "a": "Sanjak",
        "b": "Federaal",
        "c": "Qabiil",
        "d": "Boqortooyo Europe"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q33",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Suleymaan Qaanuuni wuxuu caan ku ahaa?",
      "options": {
        "a": "Sharci dejin",
        "b": "Ganacsi",
        "c": "Beeraha",
        "d": "Dagaal kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q34",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Rohinga waa?",
      "options": {
        "a": "Qowmiyad Muslim ah",
        "b": "Qabiil Hindu",
        "c": "Qabiil Budhist",
        "d": "Yuhuud"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q35",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Ururka 969 wuxuu la aas aasay?",
      "options": {
        "a": "1999",
        "b": "2005",
        "c": "1980",
        "d": "2010"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q36",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Dowladda Israa’iil waxay burburisay Falastiin sanadkii?",
      "options": {
        "a": "1948",
        "b": "1939",
        "c": "1950",
        "d": "1920"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q37",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Kashmiir waxaa ku nool?",
      "options": {
        "a": "12 milyan",
        "b": "5 milyan",
        "c": "20 milyan",
        "d": "50 milyan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q38",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Balfour Declaration wuxuu dhacay?",
      "options": {
        "a": "1917",
        "b": "1920",
        "c": "1930",
        "d": "1900"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q39",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Miyanmaar caasimaddeedu waa?",
      "options": {
        "a": "Rangoon",
        "b": "Tokyo",
        "c": "Delhi",
        "d": "Dhaka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap2_Q40",
      "subjectId": "his",
      "chapterId": "Chapter 2",
      "question": "Falastiin Faarisiyiintu qabsadeen sanadkii?",
      "options": {
        "a": "539 NCH",
        "b": "600 NCH",
        "c": "700 NCH",
        "d": "800 NCH"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Waa maxay dawladnimo gaarsiinta?",
      "options": {
        "a": "Qaab maamul gumeysi cusub ah",
        "b": "Hab ka mid ah hababka dowladihii WWII kadib loo sameeyay dalal",
        "c": "Nidaam ciidan kaliya",
        "d": "Xukun boqortooyo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Dawladnimo gaarsiintu waxay la xiriirtaa xilligii?",
      "options": {
        "a": "Dagaalkii 1aad",
        "b": "Dagaalkii 2aad kadib",
        "c": "Qarnigii 19aad",
        "d": "Qarnigii 21aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Yaa maamulayay koonfurta Soomaaliya 1941 kadib?",
      "options": {
        "a": "Talyaaniga",
        "b": "Ingiriiska",
        "c": "Faransiiska",
        "d": "Ethiopia"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Yaa ugu dambeyn loo xilsaaray dawladnimo gaarsiinta Soomaaliya?",
      "options": {
        "a": "Ingiriiska",
        "b": "Talyaaniga",
        "c": "Ethiopia",
        "d": "Qaramada Midoobay"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Ujeedada dawladnimo gaarsiintu waxay ahayd?",
      "options": {
        "a": "In dalka la burburiyo",
        "b": "In dalka loo diyaariyo madax-bannaani",
        "c": "In la kordhiyo gumeysi",
        "d": "In la joojiyo waxbarashada"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Talyaanigu Soomaaliya ayuu maamulay kadib heshiis?",
      "options": {
        "a": "Qaramada Midoobay",
        "b": "Ingiriiska kaliya",
        "c": "NATO",
        "d": "Midowga Afrika"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Dawladnimo gaarsiintu waxay socotay ilaa Soomaaliya ay heshay?",
      "options": {
        "a": "Dastuur cusub",
        "b": "Madax-bannaani",
        "c": "Ciidan shisheeye",
        "d": "Boqortooyo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap3_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Qaramada Midoobay waxay dooratay Talyaaniga sababtoo ah?",
      "options": {
        "a": "Awood ciidan",
        "b": "Khibrad hore oo gumeysi",
        "c": "Heshiis ganacsi",
        "d": "Xiriir diimeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Golaha dawladnimo gaarsiinta waxaa laga rabay inuu sameeyo?",
      "options": {
        "a": "Dagaal",
        "b": "Horumar iyo ismaamul",
        "c": "Kordhinta gumeysiga",
        "d": "Xukun boqor"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Mid ka mid ah gobolladii la hoos geeyay wuxuu noqday?",
      "options": {
        "a": "Xor iyo ismaamul",
        "b": "Boqortooyo",
        "c": "Gumeysi joogto ah",
        "d": "Dal cusub"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Horumarka siyaasadeed wuxuu ka mid ahaa qorshaha?",
      "options": {
        "a": "Dawladnimo gaarsiinta",
        "b": "Dagaal qabaa’il",
        "c": "Gumeysi toos ah",
        "d": "Kala qaybin"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Golayaasha la tashiga waxay ka caawiyeen?",
      "options": {
        "a": "Doorashooyin",
        "b": "Dagaal",
        "c": "Xiritaan xisbiyo",
        "d": "Gumeysi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "SYL waxay caan ku ahayd?",
      "options": {
        "a": "Dagaal hubeysan",
        "b": "Madax-bannaani doon",
        "c": "Ganacsi",
        "d": "Ciidan shisheeye"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Jeneral Daa’uud Cabdulle Xirsi wuxuu ahaa?",
      "options": {
        "a": "Ganacsade",
        "b": "Taliye ciidan",
        "c": "Saxafi",
        "d": "Qareen"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap3_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Ingiriiska iyo Talyaaniga loolankooda ugu weyn wuxuu ahaa?",
      "options": {
        "a": "Dhaqan",
        "b": "Maamul Soomaaliya",
        "c": "Diin",
        "d": "Ciyaaro"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Qaramada Midoobay go’aankeedii ugu dambeeyay wuxuu ahaa?",
      "options": {
        "a": "Ingiriiska ha maamulo",
        "b": "Talyaaniga ha maamulo",
        "c": "Soomaaliya ha la burburiyo",
        "d": "Ethiopia ha maamulo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Habka dawladnimo gaarsiintu wuxuu socday muddo?",
      "options": {
        "a": "10 sano",
        "b": "5 sano",
        "c": "20 sano",
        "d": "1 sano"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Talyaanigu Soomaaliya wuxuu kala wareegay Ingiriiska sanadkii?",
      "options": {
        "a": "1950",
        "b": "1941",
        "c": "1960",
        "d": "1930"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Doorashada 1967 waxaa ku guuleystay?",
      "options": {
        "a": "Siyaad Barre",
        "b": "Cabdirashiid Cali Sharma’arke",
        "c": "Aden Cadde",
        "d": "Maxamed Siyaad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Afgembigii Soomaaliya wuxuu dhacay sanadkii?",
      "options": {
        "a": "1969",
        "b": "1960",
        "c": "1950",
        "d": "1972"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Calanka Soomaaliya waxaa hindisay?",
      "options": {
        "a": "SYL",
        "b": "Maxamed Cawaale Liibaan",
        "c": "Siyaad Barre",
        "d": "Ingiriis"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q22",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Afka Soomaaliga waxaa la qoray sanadkii?",
      "options": {
        "a": "1972",
        "b": "1960",
        "c": "1950",
        "d": "1980"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q23",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Hannaanka ciidanka Soomaaliya wuxuu ahaa?",
      "options": {
        "a": "Hantiwadaag",
        "b": "Boqortooyo",
        "c": "Federaal",
        "d": "Gumeysi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q24",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Abaartii Daba-dheer waxay dhacday?",
      "options": {
        "a": "1974",
        "b": "1960",
        "c": "1980",
        "d": "1950"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap3_Q25",
      "subjectId": "his",
      "chapterId": "Chapter 3",
      "question": "Madaxweynaha ugu horreeyay ee kacaanka wuxuu ahaa?",
      "options": {
        "a": "Cabdirashiid",
        "b": "Siyaad Barre",
        "c": "Aden Cadde",
        "d": "Maxamed Liibaan"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Maxaa sababay dhaqdhaqaaqa Mahdiga Suudaan?",
      "options": {
        "a": "Horumar dhaqaale",
        "b": "Cadaadis gumeysi iyo dulmi Ingiriis",
        "c": "Ganacsi furan",
        "d": "Iskaashi dowladeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dhaqdhaqaaqii Mahdiga Suudaan wuxuu ahaa kacdoon?",
      "options": {
        "a": "Ganacsi",
        "b": "Diimeed iyo gumeysi-diid",
        "c": "Ciyaaro",
        "d": "Farsamo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dhaqdhaqaaqa Mahdiga wuxuu ka dhacay dalka?",
      "options": {
        "a": "Masar",
        "b": "Suudaan",
        "c": "Liibiya",
        "d": "Algeria"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Cumar Mukhtaar wuxuu ku dhashay dalka?",
      "options": {
        "a": "Liibiya",
        "b": "Masar",
        "c": "Tunisia",
        "d": "Sudan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Cumar Mukhtaar wuxuu la dagaallamay?",
      "options": {
        "a": "Ingiriiska",
        "b": "Talyaaniga",
        "c": "Faransiiska",
        "d": "Portugal"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Ujeedada Azhar ee kacdoonnada waxay ahayd?",
      "options": {
        "a": "Ganacsi",
        "b": "Ka hortag gumeysi Faransiis",
        "c": "Ciyaaro",
        "d": "Dhismaha waddooyin"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "ANC waxaa la aasaasay sanadkii?",
      "options": {
        "a": "1912",
        "b": "1900",
        "c": "1950",
        "d": "1961"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap4_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dhaqdhaqaaqa Mahdiga Suudaan wuxuu ka dhan ahaa?",
      "options": {
        "a": "Talyaaniga",
        "b": "Ingiriiska",
        "c": "Portugal",
        "d": "Ethiopia"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Cumar Mukhtaar wuxuu saldhig ka sameeyay magaalada?",
      "options": {
        "a": "Tripoli",
        "b": "Zaawiyata Qusuur",
        "c": "Cairo",
        "d": "Khartoum"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dagaalkii Azhar ee Qaahira wuxuu ka dhacay?",
      "options": {
        "a": "1798",
        "b": "1800",
        "c": "1810",
        "d": "1820"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Garabka militari ee ANC waxaa la yiraahdaa?",
      "options": {
        "a": "Warankii Ummadda",
        "b": "Guuto Afrika",
        "c": "Ciidanka Xoriyadda",
        "d": "Army South"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Hogaamiyihii ugu caansanaa Koonfur Afrika wuxuu ahaa?",
      "options": {
        "a": "Nelson Mandela",
        "b": "Julius Nyerere",
        "c": "Kwame Nkrumah",
        "d": "Haile Selassie"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dhaqdhaqaaqa Mahdiga wuxuu dhacay qarnigii?",
      "options": {
        "a": "18aad",
        "b": "19aad",
        "c": "20aad",
        "d": "21aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Azhar waxay ka mid ahayd?",
      "options": {
        "a": "Ciidan Faransiis",
        "b": "Xarumaha diimeed ee Masar",
        "c": "Ganacsi Europe",
        "d": "Boqortooyo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap4_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Dhaqdhaqaaqa Mahdiga Suudaan wuxuu ka mid ahaa?",
      "options": {
        "a": "Kacdoonnada Afrika ee gumeysi-diid",
        "b": "Dagaal ganacsi",
        "c": "Iskaashi Europe",
        "d": "Ciyaaro"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Cumar Mukhtaar waxaa lagu qabtay sanadkii?",
      "options": {
        "a": "1931",
        "b": "1911",
        "c": "1920",
        "d": "1940"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Talyaaniga iyo Cumar Mukhtaar dagaalkoodu wuxuu socday ku dhowaad?",
      "options": {
        "a": "10 sano",
        "b": "20 sano",
        "c": "30 sano",
        "d": "5 sano"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Halgankii Cumar Mukhtaar wuxuu ka bilaabmay kadib soo degitaanka Talyaaniga sanadkii?",
      "options": {
        "a": "1911",
        "b": "1900",
        "c": "1925",
        "d": "1935"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Janaraalkii Faransiiska ee Qaahira kacdoonkii lala diriray wuxuu ahaa?",
      "options": {
        "a": "Diibwii",
        "b": "Napoleon",
        "c": "Kiliibar",
        "d": "De Gaulle"
      },
      "correctAnswer": "c",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Azhar waxay door weyn ku lahayd kacdoonkii Faransiiska sababtoo ah?",
      "options": {
        "a": "Waxay hoggaamisay arday iyo culimo",
        "b": "Waxay taageertay Faransiiska",
        "c": "Waxay ahayd ganacsi",
        "d": "Waxay ahayd ciidan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap4_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 4",
      "question": "Nelson Mandela waxaa loo aqoonsaday?",
      "options": {
        "a": "Ganacsade",
        "b": "Hoggaamiye xorriyad",
        "c": "Ciidamo Faransiis",
        "d": "Boqor"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap5_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Sharax xaaladda Ruushka xilligii dhalashada kacaanka?",
      "options": {
        "a": "Ruushka waxa uu ahaa mid nabad ah oo aan dagaal jirin",
        "b": "Ruushka waxa uu galay dagaal Jabaan ah oo uu ku guuldarreystay",
        "c": "Ruushka waxa uu ahaa gumeysi Ingiriis",
        "d": "Ruushka waxa uu ku jiray midow Yurub"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Waa maxay sababta ugu weyn ee dhalisay kacaankii Ruushka?",
      "options": {
        "a": "Dhibaatooyinka beeraha iyo nolol xumo",
        "b": "Kobaca dhaqaalaha",
        "c": "Guusha dagaallada",
        "d": "Midowga Yurub"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Waa maxay mabaadii’da kacaanka Ruushka?",
      "options": {
        "a": "Xukun boqortooyo",
        "b": "Kobcinta ganacsiga kaliya",
        "c": "Isku day qabsashada dhul iyo fashilka nidaamka kalitalisnimo",
        "d": "Heshiisyo diblomaasiyadeed"
      },
      "correctAnswer": "c",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Saameynta kacaankii Ruushka ee caalamka waxa ka mid ah?",
      "options": {
        "a": "Kor u kaca shuucinimada",
        "b": "Hoos u dhaca Yurub",
        "c": "Burburka Afrika",
        "d": "Midowga Carabta"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Sheeg laba qof oo muhiim ah kacaankii Ruushka?",
      "options": {
        "a": "Napoleon iyo Caesar",
        "b": "Hitler iyo Mussolini",
        "c": "Trotsky iyo Lenin",
        "d": "Churchill iyo Roosevelt"
      },
      "correctAnswer": "c",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Maxaa ka jiray adduunka ka hor Dagaalkii 2aad ee dunida?",
      "options": {
        "a": "Nabad buuxda",
        "b": "Isballaarin iyo keli-taliye",
        "c": "Midow buuxa",
        "d": "Dhaqaale deggan"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Midkee ka mid ah sababihii Dagaalkii 2aad ee adduunka?",
      "options": {
        "a": "Heshiis Versailles",
        "b": "Midow Afrika",
        "c": "Dhimashada Lenin",
        "d": "Xorriyadda Yurub"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Natiijada Dagaalkii 2aad ee adduunka waxa ka mid ah?",
      "options": {
        "a": "Qaramada Midoobay",
        "b": "Midow Afrika",
        "c": "Dhimashada Afrika",
        "d": "Burburka Aasiya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Dagaalkii 2aad ee adduunka waxa ku dhintay qiyaastii?",
      "options": {
        "a": "10 milyan",
        "b": "62 milyan",
        "c": "5 milyan",
        "d": "100 milyan"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Midkee waa dagaal Carabta iyo Israa’iil?",
      "options": {
        "a": "1948",
        "b": "1914",
        "c": "1930",
        "d": "2000"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Aasaasidda Israa’iil waxa lagu dhawaaqay sanadkee?",
      "options": {
        "a": "1945",
        "b": "1948",
        "c": "1956",
        "d": "1967"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Sababta Dagaalkii Qaboobaa ugu weyn waa?",
      "options": {
        "a": "Isfaham",
        "b": "Loolan Mareykanka iyo Soofiyeeti",
        "c": "Midow Yurub",
        "d": "Dagaal Afrika"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Yaa hoggaaminayay Midowgii Soofiyeeti kacaanka?",
      "options": {
        "a": "Lenin",
        "b": "Churchill",
        "c": "Hitler",
        "d": "Obama"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Dagaalkii Qaboobaa waxa uu dhammaaday kadib?",
      "options": {
        "a": "1991 burburkii Soofiyeeti",
        "b": "1945",
        "c": "1939",
        "d": "2001"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Qaybinta Jarmalka waxay dhacday xilligii?",
      "options": {
        "a": "Dagaalkii 1aad",
        "b": "Dagaalkii Qaboobaa",
        "c": "Kacaankii Ruushka",
        "d": "Dagaalkii Carabta"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Heerarka Dagaalkii 2aad ee adduunka waa imisa?",
      "options": {
        "a": "2",
        "b": "3",
        "c": "4",
        "d": "5"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Talyaanigu wuxuu ku duulay Albaaniya sanadkee?",
      "options": {
        "a": "1939",
        "b": "1945",
        "c": "1918",
        "d": "1950"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Qorshaha Marshall wuxuu ahaa?",
      "options": {
        "a": "Dagaal",
        "b": "Dib u dhis Yurub",
        "c": "Kacaan",
        "d": "Ganacsi Afrika"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Midkee waa natiijada Dagaalkii 2aad?",
      "options": {
        "a": "Qaramada Midoobay",
        "b": "Midow Afrika",
        "c": "Isbeddel diimeed",
        "d": "Burburka Carabta"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Dagaalkii 6da Oktoobar waxa kale loo yaqaan?",
      "options": {
        "a": "1973 dagaal",
        "b": "1948 dagaal",
        "c": "1960 dagaal",
        "d": "1982 dagaal"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Heshiiskii Versailles waxa uu sababay?",
      "options": {
        "a": "Dagaalkii 1aad oo dhammaaday",
        "b": "Dagaalkii 2aad oo qarxay",
        "c": "Midow Afrika",
        "d": "Isbeddel Carbeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap5_Q22",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Midkee waa saameynta Dagaalkii 2aad?",
      "options": {
        "a": "Kor u kac dhaqaale Yurub",
        "b": "Burbur siiqo la’aan",
        "c": "Midow Afrika",
        "d": "Kobac Aasiya kaliya"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap5_Q23",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "ANC waxaa la aasaasay sanadkee?",
      "options": {
        "a": "1912",
        "b": "1948",
        "c": "1960",
        "d": "1980"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q24",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Nelson Mandela wuxuu noqdown?",
      "options": {
        "a": "Hoggaamiye ANC",
        "b": "Boqor",
        "c": "Ra’iisul wasaare Britain",
        "d": "Madaxweyne USA"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap5_Q25",
      "subjectId": "his",
      "chapterId": "Chapter 5",
      "question": "Dagaalkii Qaboobaa wuxuu ahaa loolan u dhexeeya?",
      "options": {
        "a": "Afrika iyo Aasiya",
        "b": "Mareykanka iyo Soofiyeeti",
        "c": "Carabta iyo Yurub",
        "d": "Hindiya iyo Shiinaha"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Sheeg xaaladihii lagu aasaasay Ururka Qaramada Midoobay?",
      "options": {
        "a": "Kadib Dagaalkii 1aad ee Adduunka",
        "b": "Intii lagu jiray Dagaalkii 2aad ee Adduunka",
        "c": "Kadib Dagaalkii Qaboobaa",
        "d": "Kadib burburkii Midowgii Afrika"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Waa maxay ujeedada Qaramada Midoobay?",
      "options": {
        "a": "Kordhinta dagaallada",
        "b": "Ilaalinta nabadda caalamka",
        "c": "Qabsashada dalal cusub",
        "d": "Kala qaybsanaanta dunida"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Xarunta ugu weyn ee Qaramada Midoobay waa halkee?",
      "options": {
        "a": "London",
        "b": "Paris",
        "c": "New York",
        "d": "Rome"
      },
      "correctAnswer": "c",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midkee ka mid ah waa xarun ka tirsan Qaramada Midoobay?",
      "options": {
        "a": "Tokyo",
        "b": "Geneva",
        "c": "Moscow",
        "d": "Cairo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Golaha ammaanka waxa uu mas'uul ka yahay maxay?",
      "options": {
        "a": "Ciyaaraha",
        "b": "Nabadda iyo amniga caalamka",
        "c": "Ganacsiga",
        "d": "Waxbarashada kaliya"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Xarunta Jaamacadda Carabta waa?",
      "options": {
        "a": "Riyadh",
        "b": "Qaahira",
        "c": "Baghdad",
        "d": "Damascus"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Midowga Afrika xaruntiisu waa?",
      "options": {
        "a": "Nairobi",
        "b": "Addis Ababa",
        "c": "Pretoria",
        "d": "Khartoum"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Qaramada Midoobay waxa la aasaasay sanadkee?",
      "options": {
        "a": "1940",
        "b": "1945",
        "c": "1950",
        "d": "1939"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midkee ka mid ah waa laan ka tirsan Jaamacadda Carabta?",
      "options": {
        "a": "Golaha Jaamacadda",
        "b": "Golaha NATO",
        "c": "Golaha Yurub",
        "d": "Golaha Aasiya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Somalia waxay ku biirtay Jaamacadda Carabta sanadkee?",
      "options": {
        "a": "1970",
        "b": "1974",
        "c": "1980",
        "d": "1969"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap6_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Maxaa keenay in la aasaaso Qaramada Midoobay?",
      "options": {
        "a": "Guulaha ciyaaraha",
        "b": "Fashilka Ururkii Ummadaha",
        "c": "Dagaalkii Qaboobaa",
        "d": "Ganacsiga caalamka"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midkee ka mid ah waa ujeeddo dhaqaalaha Qaramada Midoobay?",
      "options": {
        "a": "Dagaal abuurid",
        "b": "Horumarinta dhaqaalaha iyo bulshada",
        "c": "Qabsashada dalal",
        "d": "Xoojinta kala qaybsanaan"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Go'aanka xubinnimada Qaramada Midoobay waxaa ansixiya?",
      "options": {
        "a": "Golaha Ciyaaraha",
        "b": "Golaha Guud kadib talo Golaha Ammaanka",
        "c": "Baarlamaanka Afrika",
        "d": "Maxkamadda Adduunka"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Jaamacadda Carabta waxa uu ujeedkiisu yahay?",
      "options": {
        "a": "Kala qaybin dalalka Carabta",
        "b": "Iskaashi siyaasadeed iyo dhaqaale",
        "c": "Dagaal abuurid",
        "d": "Ganacsi gaar ah"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Midowga Afrika waxa uu bedelay?",
      "options": {
        "a": "UN",
        "b": "Midnimada Afrika (OAU)",
        "c": "NATO",
        "d": "EU"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midkee ka mid ah waa caqabad gudaha ee Midowga Afrika?",
      "options": {
        "a": "Cimilada",
        "b": "Af-gembiyada",
        "c": "Dabaylaha",
        "d": "Badda"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Qaramada Midoobay waxa ay ka caawisaa dalalka maxay?",
      "options": {
        "a": "Dagaal",
        "b": "Horumar dhaqaale iyo bulsho",
        "c": "Qabsasho",
        "d": "Kala qaybin"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midkee waa ujeeddo siyaasadeed ee Ururka Islaamka?",
      "options": {
        "a": "Midnimo Islaami ah",
        "b": "Kala qaybin",
        "c": "Dagaal",
        "d": "Ganacsi kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Bangiga Horumarinta Islaamka waxa uu ka tirsan yahay?",
      "options": {
        "a": "EU",
        "b": "OIC",
        "c": "UNICEF",
        "d": "NATO"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Maxaa sababay in Qaramada Midoobay la sameeyo?",
      "options": {
        "a": "Fashilka League of Nations",
        "b": "Ciyaaraha Olombikada",
        "c": "Dhaqaale kaliya",
        "d": "Ganacsi"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap6_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Goorma ayaa Ururka Midowga Afrika la aasaasay (AU)?",
      "options": {
        "a": "1963",
        "b": "2002",
        "c": "1990",
        "d": "1980"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q22",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Qaramada Midoobay waxaa si rasmi ah loo aasaasay kadib?",
      "options": {
        "a": "Dagaalkii 1aad",
        "b": "Dagaalkii 2aad",
        "c": "Dagaalkii Carabta",
        "d": "Dagaalkii Afrika"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q23",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Fikradda Jaamacadda Carabta waxaa asal ahaan soo jeediyay?",
      "options": {
        "a": "Jamaal Al-Diin Al-Afgaani",
        "b": "Nelson Mandela",
        "c": "Hitler",
        "d": "Churchill"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q24",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Maxkamadda Caalamiga ah ee Caddaaladda waxaa la aasaasay sanadkee?",
      "options": {
        "a": "1945",
        "b": "1930",
        "c": "1960",
        "d": "1975"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q25",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Ururka Iskaashiga Islaamka (OIC) xaruntiisu waa?",
      "options": {
        "a": "Makkah",
        "b": "Jeddah",
        "c": "Cairo",
        "d": "Riyadh"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q26",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Midowga Afrika waxa uu ka hor ahaa?",
      "options": {
        "a": "NATO",
        "b": "Midnimada Afrika (OAU)",
        "c": "EU",
        "d": "UNESCO"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q27",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Fikradda Qaramada Midoobay waxay soo bilaabatay intii uu socday?",
      "options": {
        "a": "Dagaalkii 1aad ee Adduunka",
        "b": "Dagaalkii 2aad ee Adduunka",
        "c": "Dagaalkii Qaboobaa",
        "d": "Dagaalkii Afrika"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q28",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Qaramada Midoobay waxa la aasaasay sanadkii?",
      "options": {
        "a": "1918",
        "b": "1945",
        "c": "1950",
        "d": "1960"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q29",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Go'aanka kama dambaysta ah ee xubinnimada UN waxaa qaata?",
      "options": {
        "a": "Golaha Guud",
        "b": "Golaha Ammaanka",
        "c": "Maxkamadda",
        "d": "Bangiga Adduunka"
      },
      "correctAnswer": "a",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap6_Q30",
      "subjectId": "his",
      "chapterId": "Chapter 6",
      "question": "Dagaalkii Qaboobaa waxa uu u dhexeeyay?",
      "options": {
        "a": "Carabta iyo Afrika",
        "b": "USA iyo USSR",
        "c": "Asia iyo Europe",
        "d": "Africa iyo Asia"
      },
      "correctAnswer": "b",
      "difficultyLevel": "hard"
    },
    {
      "id": "Chap7_Q01",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Qeex dastuurka?",
      "options": {
        "a": "Qawaaniin ciidan kaliya ah",
        "b": "Mabaadi'da aasaasiga ah ee habeynta awoodaha dowladda iyo xuquuqda dadka",
        "c": "Kaliya xeerarka ganacsiga",
        "d": "Sharciga maxkamadaha kaliya"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q02",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xaddid qeexidda sharciga?",
      "options": {
        "a": "Qawaaniin hagta nolosha iyo xiriirka bulshada iyo dowladda",
        "b": "Ciyaaraha bulshada",
        "c": "Heshiisyo ganacsi kaliya",
        "d": "Xeerar diimeed kaliya"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q03",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xiriirka sharciga iyo bulshada waa maxay?",
      "options": {
        "a": "Xiriir aan jirin",
        "b": "Xiriir adag oo labada dhinac is saameeyaan",
        "c": "Bulsho aan sharci lahayn",
        "d": "Sharci aan bulsho la xiriirin"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q04",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Maxkamadda dastuuriga ah waa maxay?",
      "options": {
        "a": "Maxkamad ganacsi",
        "b": "Maxkamadda sare ee garsoorka dastuurka",
        "c": "Maxkamad ciidan",
        "d": "Maxkamad hoose"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q05",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Midkee ka mid ah waa ujeeddooyinka sharciga?",
      "options": {
        "a": "Kordhinta dagaalka",
        "b": "Amniga iyo cadaaladda bulshada",
        "c": "Kala qaybsanaanta dadka",
        "d": "Xakameynta waxbarashada kaliya"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q06",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Sharcigu muhiimad ahaan waxa uu ilaaliyaa?",
      "options": {
        "a": "Kaliya ciyaaraha",
        "b": "Xasilloonida iyo xuquuqda bulshada",
        "c": "Ganacsiga kaliya",
        "d": "Safarrada"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q07",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Noocyada dastuurka waxaa ka mid ah?",
      "options": {
        "a": "Dastuur ciyaareed",
        "b": "Dastuur qoran iyo aan qorneyn",
        "c": "Dastuur caafimaad",
        "d": "Dastuur ciidan kaliya"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q08",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Shuurada maxay tahay?",
      "options": {
        "a": "Ra'yiga dadka lagu tixgeliyo talada",
        "b": "Ciidan amar bixiya",
        "c": "Ganacsi nidaam",
        "d": "Sharci ciqaab"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q09",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Dimuqraadiyaddu waxay micneheedu tahay?",
      "options": {
        "a": "Xukunka boqorka",
        "b": "Xukunka shacabka",
        "c": "Xukun ciidan",
        "d": "Xukun ganacsi"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q10",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Aayadda shuurada ee Qur'aanka waa?",
      "options": {
        "a": "Al-Fatiha",
        "b": "وأمرهم شورى بينهم",
        "c": "Ayatul Kursi",
        "d": "Al-Ikhlas"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q11",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Faa'iidada shuurada waa maxay?",
      "options": {
        "a": "Kala qaybin bulshada",
        "b": "Is-afgarad iyo khilaaf yaraan",
        "c": "Dagaal kordhin",
        "d": "Musuqmaasuq"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q12",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Tiirarka dimuqraadiyadda waxaa ka mid ah?",
      "options": {
        "a": "Ciidan kaliya",
        "b": "Doorasho iyo xorriyad fikir",
        "c": "Xayiraad warbaahin",
        "d": "Xukun hal qof"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q13",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Dimuqraadiyadda iyo shuurada farqigooda waa?",
      "options": {
        "a": "Isku mid yihiin",
        "b": "Mid waa shacab, midna waa diin ku saleysan",
        "c": "Labaduba ciidan yihiin",
        "d": "Labaduba waa ganacsi"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q14",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Dimuqraadiyaddu waxay asal ahaan ka timid?",
      "options": {
        "a": "Afrika",
        "b": "Giriigga iyo Roomaanka",
        "c": "Aasiya",
        "d": "Carabta"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q15",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xisbi siyaasadeed waa maxay?",
      "options": {
        "a": "Koox ciyaartoy",
        "b": "Koox siyaasadeed oo doonaysa talo qabasho",
        "c": "Urur diimeed",
        "d": "Urur ganacsi"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q16",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Ka qeybgalka siyaasadda waa?",
      "options": {
        "a": "Ka fogaanshaha dowladda",
        "b": "Saameynta go'aan qaadashada dowladda",
        "c": "Ciyaar siyaasadeed",
        "d": "Ganacsi"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q17",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xisbiyada siyaasadeed waxay bilaabeen qarnigii?",
      "options": {
        "a": "17aad",
        "b": "19aad (1850kii)",
        "c": "21aad",
        "d": "15aad"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q18",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xisbiyada Soomaaliya waxay ka soo baxeen?",
      "options": {
        "a": "Ciidanka kaliya",
        "b": "Ururrada shaqaalaha iyo ardayda",
        "c": "Ganacsato kaliya",
        "d": "Dalal shisheeye"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q19",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Qaabka ka qeybgalka siyaasadda waxaa ka mid ah?",
      "options": {
        "a": "Cod-bixin iyo musharraxnimo",
        "b": "Dagaal",
        "c": "Ganacsi",
        "d": "Safar"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q20",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Taariikhda siyaasadda Soomaaliya 1969 waxa dhacay?",
      "options": {
        "a": "Doorasho",
        "b": "Afgambi milatari",
        "c": "Heshiis nabadeed",
        "d": "Midow dowladeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q21",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Heerarka ka qeybgalka siyaasadda waxaa ka mid ah?",
      "options": {
        "a": "Fikir, hawlgal, dhaqdhaqaaq",
        "b": "Ciyaar kaliya",
        "c": "Ganacsi",
        "d": "Ciidan"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "Chap7_Q22",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xisbiyada tartama waxaa loo qeybiyaa?",
      "options": {
        "a": "Hal nidaam kaliya",
        "b": "Nidaamyo kala duwan sida laba xisbi iyo xisbiyo badan",
        "c": "Ciidan iyo shacab",
        "d": "Dalal iyo gobollo"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q23",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Xisbiyada waxaa jira?",
      "options": {
        "a": "Kaliya tartama",
        "b": "Tartama iyo aan tartamin",
        "c": "Kaliya ciidan",
        "d": "Kaliya diimeed"
      },
      "correctAnswer": "b",
      "difficultyLevel": "easy"
    },
    {
      "id": "Chap7_Q24",
      "subjectId": "his",
      "chapterId": "Chapter 7",
      "question": "Shuruudaha xisbiga siyaasadeed waxaa ka mid ah?",
      "options": {
        "a": "In uu lahaado ciidan",
        "b": "In uusan ka hor imaan dastuurka iyo nabadda",
        "c": "In uu noqdo urur ciyaareed",
        "d": "In uu xiran yahay"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_0",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Qeex cilmiga jiyooloojiga?",
      "options": {
        "a": "cilmiga jiyooloojiga waa aqoon ama cilmi la xariiro barashada ama",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_1",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Tilmaam laamaha ugu muhiimsan ee cimiga Jiyooloojiga?",
      "options": {
        "a": "b. Jiyooloojiga bay’ada(deegaanka).",
        "b": "Jiyooloojiga handasada.",
        "c": "Jiyooloojiga waxbarshada.",
        "d": "Jiyooloojiga saliidda iyo dhaqaalaha."
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_2",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "caddee waayada jiyooloojiga?",
      "options": {
        "a": "b. Kambiriyan ka horreeye(Arch or pre-Cambrian time)",
        "b": "N/A",
        "c": "Waaga labaad(waagii mesosooik) ama waagii nolosha dhexe",
        "d": "Waaga seddexaad(kinozoi)"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_3",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "falanqee ahmiyadda dhaqaale ee waayada jiyooloojiga?",
      "options": {
        "a": "N/A",
        "b": "Waagii baaliyosooiga wuxuu ka kooban yahay caydhiinka macaadinta birta",
        "c": "Waagii mesosooik ama waagii nolosha dhexe saliidda waxa ay kamid tahay",
        "d": "Waagii Kinozoi waxa sameysmay dhagaxa nuuriyadda iyo dhagaxa"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_4",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "caddee kaalinta culimada muslimiinta ay kulahaayeen cilmiga jiyooloojiga?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Culimada muslimiinta waxa ay kudhiseen cilmiga jiyooloojiga qaab maangal",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_5",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "qeex qaab dhismeedka jiyooloojiga dhulka Soomaaliya?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Qaab dhismeedka jiyooloojiga Soomaaliya waxa ay ka timid sagxaddii hore",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_6",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Tilmaan xiliyada jiyoolooji ee Soomaaliya?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "b. Waaga koowaad am xilliga Tirisik",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_7",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "falanqee dhaqdhaqaaqayada gilgil iyo saameynta ay ku yeesheen qaab",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Wuxuu laxariiraa sameysanka Gacanka cadmeed(laga soo bilaabo galbeed",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_8",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "caddee nuucyada carrada dhulka Soomaaliya?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "b. carrada bannaan xeebeedka",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_9",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Wax ka qor dhibaatooyinka carrada dhulka Soomaaliya",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Guud ahaan dhulka Soomaaliya waxa haysta dhibaatooyin ay kimid tahay",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_10",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "caddee waxa loola jeedo cilmiga jiyooloojiga?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Cilmiga jiyooloojiga waa barashada dhulka iyo qeybihiisa kala duwan sida:",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_11",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "qor warbixin kusaabsab waayada jiyooloojiga Soomaaliya?",
      "options": {
        "a": "Waaga koowaad: waxa la oran karaa kama hiro dhulka Soomaaliya,",
        "b": "Waaga labaad: dhadhaabyada waagan waxa laga helaa dhul aad u ballaaran",
        "c": "Waaga saddexaad: waagan qeyb ballaaran oo ka mid ah dhulka jasiirad u egta",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_12",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "sababee filiqsanaanta berriga iyo biyaha dhulka Soomaaliya ee xilligan aynu",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "sababtoo ah xilligan aynu kujirno waxaa dhacay rogrogan xagga dhulka ah",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_13",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Waxaa lagu qiyaasaa da’da dhulka ku dhawaad",
      "options": {
        "a": "3000 milyan sano",
        "b": "2000 milyan sano",
        "c": "4000 milyan sano",
        "d": "5000 milyan sano"
      },
      "correctAnswer": "b",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_14",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Waxa lagu qiyaasaa da’da qolofta dhulka ku dhawaad",
      "options": {
        "a": "1500 milyan sano",
        "b": "1600 milyan sano",
        "c": "2000 milyan sano",
        "d": "1800 milyan sano"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_15",
      "subjectId": "geo",
      "chapterId": "geo_ch1",
      "question": "Waaga ugu dheer waayada jiyooloojiga waa",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "Waaga saddexaad( Kaayoonusawi)",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_16",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sharax astaamaha nololeyda?",
      "options": {
        "a": "Gibilka nololeyda waxa lagu yaqaanaa kala duwanaanta waxa uu ka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_17",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Qeex carrada?",
      "options": {
        "a": "carradu waa dhagax burburay kaa oo ay ku dhacday isbeddello kiimiko ah,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_18",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Wax ka qor waxtarka carrada ay u leedahay noolaha?",
      "options": {
        "a": "waxey kashaqeysaa ciidu in ay cunnada soo gudbiso.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_19",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaan waxyaabaha ay kakoobantahay carrada?",
      "options": {
        "a": "b- walxo macdaneed.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_20",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sheeg waxyaabaha kaqeyb qaata sameysanka carrada?",
      "options": {
        "a": "b- carro guurka.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_21",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sheeg nuucyada dhirta dabiiciga ah?",
      "options": {
        "a": "b- Kaymaha.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_22",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaam waxayaabaha saameynta kuleh koritaanka dhirta dabiiciga ah?",
      "options": {
        "a": "b- waa carrada, kala sarreynta dhulka, xaddiga da’aaga roobka, heerkulka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_23",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Wax kaqor waxtarka dhirta dabiiciga ah?",
      "options": {
        "a": "b- waxay ilaalisaa qoyaanka carrada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_24",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Falaanqee dhibaatooyinka haysta dhirta dabiiciga ah?",
      "options": {
        "a": "Waxa haysta isticmaal xumida aadanaha, waxaana kamid ah ballaarinta",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_25",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Muuji kaalinta aadanaha uuw kuleeyahay adduunweynaha iyo",
      "options": {
        "a": "waxa uuw kuleeyahay hagaajinta dhul-beereedka, dhismooyinka daaraha,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_26",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Qeex noocyada xayawaanada?",
      "options": {
        "a": "noocyada xayawaanada waa shimbiraha, daaq cune, ugaarsade, cayayaan",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_27",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaam waxyaabaha Juqraafiga ah ee saameeya filiqsanaanta",
      "options": {
        "a": "b- dhirta dabiiciga ah.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_28",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Caddee waxa loola jeedo gobol dabiici ah?",
      "options": {
        "a": "waa gobol dhulka kamid ah oo leh astaamo isku mid ah marka laga eego",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_29",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaam gobolada dabiiciga ah ee dunida?",
      "options": {
        "a": "gobollada kulaalayda kulul, gobollada diiri-maad dhex-dhexaadka ah,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_30",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Isbarbar dhig astaamaha gobollada kulul iyo kuwa qabow ee dunida?",
      "options": {
        "a": "gobollada kulul waxa lagu yaqaa heerkulka oo aad u sarreyo, iyo roobab",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_31",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sheeg gobollada ay Soomaaliya katirsan tahay?",
      "options": {
        "a": "waxa ay katirsan tahay gobollada kulaaleyda ah(tropical regions).",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_32",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Maxay tahay nolosha dhirta iyo xayawaanada dalka Soomaaliya?",
      "options": {
        "a": "way kobceysaa, way yaraaneysaa, way abaarsaneysaa hadba sida ay tahay",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_33",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaam caqabadaha haysta dhirta iyo xayawaanada Soomaaliya?",
      "options": {
        "a": "xaalufinta Keymaha iyo isbeddelada xun ee ku dhacaya deegaanka sida",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_34",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Caddee dhibaatooyinka haysta dhirta dhulka Soomaaliya?",
      "options": {
        "a": "isticmaal xumida aadanaha sida jarista dhirta ayadoon la’abuureyn dhir",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_35",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Wax ka qor waxtarka kheyraadka xoolaha Soomaaliya?",
      "options": {
        "a": "guud ahaan dadka Soomaaliyeed waxay si weyn ugu tiirsan yihiin",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_36",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Ka fekir oo soo bandhig hababka looga gudbi karo laguna maareyn karo",
      "options": {
        "a": "in haddii geed lajaro lajaro lagu bedelo geed kale oo latalaalayo, iyo in",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_37",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Qeex waxa loola jeedo nololey?",
      "options": {
        "a": "waa dhamaan nonoleyda ama noolaha laga helo oogada sare ee dhulka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_38",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Tilmaam waxa ay kakoobantahay gibilka nololeyda?",
      "options": {
        "a": "waxa ay kakoobantahay carrada, dhirta, xayawaanka iyo aadanaha.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_39",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sheeg noocyada carrada?",
      "options": {
        "a": "Carro madow, carro gaduud, carro hurdiga ayaa ah noocyada carrada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_40",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "B- kaymaha: waa qeybta ugu weyn uguna muhiimsan qeybaha dhirta,",
      "options": {
        "a": "Caws: waa dhir gaagaaban oo kala nooc ah taa oo kabaxdo meelo kala",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_41",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Ka hadal nolosha dhirta iyo xayawaanada Soomaaliya?",
      "options": {
        "a": "dhirta soomaaliya kubadan waa tan dabiiciga taas oo sidhameystiran ugu",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_42",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sharaxaad kabixi waxyaabaha saameeya dhirta dabiiciga iyo",
      "options": {
        "a": "b- carrada: waa meesha ay kabaxdo dhirta isla markaana lagama",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_43",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Sababee waxyaabaha soo socda:",
      "options": {
        "a": "sababtoo ah dhirta waxa ay soo saartaa neefta lagama maarmaanka u ah",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_44",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Noocyada carrada tan ugu bacrinsan waa",
      "options": {
        "a": "Carrada gaduudan",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_45",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Waxaa lagu magacaabaa cowska meelaha dhex-dhexaadka ah",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_46",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Gobolka kulaaleylada wuxuu fidsan yahay inta udhexeysa",
      "options": {
        "a": "40-50 koonfurta kulaalaha koonfureed.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_47",
      "subjectId": "geo",
      "chapterId": "geo_ch2",
      "question": "Roobabka gobolka badhaalaha waxay da’aan sanadka oo dhan iyaga oo",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_48",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Qeex kala duwanaashiyaha deegaanka?",
      "options": {
        "a": "waa kala duwanaashiyaha noolaha sida kala duwanaashiyaha qaab",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_49",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg muhiimadda kala duwanaashiyaha deegaanka?",
      "options": {
        "a": "waa kala duwanaanta cimilada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_50",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg sababaha keena burburka deegaan ee kaymaha dunida?",
      "options": {
        "a": "waa baahidda beerashada iyo fititaanka magaalooyinka oo dhib weyn",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_51",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Falaanqee dhibaatada deegaanka iyo saameynta ay kuleedahay",
      "options": {
        "a": "dhibaatooyinku waa wasakhoobidda hawada, biyaha, carrada, iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_52",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg khatarta deegaan ee ugu badan oo aadanaha waxyeeleyn karta?",
      "options": {
        "a": "waa wasakhoowga iyo isbeddelka cimilada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_53",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Maxey yihiin noocyada wasakhoowga deegaanka?",
      "options": {
        "a": "wasakhoowga biyaha.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_54",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay xaaluf?",
      "options": {
        "a": "Waa hoos ushac kuyimaada carrada dhulka qallalan iyo dhulka biyaha leh,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_55",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg qeyb ka mid ah dhibaatooyinka xaalufka?",
      "options": {
        "a": "xaalufku waxa uuw hakiyaa horumarka bulshada iyo dhaqaalaha dalka.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_56",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Falaanqee xalka ka hortagga xaalufka?",
      "options": {
        "a": "sameynta seero deegaan oo la ilaaliyo.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_57",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Qeex macnaha xarfashada ciida?",
      "options": {
        "a": "waa dhaqaaq tartiib ah ee ciidda oo ay dabeeyshu dhaqaajiso.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_58",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg sababaha xarfashada carrada?",
      "options": {
        "a": "daaqa aan loo meel dayin.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_59",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Falaanqee noocyada xarfashada iyo sida loo yareyn karo?",
      "options": {
        "a": "in la joojiyo si xun u isticmaalka carrada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_60",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg dhibaatooyinka ugu badan ee ka dhasha daadadka?",
      "options": {
        "a": "b- khasaaro naf iyo maal ah.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_61",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg sababaha daadadka iyo sida looga hortagi karo?",
      "options": {
        "a": "sababaha daadadka waa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_62",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg dhibaatada deegaanka Soomaaliya?",
      "options": {
        "a": "dhibaatada deegaanka Soomaaliya waa jaridda dhirta, abaaraha, iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_63",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Sheeg dhibaatooyinka ugu badan ee ka dhasha dhibaatada deegaanka",
      "options": {
        "a": "waa wasakhowga biyaha, hawada, carrada iyo nabaad guurka carrada iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_64",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Maxay kor ugu kacday daneynta caalamka ay daneeyaan kala",
      "options": {
        "a": "maxaa yeelay kala duwanaashiyaha nooluhu wuxuu hormarinayaa wax",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_65",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "wax ka qor dhibaatooyinka deegaan ee xarfashada carrada?",
      "options": {
        "a": "wax soo saarka oo isbedel kuyimaado iyo bixitaankii dhirta oo gaabis",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_66",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Wax ka qor dhibaatooyinka deegaan ee daadadka?",
      "options": {
        "a": "dhibaatooyinka deegaan ee daadadka waa musiibooyin wata khasaaro",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_67",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay kala duwanaashiyaha noolaha?",
      "options": {
        "a": "kala duwanaashiyaha deegaanka ayaa ah kala duwanaashiyaha noolaha.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_68",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay wasakhow?",
      "options": {
        "a": "wasakhowga waa isbeddel iyo daryeel la’aan ku timaada deegaanka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_69",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay nabaad guur?",
      "options": {
        "a": "nabaad guurku waa nafaqaddaro dhulka gaartay aawgeed in ay geedo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_70",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay xarfashada carrada?",
      "options": {
        "a": "dhaqaaq tartiib ah ee ciidda ama carrada oo ay dabeeyshu dhaqaajiso.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_71",
      "subjectId": "geo",
      "chapterId": "geo_ch3",
      "question": "Waa maxay daadad?",
      "options": {
        "a": "daadadku waa musiibooyin inta badan ku yimaado xaddiga da’aaga",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_72",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Caddee halka Soomaaliya dhacdo falaki ahaan iyo saameyntiisa xagga",
      "options": {
        "a": "Soomaaliya waxay dhacdaa falaki ahaan inta u dhaxeysa loolka 2⁰",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_73",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Tilmaan saameynta deriska juqraafi ahaaneed ee dalka?",
      "options": {
        "a": "xadka dalka Soomaaliya iyo dalalka deriska la ah wuxuu ka mid yahay",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_74",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Falanqee ahmiyaddda istiraatiijiyadeed ee dhulka Soomaaliya?",
      "options": {
        "a": "waa dhul kaabad ah ama buundo ah taa oo isku xireysa saddexda",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_75",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Habee gobollada Soomaaliya adigoo ka soo bilaabayo dhanka",
      "options": {
        "a": "Jubbada dhoose, Jubbada dhexe, Gedo, Baay, Bakool, Shabeelada hoose,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_76",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Wax ka qor muuqaallada dhulka oogada sare ee Soomaaliya.?",
      "options": {
        "a": "jiidda banaannada T- Jiidda dulaha J- Jiidda buuraleyda.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_77",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Sheeg tilmaamaha oogada sare ee dhulka Soomaaliya?",
      "options": {
        "a": "Kala sarreynta dhulka Soomaaliya waa kala jaad, inkastoo nooca ugu",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_78",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Sheeg buurta ugu dheer Soomaaliya?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_79",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Isbarbar dhig adeegsiga noocyada toboogaraafiyada dhulka Soomaaliya?",
      "options": {
        "a": "■ Jiidda Buuraleyda Soomaaliya ama taxanaha buuraleyda ah ee ku fidsan",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_80",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "wax ka qor waxyaabaha saameeya cimilada Soomaaliya?",
      "options": {
        "a": "■ xilliga ay cadceeddu dul istaageyso.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_81",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Caddee kaalinta joogga sare, badda iyo dhirta ay ku leeyihiin hoos",
      "options": {
        "a": "kaalinta joogga sare, badda iyo dhirta ay ku leeyihiin hoos udhigidda heer",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_82",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Isbarbar dhig magaalooyinka xeebaha iyo kuwa xeeb ka fogta ah adigoo",
      "options": {
        "a": "Haddii aynu eegno Kismaayo huur u eeggu wuu kordhayaa, taa oo aan ka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_83",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Wax ka qor abaaraha iyo daadadka Soomaaliya?",
      "options": {
        "a": "Abaaraha Soomaaliya ku dhaca way kala duwan tahay taa oo ka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_84",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Tilmaan caqabadaha heysta tiro koobidda dadka Soomaaliya?",
      "options": {
        "a": "■isgaarsiinta oo aad u liidata, gaadiid xumo iyo waddooyinka oo iyagana",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_85",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Caddee celceliska cufnaanta dadka Soomaaliyeed iyo hannaanka",
      "options": {
        "a": "Hannaanka filiqsanaanta dadka Soomaaliyeed ee la xiriira bedka dalka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_86",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Wax ka qor ahmiyadda qaab dhismeedka da’da dalka iyo tilmaamaha",
      "options": {
        "a": "Ahmiyadda qaab dhismeedka da’da dalka waxa lagu tilmaamaa mid aad",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_87",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "sheeg hannaanka qaab dhismeed ka dhaqaale ee Soomaaliya?",
      "options": {
        "a": "xoolo dhaqato 65%, beeraley 14%, xirfadleyaasha 8% kaluumeysato 1%",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_88",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "sababee saamiga celceliska yar ee reer magaalka yar ee dalka",
      "options": {
        "a": "sababtoo ah isha dhaqaale oo ay kutiirsanyihiin oo ugu muhiimsan baa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_89",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Caddee ahmiyada waaxda xoolo dhaqashadq Soomaaliya?",
      "options": {
        "a": "■ ahmiyadda xagga cunnada:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_90",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "tilmaan caqabadaha dabiiciga ah iyo kuwa aadanaha la xiriira ee waaxda",
      "options": {
        "a": "calaf isku dheelitirnaanta aad u yar.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_91",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "wax ka qor hababka lagu hormarin karo waaxda xoolo dhaqashada",
      "options": {
        "a": "■ in laga guuro xoolo dhaqasho dhaqameedka loona guuro xoolo dhaqashada",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_92",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Tilmaan dhulka ku haboon beerashada, saamiga laga faa’iideysto iyo",
      "options": {
        "a": "dhulka ku haboon qodashada beeraha waxay mataleysaa 12.9% bedka guud,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_93",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "5% bedka ku haboon beeraha.",
      "options": {
        "a": "waxa lasameeyay tiro badan oo iskaashatooyin iyo wakaalado ah sida:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_94",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "tilmaan caqabadaha dabiiciga ah iyo kuwa aadanaha laxariira ee waaxda",
      "options": {
        "a": "caqabadaha dabiiciga ah:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_95",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Sharaxaad ka bixi hannaanka wax soo saarka warshadaha Soomaaliya?",
      "options": {
        "a": "Hannaanka waxsoosaarka warshadaha Soomaaliya waxaa lagu tilmaamaa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_96",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Sheeg caqabadaha waaxda kalluumeysiga Soomaaliya?",
      "options": {
        "a": "■Dhaqamada laga dhaxlay awooweyaasha ee kallun cunidda gaarsiiyay ilaa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_97",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "wax ka qor hababka lagu maareyn karo caqabadaha waaxda kalluumeysiga?",
      "options": {
        "a": "waxa lagu maareyn karaa in bulshada labaro muhiimada dhaqaale iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_98",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Falanqee waaxda ganacsiga ee dib u soo nooleeynta waaxaha dhaqaalaha",
      "options": {
        "a": "Ganacsiga xagga dibedda waxay kaalin muhiim ka qaadataa dhaqaalaha",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_99",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "sharax doorka gaadiidka dib u soo nooleeynta waaxaha dhaqaalaha",
      "options": {
        "a": "doorka gaariidka waa mid muhiim u ah dhaqdhaqaaqa dadweynaha iyo isu",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_100",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Isbarbar dhig kaabayaasha iyo caqabadaha gaadiidka Soomaaliya?",
      "options": {
        "a": "caqabadaha gaadiidka iyo kaabayaasha waa Masaafooyinka oo ay aad u kala",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_101",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "qor warbixin ku saabsan ahmiyadda waaxda dalxiiska Soomaaliya?",
      "options": {
        "a": "inkastoo Soomaaliya aysan ka faa’ideysan waaxda dalxiiska haddana waxa ay",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_102",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Tilmaan xiriirka ka dhexeeya halka dali uu dunida kaga yaal juqraafi ahaan",
      "options": {
        "a": "Halka uu dali kaga yaal juqraafi ahaan dunida sida cimiladiisa istiraatijiyadda",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_103",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Caddee tilmaamaha dadka Soomaaliyeed?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_104",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "falanqee ilaha dhaqaale ee Soomaaliya iyo caqabadaha heysta?",
      "options": {
        "a": "Ilaha dhaqaale ee soomaaliya waa beeraha, xoolaha, kalluumeysiga.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_105",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "wax ka qor Halka Soomaaliya ay dhacdo juqraafi ahaan?",
      "options": {
        "a": "Soomaaliya waxa ay dhacdaa Bariga qaaradda Afrika.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_106",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "wax ka qor dalalka soohdinta la leh Soomaaliya ama deriska la ah?",
      "options": {
        "a": "Dalalka soohdinta la leh Soomaaliya waa dalka Jabuuti oo dhanka waqooyi",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_107",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Soomaaliya waxay dhacdaa ......................",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_108",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Soomaaliya waxay dhacdaa.......................",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_109",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "sababee daganaan la’aanta sohdimaha Soomaaliya iyadoo ay jirto in ay deris",
      "options": {
        "a": "sababtu waxay tahay loolka ka dhexeeya Soomaaliya iyo labada dal ee",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_110",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "Sababee dhaqaalo yarida dalka Soomaaliya iyadoo ay jirto ilaha dhaqaale oo",
      "options": {
        "a": "Sababtoo ah dalku waa mid tabar daran oo aan ka faa’ideysan karin ilahaas",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_111",
      "subjectId": "geo",
      "chapterId": "geo_ch4",
      "question": "qor muhiimadda Badda?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_112",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Qeex waxa loola jeedo filiqsanaanta dadka dunida?",
      "options": {
        "a": "dadka dunida ku nool dhulka dushiisa waxay ugu filiqsan yihiin qaab aan isla",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_113",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan ilaha daraaseynta dadka?",
      "options": {
        "a": "■Tirokoobka dadka.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_114",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Falanqee ahmiyadda daraaseynta dadka?",
      "options": {
        "a": "In lala socdo korarka dadka ee joogtada ah, iyo in laga war hayo waxa loo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_115",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Falanqee qodobbada dabiiciga ah ee saameeya baahsanaanta tirada dadka?",
      "options": {
        "a": "Qodobada dabiiciga ah ee saameeya baahsanaanta tirada dadka waa Cimilada,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_116",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan qodobbada aadanaha la xariira ee saameeya baahsanaanta tirada",
      "options": {
        "a": "■Heerka dhalashada iyo dhimashada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_117",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan xiriirka ka dhexeeya qodobbada dabiiciga ah iyo kuwa aadanaha la",
      "options": {
        "a": "Xiriirka ka dhexeeya qodobada dabiiciga iyo kuwa aadanaha la xariiraahi waa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_118",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Qeex waxa loola jeedo cufnaanta tirada dadka?",
      "options": {
        "a": "cufnaanta tirada dadka waxaa loola jeedaa saamiga dadka marka loo eego",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_119",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Kala sooc dalalka dunida adigoo u eegayo cufnaanta tirada dadka?",
      "options": {
        "a": "■Gobol cufnaanta tirada dadka ay aad u sarreyso: goobahani cufnaanta tirada",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_120",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan qaabka loo xisaabiyo cufnaanta tirada dadka?",
      "options": {
        "a": "cufnaanta tirada dadka = tirada guud dadka meel dhulka mid ah ÷ Baaxadda",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_121",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan tirada dadka Soomaaliyeed?",
      "options": {
        "a": "Tirada dadka Soomaaliyeed waxay gaareeysaa sida lagu xusay tirokoobkii",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_122",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Falanqee baahsanaanta dadka iyo cufnaanta tirada dadka Soomaaliyeed?",
      "options": {
        "a": "Tirada dadka Soomaaliyeed uguma filiqsana dhulka dushiisa si siman, dadku",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_123",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Caddee waxa loola jeedo tirokoobka juqraafi?",
      "options": {
        "a": "waa cilmiga la xariira soo ururinta xogaha, nidaamintooda iyo soo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_124",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Falanqee noocyada tirokoobka juqraafi?",
      "options": {
        "a": "Tirokoob Tilmaamid ah:waa kan ku tiirsan tilmaamid muuqaal xilli gaar ah",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_125",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Tilmaan ilaha xogaha tirokoobka?",
      "options": {
        "a": "■ Maktabadda.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_126",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Sheeg aragtida tirokoobka iyo Qur’aanka?",
      "options": {
        "a": "Eebbe waxa uu noo sheegay in aan tiri karno nimcooyinka uu noogu deeqay",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_127",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Qeex erayada soo socda:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_128",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Qor warbixin ku saabsan waxyaabaha saameeya baahsanaanta tirada dadka",
      "options": {
        "a": "waxyaabaha saameeya baahsanaanta tirada dadka waxaa ka mid ah cimilada",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_129",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Isbarbar dhig saameynta colaadda iyo cimilada baahsanaanta dadka iyo",
      "options": {
        "a": "colaadda waa dhibaato ay ka cararayaan dadka waxayna u cararayaan goobo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_130",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Diyaari warbixin ku saabsan sababaha ay dadka ugu soo hijroonayaan",
      "options": {
        "a": "sababaha ay dadka miyiga uga soo tegayaan iyagoo soo aadaya magaalada",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_131",
      "subjectId": "geo",
      "chapterId": "geo_ch5",
      "question": "Sheeg qeybaha socdaalidda(Hijrada)?",
      "options": {
        "a": "b: Socdaal gudaha ah(hijrada gudaha).",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_132",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Sheeg sababaha keena in loo hayaamo magaalooyinka?",
      "options": {
        "a": "■ nolosha miyiga oo aan ahayn mid lagu maqsuudo waayo waxay ka liidataa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_133",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Falanqee astaamaha bulshada magaalada jooga ah?",
      "options": {
        "a": "■ Tirada dadka magaalada oo aad u badan.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_134",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Soo jeedi xal ku habboon dhibaatooyinka ka jira degmo magaaleedka?",
      "options": {
        "a": "xalka aan soo jeedinaahi waxa uu noqonayaa sidan:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_135",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Sheeg shaqooyinka magaalada ee kala duwan?",
      "options": {
        "a": "■ magaalo diimeed.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_136",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Falanqee dhibaatooyinka magaalada?",
      "options": {
        "a": "■ ciriiriga waddooyinka ayaa ah dhibaato taagan.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_137",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Soo jeedi xal ku haboon dhibaatooyinka magaalada?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_138",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Ka hadal magaalooyinka Soomaaliya?",
      "options": {
        "a": "Soomaaliya waxay leedahay ilaa 22 magaalo oo waa weyn oo mid waliba",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_139",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Falanqee kaalinta socdaalka uu ku leeyahay kala duwanaashiyaha kobaca",
      "options": {
        "a": "Socdaalka dibadda iyo gudaha ayaa wuxuu kaalin ka qaatay kala",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_140",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Sheeg waxa ay ku kala duwan yihiin magaalooyinka Soomaaliya?",
      "options": {
        "a": "magaalooyinka Soomaaliya waxa ay ku kala duwanyihiin dadka ku nool",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_141",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Qeex micnaha magaalo?",
      "options": {
        "a": "magaalo waa deegaan ay ku noolyihiin dad farabadan, waxayna leedahay",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_142",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Maxaa loola jeedaa degmo magaaleed?",
      "options": {
        "a": "degmo magaaleed waa fiditaanka magaalooyinka?",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_143",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Falanqee degmooyinka Soomaaliya?",
      "options": {
        "a": "1. Gobolka Banaadir.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_144",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Shabelada Dhexe.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_145",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Hiiraan.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_146",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Galguduud.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_147",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Mudug",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_148",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Nugaal.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_149",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Bari.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_150",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Sool.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_151",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Sanaag.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_152",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Togdheer.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_153",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka waqooyi galbeed.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_154",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Awdal.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_155",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Sh/hoose.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_156",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Bay.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_157",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Gedo.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_158",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Bakool.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_159",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Jubada Dhexe.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_160",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Gobolka Jubada Hoose.",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_161",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Isku xir magaalooyinka soo socda iyo shaqadooda:",
      "options": {
        "a": "Okisford waa magaalo waxbarasho, Muqdisho waa magaalo maamul iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_162",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Mid ka mid ah astaamaha soo socdo ma aha astaamaha magaalada:",
      "options": {
        "a": "Caadooyinka iyo dhaqanka oo saameyn ku leh dadka(B)",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_163",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Tusaale ukeen waxyaabahan soo socda:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_164",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "magaalo waxbarasho?",
      "options": {
        "a": "Oxford, iyo Calaykara.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_165",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "magaalo ganacsi?",
      "options": {
        "a": "Dubay, iyo Tokyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_166",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "magaalo warshadeed?",
      "options": {
        "a": "Diitarot oo mareykanka ah iyo Liyoon oo faransiiska ah.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_167",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "magaalo diimeed?",
      "options": {
        "a": "Maka al Mukarama iyo Madiina.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_168",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Maxaad ku micneyn lahayd warshadaha oo ku badan magaalada Muqdisho?",
      "options": {
        "a": "waxan ku micneyn lahaa wadadii horumarka in ay cagta saartay.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_169",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "maxaad ku micneyn lahayd kaalinta furdooyinka ay ku leeyihiin ganacsiga?",
      "options": {
        "a": "kaalinta ay ka qaadaneysaahi waa in alaabta ganacsiga ee dalka imaaneysa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_170",
      "subjectId": "geo",
      "chapterId": "geo_ch6",
      "question": "Kasamee erayadan xog juqraafi:",
      "options": {
        "a": "Cidhiidhiga wadooyinka iyo wasakhowga waa mid ka mid ah dhibaatooyinka",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_171",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Qeex waxa loola jeedo sanaaca?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_172",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Kala sooc noocyada warshadaha?",
      "options": {
        "a": "warshado fudud.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_173",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Tiri kaabayaasha warshadaha?",
      "options": {
        "a": "Alaabta ceeriin(raw materials)",
        "b": "Ilaha tamarta",
        "c": "Helitaanka gaadiid",
        "d": "Saylad(suuq)"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_174",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Tilmaan goobaha warshadaha dunida?",
      "options": {
        "a": "Ruushka.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_175",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Maxaa loola jeedaa tamar?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_176",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Kala sooc ilaha tamarta?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_177",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Kala sooc tilmaamaha tamarta cusboonaata iyo tamarta aan cusboonaan?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_178",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Qeex waxa loola jeedo gaadiid iyo isgaarsiin?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_179",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Kala sooc noocyada gaadiidka?",
      "options": {
        "a": "Gaadiidka cirka.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_180",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Caddie ahmiyadda gaadiidka?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_181",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Kala saar astaamaha noocyada gaadiidka?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_182",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Maxaa loola jeedaa geddis?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_183",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Caddee ahmiyadda geddiska?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_184",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Falanqee waxyaabaha saameeya dhaqdhaqaaqa ganacsiga?",
      "options": {
        "a": "Horumarka cilmiga iyo tiknoolojiyada.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_185",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Qeex maxaa loola jeedaa dalxiis muxuuse muhiim u yahay?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_186",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Falanqee qodobbada horumarka dalxiiska iyo saameynta uu leeyahay?",
      "options": {
        "a": "Baahida aragtida ama fikradda safarrada dalxiiska ee loo safrayo si wadar",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_187",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Tilmaam noocyada dalxiiska?",
      "options": {
        "a": "Dalxiis isirka la xariira.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_188",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Tilmaam dalalka ugu horeeyo ee dalxiiska xaga aduunka?",
      "options": {
        "a": "Ameerika.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_189",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Ku qor calaamadda(√) weedha saxda ah iyo (ꓫ) weedha qaldan:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_190",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Geli ereyo ku habboon meelaha bannaan ee soo socda:",
      "options": {
        "a": "Loodsanaan.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_191",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Sheeg noocyada qiyaasta dhabbaha tareennada laga isticmaalo dunida?",
      "options": {
        "a": "Xarriiq dhexdhexaad ah, fogaanta u dhexeysa biraha waa 143.5cm.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_192",
      "subjectId": "geo",
      "chapterId": "geo_ch7",
      "question": "Isbarbar dhig tamarta cadceedda iyo tamarta biyaha xagga habka ka",
      "options": {
        "a": "tamarta cadceedda waxaa loo isticmaalaa goobaha wareejinta dhulka, taa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_193",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Qeex micnaha sohdin siyaasadeed?",
      "options": {
        "a": "sohdin siyaasadeedku waa muuqaal dunida ku baahsan, waayo dadka ayaa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_194",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sheeg laba astaan oo ay ku kala duwan yihiin sohdin iyo jiid?",
      "options": {
        "a": "Jiid isma beddesho marnaba duruuf walba oo timaado, balse sohdintu waa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_195",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Caddee heerarka qorsheynta sohdin siyaasadeedka?",
      "options": {
        "a": "sohdinta dowladuhu waxay maraan afar heer oo kala ah:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_196",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sheeg shaqooyinka sohdin siyaasadeedka.",
      "options": {
        "a": "shaqooyinka sohdin siyaasadeed waa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_197",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Caddee muhiimadda sohdin siyaasadeedka?",
      "options": {
        "a": "muhiimadda sohdinta siyaasadeed waa nabadgelyada iyo ka hortagidda",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_198",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sheeg wax yaabaha dowladaha xaq u siiyay in ay ilaaliyaan amniga",
      "options": {
        "a": "waxaa xaq usiinayo nidaamka caalamiga ah ee maanta jira iyo heshiisyadii",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_199",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Kala sooc xuduudaha siyaasadeed ee dunida?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_200",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "J- xuduudo dabiici ah:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_201",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Caddee farqiga u dhexeeya xudduudda dabiiciga ah iyo kuwa aadanaha",
      "options": {
        "a": "xudduud dabiici ah waa xudduud ama sohdin lagu saleynayo astayntooda",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_202",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Isbarbar dhig xudduudaha dabiiciga ah qaababkooda kala duwan?",
      "options": {
        "a": "qaabka xudduuda siyaasadeed ee buuraha:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_203",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sheeg tusaalooyin ku saabsan xudduudda siyaasadeed ee dunida?",
      "options": {
        "a": "webiga Riyojaraid ee kala qeybiyo Mareykanka iyo Meksiko, iyo sidoo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_204",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Qeex dhammaan erayada soo socda:",
      "options": {
        "a": "Biyaha dheeriga ah:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_205",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Muuji qiimaha xuduudaha siyaasadeed ay u leeyihiin ilaalinta amniga",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_206",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "J- Shaqada ugu muhiimsan ee sohdinta ayaaba ah nabadgelyada iyo ka",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_207",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Caddee noocyada xadka Soomaaliya iyo dalalka deriska la ah?",
      "options": {
        "a": "■Xadka u dhaxeeya Soomaaliya iyo Jabuuti:",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_208",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Raad raac ku samee halka ay salka ku hayso astaynta xadduuda",
      "options": {
        "a": "waxey salka ku haysaa heshiisyadii ay wada galeen dalalkii",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_209",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "La soo bax xiriirka ka dhexeeya astaynta xudduudda dalka Soomaaliya",
      "options": {
        "a": "waxaa ka dhexeeya xiriir aad u weyn waana sababta keenta dhibaatada",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_210",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Muuji mowqifka dadka Soomaaliyeed ee ku aadan dhulka maqan iyo dib",
      "options": {
        "a": "Mowqifka dadka Soomaaliyeed ee ku aaddan dhulka maqan iyo dib ula",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_211",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Tilmaan baaxadda ama bedka dhulka Soomaaliya ee raacsan dalalka",
      "options": {
        "a": "Baaxadda ama bedka dhulka Soomaaliya ee raacsan Kiinya waa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_212",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Falanqee xiriirka ka dhexeeya isticmaarka iyo jiritaanka mashaakilka",
      "options": {
        "a": "xariir ayaa ka dhexeeya maxaa yeelay Isticmaarku waxa uu asteeyaa",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_213",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Caddee kaalinta juqraafiga siyaasadeed uu ku leeyahay fahamka",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_214",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Falanqee asalka mashaakilka Kashmiir?",
      "options": {
        "a": "Asalka mashaakilka Kashmiir waa asteynta xudduuda iyo qeybintii uu",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_215",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Falanqee qalalaasaha ka taagan xuduudda Soomaaliya ay la leedahay",
      "options": {
        "a": "waa muran ka dhashay xudduud siyaasadeed oo ka dhexeysa dalalkaas iyo",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_216",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Qiimee qaababka ay Soomaaliya ula dhaqantay dalalka deriska la ah ee",
      "options": {
        "a": "Soomaaliya waxa ay qaaday 3 tilaabo si loogu soo celiyo gobollada maqan",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_217",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sheeg noocyada xuduud ay Soomaaliya la leedahay dowladaha dariska la",
      "options": {
        "a": "waa xuduudo ubadan handasi balse dabiicina uu jiro.",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_218",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sidee u aragtaa go’aanka Soomaaliya ay ka qaadatay raadinta gobollada",
      "options": {
        "a": "waxan u arkaa go’aan geesinimo, sharci u hogaansamid iyo fududaasho",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_219",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Soo jeedi xal aad is leedahay waa lagu xallin karaa khilaafka",
      "options": {
        "a": "In ay miiska wadahadal ka iskugu imaadaan Soomaaliya, dalalka deriska,",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_220",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Waa maxay xiriirka ka dhexeeya dadka oo kordho iyo sohdinta",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_221",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Waa maxay xiriirka ka dhexeeya gumeystaha iyo sohdin siyaasadeedka?",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_222",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Waa maxay xiriirka ka dhexeeya horumarka laga gaaray agabka dagaalka",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_223",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sohdin siyaasadeedka xariiqimaha ah waxa uu ku samaysmay heshiis ay",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_224",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Soo ifbixidda hubka casriga ah wuxuu meesha ka saaray aragtida",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_225",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Sohdin siyaasadeedka waa goobo juqraafi oo dherer balac leh.( ꓫ )",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_226",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Kaymaha iyo buuraha waxay ahaan jireen jiido kala qaybiya dowladaha",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_227",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Xudduudda handasiga ah waxay martaa meelo dadku ku firirsanyihiin",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_228",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Dowlad waliba faragelin way ku sameyn kartaa xuriyad umaridda biyo",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_229",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Dowladaha qaarkood waxay sheegtaan qaybo kala duwan oo badaha ah in",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_230",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Biyo goboleed meesha ay ka bilowdaan ayaa u ah dowlad waliba sohdin",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_231",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Waxaa la adeegsadaa khariidada faahfaahsan si loo sawiro sohdinta",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_232",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Jiid waxaa lagu tilmaamaa:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_233",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Heerka kowaad ee qorsheynta sohdinta waa:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "geo_q_234",
      "subjectId": "geo",
      "chapterId": "geo_ch8",
      "question": "Waxyaabaha soo socda waa astaamaha sohdinta siyaasiga ah:",
      "options": {
        "a": "N/A",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_0",
      "subjectId": "islam",
      "chapterId": "islam_ch2",
      "question": "اسيا ص٥اصلخا وًتب ١كيأتلما ،١َٝاطيا ُ٘ٝياعتب سدتفٜٚ ،ٜ٘ٓدب صتعٜ ًِطلما ٕإ -1\n٢ًع تيصْ ١ٜآ ٍٚأ ٌب ،١ًُٝعيا ١طٗٓيا ّاَأ ٠سجع ٠سذس ّاٜلأا َٔ ّٜٛ في ١عٜسػيا ٔهت لم -2\n.)أسق( ٖٞ ًِضٚ ً٘ٝع للها ٢ًص دُلذ اْدٝض\n.عقاٛياب ١طبتسَ اًٝع ٌجبم ت٤اد ،١ٝعقاٚ ١عٜسغ اْٗأ ١َٝلاضلإا ١عٜسػيا اٜاصَ َٔ -3",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_1",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "اب-2\n.يرػًي ٤ارٜإ ٘ٝف",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_2",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "ابًي ٤ارٜإ",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_3",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "ابيا .4\n.١َاٝكيا ّٜٛ ٤ادٗػيا عَ ًِطلما مٚدؿيا ينَلأا سجاتيا .5\n0618012287 / 0616693715",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_4",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "ابيا ٌبكٜ ٕأ",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_5",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "ٝصٛيافًتتخ .١\n)أطخ ( .اٖضهَٚأاصاتمخاٗبٞصٛلمإان٤اٛ",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "islam_q_6",
      "subjectId": "islam",
      "chapterId": "islam_ch10",
      "question": "ٝصٛياحصت .٢\n)أطخ ( .ٍاٛحلأاٌنفيخصاًٛي١ٝصٛياطٛتج .٣\n)حص ( .١نترياحًثٔعزٜظتلاأ٘ب٢صٛلماطٚضؽَٔ .٤\n.) أطخ ( .١ٝصعلما٢ًعينعٌٍٜعفب١ٝصٛياطٛتج .٥\n.ًِعٚ ً٘ٝع للها ٢ًص ٍٛعضيا ٠افٚ",
      "options": {
        "a": "Answer in textbook",
        "b": "N/A",
        "c": "N/A",
        "d": "N/A"
      },
      "correctAnswer": "a",
      "difficultyLevel": "medium"
    },
    {
      "id": "bio_q1",
      "subjectId": "bio",
      "chapterId": "bio_ch1",
      "question": "Placeholder question",
      "options": {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "chem_q1",
      "subjectId": "chem",
      "chapterId": "chem_ch1",
      "question": "Placeholder question",
      "options": {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "phy_q1",
      "subjectId": "phy",
      "chapterId": "phy_ch1",
      "question": "Placeholder question",
      "options": {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    },
    {
      "id": "som_q1",
      "subjectId": "som",
      "chapterId": "som_ch1",
      "question": "Placeholder question",
      "options": {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D"
      },
      "correctAnswer": "a",
      "difficultyLevel": "easy"
    }
  ]
}
''';
