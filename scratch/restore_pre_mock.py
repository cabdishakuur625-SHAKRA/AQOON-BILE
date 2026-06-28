import json
import re
import os

JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\seed_data.json'
DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert from Object format to List format if needed
def to_list(obj_or_list, id_field="id"):
    if isinstance(obj_or_list, list):
        return obj_or_list
    res = []
    for k, v in obj_or_list.items():
        item = v.copy()
        item[id_field] = k
        res.append(item)
    return res

subjects = to_list(data['subjects'])
chapters = to_list(data['chapters'])
questions = to_list(data['questions'])

final_data = {
    "subjects": subjects,
    "chapters": chapters,
    "questions": questions
}

with open(DART_FILE, 'r', encoding='utf-8') as f:
    dart_content = f.read()

json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
if json_match:
    new_json_str = json.dumps(final_data, indent=2, ensure_ascii=False)
    new_dart_content = dart_content.replace(json_match.group(1).strip(), new_json_str)
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_dart_content)
    print(f"Restored data from just before Mock Exams. Total Questions: {len(questions)}")
else:
    print("Could not find fullSeedJson in seed_data.dart")
