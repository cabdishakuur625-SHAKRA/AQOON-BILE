import json
import re
import os

text_file = r'c:\flutterApp\Aqoon_Bile\scratch\extracted_texts\buug Juqraafi S&J.txt'

with open(text_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

chapters = []
current_chapter = None
questions = []

# Regex for chapter headings
chapter_pattern = re.compile(r'Cutubka (\d+)[aad]*:\s*(.*)')

# Regex for question start (e.g. "1:", "1.", "14.")
q_start_pattern = re.compile(r'^(\d+)\s*[:\.]\s*(.*)')

# Regex for options (B., T., J., X.)
option_pattern = re.compile(r'^([BTJX])\.\s*(.*)')
correct_option_pattern = re.compile(r'^⸨([BTJX])\.⸩\s*(.*)')

# Map Somali options to a, b, c, d
option_map = {'B': 'a', 'T': 'b', 'J': 'c', 'X': 'd'}

def clean_text(text):
    # Remove things like "Hassan Mohamud Ali 0615-917110 Page X"
    text = re.sub(r'Hassan Mohamud Ali.*Page \d+', '', text)
    # Remove repetitive headers
    text = text.replace('WEYDIN IYO WARCILIN MAADADA JUQRAAFI FASALKA 12AAD', '')
    return text.strip()

for i, line in enumerate(lines):
    line = line.strip()
    if not line: continue
    
    # Check for chapter heading
    chap_match = chapter_pattern.search(line)
    if chap_match:
        chap_num = chap_match.group(1)
        chap_title = clean_text(chap_match.group(2))
        current_chapter = {
            "id": f"Geography_Ch{chap_num}",
            "subjectId": "Geography",
            "title": f"Cutubka {chap_num}: {chap_title}"
        }
        chapters.append(current_chapter)
        continue
    
    # Check for question start
    q_match = q_start_pattern.match(line)
    if q_match and current_chapter:
        q_num = q_match.group(1)
        q_text = clean_text(q_match.group(2))
        
        # Look ahead for options or answer
        options = {}
        correct_answer = "a"
        difficulty = "medium"
        
        j = i + 1
        found_options = False
        while j < len(lines):
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            
            # If next line is another question or chapter, stop
            if q_start_pattern.match(next_line) or chapter_pattern.search(next_line):
                break
            
            # Check for J: (open answer)
            if next_line.startswith('J:') or next_line.startswith('J-'):
                ans_text = clean_text(next_line[2:])
                # Continue reading if it spans multiple lines
                k = j + 1
                while k < len(lines):
                    cont_line = lines[k].strip()
                    if not cont_line or q_start_pattern.match(cont_line) or chapter_pattern.search(cont_line) or option_pattern.match(cont_line):
                        break
                    ans_text += " " + clean_text(cont_line)
                    k += 1
                
                options = {
                    "a": ans_text,
                    "b": "Jawaab qaldan 1",
                    "c": "Jawaab qaldan 2",
                    "d": "Jawaab qaldan 3"
                }
                found_options = True
                break
                
            # Check for multiple choice options
            opt_match = option_pattern.match(next_line)
            c_opt_match = correct_option_pattern.match(next_line)
            
            if c_opt_match:
                opt_key = option_map.get(c_opt_match.group(1))
                options[opt_key] = clean_text(c_opt_match.group(2))
                correct_answer = opt_key
                found_options = True
            elif opt_match:
                opt_key = option_map.get(opt_match.group(1))
                options[opt_key] = clean_text(opt_match.group(2))
                found_options = True
            
            j += 1
            
        if found_options:
            # Fill missing options if any
            for key in ['a', 'b', 'c', 'd']:
                if key not in options:
                    options[key] = "N/A"
            
            questions.append({
                "id": f"geo_q_{len(questions)}",
                "subjectId": "Geography",
                "chapterId": current_chapter["id"],
                "question": q_text,
                "options": options,
                "correctAnswer": correct_answer,
                "difficultyLevel": difficulty
            })

print(f"Extracted {len(chapters)} chapters and {len(questions)} questions.")

# Update seed_data.dart
dart_file = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'
with open(dart_file, 'r', encoding='utf-8') as f:
    dart_content = f.read()

json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
if json_match:
    json_str = json_match.group(1).strip()
    data = json.loads(json_str)
    
    # Keep only History subjects/chapters
    history_subjects = [s for s in data['subjects'] if s['id'] == 'History']
    history_chapters = [c for c in data['chapters'] if c['subjectId'] == 'History']
    history_questions = [q for q in data['questions'] if q['subjectId'] == 'History']
    
    # Add Geography
    geo_subjects = [{"id": "Geography", "name": "Geography"}]
    data['subjects'] = history_subjects + geo_subjects
    data['chapters'] = history_chapters + chapters
    data['questions'] = history_questions + questions
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_dart_content = dart_content.replace(json_match.group(1).strip(), new_json_str)
    
    with open(dart_file, 'w', encoding='utf-8') as f:
        f.write(new_dart_content)
    
    print("Updated seed_data.dart successfully with 8 chapters.")
else:
    print("Could not find fullSeedJson")
