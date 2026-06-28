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
    # Strip variables that might not be defined or just execute the list assignment
    g = {}
    exec(list_str, g)
    return g['new_questions_raw']

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    
    # 1. Load questions for all chapters
    ch_questions = {}
    for i in range(1, 8):
        path = f'scratch/update_his_ch{i}_user.py'
        if not os.path.exists(path):
            print(f"Error: {path} not found")
            return
        ch_questions[i] = load_questions_from_file(path)
        print(f"Loaded Ch {i} original questions count: {len(ch_questions[i])}")
        
    # 2. Add missing questions to Chapter 1, 2, 3, 4
    # Ch 1 missing: 3 Easy, 3 Medium
    ch1_easy_missing = [
        {"question": "Magaalada Bursa waxay ku taallaa dalka:", "options": {"a": "Masar", "b": "Turkiga", "c": "Suuriya", "d": "Ciraaq"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Waa kuma suldaankii furtay magaalada Istanbuul?", "options": {"a": "Cusmaan 1-aad", "b": "Muxammad Al-Faatix", "c": "Sulaymaan Qaanuuni", "d": "Muraad 1-aad"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Dawladdii Cusmaaniyiinta waxay si rasmi ah u bilaabantay qarnigii:", "options": {"a": "10-aad", "b": "13-aad", "c": "15-aad", "d": "17-aad"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch1_med_missing = [
        {"question": "Waa maxay ujeeddada ugu weyn ee nidaamka Sanjaq?", "options": {"a": "In la dhisayo ciidan badda", "b": "In loo qaybiyo dalka gobollo maamul si habboon loo xukumo", "c": "In la canshuuro ganacsiga", "d": "In la xaddido awoodda Suldaanka"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Muxuu ahaa dardaarankii ugu dambeeyay ee Cusmaan ee ku aaddan diinta?", "options": {"a": "In heshiis la la galo dawladaha reer Yurub", "b": "In la sii wado sarreeynta diinta Islaamka iyo jihaadka", "c": "In la beddelo shareecada", "d": "In la dhiso qalcadaha badda"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxay aheyd muhiimadda furashada Adraana sanadkii 1361?", "options": {"a": "Waxay soo afjartay dowladdii Seljuuqa", "b": "Waxay saldhig u noqotay is-ballaarinta koonfur-bari ee Yurub", "c": "Waxay keentay burburkii dowladda", "d": "Waxay ahayd markii ugu horreysay ee badda la galo"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[1].extend(ch1_easy_missing)
    ch_questions[1].extend(ch1_med_missing)
    
    # Ch 2 missing: 3 Easy, 3 Medium
    ch2_easy_missing = [
        {"question": "Halkee bay ku taallaa xeebta badda dhexe marka loo eego Falastiin?", "options": {"a": "Dhanka bari", "b": "Dhanka galbeed", "c": "Dhanka koonfur", "d": "Dhanka waqooyi"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Dadka Ruhindiga ah waxay ku nool yihiin dalka:", "options": {"a": "Bakistaan", "b": "Miyanmaar (Barma)", "c": "Hindiya", "d": "Shiinaha"}, "correctAnswer": "b", "difficultyLevel": "easy"},
        {"question": "Magaalada Qudus (Jerusalem) waxay ku taallaa dalka:", "options": {"a": "Suuriya", "b": "Falastiin", "c": "Masar", "d": "Urdun"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch2_med_missing = [
        {"question": "Maxay aheyd ujeeddadii laga lahaa baaqii Belfoor ee sanadkii 1917?", "options": {"a": "In la xoreeyo dadka Ruhindiga ah", "b": "In Yuhuudda looga dhiso hooy qaran dhulka Falastiin", "c": "In la qaybiyo Kashmiir", "d": "In laga adkaado dowladda Jabaan"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxay Kashmiir muhiim ugu tahay Hindiya iyo Bakistaan?", "options": {"a": "Batrool badan oo laga helo darteed", "b": "Muhiimaddeeda difaac, amni iyo webiyada biyaha ka soo baxa", "c": "Maaddaama ay tahay jasiirad weyn", "d": "Sababtoo ah waa dhul ka hooseeya badda"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Goormee ayay bilaabantay qaddiyadda Ruhindiga ee Barma markii ugu horreysay?", "options": {"a": "1947", "b": "1784 markii boqorka Buudistaha uu qabsaday Aarakaan", "c": "1999", "d": "1917"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[2].extend(ch2_easy_missing)
    ch_questions[2].extend(ch2_med_missing)
    
    # Ch 3 missing: 1 Easy, 3 Medium
    ch3_easy_missing = [
        {"question": "Waa kuma hindisaha calanka Soomaaliyeed?", "options": {"a": "Aadan Cabdulle Cusmaan", "b": "Maxamed Cawaale Liibaan", "c": "Jeneral Daa'uud", "d": "Cabdirashiid Cali Sharma'arke"}, "correctAnswer": "b", "difficultyLevel": "easy"}
    ]
    ch3_med_missing = [
        {"question": "Muxuu ahaa go'aankii Qaramada Midoobay ee ku aaddan koonfurta Soomaaliya sanadkii 1949?", "options": {"a": "In Ingiriisku maamulo weligiis", "b": "In la geliyo maamulka dawladno-gaarsiinta ee Talyaaniga muddo 10 sano ah", "c": "In la siiyo Itoobiya", "d": "In si degdeg ah xornimo loo siiyo"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxay aheyd guushii ugu weyneyd ee maamulkii ciidanka ee Soomaaliya ee la xiriirta luuqadda?", "options": {"a": "Barashada luuqadda Ingiriiska", "b": "Qorista iyo rasmeynta af-Soomaaliga sanadkii 1972", "c": "Barashada luuqadda Talyaaniga", "d": "Joojinta qorista afka"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Halkee lagu dilay madaxweynihii labaad ee Soomaaliya Cabdirashiid Cali Sharma'arke sanadkii 1969?", "options": {"a": "Muqdisho", "b": "Laas-Caanood", "c": "Hargeysa", "d": "Kismaayo"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[3].extend(ch3_easy_missing)
    ch_questions[3].extend(ch3_med_missing)
    
    # Ch 4 missing: 6 Medium
    ch4_med_missing = [
        {"question": "Waa kuwee hoggaamiyayaashii kacdoonkii Qaahira ee dhiiri-geliyay dadka?", "options": {"a": "Muxammad Cali", "b": "Cumar Makram iyo Axmed Maxruuqi", "c": "Nelson Mandeela", "d": "Cumar Mukhtaar"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Sanadkee ayay ANC (Golaha Waddaniga ee Koonfur Afrika) sameysatay garabka militariga?", "options": {"a": "1912", "b": "1961", "c": "1994", "d": "1931"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Halkee ayuu ku dhashay halyeygii reer Liibiya ee Cumar Mukhtaar?", "options": {"a": "Bingaazi", "b": "Tuulada Janzuur ee bariga Liibiya", "c": "Kafra", "d": "Tripoli"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Muxuu ahaa ujeeddada koowaad ee ururkii ANC ee Koonfur Afrika?", "options": {"a": "In la qabsado dhulka dalalka deriska ah", "b": "In meesha laga saaro midab-takoorkii (Apartheid) iyo difaaca xuquuqda madowga", "c": "In la taageero Faransiiska", "d": "In la dhiso warshado batrool"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Sidee ayuu u dhintay halyeygii Cumar Mukhtaar sanadkii 1931-dii?", "options": {"a": "Xanuun kedis ah", "b": "Waxaa daldalay gumeystihii Talyaaniga", "c": "Dagaal toos ah ayuu ku dhintay", "d": "Wuu ka baxsaday Liibiya"}, "correctAnswer": "b", "difficultyLevel": "medium"},
        {"question": "Maxaa sababay in ardayda Azhar ee Masar ay u istaagaan dagaalka Faransiiska?", "options": {"a": "Inay lacag rabeen", "b": "Si ay u difaacaan dalkooda iyo diintooda oo Faransiisku ku xad-gudbay", "c": "Inay rabeen inay aadaan Yurub", "d": "Si ay u taageeraan Ingiriiska"}, "correctAnswer": "b", "difficultyLevel": "medium"}
    ]
    ch_questions[4].extend(ch4_med_missing)
    
    # 3. Clean, partition and format all chapters
    all_final_questions = []
    
    for ch_num in range(1, 8):
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
        
        ch_id = f"his_ch{ch_num}"
        
        # Add to main list with structured IDs
        # Easy: Q01 to Q23
        for i, q in enumerate(final_easy):
            all_final_questions.append({
                "id": f"His_Ch{ch_num}_Q{str(i+1).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "easy",
                "subjectId": "his",
                "chapterId": ch_id
            })
            
        # Medium: Q24 to Q50
        for i, q in enumerate(final_med):
            all_final_questions.append({
                "id": f"His_Ch{ch_num}_Q{str(i+24).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "medium",
                "subjectId": "his",
                "chapterId": ch_id
            })
            
        # Hard: Q51 to Q80
        for i, q in enumerate(final_hard):
            all_final_questions.append({
                "id": f"His_Ch{ch_num}_Q{str(i+51).zfill(2)}",
                "question": q["question"],
                "options": {k.lower(): str(v) for k, v in q["options"].items()},
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": "hard",
                "subjectId": "his",
                "chapterId": ch_id
            })
            
    print(f"Successfully compiled {len(all_final_questions)} final History questions.")
    
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
    
    # Update questions: remove existing his questions, then append new ones
    data_questions = data.get('questions', [])
    data_questions = [q for q in data_questions if q.get('subjectId') != 'his']
    data_questions.extend(all_final_questions)
    data['questions'] = data_questions
    
    # Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + updated_json + "\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully integrated {len(all_final_questions)} History questions into seed_data.dart!")

if __name__ == '__main__':
    main()
