import json

def main():
    seed_file_path = 'lib/services/seed_data.dart'
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    print("Top-level keys in JSON:", list(data.keys()))
    for key in data.keys():
        val = data[key]
        if isinstance(val, list):
            print(f"Key '{key}': list of length {len(val)}")
            if len(val) > 0:
                print(f"  First item fields: {list(val[0].keys())}")
        else:
            print(f"Key '{key}': type {type(val)}")
            
    # Check subjects details
    print("\nSubjects list details:")
    for sub in data.get('subjects', []):
        print(f"  ID: {sub.get('id')} | Name: {sub.get('name')} | Has nested chapters: {'chapters' in sub}")

if __name__ == "__main__":
    main()
