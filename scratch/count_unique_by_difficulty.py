import json
import os

for i in range(1, 10):
    path = f"scratch/somali_ch{i}.json"
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    by_diff = {"easy": set(), "medium": set(), "hard": set()}
    for q in data:
        text = q["question"]
        if "Su'aasha" in text:
            text = text.split(":", 1)[1].strip()
        if "Nooca" in text:
            text = text.split("(", 1)[0].strip()
        diff = q.get("difficultyLevel", "easy")
        by_diff[diff].add(text.lower())
        
    print(f"Ch {i}: Easy: {len(by_diff['easy'])} unique, Medium: {len(by_diff['medium'])} unique, Hard: {len(by_diff['hard'])} unique")
