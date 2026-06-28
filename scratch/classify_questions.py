import re
import json

def main():
    with open("scratch/temp_inspect.txt", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    matches = re.finditer(r'\{\s*"q":\s*"(.*?)",\s*"opts":\s*\{(.*?)\},\s*"ans":\s*"(.*?)"\s*\}', content, re.DOTALL)
    
    ch4_qs = []
    ch5_qs = []
    ch6_qs = []
    
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
        
        # Classify
        if any(w in q_text for w in ["عمر", "خلافة", "الخطاب", "بدر", "أرض", "فتح", "ديوان", "بجوار", "الوثيقة", "أمير", "رعية", "عسّ", "الرمادة", "الأمصار", "العطاء", "العهدة"]):
            ch4_qs.append(q_obj)
        elif any(w in q_text for w in ["مخدر", "سموم", "قبلية", "عصبية", "ثأر", "إدمان", "الدوبامين", "التحمل", "المنبهة", "الانتكاسة", "القات", "العشائري", "القرابة", "الأنساب", "تعارفوا", "أتقاكم", "شرفاً"]):
            ch5_qs.append(q_obj)
        elif any(w in q_text for w in ["أشعب", "طمع", "نوادر", "جحا", "حكاية", "فولكلور", "صومالي", "الجاحظ", "الأرانب", "السخرية", "المقامات", "تطفل", "البخلاء", "الشعبية", "الشفهية", "ألف ليلة", "الأرنب", "الضبع", "البادية"]):
            ch6_qs.append(q_obj)
        else:
            # Fallback based on typical context if not matched
            if "القصاص" in q_text or "العدالة" in q_text or "المساواة" in q_text or "الإسلام" in q_text or "الحج" in q_text or "الطبقي" in q_text:
                ch5_qs.append(q_obj)
            else:
                ch6_qs.append(q_obj)
                
    with open("scratch/classified_temp_inspect.txt", "w", encoding="utf-8") as out:
        out.write(f"Total classified: {len(ch4_qs) + len(ch5_qs) + len(ch6_qs)}\n\n")
        
        out.write(f"=== Ch4 Questions ({len(ch4_qs)}) ===\n")
        for idx, q in enumerate(ch4_qs):
            out.write(f"{idx+1}. {q['q']}\n")
            
        out.write(f"\n=== Ch5 Questions ({len(ch5_qs)}) ===\n")
        for idx, q in enumerate(ch5_qs):
            out.write(f"{idx+1}. {q['q']}\n")
            
        out.write(f"\n=== Ch6 Questions ({len(ch6_qs)}) ===\n")
        for idx, q in enumerate(ch6_qs):
            out.write(f"{idx+1}. {q['q']}\n")

    print("Done classifying and writing.")

if __name__ == "__main__":
    main()
