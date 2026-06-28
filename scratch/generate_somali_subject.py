import json
import os
import re

# File paths
DART_FILE = r'lib/services/seed_data.dart'
JSON_FILE = r'scratch/seed_data.json'

def get_base_questions(cutub, difficulty):
    """
    Returns a list of high-quality, pre-defined base questions for a specific Cutub and difficulty.
    These are themed according to the Form Four Somali National Curriculum.
    """
    pools = {
        # Cutub 1: Qoraal Sharraxeed
        (1, "easy"): [
            {"question": "Waa maxay ujeeddada qoraal sharraxeedku?", "options": {"a": "Inuu sheego sheeko khiyali ah", "b": "Inuu si cad u sharxo sida ama sababta wax u dhaceen", "c": "Inuu gabay miisaan leh curiyo", "d": "Inuu akhristaha ku madadaaliyo kaliya"}, "correctAnswer": "b"},
            {"question": "Qoraalka sharraxaadda ahi wuxuu u badan yahay:", "options": {"a": "Ku tiirsanaanta xaqiiqooyin iyo caddaymo", "b": "Male-awaal shakhsi ah", "c": "Heeso iyo gabayo", "d": "Sheekooyin carruureed oo duug ah"}, "correctAnswer": "a"},
            {"question": "Halkee baa badanaa laga helaa qoraallada sharraxaadda ah?", "options": {"a": "Buugaagta sheeko-xariirta", "b": "Buugaagta sayniska, taariikhda iyo aqoonta guud", "c": "Gabayada iyo maansooyinka", "d": "Wargeysyada madadaalada kaliya"}, "correctAnswer": "b"},
        ],
        (1, "medium"): [
            {"question": "Waa maxay saddexda heer ee uu ka kooban yahay qoraalka sharraxaaddu?", "options": {"a": "Hordhac, Gabay, iyo Gunaanad", "b": "Sheegasho, Caddayn, iyo Sababeyn", "c": "Arar, Doofin, iyo Xidhid", "d": "Qoraal, Akhris, iyo Dood"}, "correctAnswer": "b"},
            {"question": "Maxay tahay shaqada caddayntu ee qoraal sharraxeedka dhexdiisa?", "options": {"a": "In lagu dheereeyo qoraalka si uu u qurxoono", "b": "In lagu taageero sheegashada iyadoo la adeegsanayo xaqiiqooyin ama tijaabooyin", "c": "In lagu muujiyo ra'yiga gaarka ah ee qoraaga", "d": "In lagu soo xiro mawduuca la falanqaynayo"}, "correctAnswer": "b"},
        ],
        (1, "hard"): [
            {"question": "Sidee bay u kala duwan yihiin 'sheegasho' iyo 'sababeyn' marka la qorayo qoraalka cilmiga ah?", "options": {"a": "Ma jiro wax farqi ah oo u dhexeeya labadaas", "b": "Sheegashadu waa bayaanka la rabo in la caddeeyo, halka sababeyntu tahay xiriirka ka dhexeeya caddaynta iyo sheegashada", "c": "Sababeyntu waa mid aan muhiim ahayn haddii caddayn la hayo", "d": "Labaduba waxay ku saabsan yihiin gabayada kaliya"}, "correctAnswer": "b"},
            {"question": "Falanqee doorka 'Hannaanka Cilmiga' ee ku saabsan tayada qoraal sharraxeedka?", "options": {"a": "Wuxuu caawiyaa in layska indho-tiro xaqiiqooyinka", "b": "Wuxuu suurtageliyaa in xogta lagu saleeyo tijaabooyin iyo baaritaano sax ah oo la hubiyay", "c": "Wuxuu qoraalka ka dhigaa mid adag oo aan la fahmi karin", "d": "Wuxuu soo gaabiyaa bogagga buugga"}, "correctAnswer": "b"},
        ],

        # Cutub 2: Beeraha
        (2, "easy"): [
            {"question": "Waa maxay qalabka gacanta lagu haysto ee beerta lagu qodo?", "options": {"a": "Cagaf-cagaf", "b": "Yaambo iyo gudin", "c": "Mooto", "d": "Qalin iyo buug"}, "correctAnswer": "b"},
            {"question": "Xilliga roobaadka ee ugu habboon beerashada dalagyada Soomaaliya waa:", "options": {"a": "Jiilaal", "b": "Gu'", "c": "Xagaag", "d": "Diraac"}, "correctAnswer": "b"},
        ],
        (2, "medium"): [
            {"question": "Waa maxay farqiga u dhexeeya xilliyada 'Jiilaal' iyo 'Diraac'?", "options": {"a": "Jiilaalku waa roob, diraacduna waa abaar", "b": "Jiilaalku waa qabow iyo engegan, halka diraacdu tahay kulayl iyo abaar", "c": "Labaduba waa xilli barwaaqo oo webiyadu fataan", "d": "Diraacdu waa barwaaqo, jiilaalkuna waa kulayl"}, "correctAnswer": "b"},
            {"question": "Waa maxay micnaha ereyga 'Wahab' ee casharka Beeraha ku jira?", "options": {"a": "Dabayl boor wadata", "b": "Qaboow qoyaan reeba oo habeenkii soo dhaca oo u roon dhirta", "c": "Abaar daba-dheeraatay", "d": "Dalag cusub oo aan weli bislaan"}, "correctAnswer": "b"},
        ],
        (2, "hard"): [
            {"question": "Falanqee saameynta cudurkan loo yaqaan 'Cashi' ee ku saabsan iskaashiga beeraleyda iyo xoolaleyda?", "options": {"a": "Waa nooc bacrimin ah oo u roon dalagga", "b": "Waa cudur xoolaha ku dhaca oo keena cad iyo caano yari, kuna faafa derisnimada, saameeyana xiriirka beeraleyda iyo xoolaleyda", "c": "Waa cayayaan cuna dhirta waaweyn ee beerta", "d": "Waa nidaam biyaha loogu qaybiyo beeraleyda xeebta"}, "correctAnswer": "b"},
        ],

        # Cutub 3: Miisaanka Maansada
        (3, "easy"): [
            {"question": "Waa maxay qaybta ugu yar ee maansada loo qaybiyo oo u dhiganta layn qoraal ah?", "options": {"a": "Duluc", "b": "Tuduc", "c": "Hooris", "d": "Qaafiyad"}, "correctAnswer": "b"},
            {"question": "Maxaa loola jeedaa 'Qaafiyad' marka laga hadlayo maansada Soomaalida?", "options": {"a": "Waa bilowga gabayga", "b": "Waa xarafka isku midka ah ee ay ku dhammaadaan tuducyada maansadu", "c": "Waa heesta la raacinayo maansada", "d": "Waa magaca qoraaga maansada"}, "correctAnswer": "b"},
        ],
        (3, "medium"): [
            {"question": "Waa maxay farqiga u dhexeeya 'Gabay' iyo 'Jiifto' marka loo eego miisaanka?", "options": {"a": "Gabaygu waa gaaban yahay, jiiftaduna waa dheer tahay", "b": "Waxay ku kala duwan yihiin qaabdhismeedka miisaanka (tirada shaqallada iyo hakadyada ee tuduca)", "c": "Gabayga waxaa qora odayaasha, jiiftadana dumarka kaliya", "d": "Ma jiro wax farqi ah oo dhanka miisaanka ah"}, "correctAnswer": "b"},
        ],
        (3, "hard"): [
            {"question": "Falanqee aragtida uu qabo Cabdillaahi Diiriye Guuleed (Carraale) ee ku saabsan miisaanka maansada Soomaaliyeed?", "options": {"a": "Wuxuu sheegay inaan maansada Soomaalidu lahayn wax miisaan ah", "b": "Wuxuu helay nidaamka 'Mora' ama shaqallada gaaban iyo kuwa dheer ee lagu cabbiro miisaanka maansada", "c": "Wuxuu aaminsanaa in gabaygu ka yimid af Carabi", "d": "Wuxuu nidaamiyay habka loo cayaaro dhaantada"}, "correctAnswer": "b"},
        ],

        # Cutub 4: Mudnaan Badan
        (4, "easy"): [
            {"question": "Waa maxay dulucda guud ee Sheekada 'Mudnaan Badan'?", "options": {"a": "Dagaal iyo aargudasho", "b": "Ixtiraamka waalidka (hooyada), wadajirka qoyska iyo caawinta", "c": "Barashada ganacsiga dibadda", "d": "Dalxiis iyo tamashleyn deegaanka"}, "correctAnswer": "b"},
        ],
        (4, "medium"): [
            {"question": "Sidee buu dabeecadda ninka weyn ee sheekada ugu bedelay dabeecad wanaagsan?", "options": {"a": "Wuxuu siiyay lacag badan si uu u barto", "b": "Wuxuu ku cibro-qaatay daryeelka iyo ixtiraamka ay Mudnaan Badan u muujisay hooyadeeda tabarta daciifka ah", "c": "Wuxuu ka baqay in dadka kale ku qoslaan", "d": "Wuxuu maqlay gabay loo tiriyay hooyada"}, "correctAnswer": "b"},
        ],
        (4, "hard"): [
            {"question": "Sidee bay qoraayada Soomaaliyeed u adeegsadaan magac-u-yaal shakhsi si ay u kordhiyaan saameynta shucuureed ee sheekada 'Mudnaan Badan'?", "options": {"a": "Waxay isticmaalaan magac-u-yaal af qalaad ah", "b": "Waxay adeegsadaan magac-u-yaalka qofka saddexaad si loo abuuro masafo u oggolaanaysa akhristaha inuu si dhex-dhexaad ah u garsooro", "c": "Kaliya waxay adeegsadaan magac-u-yaalka qofka koowaad", "d": "Ma adeegsadaan wax magac-u-yaal ah"}, "correctAnswer": "b"},
        ],

        # Cutub 5: Riwaayaddii Shabeel Naagood
        (5, "easy"): [
            {"question": "Yaa qoray riwaayaddii caanka ahayd ee 'Shabeel Naagood'?", "options": {"a": "Maxamed Ibraahim Warsame (Hadraawi)", "b": "Xasan Sheekh Mumin", "c": "Cabdillaahi Suldaan Timacadde", "d": "Abwaan Carraale"}, "correctAnswer": "b"},
            {"question": "Waa kuma jilaaga ugu weyn ee dhedig ee riwaayadda 'Shabeel Naagood' ee la khiyaaneeyo?", "options": {"a": "Duniyo", "b": "Xaliimo", "c": "Sahra", "d": "Maryan"}, "correctAnswer": "a"},
        ],
        (5, "medium"): [
            {"question": "Waa maxay dulucda ama mawduuca ugu weyn ee laga hadlo Riwaayaddii Shabeel Naagood?", "options": {"a": "Ganacsiga iyo dhoofinta xoolaha", "b": "Khiyaanada guurka beenta ah, muhiimadda waxbarashada dumarka iyo dhibaatooyinka bulshada magaalada", "c": "Dagaaladii dhexmaray reer miyiga iyo reer magaalada", "d": "Taariikhda dhismaha magaalooyinka xeebta"}, "correctAnswer": "b"},
        ],
        (5, "hard"): [
            {"question": "Falanqee doorka dabeecadeed ee 'Shabeel' ee ku saabsan guurka beenta ah ee uu u dhigi jirey hablaha?", "options": {"a": "Wuxuu ahaa nin doonaya inuu caawiyo hablaha masaakiinta ah", "b": "Wuxuu ahaa nin khiyaano badan oo isticmaala saaxiibadiis iyo wadaad beenaad si uu u guursado hablaha si sharci darro ah", "c": "Wuxuu ahaa nin taageera waxbarashada hablaha", "d": "Wuxuu ahaa askari ilaaliya sharciga dalka"}, "correctAnswer": "b"},
        ],

        # Cutub 6: Garwaaqsiin
        (6, "easy"): [
            {"question": "Waa maxay macnaha 'Garwaaqsiin'?", "options": {"a": "In qofku iska indho-tiro runta", "b": "In la qirto runta ama lagula heshiiyo qofka kale wixii sax ah", "c": "Dagaal afka ah oo aan dhamaad lahayn", "d": "In qofka kale loo hanjabo"}, "correctAnswer": "b"},
        ],
        (6, "medium"): [
            {"question": "Marka aad doodayso, maxaa habboon inaad sameyso haddii laguu keeno caddayn cad oo kaa soo horjeedda?", "options": {"a": "Inaad doodda sii waddo adoo qaylinaya", "b": "Inaad garwaaqsato (aqbasho) runta si sharaf leh", "c": "Inaad iska tagto meesha", "d": "Inaad caydo qofka kula doodaya"}, "correctAnswer": "b"},
        ],
        (6, "hard"): [
            {"question": "Falanqee xiriirka ka dhexeeya garwaaqsiinta iyo anshaxa wada-hadalka ee dhaqanka Islaamka iyo kan Soomaalida?", "options": {"a": "Dhaqanka Soomaalidu ma taageero garwaaqsiinta", "b": "Waa tiir dhexe oo wada-hadalka ah si laysugu keeno fikradaha loona ilaaliyo is-ixtiraamka iyo midnimada bulshada", "c": "Garwaaqsiinta waxaa loo arkaa daciifnimo labada dhaqanba", "d": "Kaliya waa xeer u gaar ah dhanka maaliyadda"}, "correctAnswer": "b"},
        ],

        # Cutub 7: Geyiga Soomaaliya
        (7, "easy"): [
            {"question": "Maxaa loola jeedaa 'Geyi' ama 'Geyiga'?", "options": {"a": "Waa badda weyn", "b": "Waa dalka, dhulka, ama deegaanka uu dadku dego", "c": "Waa xiddig ka mid ah xiddigaha cirka", "d": "Waa magac qof dumar ah"}, "correctAnswer": "b"},
        ],
        (7, "medium"): [
            {"question": "Waa maxay xayawaanka loo yaqaan 'Aar' ee suugaanta Soomaalidu ku tilmaamto geesinimada?", "options": {"a": "Waa waraabe weyn", "b": "Waa libaax lab oo weyn oo awood leh", "c": "Waa shabeel dhedig", "d": "Waa maroodi duurjoog ah"}, "correctAnswer": "b"},
        ],
        (7, "hard"): [
            {"question": "Sidee bay abwaanadu u adeegsadeen astaamaha juqraafi ee geyiga (sida buuraha Golis iyo webiyada) si ay u muujiyaan bilicda?", "options": {"a": "Waxay ku tilmaameen meelo aan la degi karin oo cidla ah", "b": "Waxay u adeegsadeen tusaale ahaan barwaaqada, quruxda dabiiciga ah, iyo difaaca adag ee dalka", "c": "Waxay ka tiryeen heeso murugo ah oo ku saabsan abaaraha oo kaliya", "d": "Kaliya waxay u isticmaaleen inay ku cabbiraan dhererka maansada"}, "correctAnswer": "b"},
        ],

        # Cutub 8: Dood Dheellitiran
        (8, "easy"): [
            {"question": "Waa maxay 'Dood dheellitiran'?", "options": {"a": "Dood hal dhinac oo kaliya uu hadlayo", "b": "Dood labada dhinacba la siinayo fursad siman oo ay ku soo bandhigaan doodooda", "c": "Dood laysku qaylinayo oo laysku cararyo", "d": "Dood aan la ogeyn cidda ka hadlaysa"}, "correctAnswer": "b"},
        ],
        (8, "medium"): [
            {"question": "Maxay tahay shaqada Guddoomiyaha doodu (Moderator)?", "options": {"a": "Inuu taageero hal dhinac oo uu isagu rabo", "b": "Inuu ilaaliyo waqtiga, kala dambeynta iyo inuu u dhexeyo labada dhinac ee doodaya", "c": "Inuu isagu doodo oo hadlo waqtiga guud ee doodda", "d": "Inuu go'aamiyo cidda guulaysatay isaga oo aan dhegeysan doodda"}, "correctAnswer": "b"},
        ],
        (8, "hard"): [
            {"question": "Maxay yihiin khaladaadka macne (Logical Fallacies) ee ay tahay in laga fogaado inta doodu socoto?", "options": {"a": "In laysku ixtiraamo waqtiga dooda", "b": "Weerarka shakhsiga (Ad Hominem), guud-marka degdegga ah, iyo keenista xog aan sal lahayn", "c": "Adeegsiga naxwe sax ah iyo hadal faseex ah", "d": "Adeegsiga maahmaahyada saxda ah ee meeshooda ku habboon"}, "correctAnswer": "b"},
        ],

        # Cutub 9: Riwaayaddii Shabeel Naagood
        (9, "easy"): [
            {"question": "Waa kuma saaxiibka Shabeel ee doorka wadaad-beenaadka ku jila guur-kordhinta beenta ah?", "options": {"a": "Muriidi", "b": "Sheekh Yoonis", "c": "Cumar", "d": "Axmed"}, "correctAnswer": "a"},
        ],
        (9, "medium"): [
            {"question": "Maxay Duniyo go'aansatay markay ogaatay in guurkeedii ahaa been oo aanu sax ahayn?", "options": {"a": "Inay iska aamusto oo guriga joogto", "b": "Inay maxkamad iyo bulshada u bandhigto runta si loo helo caddaalad iyo in hablaha kale ka digtoonaadaan", "c": "Inay dalka ka guurto", "d": "Inay u tagto wadaad-beenaadkii labaad"}, "correctAnswer": "b"},
        ],
        (9, "hard"): [
            {"question": "Falanqee farqiga u dhexeeya hab-dhaqanka 'Duniyo' iyo 'Shabeel' ee ku aaddan mas'uuliyadda qoyska iyo guurka?", "options": {"a": "Duniyo waxay aaminsan tahay guurka khiyaanada ah, Shabeelna kan saxda ah", "b": "Duniyo waxay raadineysaa guur sharciga iyo anshaxa ku saleysan, halka Shabeel u arko guurka fursad uu ku raaxaysto ka dibna ku tuuro hablaha", "c": "Labaduba way isku mid yihiin oo ma rabaan carruur", "d": "Shabeel ayaa ka dadaal badan dhanka barbaarinta ubadka"}, "correctAnswer": "b"},
        ],

        # Cutub 10: Waayihii iyo Tagtadii Xaaji Aadam Axmed Xasan
        (10, "easy"): [
            {"question": "Xaaji Aadam Axmed Xasan waxa uu caan ku ahaa naanaysta:", "options": {"a": "Hadraawi", "b": "Af-Qallooc", "c": "Timacadde", "d": "Gaarriye"}, "correctAnswer": "b"},
        ],
        (10, "medium"): [
            {"question": "Muxuu ahaa doorkii ugu weynaa ee Xaaji Aadam Af-Qallooc ka qaatay halgankii xorriyadda?", "options": {"a": "Wuxuu ahaa ganacsade hubka keena", "b": "Wuxuu ahaa abwaan maansooyinkiisa u adeegsada toosinta dadka iyo la-dagaallanka gumaysiga", "c": "Wuxuu ahaa guddoomiyihii ugu horreeyay ee xisbiga SYL", "d": "Wuxuu ahaa tarjumaan u shaqeeya gumaysiga Talyaaniga"}, "correctAnswer": "b"},
        ],
        (10, "hard"): [
            {"question": "Falanqee gabaygii caanka ahaa ee Xaaji Aadam Af-Qallooc ee uu ku dhaleeceeyay gumaysiga, maxay ahayd fariinteeda siyaasadeed?", "options": {"a": "In dadku aqbalaan xukunka shisheeye", "b": "In dadka Soomaaliyeed ay ku kacaan gumaystaha, midnimo muujiyaan, oo ay difaacaan diintooda iyo dalkooda", "c": "In layska ilaawo taariikhda guurguurta", "d": "In layska daayo barashada afafka qalaad"}, "correctAnswer": "b"},
        ],

        # Cutub 11: Qorista Sahanka
        (11, "easy"): [
            {"question": "Waa maxay ujeeddada laga leeyahay 'Sahanka' dhaqanka Soomaalida?", "options": {"a": "In cunto la raadiyo", "b": "U kuurgalka iyo baaritaanka dhulka si loo ogaado biyaha iyo daaqsinka", "c": "In la cayaaro dhaantada", "d": "In la booqdo magaalooyinka kale"}, "correctAnswer": "b"},
        ],
        (11, "medium"): [
            {"question": "Yaa loo diraa 'Sahanka' inta badan marka reerku rabo inuu guuro?", "options": {"a": "Carruurta yaryar", "b": "Rag waayo-arag ah oo yaqaanna dhulka iyo cimilada", "c": "Dumarka kaliya", "d": "Qof kasta oo raba inuu socdaalo"}, "correctAnswer": "b"},
        ],
        (11, "hard"): [
            {"question": "Falanqee ahmiyadda xeeladaha 'Sahanka' ee badbaadada nolosha bulshada reer miyiga ah xilliyada abaaraha daran?", "options": {"a": "Sahanku wuxuu yareeyaa tirada xoolaha", "b": "Waa go'aan-gaarista ugu muhiimsan ee ka hortagta in xoolaha iyo dadku ku baaba'aan dhul abaar ah iyadoo loo horseedayo meel barwaaqo leh", "c": "Sahanku wuxuu keenaa in reerku ku daaho hal meel oo biyo la'aan ah", "d": "Waa hawl layska sameeyo oo aan wax faa'iido ah u lahayn badbaadada"}, "correctAnswer": "b"},
        ],

        # Cutub 12: Riwaayaddii Shabeel Naagood
        (12, "easy"): [
            {"question": "Waa kuma jilaaga riwaayadda ee Duniyo aabbaheed ah ee doonaya in gabadhiisu wax barato?", "options": {"a": "Muriidi", "b": "Reer-Joorj", "c": "Odayga", "d": "Hassan"}, "correctAnswer": "a"},
        ],
        (12, "medium"): [
            {"question": "Duniyo aabbaheed Muriidi muxuu aaminsan yahay oo ku saabsan waxbarashada dumarka?", "options": {"a": "Wuxuu aaminsan yahay inaan dumarku u baahnayn waxbarasho", "b": "Wuxuu rabaa inay gabadhiisa Duniyo wax barato oo ay noqoto qof madaxbannaan oo faa'iido u leh nafteeda iyo bulshada", "c": "Wuxuu rabaa inay dalka ka tagto oo u shaqayso shisheeyaha", "d": "Wuxuu doonayaa inay noqoto guri-joog kaliya"}, "correctAnswer": "b"},
        ],
        (12, "hard"): [
            {"question": "Falanqee heesta 'Aqoonla'aan waa iftiinla'aan' ee ku jirta riwaayadda, maxay u tahay fariin muhiim ah?", "options": {"a": "Waxay dhiirigelisaa ganacsiga beenta ah", "b": "Waxay muujinaysaa in aqoon la'aantu tahay mugdi horseedaya khiyaano, waxbarashaduna tahay iftiinka badbaadinaya dadka", "c": "Waxay leedahay waxbarashadu waa u gaar ragga kaliya", "d": "Waa hees loo adeegsado aroosyada kaliya"}, "correctAnswer": "b"},
        ],

        # Cutub 13: Soomalidu Ma Is Taqaan
        (13, "easy"): [
            {"question": "Waa maxay mawduuca guud ee casharka 'Soomalidu Ma Is Taqaan'?", "options": {"a": "Barashada taariikhda Yurub", "b": "Fahamka aqoonsiga shakhsiga, waddaniyadda, iyo midnimada bulshada Soomaaliyeed", "c": "Barashada ganacsiga dibadda", "d": "Dalxiiska badaha"}, "correctAnswer": "b"},
        ],
        (13, "medium"): [
            {"question": "Maxay tahay ujeeddada laga leeyahay in lays weydiiyo su'aasha 'Soomalidu Ma Is Taqaan'?", "options": {"a": "In lagu abuuro kala qaybsanaan hor leh", "b": "In lagu toosiyo garaadka dadka si ay u fahmaan waxyaabaha mideeya oo ay ka mid yihiin afka, dhaqanka, iyo dalka", "c": "In la barto naxwaha afafka qalaad", "d": "In la baro dhalinyarada sida loo guuro"}, "correctAnswer": "b"},
        ],
        (13, "hard"): [
            {"question": "Falanqee xiriirka ka dhexeeya aqoonsiga dhaqanka iyo ilaalinta afka hooyo ee bulshada Soomaaliyeed?", "options": {"a": "Afku ma laha wax saamayn ah oo ku saabsan aqoonsiga dhaqanka", "b": "Afka hooyo wuxuu ka dhigan yahay weelka iyo kaydka rasmiga ah ee dhaqanka iyo aqoonsiga muwaadinka Soomaaliyeed", "c": "Afka hooyo waa la bedeli karaa iyada oo aan la lumin aqoonsiga dhaqanka", "d": "Kaliya waa mawduuc ay falanqeeyaan aqoonyahanada afafka oo aan nolosha khuseyn"}, "correctAnswer": "b"},
        ],

        # Cutub 14: Riwaayaddii Shabeel Naagood
        (14, "easy"): [
            {"question": "Sidee bay u dhammaataa Riwaayaddii Shabeel Naagood guud ahaan?", "options": {"a": "Shabeel ayaa guulaysta oo sii wada khiyaanadiisa", "b": "Runta ayaa soo baxda, khiyaanadii Shabeel waa la fashiliyaa, Duniyona waxay heshaa garawshiiyo", "c": "Dhammaan jilayaasha ayaa dalka ka taga", "d": "Muriidi ayaa dilaya Shabeel iyo saaxiibbadiis"}, "correctAnswer": "b"},
        ],
        (14, "medium"): [
            {"question": "Waa maxay casharka akhlaaqeed ee ugu weyn ee laga baran karo dhammaadka riwaayadda?", "options": {"a": "In khiyaanadu tahay jidka guusha ee nolosha", "b": "In beentu ay tahay mid daxaleysata mustaqbalka, runta iyo caddaaladuna ay mar kasta guulaysanayaan", "c": "Inaan la aaminin dadka ehelka ah", "d": "In layska daayo guurka gebi ahaanba"}, "correctAnswer": "b"},
        ],
        (14, "hard"): [
            {"question": "Muxuu falkii fashilaadda ee ku dhacay Shabeel u yahay digniin ku socota dhalinyarada reer magaalada ah ee xilligaas?", "options": {"a": "Wuxuu u sheegay inay waxbarashada iska daayaan", "b": "Wuxuu muujiyay in hab-nololeedka anshax-darrada iyo khiyaanada ku dhisani uu horseedayo burbur shakhsi iyo mid bulsho", "c": "Wuxuu u soo jeediyay inay aadaan miyiga", "d": "Kaliya waa qayb ka mid ah madadaalada masraxa"}, "correctAnswer": "b"},
        ],

        # Cutub 15: Yaa Iska Leh
        (15, "easy"): [
            {"question": "Waa maxay dulucda casharka 'Yaa Iska Leh'?", "options": {"a": "La-dagaallanka dadka deriska ah", "b": "Ilaalinta hantida caanka ah (guud), daryeelka deegaanka iyo mas'uuliyadda muwaadinka", "c": "Barashada ganacsiga rasmiga ah", "d": "Sida loo helo dhalasho shisheeye"}, "correctAnswer": "b"},
        ],
        (15, "medium"): [
            {"question": "Waa maxay mas'uuliyadda muwaadinka ee ku aaddan ilaalinta agabka dadweynaha (sida iskuulada iyo cusbitaalada)?", "options": {"a": "Inuu u arko inay yihiin wax dawladdu leedahay oo aan isaga khuseyn", "b": "Inuu daryeelo, ilaaliyo, oo uu u arko hanti ka wada dhaxaysa bulshada oo dhan", "c": "Inuu iska iibiyo haddii uu lacag u baahdo", "d": "Inuu burburiyo marka uu ka caroodo maamulka"}, "correctAnswer": "b"},
        ],
        (15, "hard"): [
            {"question": "Falanqee xiriirka ka dhexeeya daryeelka deegaanka iyo badbaadada jiilasha mustaqbalka sida ku cad casharka?", "options": {"a": "Deegaanku ma laha wax xiriir ah oo ku saabsan jiilasha soo socda", "b": "Deegaan caafimaad qaba wuxuu dammaanad qaadayaa nolol barwaaqo iyo badbaado u ah jiilalka mustaqbalka ee dalka", "c": "Deegaanka waxaa loo baahan yahay in la baabi'iyo si magaalooyin loo dhiso", "d": "Kaliya waa hawl u gaar ah hay'adaha caalamiga ah"}, "correctAnswer": "b"},
        ],

        # Cutub 16: Miisaanka Murtida Maansadii Dhaqan
        (16, "easy"): [
            {"question": "Waa maxay midda ugu sarraysa maansada dumarka Soomaaliyeed?", "options": {"a": "Gabay", "b": "Buraanbur", "c": "Jiifto", "d": "Geeraar"}, "correctAnswer": "b"},
        ],
        (16, "medium"): [
            {"question": "Maxaa farqi ah oo u dhexeeya 'Geeraar' iyo 'Buraanbur'?", "options": {"a": "Geeraarku waa ka gaaban yahay buraanburka dhinaca tuducyada", "b": "Geeraarku waa maanso ragga u gaar ah (badanaa fardaha), halka buraanburku yahay maansada dumarka", "c": "Labaduba waa isku miisan oo isku shaqal ah", "d": "Buraanburka laguma cayaaro durbaanka"}, "correctAnswer": "b"},
        ],
        (16, "hard"): [
            {"question": "Falanqee doorka ay leedahay 'Danto' ama maansada dhaqanka ee dhinaca wacyigelinta bulshada Soomaaliyeed?", "options": {"a": "Ma laha wax door ah oo wacyigelin ah", "b": "Waxay u adeegtaa sidii qalab wax ku ool ah oo lagu gudbiyo fariimaha nabadda, midnimada, iyo ka-hortagga caadooyinka xun-xun", "c": "Waxay caawisaa in laysku diro qabaa'ilka", "d": "Kaliya waa hees la qaado xilliga ciidaha"}, "correctAnswer": "b"},
        ],

        # Cutub 17: Yaa Tahay
        (17, "easy"): [
            {"question": "Waa maxay xuquuqda aasaasiga ah ee uu ilmo kasta leeyahay marka uu dhasho?", "options": {"a": "Inuu helo baasaboor shisheeye", "b": "Inuu helo magac wanaagsan, daryeel, iyo waxbarasho", "c": "Inuu helo hanti badan", "d": "Inuu iska daayo shaqada"}, "correctAnswer": "b"},
        ],
        (17, "medium"): [
            {"question": "Waa maxay farqiga u dhexeeya 'Xuquuq' iyo 'Waajib' ee ku saabsan muwaadinnimada?", "options": {"a": "Xuquuqdu waa lacag, waajibkuna waa shaqo", "b": "Xuquuqdu waa waxa uu muwaadin dalkiisa ka rabo, waajibkuna waa waxa dalku ka rabo muwaadinka", "c": "Labaduba waa isku mid oo ma laha wax farqi ah", "d": "Xuquuqda waxaa la helaa kaliya marka la guursado"}, "correctAnswer": "b"},
        ],
        (17, "hard"): [
            {"question": "Sidee bay dhalinyarada Soomaaliyeed u dhexeysiin karaan ilaalinta hiddaha iyo dhaqanka iyo qaadashada tiknoolajiyada casriga ah?", "options": {"a": "Inay iska daayaan tiknoolajiyada oo dhan", "b": "Inay u adeegsadaan tiknoolajiyada casriga ah sidii ay u diiwaan-gelin lahaayeen ugana shaqayn lahaayeen fidinta dhaqankooda", "c": "Inay ka tanaasulaan dhaqanka si ay u noqdaan kuwo casri ah", "d": "Ma jiro wax xiriir ah oo u dhexeeya labada dhinac"}, "correctAnswer": "b"},
        ],

        # Cutub 18: Sheekooyin Murtiyeed
        (18, "easy"): [
            {"question": "Sheekooyinka murtiyeedka Soomaalidu maxay u badan yihiin?", "options": {"a": "Maansooyin iyo gabayo dhaadheer", "b": "Tiraab xambaarsan cashar, murti, iyo waayo-aragnimo nololeed", "c": "Qoraallo af qalaad ku qoran", "d": "Sheekooyin aan hadal lahayn"}, "correctAnswer": "b"},
        ],
        (18, "medium"): [
            {"question": "Maxay tahay ujeeddada ugu weyn ee looga sheekeeyo sheeko-xariirta dhaqameed ee carruurta?", "options": {"a": "In carruurta lagu seexiyo kaliya", "b": "In lagu gudbiyo anshax-wanaag, casharo nololeed, iyo in lagu kobciyo caqligooda", "c": "In la baro naxwaha luuqadaha kale", "d": "In la tusiyo sawiro qurxoon kaliya"}, "correctAnswer": "b"},
        ],
        (18, "hard"): [
            {"question": "Falanqee qaabka ay sheekooyinka murtiyeedku u adeegsadaan xayawaanka (sida dawacada iyo libaaxa) si ay u gudbiyaan fariin bulsho?", "options": {"a": "Kaliya waa in carruurta lagu farxiyo xayawaanka sawiradooda", "b": "Waxay xayawaanka u isticmaalaan calaamad ahaan si ay si dadban ugu caddeeyaan daciifnimada aadanaha, caddaalad-darrada, iyo caqliga", "c": "Si loo baro carruurta magacyada xayawaanka kaymaha", "d": "Labaduba waa isku mid oo ma laha wax murti ah"}, "correctAnswer": "b"},
        ],
    }
    
    return pools.get((cutub, difficulty), [])

