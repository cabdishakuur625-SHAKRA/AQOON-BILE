import json

log_path = r'C:\Users\cabdi\.gemini\antigravity-ide\brain\7b99cae8-1835-4b93-8012-f71800e97b7d\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            content = str(data.get('content', ''))
            tool_calls = str(data.get('tool_calls', ''))
            if 'somali' in content.lower() or 'curricu' in content.lower() or 'somali' in tool_calls.lower():
                print(f"Step {data.get('step_index')}: {content[:100]}... / tools: {tool_calls[:100]}")
        except Exception as e:
            print(f"Error reading line {i}: {e}")
