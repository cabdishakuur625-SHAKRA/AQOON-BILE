import json
import os

def main():
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    out_path = r"c:\flutterApp\Aqoon_Bile\scratch\logs_output.txt"
    
    if not os.path.exists(log_path):
        print(f"Log path {log_path} not found.")
        return

    out_file = open(out_path, "w", encoding="utf-8")

    with open(log_path, "r", encoding="utf-8", errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            if "create_ch5_questions" in line or "create_ch6_questions" in line:
                out_file.write(f"=== Found target in line {line_num} ===\n")
                try:
                    data = json.loads(line)
                    
                    if "tool_calls" in data:
                        for tc in data["tool_calls"]:
                            args = tc.get("args", {})
                            for k, v in args.items():
                                if isinstance(v, str) and ("create_ch5_questions" in v or "create_ch6_questions" in v):
                                    out_file.write(f"Tool call arg '{k}' contains it. Length: {len(v)}\n")
                                    for func in ["def create_ch4_questions", "def create_ch5_questions", "def create_ch6_questions"]:
                                        idx = v.find(func)
                                        if idx != -1:
                                            out_file.write(f"Found {func} at index {idx}:\n")
                                            out_file.write(v[idx:idx+8000] + "\n")
                    
                    content = data.get("content", "")
                    if content and ("create_ch5_questions" in content or "create_ch6_questions" in content):
                        out_file.write(f"Content contains it. Length: {len(content)}\n")
                        for func in ["def create_ch4_questions", "def create_ch5_questions", "def create_ch6_questions"]:
                            idx = content.find(func)
                            if idx != -1:
                                out_file.write(f"Found {func} in content:\n")
                                out_file.write(content[idx:idx+8000] + "\n")
                                
                except Exception as e:
                    out_file.write(f"Error parsing line {line_num}: {e}\n")

    out_file.close()
    print("Done writing matches to scratch/logs_output.txt")

if __name__ == "__main__":
    main()
