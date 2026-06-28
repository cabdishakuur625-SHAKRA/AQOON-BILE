import json
import re

def main():
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    
    with open(log_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                content = str(data.get("content", ""))
                tool_calls = data.get("tool_calls", [])
                
                # Check for create_ch5_questions in content
                if "create_ch5_questions" in content or "def create_ch5_questions" in content:
                    print(f"Match in content at line {line_num}")
                    # Find and print code blocks
                    matches = re.findall(r"```python(.*?)```", content, re.DOTALL)
                    for idx, m in enumerate(matches):
                        print(f"--- Code block {idx} ---")
                        # print first 5 lines and last 5 lines
                        lines = m.strip().split("\n")
                        print("\n".join(lines[:10]))
                        print("...")
                        print("\n".join(lines[-10:]))
                
                for tc in tool_calls:
                    args = tc.get("args", {})
                    # If it's a file write or edit of generate_arabic_subject.py
                    target_file = args.get("TargetFile", "") or args.get("AbsolutePath", "")
                    if "generate_arabic_subject.py" in target_file:
                        print(f"Match in tool call at line {line_num}: {tc.get('name')}")
                        code = args.get("CodeContent", "") or args.get("ReplacementContent", "")
                        if code:
                            print(f"Found code content of length {len(code)}")
                            if "create_ch5_questions" in code:
                                print("Code contains create_ch5_questions!")
                                # Print around create_ch5_questions
                                idx = code.find("def create_ch5_questions()")
                                if idx != -1:
                                    print(code[idx:idx+1500])
                                    print("...")
                                    idx6 = code.find("def create_ch6_questions()")
                                    if idx6 != -1:
                                        print(code[idx6:idx6+1500])
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
