import json
import sys

def main():
    # Force output to use utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    seed_file_path = 'lib/services/seed_data.dart'
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    print("Subjects:")
    for sub in data.get('subjects', []):
        name = sub.get('name')
        sub_id = sub.get('id')
        keys = list(sub.keys())
        print(f"  ID: {sub_id} | Name: {name} | Keys: {keys}")
        if 'chapters' in sub:
            ch_list = sub['chapters']
            print(f"    Nested chapters: {len(ch_list)}")
            if len(ch_list) > 0:
                print(f"    First nested chapter keys: {list(ch_list[0].keys())}")
                if 'questions' in ch_list[0]:
                    print(f"      Has nested questions: {len(ch_list[0]['questions'])}")

if __name__ == "__main__":
    main()
