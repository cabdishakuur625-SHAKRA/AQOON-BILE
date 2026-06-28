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
    math_sub = [s for s in subjects if s.get('id') == 'math']
    if not math_sub:
        print("Error: Subject 'math' not found in subjects list.")
        sys.exit(1)
    print("✓ Subject 'math' exists:", math_sub[0])
    
    # 2. Validate Chapters
    chapters = data.get('chapters', [])
    math_chaps = [c for c in chapters if c.get('subjectId') == 'math']
    if len(math_chaps) != 7:
        print(f"Error: Expected exactly 7 chapters for Math, found {len(math_chaps)}.")
        sys.exit(1)
    print("✓ Exactly 7 chapters found for Mathematics subject.")
    
    expected_titles = {
        "math_ch1": "Chapter 1: Circular Functions and Trigonometry",
        "math_ch2": "Chapter 2: Coordinate Geometry (Analytic Geometry)",
        "math_ch3": "Chapter 3: Geometry and Vectors",
        "math_ch4": "Chapter 4: Probability",
        "math_ch5": "Chapter 5: Complex Numbers",
        "math_ch6": "Chapter 6: Differentiation (Calculus)",
        "math_ch7": "Chapter 7: Limits, Continuity and Integration (Calculus)"
    }
    
    for ch in math_chaps:
        ch_id = ch.get('id')
        title = ch.get('title')
        if ch_id not in expected_titles:
            print(f"Error: Unexpected chapter ID: {ch_id}")
            sys.exit(1)
        if title != expected_titles[ch_id]:
            print(f"Error: Chapter {ch_id} title mismatch. Expected: '{expected_titles[ch_id]}', Found: '{title}'")
            sys.exit(1)
    print("✓ All 7 Math chapter IDs and titles match expectations.")
    
    # 3. Validate Questions
    questions = data.get('questions', [])
    math_qs = [q for q in questions if q.get('subjectId') == 'math']
    
    if len(math_qs) != 602:
        print(f"Error: Expected exactly 602 questions for Math, found {len(math_qs)}.")
        sys.exit(1)
    print("✓ Exactly 602 questions found for Mathematics subject.")
    
    # Check uniqueness of IDs
    q_ids = [q.get('id') for q in math_qs]
    if len(set(q_ids)) != 602:
        print("Error: Duplicate question IDs detected.")
        sys.exit(1)
    print("✓ All 602 question IDs are unique.")
    
    # Verify difficulty level distribution per chapter
    for ch_num in range(1, 8):
        ch_id = f"math_ch{ch_num}"
        ch_qs = [q for q in math_qs if q.get('chapterId') == ch_id]
        
        if len(ch_qs) != 86:
            print(f"Error: Chapter {ch_id} has {len(ch_qs)} questions, expected 86.")
            sys.exit(1)
            
        easy_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'easy'])
        med_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'medium'])
        hard_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'hard'])
        
        if easy_count != 25:
            print(f"Error: Chapter {ch_id} has {easy_count} easy questions, expected 25.")
            sys.exit(1)
        if med_count != 29:
            print(f"Error: Chapter {ch_id} has {med_count} medium questions, expected 29.")
            sys.exit(1)
        if hard_count != 32:
            print(f"Error: Chapter {ch_id} has {hard_count} hard questions, expected 32.")
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
                
        print(f"✓ Chapter {ch_id}: 86 questions total (25 easy, 29 medium, 32 hard) verified successfully.")
        
    print("\nDATABASE VALIDATION COMPLETED SUCCESSFULLY! ALL CHECKS PASSED!")

if __name__ == "__main__":
    import os
    main()
