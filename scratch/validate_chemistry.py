import json
import sys
import os
import re

def validate_question_text(q_id, question_text):
    # Regex check for prefix patterns
    prefix_patterns = [
        r'^[Qq]uestion\s*\d+',
        r'^[Ss]u\'aasha\s*\d+',
        r'^[Ee]asy\d*\s*question',
        r'^[Mm]edium\d*\s*question',
        r'^[Hh]ard\d*\s*question',
        r'^[Qq]\d+\s*[:\.]',
        r'^\d+\s*[\.:-]\s+'
    ]
    for pattern in prefix_patterns:
        if re.match(pattern, question_text):
            print(f"Error: Question {q_id} has forbidden prefix pattern '{pattern}': '{question_text}'")
            return False
            
    # Simple Somali keyword presence check to guarantee English
    somali_keywords = ["waa maxay", "xisaabi", "muraayad", "iftiin", "walax", "halbeegga", "su'aal", "qiyaas", "dhexeeya", "aqoon", "bile"]
    for kw in somali_keywords:
        if kw in question_text.lower():
            print(f"Error: Question {q_id} contains Somali keyword '{kw}': '{question_text}'")
            return False
            
    return True

def validate_dart_file(path):
    print(f"=== Validating {path} ===")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not parse JSON bounds in seed_data.dart")
        return False
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Find Chemistry subject
    subjects = data.get('subjects', [])
    chem_sub = None
    for s in subjects:
        if s.get('id') == 'chem' or s.get('name') == 'Chemistry':
            chem_sub = s
            break
            
    if not chem_sub:
        print("Error: Subject 'chem' not found in subjects list in seed_data.dart")
        return False
        
    print("✓ Subject 'chem' exists in seed_data.dart")
    
    chapters = chem_sub.get('chapters', [])
    if len(chapters) != 8:
        print(f"Error: Expected exactly 8 chapters in seed_data.dart, found {len(chapters)}")
        return False
        
    print("✓ Exactly 8 chapters found in seed_data.dart")
    
    expected_titles = {
        1: "Hydrocarbons",
        2: "Alcohols, Phenols and Ethers",
        3: "Aldehydes, Ketones and Carboxylic Acids",
        4: "Biochemistry",
        5: "p-Block Elements",
        6: "Chemical Kinetics",
        7: "Chemical Equilibrium",
        8: "Introduction to Nuclear Chemistry"
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
        
        if len(qs) != 91:
            print(f"Error: Expected 91 questions in Chapter {ch_num}, found {len(qs)}")
            return False
        if len(easy) != 27:
            print(f"Error: Expected 27 easy questions in Chapter {ch_num}, found {len(easy)}")
            return False
        if len(med) != 29:
            print(f"Error: Expected 29 medium questions in Chapter {ch_num}, found {len(med)}")
            return False
        if len(hard) != 35:
            print(f"Error: Expected 35 hard questions in Chapter {ch_num}, found {len(hard)}")
            return False
            
        # Check IDs and question format
        for q_idx, q in enumerate(qs):
            expected_id = f"Chem_Ch{ch_num}_Q{q_idx+1:02d}"
            q_id = q.get('id')
            if q_id != expected_id:
                print(f"Error: Expected question ID {expected_id}, found {q_id}")
                return False
                
            q_text = q.get('question', '')
            if not validate_question_text(q_id, q_text):
                return False
                
        total_qs += len(qs)
        
    print(f"✓ All questions in seed_data.dart are verified. Total={total_qs}")
    return True

def validate_json_file(path):
    print(f"=== Validating {path} ===")
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return False
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Check subjects
    subjects = data.get('subjects', {})
    if "chem" not in subjects:
        print("Error: 'chem' key not found in subjects dictionary in seed_data.json")
        return False
    print("✓ Subject 'chem' exists in seed_data.json")
    
    # Check chapters
    chapters = data.get('chapters', {})
    chem_chaps = {k: v for k, v in chapters.items() if v.get('subjectId') == 'chem'}
    if len(chem_chaps) != 8:
        print(f"Error: Expected exactly 8 chapters in seed_data.json, found {len(chem_chaps)}")
        return False
    print("✓ Exactly 8 chapters found in seed_data.json")
    
    # Check questions
    questions = data.get('questions', {})
    chem_qs = {k: v for k, v in questions.items() if v.get('subjectId') == 'chem' or v.get('chapterId', '').startswith('chem_')}
    
    if len(chem_qs) != 728:
        print(f"Error: Expected exactly 728 questions for Chemistry in seed_data.json, found {len(chem_qs)}")
        return False
    print(f"✓ Exactly 728 questions found in seed_data.json")
    
    # Verify difficulty levels count per chapter
    for ch_num in range(1, 9):
        ch_id = f"chem_ch{ch_num}"
        ch_qs = [v for k, v in chem_qs.items() if v.get('chapterId') == ch_id]
        
        easy = len([q for q in ch_qs if q.get('difficultyLevel') == 'easy'])
        med = len([q for q in ch_qs if q.get('difficultyLevel') == 'medium'])
        hard = len([q for q in ch_qs if q.get('difficultyLevel') == 'hard'])
        
        if len(ch_qs) != 91:
            print(f"Error: Chapter {ch_id} has {len(ch_qs)} questions, expected 91")
            return False
        if easy != 27:
            print(f"Error: Chapter {ch_id} has {easy} easy questions, expected 27")
            return False
        if med != 29:
            print(f"Error: Chapter {ch_id} has {med} medium questions, expected 29")
            return False
        if hard != 35:
            print(f"Error: Chapter {ch_id} has {hard} hard questions, expected 35")
            return False
            
        # Check question content
        for q_id, q in chem_qs.items():
            if q.get('chapterId') == ch_id:
                if not validate_question_text(q_id, q.get('question', '')):
                    return False
            
    print("✓ All questions in seed_data.json are verified.")
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
