import json

def main():
    with open('lib/services/seed_data.dart', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('{', content.find("const String fullSeedJson = r'''"))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    print("Subject IDs:", [s.get('id') for s in data.get('subjects', [])])

if __name__ == "__main__":
    main()
