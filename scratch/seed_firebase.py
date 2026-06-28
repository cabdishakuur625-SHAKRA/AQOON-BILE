import json
import urllib.request
import os

def main():
    json_path = 'scratch/seed_data.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    print(f"Reading {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build the nested Subjects structure:
    # Subjects / subject_id / name
    # Subjects / subject_id / Chapters / chapter_id / title
    # Subjects / subject_id / Chapters / chapter_id / Questions / q_id -> question
    subjects_node = {}

    # 1. Initialize subjects
    for s_id, s_info in data.get('subjects', {}).items():
        subjects_node[s_id] = {
            "name": s_info.get("name", ""),
            "Chapters": {}
        }
        
    # 2. Add chapters
    for c_id, c_info in data.get('chapters', {}).items():
        s_id = c_info.get('subjectId')
        title = c_info.get('title')
        if s_id in subjects_node:
            subjects_node[s_id]["Chapters"][c_id] = {
                "title": title,
                "Questions": {}
            }
            
    # 3. Add questions
    for q_id, q_info in data.get('questions', {}).items():
        s_id = q_info.get('subjectId')
        c_id = q_info.get('chapterId')
        if s_id in subjects_node:
            if c_id in subjects_node[s_id]["Chapters"]:
                subjects_node[s_id]["Chapters"][c_id]["Questions"][q_id] = {
                    "id": q_id,
                    "question": q_info.get("question"),
                    "options": q_info.get("options"),
                    "correctAnswer": q_info.get("correctAnswer"),
                    "difficultyLevel": q_info.get("difficultyLevel"),
                    "subjectId": s_id,
                    "chapterId": c_id
                }

    db_url = "https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app"
    
    print("Cleaning up database nodes...")
    for path in ["Subjects", "subjects", "chapters", "questions"]:
        try:
            req = urllib.request.Request(f"{db_url}/{path}.json", method='DELETE')
            urllib.request.urlopen(req)
            print(f"  Deleted /{path}")
        except Exception as e:
            print(f"  Failed to delete /{path}: {e}")
        
    print("Writing new nested Subjects data to Firebase...")
    try:
        req = urllib.request.Request(
            f"{db_url}/Subjects.json",
            data=json.dumps(subjects_node, ensure_ascii=False).encode('utf-8'),
            method='PUT'
        )
        urllib.request.urlopen(req)
        print("Success! Firebase Database successfully seeded via REST API.")
    except Exception as e:
        print(f"Failed to write Subjects: {e}")

if __name__ == "__main__":
    main()
