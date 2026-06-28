import sys
import os

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    script_path = "scratch/generate_arabic_subject.py"
    
    if not os.path.exists(script_path):
        print("File not found")
        return
        
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's count definitions of functions or let's import the file and call them!
    sys.path.append("scratch")
    try:
        import generate_arabic_subject
        
        funcs = [
            generate_arabic_subject.create_ch1_questions,
            generate_arabic_subject.create_ch2_questions,
            generate_arabic_subject.create_ch3_questions,
            generate_arabic_subject.create_ch4_questions,
            generate_arabic_subject.create_ch5_questions,
            generate_arabic_subject.create_ch6_questions,
        ]
        
        for idx, func in enumerate(funcs, 1):
            try:
                easy, med, hard = func()
                print(f"Chapter {idx}: Easy: {len(easy)}, Medium: {len(med)}, Hard: {len(hard)}, Total: {len(easy)+len(med)+len(hard)}")
            except Exception as e:
                print(f"Error calling create_ch{idx}_questions: {e}")
                
    except Exception as e:
        print(f"Error importing generate_arabic_subject: {e}")

if __name__ == "__main__":
    main()
