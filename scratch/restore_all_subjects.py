import json
import re
import os

# --- PATHS ---
TEXTS_DIR = r'c:\flutterApp\Aqoon_Bile\scratch\extracted_texts'
DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'

def extract_geo():
    file_path = os.path.join(TEXTS_DIR, 'buug Juqraafi S&J.txt')
    chapters = []
    questions = []
    if not os.path.exists(file_path): return [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    chapter_pattern = re.compile(r'Cutubka (\d+)[aad]*:\s*(.*)')
    q_start_pattern = re.compile(r'^(\d+)\s*[:\.]\s*(.*)')
    option_pattern = re.compile(r'^([BTJX])\.\s*(.*)')
    correct_option_pattern = re.compile(r'^⸨([BTJX])\.⸩\s*(.*)')
    option_map = {'B': 'a', 'T': 'b', 'J': 'c', 'X': 'd'}
    current_chapter = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        chap_match = chapter_pattern.search(line)
        if chap_match:
            chap_num = chap_match.group(1)
            current_chapter = {"id": f"geo_ch{chap_num}", "subjectId": "geo", "title": f"Cutubka {chap_num}: {chap_match.group(2).strip()}"}
            chapters.append(current_chapter)
            continue
        q_match = q_start_pattern.match(line)
        if q_match and current_chapter:
            q_text = q_match.group(2).strip()
            options = {"a": "N/A", "b": "N/A", "c": "N/A", "d": "N/A"}
            correct = "a"
            j = i + 1
            while j < len(lines) and not q_start_pattern.match(lines[j]) and not chapter_pattern.search(lines[j]):
                l = lines[j].strip()
                if l.startswith('J:') or l.startswith('J-'):
                    options['a'] = l[2:].strip()
                c_opt = correct_option_pattern.match(l)
                if c_opt:
                    k = option_map.get(c_opt.group(1))
                    options[k] = c_opt.group(2).strip()
                    correct = k
                elif option_pattern.match(l):
                    opt = option_pattern.match(l)
                    k = option_map.get(opt.group(1))
                    options[k] = opt.group(2).strip()
                j += 1
            questions.append({"id": f"geo_q_{len(questions)}", "subjectId": "geo", "chapterId": current_chapter["id"], "question": q_text, "options": options, "correctAnswer": correct, "difficultyLevel": "medium"})
    return chapters, questions

def extract_islamic():
    file_path = os.path.join(TEXTS_DIR, 'TarbiyoDhameystiran-Reduced.txt')
    chapters = []
    questions = []
    if not os.path.exists(file_path): return [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by lessons/chapters
    parts = re.split(r'عزديا\s*[:]\s*(.*)', content)
    for i in range(1, len(parts), 2):
        chap_title = parts[i].strip()
        part_content = parts[i+1]
        chap_id = f"islam_ch{i//2 + 1}"
        chapters.append({"id": chap_id, "subjectId": "islam", "title": chap_title})
        
        # Look for question blocks
        q_blocks = re.split(r'ع(\d+)', part_content)
        for j in range(1, len(q_blocks), 2):
            q_body = q_blocks[j+1].split(':')[0].strip()
            if q_body:
                questions.append({"id": f"islam_q_{len(questions)}", "subjectId": "islam", "chapterId": chap_id, "question": q_body, "options": {"a": "Answer in textbook", "b": "N/A", "c": "N/A", "d": "N/A"}, "correctAnswer": "a", "difficultyLevel": "medium"})
    return chapters, questions

# --- MAIN ---
subjects = [
    {"id": "bio", "name": "Biology"},
    {"id": "chem", "name": "Chemistry"},
    {"id": "phy", "name": "Physics"},
    {"id": "som", "name": "Somali"},
    {"id": "his", "name": "History"},
    {"id": "geo", "name": "Geography"},
    {"id": "islam", "name": "Islamic Studies"}
]

with open(DART_FILE, 'r', encoding='utf-8') as f:
    dart_content = f.read()
json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
current_data = json.loads(json_match.group(1))

h_chapters = [c for c in current_data['chapters'] if c['subjectId'] in ['History', 'his']]
for c in h_chapters: c['subjectId'] = 'his'
h_questions = [q for q in current_data['questions'] if q['subjectId'] in ['History', 'his']]
for q in h_questions: q['subjectId'] = 'his'

g_chapters, g_questions = extract_geo()
i_chapters, i_questions = extract_islamic()

# Merge all
all_chapters = h_chapters + g_chapters + i_chapters
all_questions = h_questions + g_questions + i_questions

# Add placeholders for others if empty
if not any(c['subjectId'] == 'bio' for c in all_chapters):
    all_chapters.append({"id": "bio_ch1", "subjectId": "bio", "title": "General Biology"})
    all_questions.append({"id": "bio_q1", "subjectId": "bio", "chapterId": "bio_ch1", "question": "Placeholder question", "options": {"a": "A", "b": "B", "c": "C", "d": "D"}, "correctAnswer": "a", "difficultyLevel": "easy"})

if not any(c['subjectId'] == 'chem' for c in all_chapters):
    all_chapters.append({"id": "chem_ch1", "subjectId": "chem", "title": "General Chemistry"})
    all_questions.append({"id": "chem_q1", "subjectId": "chem", "chapterId": "chem_ch1", "question": "Placeholder question", "options": {"a": "A", "b": "B", "c": "C", "d": "D"}, "correctAnswer": "a", "difficultyLevel": "easy"})

if not any(c['subjectId'] == 'phy' for c in all_chapters):
    all_chapters.append({"id": "phy_ch1", "subjectId": "phy", "title": "General Physics"})
    all_questions.append({"id": "phy_q1", "subjectId": "phy", "chapterId": "phy_ch1", "question": "Placeholder question", "options": {"a": "A", "b": "B", "c": "C", "d": "D"}, "correctAnswer": "a", "difficultyLevel": "easy"})

if not any(c['subjectId'] == 'som' for c in all_chapters):
    all_chapters.append({"id": "som_ch1", "subjectId": "som", "title": "General Somali"})
    all_questions.append({"id": "som_q1", "subjectId": "som", "chapterId": "som_ch1", "question": "Placeholder question", "options": {"a": "A", "b": "B", "c": "C", "d": "D"}, "correctAnswer": "a", "difficultyLevel": "easy"})

final_data = {"subjects": subjects, "chapters": all_chapters, "questions": all_questions}
new_json_str = json.dumps(final_data, indent=2, ensure_ascii=False)
new_dart_content = dart_content.replace(json_match.group(1).strip(), new_json_str)

with open(DART_FILE, 'w', encoding='utf-8') as f:
    f.write(new_dart_content)

print(f"Restoration complete! Total subjects: {len(subjects)}, Chapters: {len(all_chapters)}, Questions: {len(all_questions)}")
