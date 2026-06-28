import json
import os

print("Inspecting Somali JSON files in scratch/...")
for i in range(1, 10):
    path = f"scratch/somali_ch{i}.json"
    if not os.path.exists(path):
        print(f"File {path} does not exist!")
        continue
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"File: {path}")
    print(f"  Total questions: {len(data)}")
    easy = [q for q in data if q.get("difficultyLevel") == "easy"]
    med = [q for q in data if q.get("difficultyLevel") == "medium"]
    hard = [q for q in data if q.get("difficultyLevel") == "hard"]
    print(f"  Easy: {len(easy)}, Medium: {len(med)}, Hard: {len(hard)}")
    if data:
        print(f"  First question: {data[0].get('question')}")
