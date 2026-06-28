import json
import sys
import os
import re

def validate_dart_file(path):
    print(f"=== Validating {path} ===")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not parse JSON boundaries in seed_data.dart")
        return False
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Find Somali subject
    subjects = data.get('subjects', [])
    somali_sub = None
    for s in subjects:
        if s.get('id') == 'somali' or s.get('name') == 'Somali':
            somali_sub = s
            break
            
    if not somali_sub:
        print("Error: Subject 'somali' not found in subjects list in seed_data.dart")
        return False
        
    print("[OK] Subject 'somali' exists in seed_data.dart")
    
    chapters = somali_sub.get('chapters', [])
    if len(chapters) != 8:
        print(f"Error: Expected exactly 8 chapters in seed_data.dart, found {len(chapters)}")
        return False
        
    print("[OK] Exactly 8 chapters found in seed_data.dart")
    
    expected_titles = {
        1: "Cutubka 1 & 2: Qoraal Sharraxeed iyo Beeraha",
        2: "Cutubka 3 & 4: Miisaanka Maansada iyo Mudnaan Badan",
        3: "Cutubka 5, 9, 12 & 14: Riwaayaddii Shabeel Naagood",
        4: "Cutubka 6 & 7: Garwaaqsiin iyo Geyiga Soomaaliya",
        5: "Cutubka 8 & 10: Dood Dheellitiran iyo Waayihii iyo Tagtadii Xaaji Aadam Axmed Xasan",
        6: "Cutubka 11 & 13: Qorista Sahanka iyo Soomalidu Ma Is Taqaan",
        7: "Cutubka 15 & 16: Yaa Iska Leh iyo Miisaanka Murtida Maansadii Dhaqan",
        8: "Cutubka 17 & 18: Yaa Tahay iyo Sheekooyin Murtiyeed"
    }
    
    chapter_cutubs = {
        1: [1, 2],
        2: [3, 4],
        3: [5, 9, 12, 14],
        4: [6, 7],
        5: [8, 10],
        6: [11, 13],
        7: [15, 16],
        8: [17, 18]
    }
    
    total_qs = 0
    for i, ch in enumerate(chapters):
        ch_num = i + 1
        title = ch.get('title')
        if title != expected_titles[ch_num]:
            print(f"Error: Chapter {ch_num} title mismatch. Expected: '{expected_titles[ch_num]}', Found: '{title}'")
            return False
            
        qs = ch.get('questions', [])
        easy = [q for q in qs if q.get('difficultyLevel') == 'easy']
        med = [q for q in qs if q.get('difficultyLevel') == 'medium']
        hard = [q for q in qs if q.get('difficultyLevel') == 'hard']
        
        print(f"  Chapter {ch_num} ({title}): Total={len(qs)}, Easy={len(easy)}, Med={len(med)}, Hard={len(hard)}")
        
        if len(qs) != 92:
            print(f"Error: Expected 92 questions in Chapter {ch_num}, found {len(qs)}")
            return False
        if len(easy) != 24:
            print(f"Error: Expected 24 easy questions in Chapter {ch_num}, found {len(easy)}")
            return False
        if len(med) != 30:
            print(f"Error: Expected 30 medium questions in Chapter {ch_num}, found {len(med)}")
            return False
        if len(hard) != 38:
            print(f"Error: Expected 38 hard questions in Chapter {ch_num}, found {len(hard)}")
            return False
            
        valid_cutubs = chapter_cutubs[ch_num]
        
        # Check IDs and prefix pattern
        for q_idx, q in enumerate(qs):
            expected_id = f"Som_Ch{ch_num}_Q{q_idx+1:02d}"
            q_id = q.get('id')
            if q_id != expected_id:
                print(f"Error: Expected question ID {expected_id}, found {q_id}")
                return False
                
            q_text = q.get('question', '')
            diff = q.get('difficultyLevel')
            
            # Match difficulty, cutub, and question number prefix: e.g. "^easy1 question 5:"
            match = re.match(r'^([a-z]+)(\d+)\s+question\s+(\d+):\s+', q_text)
            if not match:
                print(f"Error: Question text does not match prefix format on ID {q_id}: '{q_text}'")
                return False
                
            p_diff, p_cutub, p_num = match.groups()
            p_cutub = int(p_cutub)
            
            if p_diff != diff:
                print(f"Error: Prefix difficulty '{p_diff}' does not match difficultyLevel '{diff}' on ID {q_id}")
                return False
                
            if p_cutub not in valid_cutubs:
                print(f"Error: Prefix Cutub {p_cutub} is not valid for Chapter {ch_num} (valid: {valid_cutubs}) on ID {q_id}")
                return False
                
        total_qs += len(qs)
        
    if total_qs != 736:
        print(f"Error: Expected 736 total questions, found {total_qs}")
        return False
        
    print(f"[OK] All questions in seed_data.dart are verified. Total={total_qs}")
    return True

def validate_json_file(path):
    print(f"=== Validating {path} ===")
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return False
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subjects = data.get('subjects', {})
    if "somali" not in subjects:
        print("Error: 'somali' key not found in subjects dictionary in seed_data.json")
        return False
    print("[OK] Subject 'somali' exists in seed_data.json")
    
    chapters = data.get('chapters', {})
    somali_chaps = {k: v for k, v in chapters.items() if v.get('subjectId') == 'somali'}
    if len(somali_chaps) != 8:
        print(f"Error: Expected exactly 8 chapters in seed_data.json, found {len(somali_chaps)}")
        return False
    print("[OK] Exactly 8 chapters found in seed_data.json")
    
    questions = data.get('questions', {})
    somali_qs = {k: v for k, v in questions.items() if v.get('subjectId') == 'somali' or v.get('chapterId', '').startswith('somali_')}
    
    if len(somali_qs) != 736:
        print(f"Error: Expected exactly 736 questions for Somali in seed_data.json, found {len(somali_qs)}")
        return False
    print(f"[OK] Exactly 736 questions found in seed_data.json")
    
    # Verify difficulty levels count per chapter
    for ch_num in range(1, 9):
        ch_id = f"somali_ch{ch_num}"
        ch_qs = [v for k, v in somali_qs.items() if v.get('chapterId') == ch_id]
        
        easy = len([q for q in ch_qs if q.get('difficultyLevel') == 'easy'])
        med = len([q for q in ch_qs if q.get('difficultyLevel') == 'medium'])
        hard = len([q for q in ch_qs if q.get('difficultyLevel') == 'hard'])
        
        if len(ch_qs) != 92:
            print(f"Error: Chapter {ch_id} has {len(ch_qs)} questions, expected 92")
            return False
        if easy != 24:
            print(f"Error: Chapter {ch_id} has {easy} easy questions, expected 24")
            return False
        if med != 30:
            print(f"Error: Chapter {ch_id} has {med} medium questions, expected 30")
            return False
        if hard != 38:
            print(f"Error: Chapter {ch_id} has {hard} hard questions, expected 38")
            return False
            
    print("[OK] All questions in seed_data.json are verified.")
    return True

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    dart_ok = validate_dart_file('lib/services/seed_data.dart')
    json_ok = validate_json_file('scratch/seed_data.json')
    
    if dart_ok and json_ok:
        print("\n🎉 ALL VALIDATIONS PASSED SUCCESSFULLY! 🎉")
    else:
        print("\n❌ VALIDATION FAILED! ❌")
        sys.exit(1)

if __name__ == "__main__":
    main()