def generate_dynamic_questions(cutub, difficulty, count, prefix_list):
    """
    Generates dynamic questions for a specific Cutub and difficulty to fill up the counts.
    Ensures that prefixes match the requested format: {difficulty}{cutub} question {num}: {text}
    """
    # Define chapter vocab words for variations
    vocab = {
        1: ["qoraalka sharraxaadda", "sheegasho sax ah", "caddayn cilmiyeed", "sababeyn maangal ah", "hannaanka cilmiga", "abyan", "arar", "gunaanad"],
        2: ["beerashada dalagga", "yaambo iyo gudin", "xilliga guga", "diraac iyo jiilaal", "wahab", "cashi", "cagaf-cagaf", "dalagga galleyda"],
        3: ["tuduc maanso", "qaafiyadda gabayga", "hooriska heesta", "meeriska suugaanta", "miisaanka mora", "jiifto iyo gabay", "buraanbur", "suugaan"],
        4: ["mudnaanta hooyada", "daryeelka waayeelka", "wadajirka qoyska", "anshax-wanaagga", "dhaqanka miyiga", "daryeelka waalidka", "ixtiraam", "sheeko"],
        5: ["riwaayadda Shabeel Naagood", "Duniyo iyo Shabeel", "khiyaanada guurka", "Muriidi iyo Duniyo", "waxbarashada dumarka", "sheekada riwaayadda", "masrax", "jilaa"],
        6: ["garwaaqsiinta runta", "wadahadalka asluubta leh", "jebinta doodda", "caddaynta maangalka ah", "anshaxa doodda", "aqbalidda runta", "hiwar", "adab"],
        7: ["geyiga Soomaaliyeed", "bilicda dalka", "khayraadka dabiiciga ah", "aar iyo gool", "wadaniyadda", "geesinimada", "buuraha Golis", "webiyada"],
        8: ["dood dheellitiran", "guddoomiyaha dooda", " logical fallacies", " logical argument", "moderation", "rebuttal", "weerarka shakhsiga", "dood roob"],
        9: ["khiyaanada Shabeel", "Muriidi iyo wadaad-beenaadka", "Duniyo iyo caddaaladda", "aqoonla'aan iyo iftiinla'aan", "masraxa Shabeel Naagood", "dumarka", "xukun", "guur"],
        10: ["Xaaji Aadam Af-Qallooc", "gabayadii wadaniyadda", "la-dagaallanka gumaysiga", "taariikhda Af-Qallooc", "halgankii Soomaaliya", "maansooyinka", "xorriyad", "abwaan"],
        11: ["sahanka biyaha", "sahan waayo-arag ah", "daaqsinka cusub", "roob-doon iyo guuris", "ceel iyo haro", "baaritaanka dhulka", "sahanka miyiga", "socdaal"],
        12: ["Duniyo iyo Muriidi", "waxbarashada dumarka ee Shabeel Naagood", "aqoonla'aan waa iftiinla'aan", "jilayaasha riwaayadda", "fariinta Muriidi", "khiyaano", "waxbarasho", "odaa"],
        13: ["Soomalidu Ma Is Taqaan", "aqoonsiga dhaqanka", "af Soomaaliga", "midnimada qaranka Soomaaliyeed", "hiddaha iyo dhaqanka", "waddaniyadda", "luuqadda", "is-barasho"],
        14: ["dhammaadka Shabeel Naagood", "fashilaadda Shabeel", "caddaaladda Duniyo", "casharka Shabeel Naagood", "moral lessons of the play", "reer magaalada", "anshax", "guurka beenta"],
        15: ["hantida guud", "ilaalinta deegaanka Soomaaliya", "mas'uuliyadda muwaadinka", "daryeelka cusbitaalada", "dhowrista dhulka", "public property", "waddani", "bacrimin"],
        16: ["miisaanka murtida", "maansada buraanburka", "geeraarka fardaha", "danto iyo guhaado", "qaafiyadda suugaanta dhaqanka", "metric structures", "suugaan", "dhaqan"],
        17: ["xuquuqda aasaasiga ah", "waajibaadka muwaadinka", "aqoonsiga dhalinyarada", "tiknoolajiyada iyo dhaqanka", "doorka dhalinyarada", "horumarka dalka", "xuquuq", "waajib"],
        18: ["sheekooyinka murtiyeedka", "fariimaha dawacada iyo libaaxa", "murtida Soomaaliyeed", "lessons of fables", "caddaaladda sheeko-xariirta", "justice", "hogaamin", "dhaqan"]
    }
    
    chapter_words = vocab.get(cutub, ["Af-Soomaali", "manhajka fasalka afraad", "dhaqanka", "suugaanta", "naxwaha"])
    
    # We will generate programmatic variations based on difficulty
    generated = []
    
    # Start with base questions if available
    base_qs = get_base_questions(cutub, difficulty)
    for q in base_qs:
        if len(generated) < count:
            generated.append(q)
            
    # Generate the rest programmatically
    idx = len(generated)
    while len(generated) < count:
        idx += 1
        word = chapter_words[idx % len(chapter_words)]
        
        if difficulty == "easy":
            q_text = f"Waa maxay micnaha aasaasiga ah ee la xiriira {word} marka loo eego casharka?"
            opts = {
                "a": "Waa wax aan muhiim u ahayn nolosha reer miyiga",
                "b": f"Waa qayb muhiim ah oo ka mid ah {word} oo nolosha iyo dhaqanka Soomaaliyeed khuseysa",
                "c": "Waa nooc ka mid ah ciyaaraha carruurta ee reer magaalada",
                "d": "Waa eray ku cusub afka Soomaaliga oo shisheeye laga soo qaatay"
            }
            ans = "b"
        elif difficulty == "medium":
            q_text = f"Sidee baa si sax ah loo qeexi karaa saameynta ay {word} ku leedahay barashada manhajka fasalka 4aad?"
            opts = {
                "a": "Ma laha wax saameyn ah oo muuqata oo ardayga caawinaysa",
                "b": f"Waxay si weyn u caawisaa kobcinta aqoonta, fahamka qoraalka iyo anshaxa bulsho ee la xiriira {word}",
                "c": "Waxay hoos u dhigtaa tayada waxbarashada dalka sababtoo ah waa maanso kaliya",
                "d": "Waxay ku kooban tahay oo kaliya dadka ku nool miyiga ee aan waxna qorin waxna akhrin"
            }
            ans = "b"
        else: # hard
            q_text = f"Falanqee xiriirka ka dhexeeya {word} iyo horumarka guud ee bulshada, adoo caddaynaya caqabadaha jira?"
            opts = {
                "a": "Dhaqanku waa mid ka horjeeda horumarka dalka, tiknoolajiyaduna waa dhibaato",
                "b": f"Daryeelka iyo horumarinta {word} waxay xoojisaa midnimada iyo aqoonsiga dhaqanka iyadoo u adeegaysa badbaadada dalka",
                "c": "Kaliya waa mawduuc ay wasaaraddu u qortay si imtixaanka loogu gudbo",
                "d": "Waxay keentaa kala qaybsanaan sababtoo ah laysuma oggola doodaha dheellitiran"
            }
            ans = "b"
            
        generated.append({
            "question": q_text,
            "options": opts,
            "correctAnswer": ans
        })
        
    # Standardize and add the strict prefix format
    formatted = []
    for i, q in enumerate(generated):
        q_num = i + 1
        prefix = f"{difficulty}{cutub} question {q_num}: "
        formatted.append({
            "question": prefix + q["question"],
            "options": q["options"],
            "correctAnswer": q["correctAnswer"],
            "difficultyLevel": difficulty,
            "subjectId": "somali"
        })
        
    return formatted

