import json
import os
import re

extracted_dir = r"c:\flutterApp\Aqoon_Bile\scratch\extracted_texts"
output_file = r"c:\flutterApp\Aqoon_Bile\scratch\full_seed_data.json"

subjects = {
    "bio": {"name": "Biology", "file": "Biology Chapter Questions and answers Form Four.txt"},
    "chem": {"name": "Chemistry", "file": "Chemistry Quiz One F4.txt"},
    "phy": {"name": "Physics", "file": "physics practice all chapter.txt"},
    "som": {"name": "Somali", "file": "F4 afsoomaali weydiimo _240515_174222.txt"},
    "his": {"name": "History", "file": "Taariikh weydiimo iyo warcilin.txt"},
    "islam": {"name": "Islamic Studies", "file": "TarbiyoDhameystiran-Reduced.txt"},
    "geo": {"name": "Geography", "file": "buug Juqraafi S&J.txt"}
}

seed_data = {
    "subjects": [],
    "chapters": [],
    "questions": []
}

for s_id, s_info in subjects.items():
    seed_data["subjects"].append({"id": s_id, "name": s_info["name"]})
    
    file_path = os.path.join(extracted_dir, s_info["file"])
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Basic logic to find chapters and questions
    # This is a simplified version to get a good batch for each
    if s_id == "chem":
        # Parse Chemistry MCQs
        matches = re.findall(r"(\d+)\.\s+(.*?)\s+a\.\s+(.*?)\s+b\.\s+(.*?)\s+c\.\s+(.*?)\s+d\.\s+(.*)", content)
        ch_id = f"{s_id}_ch1"
        seed_data["chapters"].append({"id": ch_id, "subjectId": s_id, "title": "Organic Chemistry"})
        for i, m in enumerate(matches[:20]): # Take first 20
            seed_data["questions"].append({
                "id": f"q_{s_id}_{i}",
                "subjectId": s_id,
                "chapterId": ch_id,
                "question": m[1].strip(),
                "options": {"a": m[2].strip(), "b": m[3].strip(), "c": m[4].strip(), "d": m[5].strip()},
                "correctAnswer": "a", # Placeholder, would need more complex logic to find "circle the correct answer"
                "difficultyLevel": "easy"
            })
    elif s_id == "phy":
        # Parse Physics Q&A and turn into MCQs
        matches = re.findall(r"(\d+)\.(.*?)\n𝐒𝐨𝐥𝐮𝐭𝐢𝐨𝐧\n.*?T = ([\d\.]+)", content)
        ch_id = f"{s_id}_ch1"
        seed_data["chapters"].append({"id": ch_id, "subjectId": s_id, "title": "Waves & Oscillations"})
        for i, m in enumerate(matches[:15]):
            ans = m[2].strip()
            seed_data["questions"].append({
                "id": f"q_{s_id}_{i}",
                "subjectId": s_id,
                "chapterId": ch_id,
                "question": m[1].strip(),
                "options": {"a": ans, "b": "0.5", "c": "1.0", "d": "0.02"},
                "correctAnswer": "a",
                "difficultyLevel": "medium"
            })
    else:
        # Generic parser for others
        ch_id = f"{s_id}_ch1"
        seed_data["chapters"].append({"id": ch_id, "subjectId": s_id, "title": "General Principles"})
        # Just grab some lines as questions for now to ensure all subjects have data
        lines = [l for l in content.split("\n") if "?" in l]
        for i, l in enumerate(lines[:10]):
            seed_data["questions"].append({
                "id": f"q_{s_id}_{i}",
                "subjectId": s_id,
                "chapterId": ch_id,
                "question": l.strip(),
                "options": {"a": "Correct Answer Placeholder", "b": "Option B", "c": "Option C", "d": "Option D"},
                "correctAnswer": "a",
                "difficultyLevel": "easy"
            })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(seed_data, f, indent=2)

print(f"Generated seed data for {len(seed_data['subjects'])} subjects")
