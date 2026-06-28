def main():
    script_path = "scratch/generate_arabic_subject.py"
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Fix 1: triple easy = [ in create_ch4_questions
    bad_easy = "easy = [\neasy = [\neasy = [\n{\"q\":"
    if bad_easy in content:
        content = content.replace(bad_easy, "easy = [\n{\"q\":")
        print("Fixed duplicate easy = [ declarations")
    else:
        content = content.replace("easy = [\neasy = [\neasy = [", "easy = [")
        print("Applied flexible duplicate replacement")

    # Fix 2: Orphaned lines in create_ch6_questions
    idx = content.find("def create_ch6_questions():")
    if idx != -1:
        ret_idx = content.find("return easy, medium, hard", idx)
        if ret_idx != -1:
            main_idx = content.find("def main():", ret_idx)
            if main_idx != -1:
                # The section between ret_idx + len("return easy, medium, hard") and main_idx is what we want to clean
                between = content[ret_idx + len("return easy, medium, hard"):main_idx]
                print(f"Removing text between return and main() (length {len(between)} characters)")
                
                content = content[:ret_idx + len("return easy, medium, hard")] + "\n\n" + content[main_idx:]
                print("Cleaned up orphaned text between Ch6 return and main()")

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Syntax fixes applied successfully.")

if __name__ == "__main__":
    main()
