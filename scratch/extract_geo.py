import json
import re
import os

text_file = r'c:\flutterApp\Aqoon_Bile\scratch\extracted_texts\buug Juqraafi S&J.txt'

with open(text_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to find questions. They often look like:
# 1. Question?
# J- Answer
# Or just start with a number.

questions = []
# Pattern: Number followed by . or ) then text ending with ?
pattern = r'(\d+)\s*[\.\)]\s*(.*?)\?\s*J-\s*(.*?)(?=\n\d+\s*[\.\)]|\Z)'
matches = re.finditer(pattern, content, re.DOTALL)

for i, match in enumerate(matches):
    num = match.group(1)
    q_text = match.group(2).strip() + "?"
    a_text = match.group(3).strip()
    
    # Create 4 options. Use the real answer as 'a' and others as placeholders.
    # In a real scenario, we'd want better options, but for now this populates the DB.
    questions.append({
        "id": f"geo_ch1_q{i+1}",
        "subjectId": "Geography",
        "chapterId": "Chapter 1",
        "question": q_text,
        "options": {
            "a": a_text,
            "b": "Jawaab qaldan 1",
            "c": "Jawaab qaldan 2",
            "d": "Jawaab qaldan 3"
        },
        "correctAnswer": "a",
        "difficultyLevel": "medium"
    })

# If we didn't find enough, try a broader pattern
if len(questions) < 5:
    pattern = r'(\d+)\s*[\.\)]\s*(.*?)\?\s*(.*?)(?=\n\d+\s*[\.\)]|\Z)'
    matches = re.finditer(pattern, content, re.DOTALL)
    questions = []
    for i, match in enumerate(matches):
        q_text = match.group(2).strip() + "?"
        a_text = match.group(3).strip()
        if "J-" in a_text:
            a_text = a_text.split("J-")[1].strip()
        
        questions.append({
            "id": f"geo_ch1_q{i+1}",
            "subjectId": "Geography",
            "chapterId": "Chapter 1",
            "question": q_text,
            "options": {
                "a": a_text,
                "b": "Ma ahan jawaabta saxda ah",
                "c": "Ma quseeyo",
                "d": "Waa qalad"
            },
            "correctAnswer": "a",
            "difficultyLevel": "medium"
        })

print(f"Extracted {len(questions)} questions.")

# Update seed_data.dart
dart_file = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
with open(dart_file, 'r', encoding='utf-8') as f:
    dart_content = f.read()

# Parse the JSON string inside the r''' ... '''
json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
if json_match:
    json_str = json_match.group(1).strip()
    data = json.loads(json_str)
    
    # Replace Geography questions
    # Keep original History questions
    history_questions = [q for q in data['questions'] if q['subjectId'] == 'History']
    data['questions'] = history_questions + questions
    
    # Ensure Geography chapter exists
    if not any(c['subjectId'] == 'Geography' for c in data['chapters']):
        data['chapters'].append({
            "id": "Chapter 1",
            "subjectId": "Geography",
            "title": "Cutubka 1: Guudmarka Juqraafiga"
        })
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_dart_content = dart_content.replace(json_match.group(1).strip(), new_json_str)
    
    with open(dart_file, 'w', encoding='utf-8') as f:
        f.write(new_dart_content)
    
    print("Updated seed_data.dart successfully.")
else:
    print("Could not find fullSeedJson in seed_data.dart")
