import json
import os
import sys
import re

def load_questions_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    start_idx = content.find('new_questions_raw = [')
    end_idx = content.find(']\n\nformatted_questions', start_idx)
    if end_idx == -1:
        end_idx = content.find(']\r\n\r\nformatted_questions', start_idx)
    if start_idx == -1 or end_idx == -1:
        end_idx = content.find(']\nformatted_questions', start_idx)
    if start_idx == -1 or end_idx == -1:
        end_idx = content.find(']\n', start_idx)
    
    list_str = content[start_idx:end_idx+1]
    g = {}
    exec(list_str, g)
    return g['new_questions_raw']

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    
    # 1. Load questions for all 8 chapters
    ch_questions = {}
    for i in range(1, 9):
        path = f'scratch/update_geo_ch{i}_user.py'
        if not os.path.exists(path):
            print(f"Error: {path} not found")
            return
        ch_questions[i] = load_questions_from_file(path)
        print(f"Loaded Ch {i} original questions count: {len(ch_questions[i])}")
        
    # 2. Add missing questions to Chapter 1, 2, 3, 4, 5, 6, 7
    # Ch 1 missing: 3 Easy, 2 Medium
    ch1_easy_missing = [
        {"question": "Waa maxay magaca kale ee loo yaqaan waaga cusub ee jiyooloojiga?", "options": {"a": "Paleozoyig", "b": "Mesozoyig", "c": "Kinozoyig", "d": "Waaga cusub (Quaternary)"}, "correctAnswer": "d", "difficultyLevel": "easy"},
        {"question": "Macaadin noocee ah ayaa inta badan laga helaa waagii Kambiriyanka ka horreeyey?", "options": {"a": "Dhuxul iyo shidaal", "b": "Macaadin qaali ah sida dahabka iyo qalinka", "c": "Nuurad iyo dhoobo", "d": "Salfar iyo sinki oo kaliya"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Buurta ugu dheer dalka Soomaaliya waxaa la yiraahdaa:", "options": {"a": "Goolis", "b": "Suurad (Shimbiris)", "c": "Oogo", "d": "Daalo"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch1_med_missing = [
        {"question": "Xilligii Ayuusiin (Aagga waaga saddexaad), maxaa ku dhacay dhulka Soomaaliya?", "options": {"a": "Dhulka ayaa kor u kacay oo baddii ka baxday", "b": "Badda Ayuusiin ayaa gudaha u soo gashay oo dhulka dabooltay", "c": "Waxaa ka qarxay foolkaanooyin waa weyn", "d": "Wuxuu noqday lama degaan engegan"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Sidee ayay u samaysantay Gacanka Cadmeed ee dhulka Soomaaliya?", "options": {"a": "Carra guur iyo daadad xooggan", "b": "Dhaqdhaqaaqyo gilgil (dhul rogrogan) iyo dildilaac", "c": "Canshuuro iyo maamul dibadda ah", "d": "Dhirta oo aad u badatay awgeed"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[1].extend(ch1_easy_missing)
    ch_questions[1].extend(ch1_med_missing)
    
    # Ch 2 missing: 1 Medium
    ch2_med_missing = [
        {"question": "Dhirta dabiiciga ah ee ka baxda meelaha uu ku da'o xaddi roobeed aad u yar waxaa la yiraahdaa:", "options": {"a": "Kaymaha", "b": "Haramaha (Savanna/Steppe)", "c": "Cawska Tundura", "d": "Dhirta biyaha dhexdooda"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[2].extend(ch2_med_missing)
    
    # Ch 3 missing: 1 Easy, 1 Medium
    ch3_easy_missing = [
        {"question": "Musiibada inta badan ku timaada xaddiga da'aaga roobka oo aad u bata waxaa la yiraahdaa:", "options": {"a": "Abaaro", "b": "Daadad", "c": "Xaar", "d": "Dhulgariir"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch3_med_missing = [
        {"question": "Waa maxay nabaad-guurka carrada?", "options": {"a": "Biyo yari baahsan oo dhulka ku dhacda", "b": "Nafoofid iyo nafaqadaro dhulka gaarta oo keenta in geedo ay ka bixi waayaan", "c": "Koritaanka dhirta oo aad u bata", "d": "Sameynta seero deegaan oo la ilaaliyo"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[3].extend(ch3_easy_missing)
    ch_questions[3].extend(ch3_med_missing)
    
    # Ch 4 missing: 3 Easy, 2 Medium
    ch4_easy_missing = [
        {"question": "Soomaaliya waxay dhacdaa dhanka:", "options": {"a": "Galbeedka Afrika", "b": "Bariga qaaradda Afrika (Geeska Afrika)", "c": "Koonfurta Afrika", "d": "Waqooyiga Afrika"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Dalka Jabuuti wuxuu kaga beegan yahay Soomaaliya dhanka:", "options": {"a": "Koonfureed", "b": "Waqooyi", "c": "Galbeed", "d": "Bari"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Xadka ugu dheer ee Soomaaliya ay la wadaagto dalalka deriska ah wuxuu u dhexeeyaa:", "options": {"a": "Soomaaliya iyo Jabuuti", "b": "Soomaaliya iyo Itoobiya", "c": "Soomaaliya iyo Kiinya", "d": "Soomaaliya iyo Suudaan"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch4_med_missing = [
        {"question": "Muxuu ahaa saameynta abaaraha ee dhacay Soomaaliya sanadihii 1974-1975?", "options": {"a": "Waxay keentay in beero badan la furo", "b": "Waxay galaafatay 25% xoolaha iyo daaqii dalka", "c": "Waxay kordhisay wax-dhoofinta dalka", "d": "Ma jirin wax khasaare ah oo ay geysatay"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Tirakoobkii dadka Soomaaliya ee la sameeyay sanadkii 2014 wuxuu sheegay in dadku gaarayeen:", "options": {"a": "5 malyan", "b": "10.5 malyan", "c": "20 malyan", "d": "15 malyan"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[4].extend(ch4_easy_missing)
    ch_questions[4].extend(ch4_med_missing)
    
    # Ch 5 missing: 3 Easy, 7 Medium
    ch5_easy_missing = [
        {"question": "Socdaalka dadku ay kaga baxayaan dal iyagoo u socdaalayo dal kale waxaa la yiraahdaa:", "options": {"a": "Hijrada gudaha", "b": "Hijrada dibadda", "c": "Dhalashada", "d": "Cilmiga tirokoobka"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Taran-fatah (population explosion) wuxuu dhacaa marka:", "options": {"a": "Dhimashadu ay ka badato dhalashada", "b": "Kororka tirada dadka uu ka sare maro ilaha dhaqaale ee dabiiciga ah", "c": "Dadku ay u guuraan miyiga", "d": "Biyo yari ay ka dhacdo dalka"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Xogaha diiwaangelinta carruurta dhalaneysa iyo dadka geeriyoonaya waxaa la yiraahdaa:", "options": {"a": "Tirokoobka juqraafi", "b": "Tirokoobyada muhiimka ah (Vital statistics)", "c": "Hijrada gudaha", "d": "Maktabad"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch5_med_missing = [
        {"question": "Sidee bay cimiladu u saameysaa baahsanaanta iyo cufnaanta dadka dunida?", "options": {"a": "Dadku waxay doorbidaan meelaha cimilada aadka u kulul ama aadka u qabow", "b": "Dadku waxay ku ururaan meelaha cimilada dhexdhexaadka ah oo u roon nolosha iyo beeraha", "c": "Cimiladu ma lahan wax saameyn ah", "d": "Cimiladu waxay kordhisaa cufnaanta lama degaanka"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Waa maxay farqiga u dhexeeya 'Tirokoob Tilmaamid ah' iyo 'Tirokoob Falanqayn ah'?", "options": {"a": "Kan koowaad wuxuu adeegsadaa kombuyuutar halka kan labaad uu qoraal yahay", "b": "Kan tilmaamidda ah wuxuu ururiyaa xogaha xilli ama goob gaar ah, halka kan falanqaynta ah uu muunad (sample) u isticmaalo inuu ku fahmo bulsho weyn", "c": "Ma jiro wax farqi ah", "d": "Labaduba waxay ku saabsan yihiin dhoofinta alaabta"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Halkee bay dadka Soomaaliyeed aad ugu badan yihiin marka loo eego filiqsanaanta dadka?", "options": {"a": "Miyiga iyo tuulooyinka fog-fog", "b": "Hareeraha webiyada Shabeelle iyo Jubba iyo magaalooyinka waa weyn sida Muqdisho", "c": "Buuraleyda taxan ee waqooyiga", "d": "Dhulka u dhow xadka Kiinya ee engegan"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Waa maxay cufnaanta tirada dadka?", "options": {"a": "Waa tirada guud ee dadka ku nool miyiga", "b": "Waa saamiga dadka marka loo eego baaxadda dhulka (tirada dadka ÷ bedka dhulka)", "c": "Waa tirada dhalashada ee sanadkii dhacda", "d": "Waa tirada carruurta waxbarata"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxay bulshada Soomaaliyeed ugu yar yihiin reer magaalku?", "options": {"a": "Sababtoo ah ma jiraan magaalooyin dalka", "b": "Sababtoo ah dhaqaalaha dalku wuxuu ku tiirsan yahay xoolo-dhaqashada oo ah reer miyi", "c": "Sababtoo ah dadka ayaan rabin magaalooyinka", "d": "Sababtoo ah cimilada magaalada ayaa xun"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Waa maxay bulshada tirokoobka (statistical population)?", "options": {"a": "Waa dadka degan caasimadda dalka kaliya", "b": "Waa koox dad ah, walxo ama cabbiro leh astaamo guud oo daraasaddu ku wareegeyso", "c": "Waa ururrada samafalka ee dalka jira", "d": "Waa tirada dadka geeriyooday"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Sidee bay colaaduhu u saameeyaan baahsanaanta dadka ee gobol dhexdiis?", "options": {"a": "Waxay kordhiyaan wax-soo-saarka beereed", "b": "Waxay keenaan barakicin iyo socdaal qasab ah oo dadku ugu guurayaan goobo nabdoon", "c": "Waxay yareeyaan cufnaanta magaalooyinka waa weyn mar kasta", "d": "Waxay meesha ka saaraan baahida adeegyada aasaasiga ah"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[5].extend(ch5_easy_missing)
    ch_questions[5].extend(ch5_med_missing)
    
    # Ch 6 missing: 1 Easy, 2 Medium
    ch6_easy_missing = [
        {"question": "Deegaan ay ku nool yihiin dad farabadan oo leh astaamo ka duwan kuwa miyiga waxaa la yiraahdaa:", "options": {"a": "Tuulo", "b": "Magaalo", "c": "Seero", "d": "Daaqsin"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch6_med_missing = [
        {"question": "Waa maxay dhibaatada ugu daran ee ka taagan xagga helitaanka biyaha ee magaalooyinka waa weyn?", "options": {"a": "Biyo yari baahsan oo ka dhalata ciriiriga iyo daryeel la'aanta tubooyinka", "b": "Biyaha oo aad u jaban awgeed", "c": "Barafka oo ku badan tubooyinka dalka", "d": "Ma jiraan dhibaatooyin biyo"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Sidee ayuu socdaalku (hijradu) u saameeyaa kobaca magaalooyinka?", "options": {"a": "Wuxuu yareeyaa tirada gawaarida ee magaalada", "b": "Marka uu bato socdaalka magaalada lagu soo galo waxaa kordha tirada dadka iyo kobaca magaalada", "c": "Wuxuu baabi'iyaa warshadaha dalka", "d": "Wuxuu keenaa biyo yari oo kaliya"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[6].extend(ch6_easy_missing)
    ch_questions[6].extend(ch6_med_missing)
    
    # Ch 7 missing: 5 Easy, 2 Medium
    ch7_easy_missing = [
        {"question": "Beddelidda alaabta ceeriin loona beddelo qaab kale oo qiimaheedu sarreeyo waxaa la yiraahdaa:", "options": {"a": "Dalxiis", "b": "Sanaaco (Warshadayn)", "c": "Geddis", "d": "Gaadiid"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Awoodda lagu qabto shaqo ama hawl waxaa la yiraahdaa:", "options": {"a": "Gaadiid", "b": "Tamar", "c": "Geddis", "d": "Saylad"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Tamarta cadceedda iyo tamarta dabaysha waxay ka mid yihiin:", "options": {"a": "Tamarta aan la cusboonaysiin karin", "b": "Tamarta dib loo cusboonaysiin karo (renewable)", "c": "Tamarta nukliyeerka", "d": "Dhuxul dhagaxa oo kaliya"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Saliidda (bitroolka) iyo gaaska dabiiciga ah waxay ka mid yihiin:", "options": {"a": "Tamarta dib loo cusboonaysiin karo", "b": "Tamarta aan la cusboonaysiin karin", "c": "Tamarta biyaha", "d": "Tamarta dabaysha"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Dalka adduunka ugu horreeya dhinaca dalxiiska waa:", "options": {"a": "Tayland", "b": "Faransiiska", "c": "Meksiko", "d": "Turkiga"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch7_med_missing = [
        {"question": "Waa maxay 'Geddis' sida ku xusan cilmiga juqraafiga?", "options": {"a": "Waa daabulidda dadka ee cirka", "b": "Waa badeecada laga soo daabulo goobaha waxsoosaarka lana geeyo goobaha isticmaalo ama sayladaha", "c": "Waa xaddidaadda xuduudaha dalalka", "d": "Waa dhismaha warshado waa weyn"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxay yihiin astaamaha lagu garto gaadiidka biyaha (maraakiibta)?", "options": {"a": "Waxay u dheereeyaan sida diyaaradaha", "b": "Xammuul aad u weyn oo ay qaadi karaan iyo kharashka oo hooseeya", "c": "Loodsanaan aad u sarreysa oo waddo kasta leh", "d": "Kharashka oo aad u sarreeya mar kasta"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[7].extend(ch7_easy_missing)
    ch_questions[7].extend(ch7_med_missing)
    
    # 3. Clean, partition and format all chapters
    all_final_questions = []
    
    for ch_num in range(1, 9):
        qs = ch_questions[ch_num]
        
        # Deduplicate by question text
        seen_texts = set()
        unique_qs = []
        for q in qs:
            q_text = q['question'].strip()
            if q_text not in seen_texts:
                seen_texts.add(q_text)
                unique_qs.append(q)
                
        # Split by difficulty
        easy_qs = [q for q in unique_qs if q['difficultyLevel'] == 'easy']
        med_qs = [q for q in unique_qs if q['difficultyLevel'] == 'medium']
        hard_qs = [q for q in unique_qs if q['difficultyLevel'] == 'hard']
        
        print(f"Ch {ch_num} clean pools - Easy: {len(easy_qs)}, Medium: {len(med_qs)}, Hard: {len(hard_qs)}")
        
        # Verify we have enough
        if len(easy_qs) < 23 or len(med_qs) < 27 or len(hard_qs) < 30:
            print(f"Error: Insufficient questions for Chapter {ch_num}!")
            return
            
        # Take exact counts
        final_easy = easy_qs[:23]
        final_med = med_qs[:27]
        final_hard = hard_qs[:30]
        
        ch_id = f"geo_ch{ch_num}"
        
        # Add to main list with structured IDs
        # Easy: Q01 to Q23
        for i, q in enumerate(final_easy):
            all_final_questions.append({
                "id": f"Geo_Ch{ch_num}_Q{str(i+1).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "easy",
                "subjectId": "geo",
                "chapterId": ch_id
            })
            
        # Medium: Q24 to Q50
        for i, q in enumerate(final_med):
            all_final_questions.append({
                "id": f"Geo_Ch{ch_num}_Q{str(i+24).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "medium",
                "subjectId": "geo",
                "chapterId": ch_id
            })
            
        # Hard: Q51 to Q80
        for i, q in enumerate(final_hard):
            all_final_questions.append({
                "id": f"Geo_Ch{ch_num}_Q{str(i+51).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "hard",
                "subjectId": "geo",
                "chapterId": ch_id
            })
            
    print(f"Successfully compiled {len(all_final_questions)} final Geography questions.")
    
    # 4. Read seed_data.dart
    seed_file_path = 'lib/services/seed_data.dart'
    if not os.path.exists(seed_file_path):
        print(f"Error: {seed_file_path} not found")
        return
        
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx_raw = content.find(start_str)
    if start_idx_raw == -1:
        print("Could not find fullSeedJson")
        return
        
    start_idx = content.find('{', start_idx_raw)
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find JSON bounds")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Update questions: remove existing geo questions, then append new ones
    data_questions = data.get('questions', [])
    data_questions = [q for q in data_questions if q.get('subjectId') != 'geo']
    data_questions.extend(all_final_questions)
    data['questions'] = data_questions
    
    # Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + updated_json + "\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully integrated {len(all_final_questions)} Geography questions into seed_data.dart!")

if __name__ == '__main__':
    main()
