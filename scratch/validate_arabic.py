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
    arabic_sub = [s for s in subjects if s.get('id') == 'arabic']
    if not arabic_sub:
        print("Error: Subject 'arabic' not found in subjects list.")
        sys.exit(1)
    print("✓ Subject 'arabic' exists:", arabic_sub[0])
    
    # 2. Validate Chapters
    chapters = data.get('chapters', [])
    arabic_chaps = [c for c in chapters if c.get('subjectId') == 'arabic']
    if len(arabic_chaps) != 6:
        print(f"Error: Expected exactly 6 chapters for Arabic, found {len(arabic_chaps)}.")
        sys.exit(1)
    print("✓ Exactly 6 chapters found for Arabic subject.")
    
    expected_titles = {
        "arabic_ch1": "الوحدة الأولى: حروف الجر والنداء",
        "arabic_ch2": "الوحدة الثانية: الأدب والنثر والشعر",
        "arabic_ch3": "الوحدة الثالثة: البلاغة: التشبيه والاستعارة",
        "arabic_ch4": "الوحدة الرابعة: الخليفة عمر بن الخطاب رضي الله عنه",
        "arabic_ch5": "الوحدة الخامسة: القبلية وأضرار المخدرات",
        "arabic_ch6": "الوحدة السادسة: نوادر أشعب وحكايات صومالية"
    }
    
    for ch in arabic_chaps:
        ch_id = ch.get('id')
        title = ch.get('title')
        if ch_id not in expected_titles:
            print(f"Error: Unexpected chapter ID: {ch_id}")
            sys.exit(1)
        if title != expected_titles[ch_id]:
            print(f"Error: Chapter {ch_id} title mismatch. Expected: '{expected_titles[ch_id]}', Found: '{title}'")
            sys.exit(1)
    print("✓ All 6 Arabic chapter IDs and titles match expectations.")
    
    # 3. Validate Questions
    questions = data.get('questions', [])
    arabic_qs = [q for q in questions if q.get('subjectId') == 'arabic']
    
    if len(arabic_qs) != 462:
        print(f"Error: Expected exactly 462 questions for Arabic, found {len(arabic_qs)}.")
        sys.exit(1)
    print("✓ Exactly 462 questions found for Arabic subject.")
    
    # Check uniqueness of IDs
    q_ids = [q.get('id') for q in arabic_qs]
    if len(set(q_ids)) != 462:
        print("Error: Duplicate question IDs detected.")
        sys.exit(1)
    print("✓ All 462 question IDs are unique.")
    
    # Verify difficulty level distribution per chapter
    for ch_num in range(1, 7):
        ch_id = f"arabic_ch{ch_num}"
        ch_qs = [q for q in arabic_qs if q.get('chapterId') == ch_id]
        
        if len(ch_qs) != 77:
            print(f"Error: Chapter {ch_id} has {len(ch_qs)} questions, expected 77.")
            sys.exit(1)
            
        easy_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'easy'])
        med_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'medium'])
        hard_count = len([q for q in ch_qs if q.get('difficultyLevel') == 'hard'])
        
        if easy_count != 22:
            print(f"Error: Chapter {ch_id} has {easy_count} easy questions, expected 22.")
            sys.exit(1)
        if med_count != 25:
            print(f"Error: Chapter {ch_id} has {med_count} medium questions, expected 25.")
            sys.exit(1)
        if hard_count != 30:
            print(f"Error: Chapter {ch_id} has {hard_count} hard questions, expected 30.")
            sys.exit(1)
            
        # Validate properties of each question
        for q in ch_qs:
            q_id = q.get('id')
            # Check options structure
            opts = q.get('options')
            if not isinstance(opts, dict) or sorted(list(opts.keys())) != ['a', 'b', 'c', 'd']:
                print(f"Error: Question {q_id} has invalid options key structure: {opts}")
                sys.exit(1)
            for k, v in opts.items():
                if not v or not v.strip():
                    print(f"Error: Question {q_id} has empty option {k}")
                    sys.exit(1)
            # Check answer
            ans = q.get('correctAnswer')
            if ans not in ['a', 'b', 'c', 'd']:
                print(f"Error: Question {q_id} has invalid correct answer: '{ans}'")
                sys.exit(1)
            # Check text
            q_text = q.get('question')
            if not q_text or not q_text.strip():
                print(f"Error: Question {q_id} has empty question text")
                sys.exit(1)
                
    print("✓ All chapters have exactly 22 easy, 25 medium, and 30 hard questions.")
    print("✓ All questions have valid text, 4 options (a, b, c, d), and a correct answer.")
    print("SUCCESS: Arabic database verification complete.")

if __name__ == "__main__":
    main()
