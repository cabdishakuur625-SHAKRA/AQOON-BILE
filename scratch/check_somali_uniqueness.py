import json
import os

for i in range(1, 10):
    path = f"scratch/somali_ch{i}.json"
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    unique_questions = set()
    for q in data:
        # Strip "Su'aasha X: " or "Nooca X"
        text = q["question"]
        if "Su'aasha" in text:
            text = text.split(":", 1)[1].strip()
        if "Nooca" in text:
            text = text.split("(", 1)[0].strip()
        unique_questions.add(text.lower())
    print(f"File {path}: Total questions {len(data)}, Unique base questions {len(unique_questions)}")
