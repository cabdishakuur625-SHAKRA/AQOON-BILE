import re
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    with open("scratch/temp_inspect.txt", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    matches = re.finditer(r'\{\s*"q":\s*"(.*?)",\s*"opts":\s*\{(.*?)\},\s*"ans":\s*"(.*?)"\s*\}', content, re.DOTALL)
    
    ch4_count = 0
    ch5_count = 0
    ch6_count = 0
    unknown = []
    
    questions = []
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
                
        q_obj = {'q': q_text, 'opts': opts, 'ans': ans_text}
        questions.append(q_obj)
        
        # Classify
        if any(w in q_text for w in ["عمر", "خلافة", "الخطاب", "بدر", "أرض", "فتح", "ديوان", "بجوار", "الوثيقة", "أمير"]):
            ch4_count += 1
        elif any(w in q_text for w in ["مخدر", "سموم", "قبلية", "عصبية", "ثأر", "إدمان", "الدوبامين", "التحمل", "المنبهة", "الانتكاسة", "القات", "العشائري"]):
            ch5_count += 1
        elif any(w in q_text for w in ["أشعب", "طمع", "نوادر", "جحا", "حكاية", "فولكلور", "صومالي", "الجاحظ", "الأرانب", "السخرية", "المقامات", "تطفل", "البخلاء"]):
            ch6_count += 1
        else:
            unknown.append(q_text)
            
    print(f"Total questions found: {len(questions)}")
    print(f"Ch4 (Umar): {ch4_count}")
    print(f"Ch5 (Drugs/Tribalism): {ch5_count}")
    print(f"Ch6 (Folktales): {ch6_count}")
    print(f"Unknown count: {len(unknown)}")
    if unknown:
        print("Unknown questions:")
        for u in unknown[:10]:
            print(f"  - {u}")

if __name__ == "__main__":
    main()
