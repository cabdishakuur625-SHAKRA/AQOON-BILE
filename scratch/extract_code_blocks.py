import json
import os

def main():
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    out_path = r"c:\flutterApp\Aqoon_Bile\scratch\extracted_code_blocks.txt"
    
    with open(log_path, "r", encoding="utf-8", errors='ignore') as f:
        lines = f.readlines()
        
    targets = [664, 674, 777, 853, 879]
    with open(out_path, "w", encoding="utf-8") as out:
        for t in targets:
            if t <= len(lines):
                out.write(f"================ LINE {t} ================\n")
                try:
                    data = json.loads(lines[t - 1])
                    content = data.get("content", "")
                    out.write(content)
                    out.write("\n\n")
                except Exception as e:
                    out.write(f"Error parsing line {t}: {e}\n")
    print(f"Successfully extracted target code blocks to {out_path}")

if __name__ == "__main__":
    main()
