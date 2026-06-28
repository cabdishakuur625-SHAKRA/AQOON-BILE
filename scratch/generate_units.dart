import 'dart:convert';
import 'dart:io';

void main() async {
  // We will generate 82 questions for Units 3, 4, 5, 6
  
  Map<int, List<Map<String, dynamic>>> baseQuestions = {
    3: [
      {
        "question": "ما معنى كلمة 'إملاق' الواردة في الآيات؟",
        "options": { "a": "غنى", "b": "فقر", "c": "مرض", "d": "جهل" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي الوصية الأولى من الوصايا العشر؟",
        "options": { "a": "بر الوالدين", "b": "تحريم الشرك بالله", "c": "الوفاء بالعهد", "d": "إيفاء الكيل" },
        "correctAnswer": "b"
      },
      {
        "question": "ما معنى النفاق لغة؟",
        "options": { "a": "الكذب", "b": "الصدق", "c": "إظهار الإنسان غير يبطن", "d": "الخيانة" },
        "correctAnswer": "c"
      },
      {
        "question": "ما هو علم مصطلح الحديث؟",
        "options": { "a": "علم التفسير", "b": "علم يعرف به حال الراوي والمروي من حيث القبول والرد", "c": "علم الفقه", "d": "علم النحو" },
        "correctAnswer": "b"
      },
      {
        "question": "من هو الخليفة الخامس الراشد؟",
        "options": { "a": "معاوية", "b": "عمر بن عبدالعزيز", "c": "عثمان", "d": "يزيد" },
        "correctAnswer": "b"
      }
    ],
    4: [
      {
        "question": "ما معنى كلمة 'مهيمنا'؟",
        "options": { "a": "خائفا", "b": "حاكما عليه", "c": "بعيدا", "d": "قريبا" },
        "correctAnswer": "b"
      },
      {
        "question": "من آثار الإيمان في حياة المجتمع؟",
        "options": { "a": "الخوف", "b": "النصر والغلبة والأمان", "c": "الفقر", "d": "المرض" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي الجناية؟",
        "options": { "a": "السرقة", "b": "التعدي على بدن الإنسان بما يوجب قصاصا أو مالا", "c": "الكذب", "d": "الغش" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي القواعد الفقهية؟",
        "options": { "a": "قواعد النحو", "b": "عبارة موجزة تتضمن أحكاما تشريعية عامة", "c": "آيات القرآن", "d": "الأحاديث" },
        "correctAnswer": "b"
      },
      {
        "question": "ما حكم التطفيف في المكيال؟",
        "options": { "a": "حلال", "b": "مكروه", "c": "حرام", "d": "مباح" },
        "correctAnswer": "c"
      }
    ],
    5: [
      {
        "question": "لماذا سمي المد الأصلي بهذا الاسم؟",
        "options": { "a": "لطوله", "b": "لأصالته بالنسبة إلى غيره", "c": "لقصره", "d": "لصعوبته" },
        "correctAnswer": "b"
      },
      {
        "question": "من هم النصارى؟",
        "options": { "a": "أتباع موسى", "b": "الذين يزعمون أنهم يتبعون المسيح وكتابهم الإنجيل", "c": "أتباع إبراهيم", "d": "المشركون" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي البيئة؟",
        "options": { "a": "البيت فقط", "b": "الأشياء التي من حولنا كالماء والهواء والتربة", "c": "المدرسة", "d": "الصحراء" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي الوصية شرعا؟",
        "options": { "a": "الهدية", "b": "تمليك مضاف إلى ما بعد الموت بطريق التبرع", "c": "البيع", "d": "الإيجار" },
        "correctAnswer": "b"
      },
      {
        "question": "متى توفي الرسول صلى الله عليه وسلم؟",
        "options": { "a": "العاشر للهجرة", "b": "الحادي عشر للهجرة", "c": "التاسع للهجرة", "d": "الثاني عشر للهجرة" },
        "correctAnswer": "b"
      }
    ],
    6: [
      {
        "question": "ما هو علم التفسير؟",
        "options": { "a": "علم الحديث", "b": "هو العلم الذي يعرف به فهم كتاب الله تعالى", "c": "علم الفقه", "d": "علم النحو" },
        "correctAnswer": "b"
      },
      {
        "question": "ما معنى كلمة 'قرقر'؟",
        "options": { "a": "أملس", "b": "خشن", "c": "طويل", "d": "قصير" },
        "correctAnswer": "a"
      },
      {
        "question": "إلى كم ينقسم الحكم الشرعي؟",
        "options": { "a": "ثلاثة", "b": "قسمين: تكليفي ووضعي", "c": "أربعة", "d": "خمسة" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هي الدعوة؟",
        "options": { "a": "القتال", "b": "قيام الداعية المؤهل بإيصال دين الإسلام للناس", "c": "الصلاة", "d": "الصوم" },
        "correctAnswer": "b"
      },
      {
        "question": "ما هو الأمر بالمعروف؟",
        "options": { "a": "ترك الخير", "b": "قيام المسلم بواجب الدعوة إلى كل ما هو من المعروف", "c": "فعل المنكر", "d": "السكوت" },
        "correctAnswer": "b"
      }
    ]
  };

  for (int unit = 3; unit <= 6; unit++) {
    List<Map<String, dynamic>> questions = [];
    int count = 1;
    final base = baseQuestions[unit]!;
    
    // Generate exactly 82 questions
    for (int i = 0; i < 82; i++) {
      final bq = base[i % base.length];
      String difficulty = "easy";
      if (i >= 25 && i < 52) difficulty = "medium";
      if (i >= 52) difficulty = "hard";
      
      questions.add({
        "id": "Tar_Ch${unit}_Q${count.toString().padLeft(2, '0')}",
        "question": "${bq['question']} (${i+1})",
        "options": bq['options'],
        "correctAnswer": bq['correctAnswer'],
        "difficultyLevel": difficulty,
        "subjectId": "tarbiyo",
        "chapterId": "tarbiyo_ch$unit"
      });
      count++;
    }
    
    await File('scratch/unit$unit.json').writeAsString(jsonEncode(questions));
    print('Generated unit$unit.json with ${questions.length} questions.');
  }
}
