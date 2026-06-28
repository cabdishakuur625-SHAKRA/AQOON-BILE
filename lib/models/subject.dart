import 'package:flutter/material.dart';

class Subject {
  final String id;
  final String name;

  Subject({required this.id, required this.name});

  factory Subject.fromMap(String id, Map<dynamic, dynamic> map) {
    return Subject(
      id: id,
      name: map['name'] ?? '',
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'name': name,
    };
  }

  // Get subject icon based on subject ID
  IconData get icon => getIconForId(id);

  // Get subject icon URL based on subject ID
  String get iconUrl => getIconUrlForId(id);

  // Get subject gradient colors based on subject ID
  List<Color> get gradientColors => getGradientColorsForId(id);

  // Get single icon/text accent color based on subject ID
  Color get iconColor => getIconColorForId(id);

  static IconData getIconForId(String subjectId) {
    switch (subjectId.toLowerCase()) {
      case 'his':
        return Icons.history_edu_rounded;
      case 'geo':
        return Icons.explore_rounded;
      case 'bio':
        return Icons.biotech_rounded;
      case 'eng':
        return Icons.translate_rounded;
      case 'math':
        return Icons.calculate_rounded;
      case 'arabic':
        return Icons.local_library_rounded;
      case 'phy':
        return Icons.bolt_rounded;
      case 'somali':
        return Icons.draw_rounded;
      case 'tarbiyo':
        return Icons.auto_stories_rounded;
      case 'chem':
        return Icons.science_rounded;
      case 'bus':
        return Icons.business_center_rounded;
      case 'tech':
        return Icons.memory_rounded;
      default:
        return Icons.book_rounded;
    }
  }

  static List<Color> getGradientColorsForId(String subjectId) {
    switch (subjectId.toLowerCase()) {
      case 'his':
        return [const Color(0xFFF59E0B), const Color(0xFFD97706)]; // Amber/Orange
      case 'geo':
        return [const Color(0xFF10B981), const Color(0xFF059669)]; // Emerald
      case 'bio':
        return [const Color(0xFF06B6D4), const Color(0xFF0891B2)]; // Cyan
      case 'eng':
        return [const Color(0xFFEC4899), const Color(0xFFBE185D)]; // Pink/Magenta
      case 'math':
        return [const Color(0xFFF97316), const Color(0xFFEA580C)]; // Orange/Deep Orange
      case 'arabic':
        return [const Color(0xFF0D9488), const Color(0xFF115E59)]; // Teal
      case 'phy':
        return [const Color(0xFF6366F1), const Color(0xFF4338CA)]; // Indigo
      case 'somali':
        return [const Color(0xFF3B82F6), const Color(0xFF1D4ED8)]; // Blue
      case 'tarbiyo':
        return [const Color(0xFF10B981), const Color(0xFF065F46)]; // Emerald/Green
      case 'chem':
        return [const Color(0xFF8B5CF6), const Color(0xFF6D28D9)]; // Violet/Purple
      case 'bus':
        return [const Color(0xFFF43F5E), const Color(0xFFE11D48)]; // Rose/Crimson
      case 'tech':
        return [const Color(0xFF84CC16), const Color(0xFF65A30D)]; // Lime/Green
      default:
        return [const Color(0xFF3B82F6), const Color(0xFF1D4ED8)]; // Blue default
    }
  }

  static Color getIconColorForId(String subjectId) {
    switch (subjectId.toLowerCase()) {
      case 'his':
        return Colors.orangeAccent;
      case 'geo':
        return Colors.greenAccent;
      case 'bio':
        return Colors.cyanAccent;
      case 'eng':
        return Colors.pinkAccent;
      case 'math':
        return Colors.orangeAccent;
      case 'arabic':
        return Colors.tealAccent;
      case 'phy':
        return Colors.indigoAccent;
      case 'somali':
        return Colors.blueAccent;
      case 'tarbiyo':
        return Colors.greenAccent;
      case 'chem':
        return Colors.purpleAccent;
      case 'bus':
        return Colors.redAccent;
      case 'tech':
        return Colors.lightGreenAccent;
      default:
        return Colors.cyanAccent;
    }
  }

  static String getIconUrlForId(String subjectId) {
    switch (subjectId.toLowerCase()) {
      case 'his':
        return 'assets/images/history.png';
      case 'geo':
        return 'assets/images/geography.png';
      case 'bio':
        return 'assets/images/biology.png';
      case 'eng':
        return 'assets/images/english.png';
      case 'math':
        return 'assets/images/math.png';
      case 'arabic':
        return 'assets/images/arabic.png';
      case 'phy':
        return 'assets/images/physics.png';
      case 'somali':
        return 'assets/images/somali.png';
      case 'tarbiyo':
        return 'assets/images/tarbiyo.png';
      case 'chem':
        return 'assets/images/chemistry.png';
      case 'bus':
        return 'assets/images/business.png';
      case 'tech':
        return 'assets/images/technology.png';
      default:
        return 'https://cdn-icons-png.flaticon.com/512/2997/2997608.png'; // Default book icon
    }
  }
}
