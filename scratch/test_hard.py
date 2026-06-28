import re

def main():
    with open("scratch/generate_arabic_subject.py", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    matches = []
    for m in re.finditer("hard =", content):
        line_num = content[:m.start()].count("\n") + 1
        matches.append(f"Match at {m.start()} line {line_num}")
        
    print("\n".join(matches))

if __name__ == '__main__':
    main()
