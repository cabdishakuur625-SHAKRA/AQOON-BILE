class Chapter {
  final String id;
  final String subjectId;
  final String title;

  Chapter({
    required this.id,
    required this.subjectId,
    required this.title,
  });

  factory Chapter.fromMap(String id, Map<dynamic, dynamic> map) {
    return Chapter(
      id: id,
      subjectId: map['subjectId'] ?? '',
      title: map['title'] ?? '',
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'subjectId': subjectId,
      'title': title,
    };
  }
}