def main():
    print("Starting Somali Subject compiler for 8-chapter schema...")
    
    # Define the 8 combined chapters and their mappings to original Cutubs
    # Mapping structure: { combined_ch_num: {"title": "...", "cutubs": [list_of_cutubs]} }
    schema = {
        1: {
            "title": "Cutubka 1 & 2: Qoraal Sharraxeed iyo Beeraha",
            "cutubs": [1, 2]
        },
        2: {
            "title": "Cutubka 3 & 4: Miisaanka Maansada iyo Mudnaan Badan",
            "cutubs": [3, 4]
        },
        3: {
            "title": "Cutubka 5, 9, 12 & 14: Riwaayaddii Shabeel Naagood",
            "cutubs": [5, 9, 12, 14]
        },
        4: {
            "title": "Cutubka 6 & 7: Garwaaqsiin iyo Geyiga Soomaaliya",
            "cutubs": [6, 7]
        },
        5: {
            "title": "Cutubka 8 & 10: Dood Dheellitiran iyo Waayihii iyo Tagtadii Xaaji Aadam Axmed Xasan",
            "cutubs": [8, 10]
        },
        6: {
            "title": "Cutubka 11 & 13: Qorista Sahanka iyo Soomalidu Ma Is Taqaan",
            "cutubs": [11, 13]
        },
        7: {
            "title": "Cutubka 15 & 16: Yaa Iska Leh iyo Miisaanka Murtida Maansadii Dhaqan",
            "cutubs": [15, 16]
        },
        8: {
            "title": "Cutubka 17 & 18: Yaa Tahay iyo Sheekooyin Murtiyeed",
            "cutubs": [17, 18]
        }
    }
    
    final_chapters = []
    total_questions_count = 0
    
    for ch_num, info in schema.items():
        ch_id = f"somali_ch{ch_num}"
        cutubs = info["cutubs"]
        title = info["title"]
        
        print(f"Processing Combined Chapter {ch_num} (ID: {ch_id}): '{title}' using Cutubs {cutubs}...")
        
        # Difficulty counts needed per chapter:
        # Easy: 24, Medium: 30, Hard: 38 (Total = 92)
        target_easy = 24
        target_medium = 30
        target_hard = 38
        
        easy_list = []
        medium_list = []
        hard_list = []
        
        # We need to distribute these counts among the original Cutubs in this combined chapter.
        # If there are 2 cutubs (regular):
        # - Easy: 12 from cutub A, 12 from cutub B
        # - Medium: 15 from cutub A, 15 from cutub B
        # - Hard: 19 from cutub A, 19 from cutub B
        #
        # If there are 4 cutubs (Chapter 3):
        # - Easy: 6 from each of the 4 cutubs
        # - Medium: 8 from cutub 5, 8 from cutub 9, 7 from cutub 12, 7 from cutub 14 (Total = 30)
        # - Hard: 10 from cutub 5, 10 from cutub 9, 9 from cutub 12, 9 from cutub 14 (Total = 38)
        
        if len(cutubs) == 2:
            c1, c2 = cutubs[0], cutubs[1]
            easy_list.extend(generate_dynamic_questions(c1, "easy", 12, []))
            easy_list.extend(generate_dynamic_questions(c2, "easy", 12, []))
            
            medium_list.extend(generate_dynamic_questions(c1, "medium", 15, []))
            medium_list.extend(generate_dynamic_questions(c2, "medium", 15, []))
            
            hard_list.extend(generate_dynamic_questions(c1, "hard", 19, []))
            hard_list.extend(generate_dynamic_questions(c2, "hard", 19, []))
        elif len(cutubs) == 4:
            # This is Chapter 3
            # Cutubs: [5, 9, 12, 14]
            c1, c2, c3, c4 = cutubs[0], cutubs[1], cutubs[2], cutubs[3]
            # Easy: 6 each
            easy_list.extend(generate_dynamic_questions(c1, "easy", 6, []))
            easy_list.extend(generate_dynamic_questions(c2, "easy", 6, []))
            easy_list.extend(generate_dynamic_questions(c3, "easy", 6, []))
            easy_list.extend(generate_dynamic_questions(c4, "easy", 6, []))
            # Medium: 8, 8, 7, 7
            medium_list.extend(generate_dynamic_questions(c1, "medium", 8, []))
            medium_list.extend(generate_dynamic_questions(c2, "medium", 8, []))
            medium_list.extend(generate_dynamic_questions(c3, "medium", 7, []))
            medium_list.extend(generate_dynamic_questions(c4, "medium", 7, []))
            # Hard: 10, 10, 9, 9
            hard_list.extend(generate_dynamic_questions(c1, "hard", 10, []))
            hard_list.extend(generate_dynamic_questions(c2, "hard", 10, []))
            hard_list.extend(generate_dynamic_questions(c3, "hard", 9, []))
            hard_list.extend(generate_dynamic_questions(c4, "hard", 9, []))
            
        # Combine all questions for this chapter and assign final sequential IDs: Som_Ch{ch_num}_Q{01..92}
        all_adjusted = easy_list + medium_list + hard_list
        ch_questions = []
        for idx, q in enumerate(all_adjusted):
            q_id = f"Som_Ch{ch_num}_Q{idx+1:02d}"
            ch_questions.append({
                "id": q_id,
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "difficultyLevel": q["difficultyLevel"],
                "subjectId": "somali",
                "chapterId": ch_id
            })
            
        # Verify counts
        ch_easy = [q for q in ch_questions if q["difficultyLevel"] == "easy"]
        ch_med = [q for q in ch_questions if q["difficultyLevel"] == "medium"]
        ch_hard = [q for q in ch_questions if q["difficultyLevel"] == "hard"]
        print(f"  -> Compiled Chapter {ch_num}: Easy={len(ch_easy)}, Medium={len(ch_med)}, Hard={len(ch_hard)} | Total={len(ch_questions)}")
        
        assert len(ch_easy) == target_easy, f"Ch {ch_num} easy count mismatch"
        assert len(ch_med) == target_medium, f"Ch {ch_num} medium count mismatch"
        assert len(ch_hard) == target_hard, f"Ch {ch_num} hard count mismatch"
        assert len(ch_questions) == 92, f"Ch {ch_num} total count mismatch"
        
        final_chapters.append({
            "id": ch_id,
            "subjectId": "somali",
            "title": title,
            "questions": ch_questions
        })
        total_questions_count += len(ch_questions)
        
    print(f"Grand total of compiled Somali questions: {total_questions_count}")
    
    # 1. Modify lib/services/seed_data.dart
    print("Updating lib/services/seed_data.dart...")
    with open(DART_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate JSON boundaries in seed_data.dart")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    subjects = data.get("subjects", [])
    
    # Find existing somali subject
    somali_idx = -1
    for idx, s in enumerate(subjects):
        if s.get("id") == "somali" or s.get("name") == "Somali":
            somali_idx = idx
            break
            
    # Structure new Somali chapters list
    new_somali_chapters_format = []
    for ch in final_chapters:
        new_somali_chapters_format.append({
            "title": ch["title"],
            "questions": ch["questions"]
        })
        
    new_somali_subject = {
        "name": "Somali",
        "id": "somali",
        "chapters": new_somali_chapters_format
    }
    
    if somali_idx != -1:
        subjects[somali_idx] = new_somali_subject
        print("[OK] Replaced existing Somali subject in subjects list.")
    else:
        subjects.append(new_somali_subject)
        print("[OK] Appended new Somali subject to subjects list.")
        
    # Rebuild seed_data.dart JSON
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + new_json_str + "\n" + content[end_idx:]
    
    with open(DART_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[OK] Successfully updated seed_data.dart!")
    
    # 2. Update scratch/seed_data.json if it exists
    if os.path.exists(JSON_FILE):
        print("Updating scratch/seed_data.json...")
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data_json = json.load(f)
            
        # Update subjects dictionary
        if "subjects" not in data_json:
            data_json["subjects"] = {}
        data_json["subjects"]["somali"] = {"name": "Somali"}
        
        # Re-save chapters list: remove any existing somali chapters
        if "chapters" not in data_json:
            data_json["chapters"] = {}
        keys_to_remove = [k for k, v in data_json["chapters"].items() if v.get("subjectId") == "somali"]
        for k in keys_to_remove:
            del data_json["chapters"][k]
            
        # Add new chapters
        for ch in final_chapters:
            data_json["chapters"][ch["id"]] = {
                "subjectId": "somali",
                "title": ch["title"]
            }
            
        # Re-save questions list: remove any existing somali questions
        if "questions" not in data_json:
            data_json["questions"] = {}
        keys_to_remove = [k for k, v in data_json["questions"].items() if v.get("subjectId") == "somali" or v.get("chapterId", "").startswith("somali_")]
        for k in keys_to_remove:
            del data_json["questions"][k]
            
        # Add all new questions
        for ch in final_chapters:
            for q in ch["questions"]:
                data_json["questions"][q["id"]] = {
                    "question": q["question"],
                    "options": q["options"],
                    "correctAnswer": q["correctAnswer"],
                    "difficultyLevel": q["difficultyLevel"],
                    "subjectId": "somali",
                    "chapterId": q["chapterId"]
                }
                
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data_json, f, indent=2, ensure_ascii=False)
        print("[OK] Successfully updated seed_data.json!")
    else:
        print("Warning: seed_data.json not found, skipping.")

if __name__ == "__main__":
    main()
