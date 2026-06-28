import json
import os
import sys
import traceback

def main():
    # Reconfigure stdout to support UTF-8 printing
    sys.stdout.reconfigure(encoding='utf-8')
    
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    
    if not os.path.exists(log_path):
        print(f"Log path {log_path} not found.")
        return

    with open(log_path, "r", encoding="utf-8", errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            if "create_ch5_questions" in line or "create_ch6_questions" in line:
                try:
                    data = json.loads(line)
                    
                    # Look for model output content
                    content = data.get("content", "")
                    if content and ("create_ch5_questions" in content or "create_ch6_questions" in content):
                        # Find python code blocks in content
                        if "```python" in content:
                            print(f"\n=== Found Code Block in Content at line {line_num} ===")
                            idx = content.find("```python")
                            end_code = content.find("```", idx + 9)
                            if end_code != -1:
                                code_block = content[idx:end_code+3]
                                if "create_ch5_questions" in code_block or "create_ch6_questions" in code_block:
                                    print(code_block)
                                    
                    # Look for tool call arguments
                    if "tool_calls" in data:
                        for tc in data["tool_calls"]:
                            args = tc.get("args", {})
                            for k, v in args.items():
                                if isinstance(v, str) and ("create_ch5_questions" in v or "create_ch6_questions" in v):
                                    print(f"\n=== Found in tool call {tc.get('name')} at line {line_num} ===")
                                    print(v)
                                    
                except Exception as e:
                    print(f"Error at line {line_num}:")
                    traceback.print_exc()

if __name__ == "__main__":
    main()
