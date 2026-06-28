class Paper {
  final String id;
  final String title;
  final String subjectId;
  final String subjectName;
  final String year;
  final String pdfUrl;
  final int uploadedAt;
  final bool isAsset;

  Paper({
    required this.id,
    required this.title,
    required this.subjectId,
    required this.subjectName,
    required this.year,
    required this.pdfUrl,
    required this.uploadedAt,
    this.isAsset = false,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'subjectId': subjectId,
      'subjectName': subjectName,
      'year': year,
      'pdfUrl': pdfUrl,
      'uploadedAt': uploadedAt,
      'isAsset': isAsset,
    };
  }

  factory Paper.fromMap(String id, Map<dynamic, dynamic> map) {
    return Paper(
      id: id,
      title: map['title'] ?? '',
      subjectId: map['subjectId'] ?? '',
      subjectName: map['subjectName'] ?? '',
      year: map['year']?.toString() ?? '',
      pdfUrl: map['pdfUrl'] ?? '',
      uploadedAt: map['uploadedAt'] ?? 0,
      isAsset: map['isAsset'] ?? false,
    );
  }
}
