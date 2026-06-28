import re
import json

def main():
    with open('scratch/generate_arabic_subject.py', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    q_list = []
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        if '"q":' in line or "'q':" in line:
            try:
                clean_line = line.strip()
                if clean_line.endswith(','):
                    clean_line = clean_line[:-1]
                
                q_match = re.search(r'"q":\s*"(.*?)"', clean_line)
                if not q_match:
                    q_match = re.search(r"'q':\s*'(.*?)'", clean_line)
                
                ans_match = re.search(r'"ans":\s*"(.*?)"', clean_line)
                if not ans_match:
                    ans_match = re.search(r"'ans':\s*'(.*?)'", clean_line)
                    
                opts_match = re.search(r'"opts":\s*\{(.*?)\}', clean_line)
                if not opts_match:
                    opts_match = re.search(r"'opts':\s*\{(.*?)\}", clean_line)
                    
                if q_match and ans_match:
                    q_text = q_match.group(1)
                    ans_text = ans_match.group(1)
                    opts_str = opts_match.group(1) if opts_match else ''
                    
                    opts = {}
                    for opt_k in ['a', 'b', 'c', 'd']:
                        opt_match = re.search(r'"' + opt_k + r'":\s*"(.*?)"', opts_str)
                        if not opt_match:
                            opt_match = re.search(r"'" + opt_k + r"':\s*'(.*?)'", opts_str)
                        if opt_match:
                            opts[opt_k] = opt_match.group(1)
                    
                    q_list.append({
                        'line': i,
                        'q': q_text,
                        'opts': opts,
                        'ans': ans_text
                    })
            except Exception as e:
                print(f'Error parsing line {i}: {e}')

    print(f'Found {len(q_list)} raw questions.')

    ch_keywords = {
        1: ['جر', 'نداء', 'منادى', 'مجرور', 'يا ', 'أداة النداء', 'يا أيها', 'المنادى', 'الاسم المجرور'],
        2: ['أدب', 'شعر', 'نثر', 'رثاء', 'هجاء', 'غزل', 'مدح', 'فخر', 'معلقة', 'معلقات', 'القافية', 'الوزن', 'البارودي', 'شوقي', 'الرابطة القلمية', 'المهجر', 'الديوان', 'المقامات', 'الجاحظ', 'كليلة ودمنة'],
        3: ['بلاغة', 'تشبيه', 'استعارة', 'مكنية', 'تصريحية', 'مجاز', 'كناية', 'إيجاز', 'إطناب', 'الخبر', 'الإنشاء', 'جناح الذل', 'ضحكت السماء', 'المنية'],
        4: ['عمر بن الخطاب', 'الفاروق', 'عمر بن العاص', 'أبو لؤلؤة', 'القادسية', 'اليرموك', 'عام الرمادة', 'أراضي السواد', 'ديوان الجند', 'ديوان العطاء', 'الحسبة', 'الخلافة', 'الشورى'],
        5: ['القبلية', 'المخدرات', 'عصبية', 'الإدمان', 'الدوبامين', 'سموم', 'قات', 'العشيرة', 'عشائر', 'الثأر', 'التعصب', 'النسب', 'غسيل الأموال', 'تحريم المخدرات'],
        6: ['أشعب', 'نوادر', 'حكايات شعبية', 'صومالية', 'الضبع', 'Waraabe', 'dawaco', 'الأرنب', 'جحا', 'البخلاء', 'حود', 'Hodd']
    }

    classified = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    unclassified = []

    for q in q_list:
        text = q['q'] + ' ' + ' '.join(q['opts'].values())
        found_ch = None
        for ch, keywords in ch_keywords.items():
            if any(kw in text for kw in keywords):
                found_ch = ch
                break
        if found_ch:
            classified[found_ch].append(q)
        else:
            unclassified.append(q)

    for ch, qs in classified.items():
        print(f'Chapter {ch}: {len(qs)} questions')

    print(f'Unclassified: {len(unclassified)}')
    for u in unclassified[:15]:
        safe_q = u["q"].encode("ascii", errors="replace").decode("ascii")
        print(f' - Line {u["line"]}: {safe_q}')

    # Output to a file
    with open('scratch/extracted_classified.json', 'w', encoding='utf-8') as f_out:
        json.dump(classified, f_out, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
