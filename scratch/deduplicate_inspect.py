import re
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    with open("scratch/temp_inspect.txt", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    matches = re.finditer(r'\{\s*"q":\s*"(.*?)",\s*"opts":\s*\{(.*?)\},\s*"ans":\s*"(.*?)"\s*\}', content, re.DOTALL)
    
    ch4_qs = {}
    ch5_qs = {}
    ch6_qs = {}
    
    for m in matches:
        q_text = m.group(1).strip()
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
            ch4_qs[q_text] = q_obj
        elif any(w in q_text for w in ["مخدر", "سموم", "قبلية", "عصبية", "ثأر", "إدمان", "الدوبامين", "التحمل", "المنبهة", "الانتكاسة", "القات", "العشائري", "القرابة", "الأنساب", "تعارفوا", "أتقاكم", "شرفاً"]):
            ch5_qs[q_text] = q_obj
        elif any(w in q_text for w in ["أشعب", "طمع", "نوادر", "جحا", "حكاية", "فولكلور", "صومالي", "الجاحظ", "الأرانب", "السخرية", "المقامات", "تطفل", "البخلاء", "الشعبية", "الشفهية", "ألف ليلة", "الأرنب", "الضبع", "البادية"]):
            ch6_qs[q_text] = q_obj
        else:
            if "القصاص" in q_text or "العدالة" in q_text or "المساواة" in q_text or "الإسلام" in q_text or "الحج" in q_text or "الطبقي" in q_text or "التهلكة" in q_text or "التدخين" in q_text or "مروجي" in q_text:
                ch5_qs[q_text] = q_obj
            else:
                ch6_qs[q_text] = q_obj
                
    print(f"Unique Ch4: {len(ch4_qs)}")
    print(f"Unique Ch5: {len(ch5_qs)}")
    print(f"Unique Ch6: {len(ch6_qs)}")

if __name__ == "__main__":
    main()
