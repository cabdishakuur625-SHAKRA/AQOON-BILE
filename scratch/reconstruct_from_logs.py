import json
import os
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    log_path = r"C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl"
    
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    records = []
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, 1):
            if "generate_arabic_subject.py" in line:
                try:
                    data = json.loads(line)
                    # Is it a tool call or content?
                    source = data.get("source", "")
                    step = data.get("step_index", "")
                    
                    # Check in tool_calls
                    for tc in data.get("tool_calls", []):
                        name = tc.get("name", "")
                        args = tc.get("args", {})
                        if "generate_arabic_subject.py" in str(args):
                            records.append({
                                'line_num': line_num,
                                'step': step,
                                'type': 'tool_call',
                                'name': name,
                                'args': args
                            })
                            
                    # Check in content (tool response or model output)
                    content = data.get("content", "")
                    if "generate_arabic_subject.py" in content:
                        records.append({
                            'line_num': line_num,
                            'step': step,
                            'type': 'content',
                            'length': len(content),
                            'snippet': content[:150]
                        })
                except Exception as e:
                    pass
                    
    print(f"Found {len(records)} records referencing generate_arabic_subject.py:")
    for r in records:
        if r['type'] == 'tool_call':
            args_summary = {k: (len(v) if isinstance(v, str) else v) for k, v in r['args'].items()}
            print(f"  Line {r['line_num']} (Step {r['step']}): Tool Call: {r['name']} args: {args_summary}")
        else:
            print(f"  Line {r['line_num']} (Step {r['step']}): Content length {r['length']}. Snippet: {r['snippet'].strip().replace('\n', ' ')}")

if __name__ == "__main__":
    main()
