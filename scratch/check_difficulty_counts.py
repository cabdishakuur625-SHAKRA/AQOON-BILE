import json
import sys

def check():
    sys.stdout.reconfigure(encoding='utf-8')
    
    # Read from live seed_data.dart
    seed_file_path = 'lib/services/seed_data.dart'
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)

    chap_questions = {}

    # 1. From nested subjects/chapters/questions
    for s in data.get('subjects', []):
        subjectId = s.get('id')
        if 'chapters' in s and isinstance(s['chapters'], list):
            for chapIndex, c in enumerate(s['chapters'], 1):
                chap_id = c.get('id') or f"{subjectId}_ch{chapIndex}"
                # Nested questions
                if 'questions' in c and isinstance(c['questions'], list):
                    for q in c['questions']:
                        if isinstance(q, dict):
                            chap_questions.setdefault(chap_id, []).append(q)

    # 2. From flat questions list (referencing chapterId)
    for q in data.get('questions', []):
        if isinstance(q, dict):
            chap_id = q.get('chapterId')
            if chap_id:
                chap_questions.setdefault(chap_id, []).append(q)

    target_chapters = [
        "his_ch1", "geo_ch1", "bio_ch1", "tarbiyo_ch1", "somali_ch1",
        "tech_ch1", "eng_ch1", "math_ch1", "arabic_ch1", "phy_ch1",
        "chem_ch1", "bus_ch1", "his_ch2", "math_ch2", "phy_ch2"
    ]

    print("Chapter ID | Easy | Medium | Hard | Medium+Hard")
    print("-" * 50)
    for cid in target_chapters:
        qs = chap_questions.get(cid, [])
        easy = sum(1 for q in qs if q.get('difficultyLevel', '').lower() == 'easy')
        med = sum(1 for q in qs if q.get('difficultyLevel', '').lower() == 'medium')
        hard = sum(1 for q in qs if q.get('difficultyLevel', '').lower() == 'hard')
        tot_mh = med + hard
        print(f"{cid:<10} | {easy:<4} | {med:<6} | {hard:<4} | {tot_mh:<11}")

if __name__ == "__main__":
    check()
