import json
import re
import os
import sys

def clean_q(q):
    return q.strip()

def classify_question(q_text):
    q_lower = q_text.lower()
    
    # Keyword sets
    ch1_words = ["جر", "نداء", "مجرور", "منادى", "منادً", "أداة النداء", "حرف الجر", "المنادى", "يا ", "أيها", "الكسرة", "الفتحة", "الضمة", "السكون"]
    ch2_words = ["أدب", "نثر", "شعر", "معلقة", "ديوان", "خطابة", "البارودي", "شوقي", "مطران", "أبولو", "المهجر", "الرابطة القلمية", "النقائض", "البحتري", "الأغاني", "صدر الإسلام", "المرسل"]
    ch3_words = ["تشبيه", "استعارة", "كناية", "مجاز", "إيجاز", "إطناب", "مساواة", "بيان", "بديع", "معاني", "فصاحة", "بلاغ", "قرينة", "بليغ", "مكنية", "تصريحية", "تمثيلي"]
    ch4_words = ["عمر", "خطاب", "فاروق", "خلافة", "الرمادة", "الأمصار", "العطاء", "عهدة", "أمير المؤمنين", "القدس", "بيت المقدس", "ديوان الجند", "شريح", "عسس", "معركة القادسية", "يرموك", "عمرو بن العاص", "سعد بن أبي وقاص"]
    ch5_words = ["مخدر", "إدمان", "قبلية", "عصبية", "ثأر", "دوبامين", "سموم", "التحمل", "الانتكاسة", "قات", "عشائر", "نسب", "أنساب", "تعارفوا", "أتقاكم", "شعباً وقبائل", "التهلكة", "التدخين"]
    ch6_words = ["أشعب", "طمع", "نوادر", "جحا", "حكاية", "صومال", "جاحظ", "بخلاء", "تطفل", "أرنب", "ضبع", "ثعلب", "أسد", "فولكلور", "خيال شعب", "ألف ليلة", "بادية", "مقامات", "سجع"]
    
    # Special grammar-specific checks to avoid false matches
    if any(w in q_lower for w in ["حرف الجر", "المنادى", "يا م", "يا ط"]):
        return 1
        
    # Check words
    score = [0] * 7
    for w in ch1_words:
        if w in q_lower: score[1] += 1
    for w in ch2_words:
        if w in q_lower: score[2] += 1
    for w in ch3_words:
        if w in q_lower: score[3] += 1
    for w in ch4_words:
        if w in q_lower: score[4] += 1
    for w in ch5_words:
        if w in q_lower: score[5] += 1
    for w in ch6_words:
        if w in q_lower: score[6] += 1
        
    max_score = max(score)
    if max_score > 0:
        return score.index(max_score)
        
    # Fallback heuristic
    if "العدالة" in q_lower or "المساواة" in q_lower or "الإسلام" in q_lower or "القصاص" in q_lower or "الطبقي" in q_lower or "التربية" in q_lower:
        return 5
    if "القصص" in q_lower or "الرواية" in q_lower or "الأمثال" in q_lower or "السخرية" in q_lower:
        return 6
        
    return 6 # default fallback

def add_questions_from_text(text, source_name, pool):
    # Match pattern {"q": "...", "opts": {...}, "ans": "..."}
    matches = re.finditer(r'\{\s*"q":\s*"(.*?)",\s*"opts":\s*\{(.*?)\},\s*"ans":\s*"(.*?)"\s*\}', text, re.DOTALL)
    count = 0
    for m in matches:
        q_text = clean_q(m.group(1))
        opts_str = m.group(2)
        ans_text = m.group(3).strip()
        
        # parse options
        opts = {}
        for opt_k in ['a', 'b', 'c', 'd']:
            opt_match = re.search(r'"' + opt_k + r'":\s*"(.*?)"', opts_str)
            if opt_match:
                opts[opt_k] = opt_match.group(1).strip()
                
        if q_text not in pool:
            pool[q_text] = {
                'q': q_text,
                'opts': opts,
                'ans': ans_text,
                'sources': [source_name]
            }
        else:
            if source_name not in pool[q_text]['sources']:
                pool[q_text]['sources'].append(source_name)
        count += 1
    print(f"Parsed {count} questions from text source: {source_name}")

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    pool = {}
    
    # 1. Parse current generate_arabic_subject.py
    if os.path.exists("scratch/generate_arabic_subject.py"):
        with open("scratch/generate_arabic_subject.py", "r", encoding="utf-8") as f:
            add_questions_from_text(f.read(), "generate_arabic_subject.py", pool)
            
    # 2. Parse temp_inspect.txt
    if os.path.exists("scratch/temp_inspect.txt"):
        with open("scratch/temp_inspect.txt", "r", encoding="utf-8") as f:
            add_questions_from_text(f.read(), "temp_inspect.txt", pool)
            
    # 3. Parse rebuild_arabic_generator.py
    if os.path.exists("scratch/rebuild_arabic_generator.py"):
        with open("scratch/rebuild_arabic_generator.py", "r", encoding="utf-8") as f:
            add_questions_from_text(f.read(), "rebuild_arabic_generator.py", pool)
            
    # 4. Parse fix_arabic_script.py
    if os.path.exists("scratch/fix_arabic_script.py"):
        with open("scratch/fix_arabic_script.py", "r", encoding="utf-8") as f:
            add_questions_from_text(f.read(), "fix_arabic_script.py", pool)

    # 5. Parse extracted_classified.json
    if os.path.exists("scratch/extracted_classified.json"):
        try:
            with open("scratch/extracted_classified.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            json_count = 0
            for k, val in data.items():
                for q_item in val:
                    q_text = clean_q(q_item.get("q", ""))
                    opts = q_item.get("opts", {})
                    ans_text = q_item.get("ans", "")
                    if q_text and q_text not in pool:
                        pool[q_text] = {
                            'q': q_text,
                            'opts': opts,
                            'ans': ans_text,
                            'sources': ["extracted_classified.json"]
                        }
                        json_count += 1
            print(f"Added {json_count} questions from extracted_classified.json")
        except Exception as e:
            print(f"Error parsing json: {e}")
            
    print(f"\nTotal unique questions collected in pool: {len(pool)}")
    
    # Classify them into chapters
    chapters = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for q_text, q_obj in pool.items():
        ch_num = classify_question(q_text)
        chapters[ch_num].append(q_obj)
        
    print("\nClassification breakdown:")
    for ch_num, qs in chapters.items():
        print(f"  Chapter {ch_num}: {len(qs)} unique questions")
        
    # Write pool to file
    with open("scratch/master_question_pool.json", "w", encoding="utf-8") as f_out:
        json.dump(chapters, f_out, indent=2, ensure_ascii=False)
    print("\nSaved classified pool to scratch/master_question_pool.json")

if __name__ == "__main__":
    main()
