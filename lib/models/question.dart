class Question {
  final String id;
  final String subjectId;
  final String chapterId;
  final String questionText;
  final Map<String, String> options;
  final String correctAnswer;
  final String difficultyLevel;

  Question({
    required this.id,
    required this.subjectId,
    required this.chapterId,
    required String questionText,
    required this.options,
    required this.correctAnswer,
    required this.difficultyLevel,
  }) : questionText = _cleanQuestionText(questionText);

  factory Question.fromMap(String id, Map<dynamic, dynamic> map) {
    return Question(
      id: id,
      subjectId: map['subjectId'] ?? '',
      chapterId: map['chapterId'] ?? '',
      questionText: map['question'] ?? '',
      options: Map<String, String>.from(map['options'] ?? {}),
      correctAnswer: map['correctAnswer'] ?? '',
      difficultyLevel: map['difficultyLevel'] ?? '',
    );
  }

  static String _cleanQuestionText(String text) {
    final regex = RegExp(
      r'^(?:easy|medium|hard)\d*\s*question\s*\d+:\s*',
      caseSensitive: false,
    );
    return text.replaceFirst(regex, '').trim();
  }

  Map<String, dynamic> toMap() {
    return {
      'subjectId': subjectId,
      'chapterId': chapterId,
      'question': questionText,
      'options': options,
      'correctAnswer': correctAnswer,
      'difficultyLevel': difficultyLevel,
    };
  }
}
