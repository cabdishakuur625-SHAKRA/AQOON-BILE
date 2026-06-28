import json

def main():
    with open('lib/services/seed_data.dart', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('{', content.find("const String fullSeedJson = r'''"))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    subjects_list = data.get("subjects", [])
    
    # We want to extract specific chapter names
    target_chapters = {
        "his": [0, 1],
        "geo": [3],
        "bio": [0],
        "tarbiyo": [0],
        "somali": [0],
        "tech": [0],
        "eng": [0],
        "math": [0, 1],
        "arabic": [0],
        "phy": [0, 7],
        "chem": [0],
        "bus": [0]
    }
    
    for s in subjects_list:
        s_id = s.get("id")
        s_name = s.get("name")
        if s_id in target_chapters:
            chapters = s.get("chapters", [])
            for idx in target_chapters[s_id]:
                if idx < len(chapters):
                    print(f"Subject: {s_name} ({s_id}), Chapter Index: {idx}, Title: {chapters[idx].get('title')}")

if __name__ == "__main__":
    main()
