import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    with open('scratch/seed_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subjects = data.get("subjects", {})
    chapters = data.get("chapters", {})
    
    sub_to_chaps = {}
    for ch_id, ch in chapters.items():
        sub_id = ch.get("subjectId")
        sub_to_chaps.setdefault(sub_id, []).append((ch_id, ch.get("title")))
        
    print("--- SUBJECTS AND CHAPTERS ---")
    for sub_id, sub_info in subjects.items():
        name = sub_info.get("name")
        chaps = sub_to_chaps.get(sub_id, [])
        print(f"\nSubject: {name} ({sub_id}) - total chapters: {len(chaps)}")
        for i, (ch_id, title) in enumerate(chaps[:2]):
            print(f"  Chapter {i+1}: {ch_id} -> {title}")

if __name__ == "__main__":
    main()
