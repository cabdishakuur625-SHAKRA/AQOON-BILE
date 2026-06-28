import json
import sys
from collections import Counter

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    
    seed_file_path = 'lib/services/seed_data.dart'
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    ch_subjects = [ch.get('subjectId') for ch in data.get('chapters', [])]
    q_subjects = [q.get('subjectId') for q in data.get('questions', [])]
    
    print("Top-level chapters count by subjectId:")
    for sub, count in Counter(ch_subjects).items():
        print(f"  Subject: {sub} | Chapters count: {count}")
        
    print("\nTop-level questions count by subjectId:")
    for sub, count in Counter(q_subjects).items():
        print(f"  Subject: {sub} | Questions count: {count}")

if __name__ == "__main__":
    main()
