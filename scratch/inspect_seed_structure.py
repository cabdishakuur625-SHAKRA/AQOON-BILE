import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    with open('lib/services/seed_data.dart', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('{', content.find("const String fullSeedJson = r'''"))
    end_idx = content.rfind("''';")
    
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Print chapters count and a sample
    chapters = data.get("chapters", [])
    print(f"Total root chapters: {len(chapters)}")
    if chapters:
        print("  Sample chapters (first 5):")
        for i, ch in enumerate(chapters[:5]):
            print(f"    - id: {ch.get('id')}, title: {ch.get('title')}, subjectId: {ch.get('subjectId')}")
            
    # Print questions count and a sample
    questions = data.get("questions", [])
    print(f"Total root questions: {len(questions)}")
    if questions:
        print("  Sample questions (first 5):")
        for i, q in enumerate(questions[:5]):
            print(f"    - id: {q.get('id')}, subjectId: {q.get('subjectId')}, chapterId: {q.get('chapterId')}, question: {q.get('question')[:50]}")

if __name__ == "__main__":
    main()
