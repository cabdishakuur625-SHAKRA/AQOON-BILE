import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    seed_file_path = 'lib/services/seed_data.dart'
    
    if not os.path.exists(seed_file_path):
        print(f"Error: {seed_file_path} not found.")
        sys.exit(1)
        
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not parse JSON bounds in seed_data.dart")
        sys.exit(1)
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # 1. Validate Subject
    subjects = data.get('subjects', [])
    eng_sub = [s for s in subjects if s.get('id') == 'eng']
    if not eng_sub:
        print("Error: Subject 'eng' not found in subjects list.")
        sys.exit(1)
    print("✓ Subject 'eng' exists:", eng_sub[0])
    
    # 2. Validate Chapters
    chapters = data.get('chapters', [])
    eng_chaps = [c for c in chapters if c.get('subjectId') == 'eng']
    if len(eng_chaps) != 9:
        print(f"Error: Expected exactly 9 chapters for English, found {len(eng_chaps)}.")
        sys.exit(1)
    print("✓ Exactly 9 chapters found for English subject.")
    
    expected_titles = {
        "eng_ch1": "Unit 1 & 2: Never Forget & Oral Presentation",
        "eng_ch2": "Unit 3 & 4: A Colossal House & Poetry Guide",
        "eng_ch3": "Unit 5 & 6: The Lion with a Thorn in His Paw & Oral Literature",
        "eng_ch4": "Unit 7 & 8: The Father and his Son & Edible Soda",
        "eng_ch5": "Unit 9 & 10: The Motherless Girl & Societies In The Past",
        "eng_ch6": "Unit 11 & 12: Nature Conservation & The Killer Plastic",
        "eng_ch7": "Unit 13 & 14: Culture Shock & Field Work",
        "eng_ch8": "Unit 15 & 16: Negotiation Skills & Our Life Today",
        "eng_ch9": "Unit 17 & 18: Problems Caused By Modern Packaging & Allergies"
    }
    
    for ch in eng_chaps:
        ch_id = ch.get('id')
        title = ch.get('title')
        if ch_id not in expected_titles:
            print(f"Error: Unexpected chapter ID: {ch_id}")
            sys.exit(1)
        if title != expected_titles[ch_id]:
            print(f"Error: Chapter {ch_id} title mismatch. Expected: '{expected_titles[ch_id]}', Found: '{title}'")
            sys.exit(1)
    print("✓ All 9 English chapter IDs and titles match expectations.")
    
    # 3. Validate Questions
    questions = data.get('questions', [])
    eng_qs = [q for q in questions if q.get('subjectId') == 'eng']
    
    if len(eng_qs) != 720:
        print(f"Error: Expected exactly 720 questions for English, found {len(eng_qs)}.")
        sys.exit(1)
    print("✓ Exactly 720 questions found for English subject.")
    
    # Check uniqueness of IDs
    q_ids = [q.get('id') for q in eng_qs]
    if len(set(q_ids)) != 720:
        print("Error: Duplicate question IDs detected.")
        sys.exit(1)
    print("✓ All 720 question IDs are unique.")
    
    # Verify difficulty level distribution per chapter
    for ch_num in range(1, 10):
        ch_id = f"eng_ch{ch_num}"
        ch_qs = [q for q in eng_qs if q.get('chapterId') == ch_id]
        
        if len(ch_qs) != 80:
            print(f"Error: Chapter {ch_id} has {len(ch_qs)} questions, expected 80.")
            sys.exit(1)
            
        easy_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'easy'])
        med_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'medium'])
        hard_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'hard'])
        
        if easy_count != 23:
            print(f"Error: Chapter {ch_id} has {easy_count} easy questions, expected 23.")
            sys.exit(1)
        if med_count != 27:
            print(f"Error: Chapter {ch_id} has {med_count} medium questions, expected 27.")
            sys.exit(1)
        if hard_count != 30:
            print(f"Error: Chapter {ch_id} has {hard_count} hard questions, expected 30.")
            sys.exit(1)
            
        # Basic check of options & answers
        for q in ch_qs:
            opts = q.get('options', {})
            ans = q.get('correctAnswer')
            if not isinstance(opts, dict) or set(opts.keys()) != {'a', 'b', 'c', 'd'}:
                print(f"Error: Question {q.get('id')} has invalid options: {opts}")
                sys.exit(1)
            if ans not in {'a', 'b', 'c', 'd'}:
                print(f"Error: Question {q.get('id')} has invalid correctAnswer: {ans}")
                sys.exit(1)
                
        print(f"✓ Chapter {ch_id}: 80 questions total (23 easy, 27 medium, 30 hard) verified successfully.")
        
    print("\nDATABASE VALIDATION COMPLETED SUCCESSFULLY! ALL CHECKS PASSED!")

if __name__ == "__main__":
    import os
    main()
