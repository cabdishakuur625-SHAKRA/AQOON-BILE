import json
import os
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    
    # 1. Load the master question pool
    pool_path = "scratch/master_question_pool.json"
    if not os.path.exists(pool_path):
        print(f"Error: {pool_path} not found. Run collect_all_questions.py first.")
        return
        
    with open(pool_path, "r", encoding="utf-8") as f:
        pool = json.load(f)
        
    # 2. Extract Ch5 and Ch6 questions from pool
    ch5_pool = pool.get("5", [])
    ch6_pool = pool.get("6", [])
    
    print(f"Loaded Ch5 pool size: {len(ch5_pool)}")
    print(f"Loaded Ch6 pool size: {len(ch6_pool)}")
    
    # Clean duplicates in pool lists just in case
    def deduplicate_list(qs):
        seen = set()
        unique_qs = []
        for q in qs:
            q_text = q['q'].strip()
            if q_text not in seen:
                seen.add(q_text)
                unique_qs.append(q)
        return unique_qs
        
    ch5_qs = deduplicate_list(ch5_pool)
    ch6_qs = deduplicate_list(ch6_pool)
    
    print(f"Unique Ch5 pool size: {len(ch5_qs)}")
    print(f"Unique Ch6 pool size: {len(ch6_qs)}")
    
    # Ensure Ch5 has at least 77 questions by adding new ones if needed
    while len(ch5_qs) < 77:
        # Add a new question
        new_q = {
            "q": f"ما هو الواجب المجتمعي والأسري تجاه المتعافين من الإدمان لمنع انتكاستهم؟",
            "opts": {
                "a": "احتضانهم ومساعدتهم على الاندماج والابتعاد عن رفقاء السوء وتقديم الدعم النفسي المستمر",
                "b": "التشهير بهم وعزلهم اجتماعياً وحرمانهم من حقوقهم في العمل والتعليم",
                "c": "سجنهم ونفيهم إلى مناطق نائية وقطع صلتهم بالأسرة والمجتمع تماماً",
                "d": "إعادة إعطائهم جرعات مخففة من المواد المخدرة تحت إشرافهم الخاص"
            },
            "ans": "a"
        }
        if new_q["q"] not in [q["q"] for q in ch5_qs]:
            ch5_qs.append(new_q)
            
    # Ensure Ch6 has at least 77 questions
    while len(ch6_qs) < 77:
        new_q = {
            "q": "ما هي الميزة الفنية الهامة في القصص الشعبية الصومالية التقليدية؟",
            "opts": {
                "a": "توصيل العبر الأخلاقية والقيم المجتمعية بأسلوب قصصي رمزي شيق يناسب الصغار والكبار",
                "b": "الاعتماد الكامل على الكتابة باللغات الأجنبية دون استخدام اللغة الوطنية الصومالية",
                "c": "الخلو التام من أي قيم تربوية أو دينية واقتصارها على التسلية الفارغة",
                "d": "استخدام المعادلات الرياضية المعقدة في وصف أحداث البادية"
            },
            "ans": "a"
        }
        if new_q["q"] not in [q["q"] for q in ch6_qs]:
            ch6_qs.append(new_q)
            
    # Partition Ch5 and Ch6 into 22 Easy, 25 Medium, 30 Hard
    ch5_easy = ch5_qs[:22]
    ch5_medium = ch5_qs[22:47]
    ch5_hard = ch5_qs[47:77]
    
    ch6_easy = ch6_qs[:22]
    ch6_medium = ch6_qs[22:47]
    ch6_hard = ch6_qs[47:77]
    
    # 3. Construct Ch4 questions
    # Let's define the 20 easy questions we recovered from generate_arabic_subject.py
    ch4_easy_recovered = [
        {"q": "من هو الخليفة الراشد الثاني للمسلمين؟", "opts": {"a": "عمر بن الخطاب رضي الله عنه", "b": "أبو بكر الصديق رضي الله عنه", "c": "عثمان بن عفان رضي الله عنه", "d": "علي بن أبي طالب رضي الله عنه"}, "ans": "a"},
        {"q": "ما هو اللقب الشهير الذي أطلقه النبي ﷺ على عمر بن الخطاب؟", "opts": {"a": "الفاروق", "b": "الصديق", "c": "ذو النورين", "d": "أسد الله"}, "ans": "a"},
        {"q": "لماذا لُقِّب عمر بن الخطاب بـ 'الفاروق'؟", "opts": {"a": "لأنه فرّق بين الحق والباطل بإسلامه وشجاعته وقراراته", "b": "لأنه فارق قبيلته وهاجر إلى الحبشة سراً", "c": "لأنه كان يفرق الأموال والمغانم بالتساوي المطلق", "d": "لأنه كتب التاريخ الهجري وفرق بين السنين والأشهر"}, "ans": "a"},
        {"q": "عمر بن الخطاب رضي الله عنه هو أحد:", "opts": {"a": "العشرة المبشرين بالجنة", "b": "الصحابة الذين هاجروا إلى الحبشة فقط", "c": "كتاب الوحي الذين لم يشاركوا في الغزوات", "d": "الخلفاء الذين تولوا الحكم بعد علي بن أبي طالب"}, "ans": "a"},
        {"q": "في أي مدينة وُلِد الخليفة عمر بن الخطاب رضي الله عنه؟", "opts": {"a": "مكة المكرمة", "b": "المدينة المنورة", "c": "الطائف", "d": "صنعاء"}, "ans": "a"},
        {"q": "من هي القبيلة القرشية التي ينتمي إليها عمر بن الخطاب؟", "opts": {"a": "بنو عدي", "b": "بنو هاشم", "c": "بنو أمية", "d": "بنو زهرة"}, "ans": "a"},
        {"q": "ما هو ترتيب إسلام عمر بن الخطاب بين الصحابة تقريباً (في أي سنة من البعثة)؟", "opts": {"a": "في السنة السادسة من البعثة النبوية بمكة", "b": "في السنة الأولى بعد الهجرة للمدينة المنورة", "c": "قبل البعثة النبوية بعدة سنوات طوال", "d": "يوم فتح مكة في السنة الثامنة للهجرة"}, "ans": "a"},
        {"q": "قبل إسلامه، اشتهر عمر بن الخطاب في مكة بـ:", "opts": {"a": "القوة والفروسية والمصارعة والسفارة وحفظ الأنساب", "b": "التجارة البحرية مع الحبشة واليمن فقط", "c": "ضعف البنية والانعزال عن شؤون قريش السياسية", "d": "كتابة الشعر العمودي في رثاء ملوك الفرس"}, "ans": "a"},
        {"q": "كيف كان إسلام عمر بن الخطاب رضي الله عنه تحولاً للمسلمين بمكة؟", "opts": {"a": "أصبح للمسلمين قوة وجهروا بصلاتهم ودينهم عند الكعبة وقرأوا القرآن علناً", "b": "تسبب في خروج المسلمين جميعاً من مكة إلى الشام مباشرة", "c": "أدى إلى استسلام قريش ودخولها الإسلام فوراً ودون قتال", "d": "أدى إلى وقف اضطهاد قريش لجميع العبيد الضعفاء بمكة"}, "ans": "a"},
        {"q": "كيف كانت هجرة عمر بن الخطاب رضي الله عنه إلى المدينة المنورة؟", "opts": {"a": "هاجر علناً متحدياً قريشاً ولم يجرؤ أحد على منعه أو اعتراضه", "b": "هاجر خفية متسللاً في الليل خوفاً من قريش وصبيانها", "c": "هاجر مع النبي ﷺ وأبو بكر الصديق في الغار الشهير", "d": "لم يهاجر إلى المدينة المنورة وبقي في مكة حتى وفاته"}, "ans": "a"},
        {"q": "كم دامت خلافة عمر بن الخطاب رضي الله عنه تقريباً؟", "opts": {"a": "حوالي 10 سنوات ونصف", "b": "سنتين وثلاثة أشهر فقط كأبي بكر", "c": "اثنتي عشرة سنة كاملة كعثمان بن عفان", "d": "خمس سنوات فقط كعلي بن أبي طالب"}, "ans": "a"},
        {"q": "أي من المعارك الشهيرة وقعت في عهد خلافة عمر بن الخطاب ضد الفرس؟", "opts": {"a": "القادسية (ونهاوند)", "b": "بدر الكبرى والفتح واليرموك الأولى", "c": "صفين والجمل والنهروان الداخلية", "d": "حطين وعين جالوت المتأخرة تاريخياً"}, "ans": "a"},
        {"q": "أي من المعارك الشهيرة وقعت في عهد خلافة عمر بن الخطاب ضد الروم البيزنطيين؟", "opts": {"a": "اليرموك (وفتح بيت المقدس الشريف)", "b": "القادسية والجلولاء ونهاوند الفارسية", "c": "ذات الصواري البحرية الإسلامية الأولى", "d": "تبوك وحنين والطائف النبوية"}, "ans": "a"},
        {"q": "من هو القائد المسلم الذي أرسله عمر بن الخطاب لفتح مصر؟", "opts": {"a": "عمرو بن العاص رضي الله عنه", "b": "خالد بن الوليد رضي الله عنه", "c": "سعد بن أبي وقاص رضي الله عنه", "d": "أبو عبيدة بن الجراح رضي الله عنه"}, "ans": "a"},
        {"q": "من هو القائد المسلم الذي قاد معركة القادسية الحاسمة ضد الفرس؟", "opts": {"a": "سعد بن أبي وقاص رضي الله عنه", "b": "خالد بن الوليد رضي الله عنه", "c": "شرحبيل بن حسنة رضي الله عنه", "d": "النعمان بن مقرن رضي الله عنه"}, "ans": "a"},
        {"q": "ما هو التقويم المعتمد الذي أنشأه الخليفة عمر بن الخطاب لتأريخ المعاملات الرسمية؟", "opts": {"a": "التقويم الهجري (بدءاً من هجرة الرسول ﷺ)", "b": "التقويم الميلادي الشمسي الغربي", "c": "التقويم القمري الجاهلي التقليدي لعمر الفيل", "d": "التقويم الفارسي الإيراني القديم"}, "ans": "a"},
        {"q": "ما هي 'الدواوين' التي استحدثها عمر بن الخطاب في الدولة الإسلامية؟", "opts": {"a": "سجلات رسمية لتنظيم الجند والرواتب والعطاء والضرائب وبيت المال", "b": "مجالس لإلقاء الشعر والخطابة ونقد القصائد الأدبية", "c": "غرف مخصصة لاستقبال السفراء الأجانب والوفود", "d": "مكتبات عامة لجمع وترجمة الكتب الأجنبية"}, "ans": "a"},
        {"q": "من هي الفئة الضعيفة التي كان عمر بن الخطاب يتفقد أحوالها بنفسه في الليل (يعسّ في المدينة)؟", "opts": {"a": "الفقراء والأرامل والأيتام وعابرو السبيل", "b": "كبار تجار قريش وملاك الأراضي الزراعية", "c": "فرسان قريش المتأهبون للقتال في الثغور والحدود", "d": "الشعراء والكتاب الباحثون عن الجوائز المالية"}, "ans": "a"},
        {"q": "أين استشهد الخليفة عمر بن الخطاب رضي الله عنه؟", "opts": {"a": "في المدينة المنورة وهو يصلي بالمسلمين الفجر في المسجد النبوي", "b": "في معركة القادسية بالسيوف والرماح ضد الفرس", "c": "في الشام متأثراً بطاعون عمواس الشهير تاريخياً", "d": "في مكة المكرمة عند الكعبة المشرفة بسهم طائش"}, "ans": "a"},
        {"q": "من هو الشخص الذي اغتال الخليفة عمر بن الخطاب رضي الله عنه؟", "opts": {"a": "أبو لؤلؤة المجوسي", "b": "عبد الرحمن بن ملجم", "c": "ابن سلول رأس النفاق بمكة", "d": "وحشي بن حرب الحبشي"}, "ans": "a"}
    ]
    
    # Let's add 2 new easy questions to make it 22
    ch4_easy_new = [
        {"q": "ما هي صلة القرابة بين عمر بن الخطاب رضي الله عنه وأم المؤمنين حفصة رضي الله عنها؟", "opts": {"a": "هو والدها", "b": "هو عمها", "c": "هو أخوها الأكبر", "d": "هو ابن خالتها"}, "ans": "a"},
        {"q": "بجوار من دُفن الخليفة عمر بن الخطاب رضي الله عنه بعد استشهاده بالمدينة المنورة؟", "opts": {"a": "بجوار النبي ﷺ وأبي بكر الصديق رضي الله عنه في الحجرة النبوية", "b": "في مقبرة البقيع العامة مع بقية الصحابة", "c": "في مقبرة المعلاة بمكة المكرمة مع أجداده", "d": "في بيت المقدس الشريف بفلسطين المحررة"}, "ans": "a"}
    ]
    
    ch4_easy = ch4_easy_recovered + ch4_easy_new
    
    # Load ch4 medium and hard questions from rebuild_arabic_generator.py by reading and executing the definitions
    rebuild_path = "scratch/rebuild_arabic_generator.py"
    try:
        with open(rebuild_path, "r", encoding="utf-8") as f:
            rebuild_lines = f.readlines()
        
        # Extract lines 44 to 121 (0-indexed 43 to 121)
        ch4_code_lines = rebuild_lines[43:121]
        ch4_code = ""
        for line in ch4_code_lines:
            if line.startswith("    "):
                ch4_code += line[4:]
            else:
                ch4_code += line
        
        local_vars = {}
        exec(ch4_code, globals(), local_vars)
        ch4_medium = local_vars["ch4_medium_questions"]
        ch4_hard = local_vars["ch4_hard_questions"]
        print("Successfully loaded Ch4 Medium and Hard from rebuild_arabic_generator.py via exec.")
    except Exception as e:
        print("Error loading Ch4 questions from rebuild_arabic_generator.py:", e)
        return
        
    # Let's check the size of Ch4 medium and hard
    print(f"Ch4 Easy: {len(ch4_easy)}, Medium: {len(ch4_medium)}, Hard: {len(ch4_hard)}")
    
    # 4. Read Chapter 1, 2, 3 questions directly from the current generate_arabic_subject.py
    # Since we modified and compiled it, let's import it and get them!
    try:
        import generate_arabic_subject
        ch1_easy, ch1_medium, ch1_hard = generate_arabic_subject.create_ch1_questions()
        ch2_easy, ch2_medium, ch2_hard = generate_arabic_subject.create_ch2_questions()
        ch3_easy, ch3_medium, ch3_hard = generate_arabic_subject.create_ch3_questions()
        print("Successfully loaded Chapters 1, 2, 3 from current generate_arabic_subject.py")
    except Exception as e:
        print("Error loading Chapters 1, 2, 3:", e)
        return
        
    # 5. Build the content of scratch/generate_arabic_subject.py
    content = f"""import json
import re
import os

def create_ch1_questions():
    # Chapter 1: Unit 1: Grammar & Syntax (حروف الجر والنداء)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch1_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch1_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch1_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard

def create_ch2_questions():
    # Chapter 2: Unit 2: Arabic Literature (مفهوم الأدب والنثر والشعر)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch2_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch2_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch2_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard

def create_ch3_questions():
    # Chapter 3: Unit 3: Rhetoric & Eloquence (البلاغة: التشبيه والاستعارة)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch3_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch3_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch3_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard

def create_ch4_questions():
    # Chapter 4: Unit 4: Islamic History & Figures (الخليفة عمر بن الخطاب رضي الله عنه)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch4_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch4_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch4_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard

def create_ch5_questions():
    # Chapter 5: Unit 5: Tribalism & Drug Harms (القبلية وأضرار المخدرات)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch5_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch5_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch5_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard

def create_ch6_questions():
    # Chapter 6: Unit 6: Folktales & Anecdotes (نوادر أشعب وحكايات صومالية)
    # 22 Easy, 25 Medium, 30 Hard (Total 77)
    easy = {json.dumps(ch6_easy, indent=8, ensure_ascii=False)}
    medium = {json.dumps(ch6_medium, indent=8, ensure_ascii=False)}
    hard = {json.dumps(ch6_hard, indent=8, ensure_ascii=False)}
    return easy, medium, hard
"""

    # Add the main() execution block to write back to seed_data.dart
    main_block = """
def main():
    seed_file_path = 'lib/services/seed_data.dart'
    
    if not os.path.exists(seed_file_path):
        print(f"Error: {seed_file_path} not found.")
        return
        
    # Read seed_data.dart
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx_raw = content.find(start_str)
    if start_idx_raw == -1:
        print("Could not find fullSeedJson")
        return
        
    start_idx = content.find('{', start_idx_raw)
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find JSON bounds")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Add Arabic Subject
    subjects = data.get('subjects', [])
    subjects = [s for s in subjects if s['id'] != 'arabic']
    subjects.append({
        'name': 'Arabic',
        'id': 'arabic'
    })
    data['subjects'] = subjects
    
    # Add Chapters (Somalia Curriculum)
    chapters = data.get('chapters', [])
    chapters = [c for c in chapters if c['subjectId'] != 'arabic']
    
    new_chapters = [
        {'subjectId': 'arabic', 'title': 'الوحدة الأولى: حروف الجر والنداء', 'id': 'arabic_ch1'},
        {'subjectId': 'arabic', 'title': 'الوحدة الثانية: الأدب والنثر والشعر', 'id': 'arabic_ch2'},
        {'subjectId': 'arabic', 'title': 'الوحدة الثالثة: البلاغة: التشبيه والاستعارة', 'id': 'arabic_ch3'},
        {'subjectId': 'arabic', 'title': 'الوحدة الرابعة: الخليفة عمر بن الخطاب رضي الله عنه', 'id': 'arabic_ch4'},
        {'subjectId': 'arabic', 'title': 'الوحدة الخامسة: القبلية وأضرار المخدرات', 'id': 'arabic_ch5'},
        {'subjectId': 'arabic', 'title': 'الوحدة السادسة: نوادر أشعب وحكايات صومالية', 'id': 'arabic_ch6'},
    ]
    
    chapters.extend(new_chapters)
    data['chapters'] = chapters
    
    # Generate Questions for each of the 6 chapters (Somalia Curriculum)
    all_questions = []
    
    ch_generators = {
        1: create_ch1_questions,
        2: create_ch2_questions,
        3: create_ch3_questions,
        4: create_ch4_questions,
        5: create_ch5_questions,
        6: create_ch6_questions,
    }
    
    for ch_num in range(1, 7):
        easy_b, med_b, hard_b = ch_generators[ch_num]()
        
        # Verify sizes
        if len(easy_b) < 22 or len(med_b) < 25 or len(hard_b) < 30:
            print(f"Error: Chapter {ch_num} has insufficient questions! Easy: {len(easy_b)}, Medium: {len(med_b)}, Hard: {len(hard_b)}")
            return
            
        ch_id = f"arabic_ch{ch_num}"
        
        # Take exactly the requested counts
        # Easy: 22
        for i in range(22):
            bq = easy_b[i]
            all_questions.append({
                "id": f"Arabic_Ch{ch_num}_Q{str(i+1).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "easy",
                "subjectId": "arabic",
                "chapterId": ch_id
            })
            
        # Medium: 25
        for i in range(25):
            bq = med_b[i]
            all_questions.append({
                "id": f"Arabic_Ch{ch_num}_Q{str(i+23).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "medium",
                "subjectId": "arabic",
                "chapterId": ch_id
            })
            
        # Hard: 30
        for i in range(30):
            bq = hard_b[i]
            all_questions.append({
                "id": f"Arabic_Ch{ch_num}_Q{str(i+48).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "hard",
                "subjectId": "arabic",
                "chapterId": ch_id
            })
            
    # Merge new questions
    questions = data.get('questions', [])
    # Remove existing arabic questions
    questions = [q for q in questions if q.get('subjectId') != 'arabic']
    questions.extend(all_questions)
    data['questions'] = questions
    
    # Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + updated_json + "\\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully generated {len(all_questions)} questions for Arabic subject (6 units) and merged them into seed_data.dart!")

if __name__ == '__main__':
    main()
"""

    content += main_block
    
    # 6. Write final generate_arabic_subject.py
    with open("scratch/generate_arabic_subject.py", "w", encoding="utf-8") as f_out:
        f_out.write(content)
        
    print("Successfully wrote generate_arabic_subject.py")

if __name__ == "__main__":
    main()
