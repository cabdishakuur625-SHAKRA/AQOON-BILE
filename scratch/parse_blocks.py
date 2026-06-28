import re
import json

def parse_questions_from_lines(lines, start_idx, end_idx):
    qs = []
    # Combine lines
    block_text = "".join(lines[start_idx:end_idx])
    # Find all dicts
    matches = re.finditer(r'\{\s*"q":\s*"(.*?)",\s*"opts":\s*\{(.*?)\},\s*"ans":\s*"(.*?)"\s*\}', block_text, re.DOTALL)
    for m in matches:
        q_text = m.group(1)
        opts_str = m.group(2)
        ans_text = m.group(3)
        
        # parse options
        opts = {}
        for opt_k in ['a', 'b', 'c', 'd']:
            opt_match = re.search(r'"' + opt_k + r'":\s*"(.*?)"', opts_str)
            if opt_match:
                opts[opt_k] = opt_match.group(1)
        
        qs.append({
            'q': q_text,
            'opts': opts,
            'ans': ans_text
        })
    return qs

def main():
    with open('scratch/generate_arabic_subject.py', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    # Let's find lines where lists start: easy = [, medium = [, hard = [
    # And trace line ranges.
    list_starts = []
    for i, line in enumerate(lines):
        if any(pat in line for pat in ['easy = [', 'medium = [', 'hard = [']):
            list_starts.append((i, line.strip()))
            
    print(f"List starts found at lines: {[ls[0]+1 for ls in list_starts]}")
    
    # Let's parse each list from its start to the next start or end of file
    for idx, (line_num, name) in enumerate(list_starts):
        start = line_num
        end = list_starts[idx+1][0] if idx+1 < len(list_starts) else len(lines)
        
        qs = parse_questions_from_lines(lines, start, end)
        safe_name = name[:25].encode('ascii', errors='replace').decode('ascii')
        print(f"List starting at line {start+1} ({safe_name}...): parsed {len(qs)} questions.")
        if qs:
            safe_q = qs[0]['q'].encode('ascii', errors='replace').decode('ascii')
            print(f"  First Q: {safe_q[:50]}")

if __name__ == '__main__':
    main()
