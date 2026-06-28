import json
import os
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    write_count = 0
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                for tc in data.get("tool_calls", []):
                    name = tc.get("name", "")
                    args = tc.get("args", {})
                    target_file = args.get("TargetFile", "") or args.get("AbsolutePath", "")
                    if "generate_arabic_subject.py" in target_file and name in ["write_to_file", "replace_file_content", "multi_replace_file_content"]:
                        write_count += 1
                        code = args.get("CodeContent", "") or args.get("ReplacementContent", "")
                        if code:
                            out_name = f"scratch/recovered_write_{write_count}_{name}.py"
                            with open(out_name, "w", encoding="utf-8") as out:
                                out.write(code)
                            print(f"Saved write #{write_count} (step {data.get('step_index')}) to {out_name} (length {len(code)})")
            except Exception as e:
                pass
                
    print(f"Extraction complete. Found {write_count} file writes.")

if __name__ == "__main__":
    main()
