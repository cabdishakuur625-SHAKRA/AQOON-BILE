import json
import os

DART_FILE = r'lib/services/seed_data.dart'
JSON_FILE = r'scratch/seed_data.json'

def main():
    print("Reading seed_data.dart...")
    if not os.path.exists(DART_FILE):
        print(f"Error: {DART_FILE} not found.")
        return
        
    with open(DART_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate JSON boundaries in seed_data.dart")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Rebuild flat structure
    flat_data = {
        "subjects": {},
        "chapters": {},
        "questions": {}
    }
    
    # 1. Process subjects list
    subjects_list = data.get("subjects", [])
    print(f"Processing {len(subjects_list)} subjects from seed_data.dart...")
    for s in subjects_list:
        s_id = s.get("id")
        s_name = s.get("name")
        if not s_id or not s_name:
            continue
        flat_data["subjects"][s_id] = {"name": s_name}
        
        # Add nested chapters/questions if present
        chapters = s.get("chapters", [])
        for ch_idx, ch in enumerate(chapters):
            ch_id = ch.get("id") or f"{s_id}_ch{ch_idx+1}"
            ch_title = ch.get("title")
            flat_data["chapters"][ch_id] = {
                "subjectId": s_id,
                "title": ch_title
            }
            
            questions = ch.get("questions", [])
            for q in questions:
                q_id = q.get("id")
                if not q_id:
                    continue
                flat_data["questions"][q_id] = {
                    "question": q.get("question"),
                    "options": q.get("options"),
                    "correctAnswer": q.get("correctAnswer"),
                    "difficultyLevel": q.get("difficultyLevel"),
                    "subjectId": s_id,
                    "chapterId": ch_id
                }
                
    # 2. Process root chapters list (flat)
    root_chapters = data.get("chapters", [])
    print(f"Processing {len(root_chapters)} root chapters...")
    for ch in root_chapters:
        ch_id = ch.get("id")
        s_id = ch.get("subjectId")
        ch_title = ch.get("title")
        if not ch_id or not s_id:
            continue
        flat_data["chapters"][ch_id] = {
            "subjectId": s_id,
            "title": ch_title
        }
        
    # 3. Process root questions list (flat)
    root_questions = data.get("questions", [])
    print(f"Processing {len(root_questions)} root questions...")
    for q in root_questions:
        q_id = q.get("id")
        s_id = q.get("subjectId")
        ch_id = q.get("chapterId")
        if not q_id or not s_id or not ch_id:
            continue
        flat_data["questions"][q_id] = {
            "question": q.get("question"),
            "options": q.get("options"),
            "correctAnswer": q.get("correctAnswer"),
            "difficultyLevel": q.get("difficultyLevel"),
            "subjectId": s_id,
            "chapterId": ch_id
        }
        
    print(f"Compiled flat schema: {len(flat_data['subjects'])} subjects, {len(flat_data['chapters'])} chapters, {len(flat_data['questions'])} questions.")
    
    print(f"Writing to {JSON_FILE}...")
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(flat_data, f, indent=2, ensure_ascii=False)
        
    print("Synchronization complete!")

if __name__ == "__main__":
    main()
