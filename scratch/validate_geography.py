import json
import sys
import os

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
    geo_sub = [s for s in subjects if s.get('id') == 'geo']
    if not geo_sub:
        print("Error: Subject 'geo' not found in subjects list.")
        sys.exit(1)
    print("✓ Subject 'geo' exists:", geo_sub[0])
    
    # 2. Validate Chapters
    chapters = data.get('chapters', [])
    geo_chaps = [c for c in chapters if c.get('subjectId') == 'geo']
    if len(geo_chaps) != 8:
        print(f"Error: Expected exactly 8 chapters for Geography, found {len(geo_chaps)}.")
        sys.exit(1)
    print("✓ Exactly 8 chapters found for Geography subject.")
    
    expected_titles = {
        "geo_ch1": "Cutubka 1aad: Hordhaca Jiyooloojiga",
        "geo_ch2": "Cutubka 2aad: Nololeyda iyo Deegaanka",
        "geo_ch3": "Cutubka 3aad: Dadka iyo Deegaanka",
        "geo_ch4": "Cutubka 4aad: Juqraafiga Soomaaliya",
        "geo_ch5": "Cutubka 5aad: Juqraafiga Dadka",
        "geo_ch6": "Cutubka 6aad: Magaalooyinka",
        "geo_ch7": "Cutubka 7aad: Sanaacada iyo Tamarta",
        "geo_ch8": "Cutubka 8aad: Juqraafiga Siyaasadda iyo Xuduudaha"
    }
    
    for ch in geo_chaps:
        ch_id = ch.get('id')
        title = ch.get('title')
        if ch_id not in expected_titles:
            print(f"Error: Unexpected chapter ID: {ch_id}")
            sys.exit(1)
        if title != expected_titles[ch_id]:
            print(f"Error: Chapter {ch_id} title mismatch. Expected: '{expected_titles[ch_id]}', Found: '{title}'")
            sys.exit(1)
    print("✓ All 8 Geography chapter IDs and titles match expectations.")
    
    # 3. Validate Questions
    questions = data.get('questions', [])
    geo_qs = [q for q in questions if q.get('subjectId') == 'geo']
    
    if len(geo_qs) != 640:
        print(f"Error: Expected exactly 640 questions for Geography, found {len(geo_qs)}.")
        sys.exit(1)
    print("✓ Exactly 640 questions found for Geography subject.")
    
    # Check uniqueness of IDs
    q_ids = [q.get('id') for q in geo_qs]
    if len(set(q_ids)) != 640:
        print("Error: Duplicate question IDs detected.")
        sys.exit(1)
    print("✓ All 640 question IDs are unique.")
    
    # Verify difficulty level distribution per chapter
    for ch_num in range(1, 9):
        ch_id = f"geo_ch{ch_num}"
        ch_qs = [q for q in geo_qs if q.get('chapterId') == ch_id]
        
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
            
        # Validate properties of each question
        for q in ch_qs:
            q_id = q.get('id')
            opts = q.get('options')
            if not isinstance(opts, dict) or sorted(list(opts.keys())) != ['a', 'b', 'c', 'd']:
                print(f"Error: Question {q_id} has invalid options key structure: {opts}")
                sys.exit(1)
            for k, v in opts.items():
                if not v or not str(v).strip():
                    print(f"Error: Question {q_id} has empty option {k}")
                    sys.exit(1)
            ans = q.get('correctAnswer')
            if ans not in ['a', 'b', 'c', 'd']:
                print(f"Error: Question {q_id} has invalid correct answer: '{ans}'")
                sys.exit(1)
            q_text = q.get('question')
            if not q_text or not q_text.strip():
                print(f"Error: Question {q_id} has empty question text")
                sys.exit(1)
                
    print("✓ All 8 chapters have exactly 23 easy, 27 medium, and 30 hard questions.")
    print("✓ All questions have valid text, 4 options (a, b, c, d), and a correct answer.")
    print("SUCCESS: Geography database verification complete.")

if __name__ == "__main__":
    main()
