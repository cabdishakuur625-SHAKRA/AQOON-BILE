import json
import re
import os

DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'

new_questions_raw = [
  { "id": 1, "question": "Waa maxay micnaha sohdin siyaasadeed?", "options": { "a": "Waa muuqaal dabiici ah oo aan isbeddelin", "b": "Waa muuqaal dadku sameeyeen si ay u ilaaliyaan danahooda", "c": "Waa dhul aan cidna lahayn", "d": "Waa buuro iyo bado kaliya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 2, "question": "Imisa heer ayay martaa qorsheynta sohdinta siyaasadeed?", "options": { "a": "2 heer", "b": "3 heer", "c": "4 heer", "d": "5 heer" }, "correctAnswer": "c", "difficultyLevel": "easy" },
  { "id": 3, "question": "Waa ku bama heerka koowaad ee qorsheynta sohdinta?", "options": { "a": "Heerka maamulidda", "b": "Heerka qeexidda iyo qorsheynta", "c": "Heerka go’aaminta", "d": "Heerka tilmaamidda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 4, "question": "Waa ku bama mid ka mid ah shaqooyinka sohdinta siyaasadeed?", "options": { "a": "Ilaalinta amniga", "b": "Kordhinta roobka", "c": "Dhisidda buuraha", "d": "Abuurista webiyada" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 5, "question": "Waa maxay farqiga u dhexeeya sohdinta iyo jiidda (frontier)?", "options": { "a": "Jiiddu waa dabiici ismana beddesho, sohdintuna waa la beddeli karaa", "b": "Sohdintu waa dabiici marnaba ma baaba'do", "c": "Jiiddu waa xariiq yar oo khariidadda ku yaal", "d": "Ma lahan wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 6, "question": "Waa ku bama tusaale ka mid ah xudduudda dabiiciga ah?", "options": { "a": "Xudduud handasi ah", "b": "Xudduud buuro ah", "c": "Xudduud ilbaxnimo", "d": "Xariijimo toosan" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 7, "question": "Webiga Riyojaraid wuxuu kala qeybiyaa dalalkee?", "options": { "a": "Soomaaliya iyo Itoobiya", "b": "Mareykanka iyo Meksiko", "c": "Faransiiska iyo Isbaanishka", "d": "Ingiriiska iyo Jarmalka" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 8, "question": "Buuraha Baraanis waxay u dhexeeyaan dalalkee?", "options": { "a": "Faransiiska iyo Isbaanishka", "b": "Kenya iyo Soomaaliya", "c": "Ruushka iyo Shiinaha", "d": "Mareykanka iyo Kanada" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 9, "question": "Waa maxay dhererka xadka u dhexeeya Soomaaliya iyo Jabuuti?", "options": { "a": "58km", "b": "678km", "c": "1590km", "d": "2000km" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 10, "question": "Waa ku bama xadka ugu dheer ee Soomaaliya ay la leedahay dalalka deriska ah?", "options": { "a": "Xadka Jabuuti", "b": "Xadka Itoobiya", "c": "Xadka Kiinya", "d": "Xadka badda" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 11, "question": "Maxaa loola jeedaa 'Biyaha Caalamiga ah'?", "options": { "a": "Biyo u furan dhamaan dalalka dunida", "b": "Biyo ay hal dowlad leedahay", "c": "Biyaha webiyada", "d": "Biyaha harooyinka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 12, "question": "Xadka u dhexeeya Soomaaliya iyo Kiinya dhererkiisu waa?", "options": { "a": "58km", "b": "678km", "c": "1590km", "d": "100km" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 13, "question": "Waa maxay 'Raso Qaaradeed'?", "options": { "a": "Fidsanaanta dhulka badda ka hooseeya", "b": "Buuraha ugu dhaadheer", "c": "Webiyada gudaha dalka", "d": "Hawada sare" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 14, "question": "Heerkee baa la adeegsadaa khariidadda faahfaahsan si sohdinta loo sawiro?", "options": { "a": "Heerka qeexidda", "b": "Heerka tilmaamidda", "c": "Heerka maamulidda", "d": "Heerka go'aaminta" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 15, "question": "Xuduudda handasiga ah maxay martaa?", "options": { "a": "Meelaha khayraadku ku yar yahay dadkuna ku firirsan yihiin", "b": "Meelaha webiyada leh", "c": "Meelaha buuraha leh", "d": "Meelaha dadku ku badan yihiin" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 16, "question": "Shaqada ugu muhiimsan ee sohdinta waa?", "options": { "a": "Nabadgelyada iyo ka hortagidda xadgudubka", "b": "Beeraha", "c": "Ganacsiga miyiga", "d": "Dhisidda guryaha" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 17, "question": "Biyaha dheeriga ah (Contiguous zone) fogaantoodu waa imisa mayl?", "options": { "a": "12 mayl", "b": "24 mayl", "c": "200 mayl", "d": "5 mayl" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 18, "question": "Waa ku bama mid ka mid ah xuduudaha aadanaha la xiriira?", "options": { "a": "Xudduud wabi ah", "b": "Xudduud handasi ah", "c": "Xudduud bad ah", "d": "Xudduud haro ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 19, "question": "Xadka Soomaaliya iyo Itoobiya waa noocee?", "options": { "a": "Xudduud wabi ah", "b": "Xudduud handasi ah", "c": "Xudduud buuro ah", "d": "Xudduud dabiici ah" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 20, "question": "Sohdin siyaasadeedka xariiqimaha ah waxaa lagu sameeyaa?", "options": { "a": "Heshiis dhex mara dowladaha", "b": "Dagaal kaliya", "c": "Roobka", "d": "Dhulgariirka" }, "correctAnswer": "a", "difficultyLevel": "easy" },
  { "id": 21, "question": "Waa ku bama dalka Soomaaliya xadka la wadaaga dhanka Koonfureed?", "options": { "a": "Itoobiya", "b": "Kiinya", "c": "Jabuuti", "d": "Yemen" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 22, "question": "Xadka Soomaaliya iyo Jabuuti waxaa asteeyay dalalkee?", "options": { "a": "Talyaani iyo Ingiriis", "b": "Faransiis iyo Ingiriis", "c": "Talyaani iyo Faransiis", "d": "Itoobiya iyo Kiinya" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 23, "question": "Biyaha gudaha (Internal waters) waxay ku yaallaan?", "options": { "a": "Bannaanka badda", "b": "Meel ka sarreysa dhul engegan dalka", "c": "Biyaha caalamiga ah dhexdiisa", "d": "Hawada sare" }, "correctAnswer": "b", "difficultyLevel": "easy" },
  { "id": 24, "question": "Maxay tahay sababta sohdintu u tahay mid isbeddeli karta mar marna u baabi’i karta?", "options": { "a": "Sababtoo ah waa dabiici", "b": "Sababtoo ah waa muuqaal sharci iyo siyaasadeed oo dadku sameeyeen", "c": "Sababtoo ah buuraha ayaa duma", "d": "Sababtoo ah biyaha ayaa qalala" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 25, "question": "Kala saar xudduudda dabiiciga ah iyo tan aadanaha la xiriirta?", "options": { "a": "Dabiiciga waxaa loo adeegsadaa muuqaallo sida buuro, tan aadanahana waa xarriijimo handasi ah", "b": "Dabiiciga waa xarriijimo toosan", "c": "Aadanaha la xiriirta waa webiyada", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 26, "question": "Sidee bay buuruhu u noqdaan xudduud siyaasadeed?", "options": { "a": "Ayadoo la raacayo khadka kala qeybinta biyaha ee figta buurta", "b": "Ayadoo buurta laga dhisayo gidaar", "c": "Ayadoo dadka laga saarayo buurta", "d": "Ayadoo buurta la rinjiyeynayo" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 27, "question": "Waa maxay ujeeddada heerka maamulidda xadka?", "options": { "a": "In la sawiro khariidadda kaliya", "b": "In la ilaaliyo sohdinta lagana dhex shaqeysiiyo qawaaniinta xadka", "c": "In buuraha la qoro magacyo", "d": "In webiga la xiro" }, "correctAnswer": "b", "difficultyLevel": "medium" },
  { "id": 28, "question": "Maxaa xaq u siinaya dowladaha inay ilaaliyaan amniga qarankooda?", "options": { "a": "Nidaamka caalamiga ah iyo heshiisyada ay galeen", "b": "Awooddooda ciidan kaliya", "c": "Sababtoo ah dhulku waa weyn yahay", "d": "Ururrada diimeed" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 29, "question": "Maxaa loola jeedaa 'Biyo Goboleed' (Territorial waters)?", "options": { "a": "Jiid badeedka fidsan laga bilaabo xeebta ilaa xadka badda ee dowlada", "b": "Webiyada dalka dhex mara", "c": "Harooyinka ku yaal caasimadda", "d": "Biyaha u furan dunida oo dhan" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 30, "question": "Falanqee xiriirka ka dhexeeya isticmaarka iyo dhibaatooyinka xadka ee Soomaaliya?", "options": { "a": "Isticmaarku wuxuu asteeyay xudduudo aan tixgelin juqraafiga iyo bulshada", "b": "Isticmaarku wuxuu dhisay waddooyin nabad ah", "c": "Isticmaarku wuxuu mideeyay dadka Soomaaliyeed", "d": "Ma jiro wax xiriir ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 31, "question": "Sidee bay sohdintu u xaddiddaa qaanuunka lagu qaadayo qofka?", "options": { "a": "Qofka waxaa lagu qaadaa qaanuunka dalka uu sohdintiisa ku jiro", "b": "Qofka qaanuun laguma qaado xadka", "c": "Qaanuunka caalamiga ah ayaa qof walba xukuma", "d": "Sohdintu ma saameyso qaanuunka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 32, "question": "Xadka Soomaaliya iyo Kiinya asal ahaan wuxuu ku saleysan yahay heshiiskii?", "options": { "a": "1924 CD ee dhex maray Ingiriiska iIyo Talyaaniga", "b": "1888 CD ee Faransiiska iyo Ingiriiska", "c": "1960 CD ee madaxbannaanida", "d": "1887 CD ee Itoobiya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 33, "question": "Maxay tahay sababta sohdinta handasiga ah loogu isticmaalo meelaha khayraadku ku yar yahay?", "options": { "a": "Sababtoo ah way fududahay in xarriijimo toosan laga sawiro meel bannaan", "b": "Sababtoo ah dadka ayaa jecel", "c": "Sababtoo ah webiyo ayaa ku yaal", "d": "Sababtoo ah waa xadka ugu adag" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 34, "question": "Waa maxay ahmiyadda xudduudda wabiyaasha leh?", "options": { "a": "Waxay raacdaa khadka dhexe ama qoto dheerida marsada ee webiga", "b": "Waxay joojisaa biyaha", "c": "Waxay kordhisaa kaluumeysiga dowlada kaliya", "d": "Webigu ma noqon karo xuduud" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 35, "question": "Maxaa loola jeedaa 'Juqraafiga Siyaasadda' sida uu qabo casharka?", "options": { "a": "Waa qayb ka mid ah juqraafiga Aadanaha oo baaraya geeddi-socodka siyaasadeed iyo saameyntiisa juqraafi", "b": "Waa barashada dhirta iyo xayawaanka", "c": "Waa barashada cimilada dunida", "d": "Waa dhismaha buuraha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 36, "question": "Muxuu qabaa Mowqifka dadka Soomaaliyeed ee ku aaddan dhulka maqan?", "options": { "a": "Waa mid ka go'an in dib loo soo celiyo dadka iyo dhulkaas", "b": "Waa mid la iska illoobay", "c": "Waa mid ku xiran go'aanka Kiinya kaliya", "d": "Waa mid ku xiran go'aanka gumeystaha" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 37, "question": "Imisa ayay tahay baaxadda dhulka Soomaaliya ee raacsan Itoobiya?", "options": { "a": "153,600 km2", "b": "128,000 km2", "c": "58,000 km2", "d": "200,000 km2" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 38, "question": "Waa ku bama mid ka mid ah tillaabooyinkii ay dowladda Soomaaliya u martay raadinta dhulka maqan?", "options": { "a": "Tillaabo sharci, diblimaasiyadeed iyo mid ciidan", "b": "Tillaabo ganacsi kaliya", "c": "Tillaabo ay ku weydiisatay gumeystaha inuu ku soo laabto", "d": "Ma jirin wax tillaabo ah oo la qaaday" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 39, "question": "Maxay 'Biyaha Dhexdhexaadka ah' u muhiim yihiin?", "options": { "a": "Waa aagga ku sii dheggan biyaha dhameystirka ee dhanka badda", "b": "Waa meesha laga cabo biyaha", "c": "Waa webiyada dalka dhexdiisa", "d": "Waa biyaha ugu qotada dheer" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 40, "question": "Maxaa dhacay sanadkii 1948 CD oo xiriir la leh xadka Soomaaliya iyo Itoobiya?", "options": { "a": "Ingiriiska ayaa aqoonsaday in dhulkaas uu ka tirsan yahay Itoobiya", "b": "Talyaaniga ayaa qabsaday Soomaaliya", "c": "Soomaaliya ayaa xorowday", "d": "Dagaalkii labaad ee dunida ayaa dhamaaday" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 41, "question": "Sidee bay tirada dadka oo kordha u saameysaa sohdinta?", "options": { "a": "Waxay horseeddaa in dowladda sohdinteeda ay fiddo", "b": "Waxay yareysaa dhulka dowlada", "c": "Ma lahan wax saameyn ah", "d": "Waxay keentaa in sohdintu baaba'do" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 42, "question": "Maxay tahay sababta hubka casriga ah u saameeyay aragtida 'sohdinta amaanka ah'?", "options": { "a": "Sababtoo ah wuxuu ka gudbi karaa xudduudaha iyadoo aan ciidan dhulka la soo marsiin", "b": "Sababtoo ah hubka ayaa xadka lagu iibiyaa", "c": "Sababtoo ah buuraha ayuu dumiyaa", "d": "Ma jiro wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 43, "question": "Kala saar 'heerka go’aaminta' iyo 'heerka tilmaamidda'?", "options": { "a": "Go'aaminta waa xadeynta, tilmaamidduna waa sawiridda khariidadda iyo saaridda calaamadaha", "b": "Labaduba waa isku mid", "c": "Tilmaamidda ayaa ka horreysa go'aaminta", "d": "Go'aaminta waa maamulka xadka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 44, "question": "Biyaha gudaha (Internal waters) maxay ka kooban yihiin?", "options": { "a": "Harooyinka xeebaha, afaafyada webiyada iyo khooriyada", "b": "Badaha fog", "c": "Biyo mareenka tareennada", "d": "Roobka kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 45, "question": "Muxuu ahaa heshiiskii 1888 CD ee xadka Jabuuti iyo Soomaaliya?", "options": { "a": "Wuxuu ahaa sohdin handasi ah oo u dhexeysa Faransiiska iyo Ingiriiska", "b": "Wuxuu ahaa mid lagu dhisay webi", "c": "Wuxuu ahaa mid u dhexeeyay Soomaali iyo Itoobiya", "d": "Wuxuu ahaa mid lagu baabi'inayay xadka" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 46, "question": "Waa maxay micnaha 'Xudduud ilbaxnimo'?", "options": { "a": "Waa xudduud lagu saleeyo diinta, luuqadda ama dhaqanka", "b": "Waa xudduud buuro leh", "c": "Waa xudduud tareennada marto", "d": "Waa xudduud dabiici ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 47, "question": "Maxay tahay sababta xudduudda u dhexaysa Soomaaliya iyo Jabuuti loogu tilmaamay inay tahay 'handasi'?", "options": { "a": "Sababtoo ah waa xariiq toosan oo la siman geeska koonfureed ee togga Cafarta", "b": "Sababtoo ah buuro ayay martaa", "c": "Sababtoo ah webi ayay martaa", "d": "Ma lahan wax sabab ah" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 48, "question": "Shaqada siyaasadeed iyo sharciyada xadka maxay ka dhigan tahay?", "options": { "a": "In dal walba uu leeyahay madaxbannaani qaanuun iyo siyaasadeed gudaha sohdintiisa", "b": "In qaanuunka dalka kale laga fuliyo xadka dhexdiisa", "c": "In qaanuun la'aan laga dhigo xadka", "d": "In la isku daro labada dal" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 49, "question": "Waa maxay 'Biyaha Dheeraadka ah' ee badda?", "options": { "a": "Waa 12 mayl oo ka bilaabata dhamaadka biyo goboleedka", "b": "Waa biyaha webiyada", "c": "Waa 200 mayl", "d": "Waa xeebta kaliya" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 50, "question": "Muxuu ahaa doorkii Ingiriiska ee xadka Soomaali Galbeed 1948?", "options": { "a": "Wuxuu aqoonsaday in dhulkaas uu Itoobiya ka tirsan yahay", "b": "Wuxuu ku celiyay Soomaaliya", "c": "Wuxuu ka dhigay dowlad madaxbannaan", "d": "Wuxuu ka dhisay waddooyin ganacsi" }, "correctAnswer": "a", "difficultyLevel": "medium" },
  { "id": 51, "question": "Falanqee xiriirka ka dhexeeya horumarka agabka dagaalka iyo aragtida 'sohdinta amaanka ah'?", "options": { "a": "Hubka casriga ah wuxuu meesha ka saaray in sohdintu tahay gaashaan aan laga gudbi karin", "b": "Hubku wuxuu ka dhigay sohdinta mid sii adkaata", "c": "Hubku ma saameeyo ammaanka xadka", "d": "Hubka casriga ah wuxuu baabi'iyaa calaamadaha xadka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 52, "question": "Maxay xudduudaha dabiiciga ah loogu tixgeliyaa inay yihiin kuwa ugu xoogga badan ee kala qeybiya shucuubta?", "options": { "a": "Sababtoo ah waa kuwo sugan, muuqda, oo ay adag tahay in laga gudbo si dabiici ah", "b": "Sababtoo ah dadka ayaa jecel buuraha", "c": "Sababtoo ah dawladaha ayaa dhisay", "d": "Sababtoo ah heshiis laguma geli karo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 53, "question": "Sidee bay 'Juqraafiga Siyaasadda' u caawisaa fahamka doorashooyinka iyo xiriirka caalamiga ah?", "options": { "a": "Ayadoo baarta sida qaybinta juqraafi ay u saamayso geeddi-socodka siyaasadeed", "b": "Ayadoo baraysa dadka sida loo codeeyo", "c": "Ayadoo sawiraysa khariidado midab leh", "d": "Ma lahan door muhiim ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 54, "question": "Falanqee dhibaatada ka dhalata xudduudda aan tixgelin xaaladaha bulsho ee dadka xoolo-dhaqatada ah ee Soomaaliya?", "options": { "a": "Waxay kala qeybisaa dad isku isir iyo nolol ah, taas oo keenta khilaaf joogto ah", "b": "Waxay u fududeysaa inay helaan biyo banyak", "c": "Waxay kordhisaa tirada xoolaha", "d": "Waxay nabad ka dhex dhalisaa dalalka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 55, "question": "Sidee loo isbarbar dhigi karaa xudduudda harooyinka raacda iyo kuwa webiyada raacda?", "options": { "a": "Labaduba waxay raaci karaan khadka dhexe ama heshiis gaar ah", "b": "Haradu waxay raacdaa figta buurta", "c": "Webigu wuxuu raacaa khad handasi ah kaliya", "d": "Harooyinka xuduud looma isticmaalo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 56, "question": "Maxay tahay sababta asalka mashaakilka Kashmiir loogu xiriiriyo gumeystihii Ingiriiska?", "options": { "a": "Sababtoo ah asteyntii xudduuda iyo qeybintii uu sameeyay ayaa abuurtay khilaafka", "b": "Sababtoo ah Ingiriiska ayaa wali xukuma Kashmiir", "c": "Sababtoo ah Kashmiir ma lahan xuduud", "d": "Sababtoo ah dadka Kashmiir ayaa Ingiriis ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 57, "question": "Falanqee 'heerka tilmaamidda' (Delimitation) iyo muhiimadda ay u leedahay sohdinta?", "options": { "a": "Waa marka sohdinta laga sawiro khariidadda laguna qeexo dukumiintiyo rasmi ah", "b": "Waa marka ciidanka la dhigayo xadka", "c": "Waa marka xadka la baabi'inayo", "d": "Waa tillaabada ugu dambeysa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 58, "question": "Sidee bay 'Biyaha caalamiga ah' u saameeyaan madaxbannaanida dalalka xeebaha leh?", "options": { "a": "Dalalku xaq uma lahan inay biyahaas ka mamnuucaan maraakiibta kale", "b": "Dal kasta wuxuu sheegan karaa inuu leeyahay biyahaas", "c": "Biyahaas laguma dhex safri karo", "d": "Waxay kordhiyaan xadka dowlada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 59, "question": "Maxay tahay sababta 'Biyaha gudaha' loogu tixgeliyaa inay yihiin qayb ka mid ah dhulka qallalan ee dalka?", "options": { "a": "Sababtoo ah waxay ku yaallaan meel ka sarreysa dhulka dalka gudahiisa ah", "b": "Sababtoo ah looma isticmaalo maraakiibta", "c": "Sababtoo ah biyahaas waa kuwo macaan", "d": "Sababtoo ah ma lahan xiriir badda" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 60, "question": "Falanqee xiriirka u dhexeeya 'heerka go’aaminta' iyo calaamadaha dhulka laga taago?", "options": { "a": "Heerka go'aaminta waa marka dhulka lagu muujiyo sohdinta iyadoo la adeegsanayo tiirar ama gidaaro", "b": "Calaamadaha dhulka looma baahna", "c": "Calaamadaha waa heerka koowaad", "d": "Heerka go'aaminta waa mid khariidadda ku eg" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 61, "question": "Sidee loo xallin karaa khilaafka xudduudeed ee Soomaaliya iyo dalalka deriska ah sida ku xusan casharka?", "options": { "a": "In wadahadal la isugu yado lana baabi'iyo xudduudihii uu gumeystuhu sameeyay", "b": "In dagaal lagu soo celiyo dhulkaas gabi ahaanba", "c": "In dalalka deriska ah la siiyo dhul intaas ka badan", "d": "In la sugo inta gumeystuhu ka soo laabanayo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 62, "question": "Maxay tahay muhiimadda 'Raso qaaradeed' (Continental shelf) ee xagga khayraadka?", "options": { "a": "Waa meesha ugu badan ee laga helo kheyraadka badda sida batroolka iyo kalluunka", "b": "Waa meesha maraakiibtu ku xirtaan kaliya", "c": "Waa meesha ugu wasakhda badan badda", "d": "Ma lahan wax khayraad ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 63, "question": "Falanqee sababta xadka Soomaaliya iyo Itoobiya uu u yahay mid dhashay 1887 CD?", "options": { "a": "Xilligaas ayay Itoobiya la wareegtay Harar waxayna bilowday qabsashada dhulka Soomaaliyeed", "b": "Xilligaas ayay Soomaaliya Itoobiya weerartay", "c": "Xilligaas ayay labada dal heshiis nabad ah galeen", "d": "Xilligaas ayaa gumeystuhu isaga baxay dalka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 64, "question": "Isbarbar dhig shaqada 'Ilaalinta Dhaqaalaha' iyo 'Shaqada Siyaasadeed' ee sohdinta?", "options": { "a": "Dhaqaalaha waa canshuurta iyo ka hortagga kontarabaanka, siyaasaduna waa madaxbannaanida qaanuunka", "b": "Labaduba waa canshuur kaliya", "c": "Siyaasaddu waa canshuurta, dhaqaaluhuna waa qaanuunka", "d": "Ma jiro wax farqi ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 65, "question": "Maxay tahay sababta 'Jiidda' (Frontier) loogu tilmaamo muuqaal sugan oo aan isbeddel laheyn?", "options": { "a": "Sababtoo ah badanaa waa muuqaallo dabiici ah oo aan qofna beddeli karin sidii uu doono", "b": "Sababtoo ah waa sharci aan la jebin karin", "c": "Sababtoo ah khariidadda ayaan laga tirtiri karin", "d": "Sababtoo ah dadka ma deggana" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 66, "question": "Falanqee saamaynta sohdinta ay ku leedahay ilaalinta 'Amniga Qaranka'?", "options": { "a": "Waxay xaddiddaa meesha ay ciidanku joogayaan iyo halka ay dowladda mas'uul ka tahay", "b": "Waxay keentaa in amnigu daciifo", "c": "Amniga sohdinta laguma ilaaliyo", "d": "Sohdintu amniga ma saameyso" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 67, "question": "Sidee bay Soomaaliya u tixgelisay dastuurkeeda raadinta gobollada maqan?", "options": { "a": "Waxay ku dartay qodob sheegaya in waddo kasta oo sharci iyo nabad ah loo marayo soo celintooda", "b": "Waxay ku dartay inaan dhulkaas dib loo raadin doonin", "c": "Waxay ku dartay in la siiyo Itoobiya", "d": "Dastuurku ma taaban dhulka maqan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 68, "question": "Maxay tahay sababta xudduudda u dhexaysa Soomaaliya iyo Jabuuti loogu tilmaamay inay tahay 'handasi'?", "options": { "a": "Sababtoo ah waa xariiq toosan oo la siman geeska koonfureed ee togga Cafarta", "b": "Sababtoo ah buuro ayay martaa", "c": "Sababtoo ah webi ayay martaa", "d": "Ma lahan wax sabab ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 69, "question": "Falanqee ujeeddada heerka afraad ee 'maamulidda xadka'?", "options": { "a": "In la ilaaliyo marinka dadka, badeecadaha iyo canshuuraha", "b": "In la bilaabo sawiridda khariidadda", "c": "In la baabi'iyo xadka", "d": "In webiga la weeciyo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 70, "question": "Sidee bay 'Biyo goboleedka' u muujiyaan awoodda dowladda?", "options": { "a": "Dowladda waxay ku leedahay madaxbannaani buuxda sida dhulkeeda qallalan oo kale", "b": "Dowladda awood kuma lahan biyahaas", "c": "Biyahaas qof walba ayaa iska leh", "d": "Awoodda dowladda waxay ku kooban tahay xeebta" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 71, "question": "Isbarbar dhig baaxadda dhulka Soomaaliyeed ee ka maqan Kiinya iyo tan Itoobiya?", "options": { "a": "Dhulka Itoobiya ka maqan (153,600km2) ayaa ka weyn kan Kiinya (128,000km2)", "b": "Dhulka Kiinya ka maqan ayaa ka weyn", "c": "Waa isku mid labada dhul", "d": "Dhulka Kiinya ayaa ka yar 50,000km2" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 72, "question": "Falanqee xiriirka u dhexeeya 'Ururrada caalamiga ah' iyo ilaalinta xuduudaha?", "options": { "a": "Ururrada waxay bixiyaan aqoonsi iyo sharciyada ilaalinaya madaxbannaanida xuduudaha", "b": "Ururrada waxay baabi'iyaan xuduudaha", "c": "Ururrada kuma lug laha arrimaha xadka", "d": "Ururrada waxay kordhiyaan dagaallada xadka" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 73, "question": "Maxay 'Biyaha Dheeraadka ah' u leeyihiin xad dhan 12 mayl?", "options": { "a": "Waa heshiis caalami ah oo lagu xaddiday fogaanta kormeerka iyo kontarabaanka", "b": "Sababtoo ah waa meesha ugu dambeysa ee biyaha", "c": "Ma lahan wax sabab ah", "d": "Waa fogaanta u dhexaysa laba dal" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 74, "question": "Sidee buu gumeystuhu u kala qeybiyay dadka Soomaaliyeed ee xoolo-dhaqatada ah?", "options": { "a": "Isagoo adeegsaday xuduudo handasi ah oo dhex maray deegaannadii ay wada degganaayeen", "b": "Isagoo ka saaray dhulka gabi ahaanba", "c": "Isagoo ka dhigay hal dowlad", "d": "Isagoo siiyay hub casri ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 75, "question": "Falanqee tillaabadii 3aad ee Soomaaliya ay qaaday markii labadii hore waxba ka soo bixi waayeen?", "options": { "a": "Waxay ahayd tillaabo ciidan oo xoog loogu soo celinayo dhulka maqan", "b": "Waxay ahayd tillaabo ganacsi", "c": "Waxay ahayd tillaabo kale oo diblimaasiyadeed", "d": "Waxay ahayd in la is dhiibo" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 76, "question": "Maxay tahay sababta 'Raso qaaradeedka' (180cm/100 joog) loogu tixgeliyo fidsanaanta dhulka qallalan?", "options": { "a": "Sababtoo ah waa qaybta badda ee sida tooska ah ula socota qaaradda ka hor intaan qotada dheer la gaarin", "b": "Sababtoo ah waa meesha ugu sarraysa buurta", "c": "Sababtoo ah biyahaas waa kuwo yar", "d": "Sababtoo ah dhulku halkaas ayuu ku dhamaadaa" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 77, "question": "Sidee bay 'Biyaha dhexdhexaadka ah' ula xiriiraan biyaha dheeraadka ah?", "options": { "a": "Waxay ku sii dheggan yihiin biyaha dheeraadka ah dhanka badda bannaanka", "b": "Waa isku mid", "c": "Waxay ku yaallaan xeebta dhexdeeda", "d": "Waxay u dhow yihiin webiyada" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 78, "question": "Maxay tahay muhiimadda 'xadeynta khayraadka' ee sohdinta siyaasadeed?", "options": { "a": "Si dal walba uu u ogaado oo u maamulo khayraadka dabiiciga ah ee ku jira dhulkiisa iyo baddiisa", "b": "Si khayraadka loo wadaago gabi ahaanba", "c": "Si khayraadka loogu daadiyo badda", "d": "Ma lahan muhiimad khayraad" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 79, "question": "Falanqee sababta xadka Soomaaliya iyo Itoobiya uu u dhashay xilligii Itoobiya qabsatay Harar?", "options": { "a": "Qabsashadaas waxay bilowday isfidinta Itoobiya ee dhulka Soomaalida, taas oo keenti in xuduud cusub la calaamadiyo", "b": "Itoobiya ayaa laga adkaaday xilligaas", "c": "Itoobiya ayaa xadka dhistay si nabad ah", "d": "Harar waxay ahayd caasimadda Soomaaliya" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 80, "question": "Waa maxay gunaanadka xiriirka ka dhexeeya isticmaarka iyo mashaakilka siyaasadeed ee dunida maanta?", "options": { "a": "Xudduudihii qalloocnaa ee uu ka tagay gumeystuhu waxay wali yihiin isha ugu weyn ee colaadaha", "b": "Isticmaarku wuxuu keenay nabad buuxda", "c": "Isticmaarku ma saameyn siyaasadda maanta", "d": "Mashaakilka siyaasadeed hadda ayuu bilowday" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 81, "question": "Sidee bay xudduudda handasiga ahi u tixgelisaa 'calaamadaha juqraafiga'?", "options": { "a": "Inta badan ma tixgeliso, waxayna raacdaa xarriijimo toosan oo handasi ah", "b": "Waxay raacdaa buuraha kaliya", "c": "Waxay raacdaa webiyada kaliya", "d": "Waxay u baahan tahay dad badan inay joogaan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 82, "question": "Maxay tahay sababta sohdintu u leedahay 'muuqaal sharci'?", "options": { "a": "Sababtoo ah waxaa lagu aqoonsan yahay heshiisyo, dukumiintiyo iyo qawaaniin caalami ah", "b": "Sababtoo ah dabiiciga ayaa u yeelay", "c": "Sababtoo ah ciidanka ayaa sidaas raba", "d": "Muuqaal sharci ma lahan" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 83, "question": "Falanqee doorka 'gaadiidka' ee sohdinta siyaasadeed?", "options": { "a": "Sohdintu waxay xaddiddaa dhibcaha ay gawaarida iyo dadku ka gudbi karaan (Customs/Border crossing)", "b": "Gaadiidku kama gudbi karo sohdinta", "c": "Gaadiidku wuxuu baabi'iyaa sohdinta", "d": "Ma lahan wax door ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 84, "question": "Maxay 'xuduudaha harooyinka' u noqon karaan kuwo raaca heshiis gaar ah?", "options": { "a": "Haddii haradu aanay si siman u qeybsami karin ama khayraad gaar ah uu ku jiro", "b": "Si harada loo qalajiyo", "c": "Sababtoo ah haradu waa weyn tahay", "d": "Haradu heshiis ma geli karto" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 85, "question": "Sidee bay 'xudduudda badaha' u saameeyaan xiriirka Soomaaliya iyo dalalka deriska ah?", "options": { "a": "Waxay abuuri karaan muran ku saabsan biyaha kheyraadka leh ee badda dhexdeeda ah", "b": "Waxay kordhiyaan kaluunka", "c": "Waxay baabi'iyaan xadka berriga", "d": "Ma lahan wax saameyn ah" }, "correctAnswer": "a", "difficultyLevel": "hard" },
  { "id": 86, "question": "Waa maxay gunaanadka tillaabadii diblimaasiyadeed ee Soomaaliya markii ay kaashatay Midowga Afrika?", "options": { "a": "Waxay gaarsiisay mowqifka Soomaaliya dhammaan jihooyinkii khuseeyay", "b": "Waxay keentay in Itoobiya dhulka ku soo celiso", "c": "Waxay keentay in Kiinya laga adkaado", "d": "Diblimaasiyadda waxba laguma gaarin" }, "correctAnswer": "a", "difficultyLevel": "hard" }
]

formatted_questions = []
for i, q in enumerate(new_questions_raw):
    formatted_q = {
        'id': f"Geo_Ch8_Q{i+1:02d}",
        'subjectId': 'geo',
        'chapterId': 'geo_ch8',
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
    
    # Remove existing geo_ch8 questions
    data['questions'] = [q for q in data['questions'] if q.get('chapterId') != 'geo_ch8']
    
    # Check if geo_ch8 chapter exists, if not, add it
    chapter_exists = any(c['id'] == 'geo_ch8' for c in data['chapters'])
    if not chapter_exists:
        data['chapters'].append({
            "subjectId": "geo",
            "title": "Cutubka 8aad: Juqraafiga Siyaasadda iyo Xuduudaha",
            "id": "geo_ch8"
        })
    else:
        # Update title if it does exist
        for c in data['chapters']:
            if c['id'] == 'geo_ch8':
                c['title'] = "Cutubka 8aad: Juqraafiga Siyaasadda iyo Xuduudaha"
                break
    
    # Add new geo_ch8 questions
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

    # Remove existing geo_ch8 questions from dict
    keys_to_remove = [k for k, v in data_json.get('questions', {}).items() if v.get('chapterId') == 'geo_ch8']
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
