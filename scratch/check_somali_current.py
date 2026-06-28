import json

seed_file_path = 'lib/services/seed_data.dart'
with open(seed_file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "const String fullSeedJson = r'''"
start_idx = content.find('{', content.find(start_str))
end_idx = content.rfind("''';")

if start_idx != -1 and end_idx != -1:
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    somali_sub = None
    for sub in data.get('subjects', []):
        if sub.get('id') == 'somali' or sub.get('name') == 'Somali':
            somali_sub = sub
            break
    if somali_sub:
        print("Somali Subject details:")
        print("Keys:", somali_sub.keys())
        print("Chapters count:", len(somali_sub.get('chapters', [])))
        for i, ch in enumerate(somali_sub.get('chapters', [])):
            qs = ch.get('questions', [])
            easy = [q for q in qs if q.get('difficultyLevel') == 'easy']
            med = [q for q in qs if q.get('difficultyLevel') == 'medium']
            hard = [q for q in qs if q.get('difficultyLevel') == 'hard']
            print(f"  Ch {i+1}: {ch.get('title')} | Questions: {len(qs)} (Easy: {len(easy)}, Med: {len(med)}, Hard: {len(hard)})")
    else:
        print("Somali subject not found in fullSeedJson subjects list.")
else:
    print("Failed to find boundaries in seed_data.dart")
