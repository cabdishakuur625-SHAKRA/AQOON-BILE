class UserModel {
  final String id;
  final String fullName;
  final String email;
  final String phoneNumber;
  final String password;
  final int coins;
  final int xp;
  final bool isAdmin;
  final int streakCount;
  final String? lastActiveDate;
  final int previousStreak;
  final int streakRestoresLeft;
  final String? lastRestoreMonth;
  final String? avatarUrl;

  UserModel({
    required this.id,
    required this.fullName,
    required this.email,
    required this.phoneNumber,
    required this.password,
    this.coins = 0,
    this.xp = 0,
    this.isAdmin = false,
    this.streakCount = 0,
    this.lastActiveDate,
    this.previousStreak = 0,
    this.streakRestoresLeft = 5,
    this.lastRestoreMonth,
    this.avatarUrl,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'fullName': fullName,
      'email': email,
      'phoneNumber': phoneNumber,
      'password': password,
      'coins': coins,
      'xp': xp,
      'isAdmin': isAdmin,
      'streakCount': streakCount,
      'lastActiveDate': lastActiveDate,
      'previousStreak': previousStreak,
      'streakRestoresLeft': streakRestoresLeft,
      'lastRestoreMonth': lastRestoreMonth,
      'avatarUrl': avatarUrl,
    };
  }

  factory UserModel.fromMap(String id, Map<dynamic, dynamic> map) {
    return UserModel(
      id: id,
      fullName: map['fullName'] ?? '',
      email: map['email'] ?? '',
      phoneNumber: map['phoneNumber'] ?? '',
      password: map['password'] ?? '',
      coins: map['coins'] ?? 0,
      xp: map['xp'] ?? 0,
      isAdmin: map['isAdmin'] ?? false,
      streakCount: map['streakCount'] ?? 0,
      lastActiveDate: map['lastActiveDate'],
      previousStreak: map['previousStreak'] ?? 0,
      streakRestoresLeft: map['streakRestoresLeft'] ?? 5,
      lastRestoreMonth: map['lastRestoreMonth'],
      avatarUrl: map['avatarUrl'],
    );
  }

  UserModel copyWith({
    String? id,
    String? fullName,
    String? email,
    String? phoneNumber,
    String? password,
    int? coins,
    int? xp,
    bool? isAdmin,
    int? streakCount,
    String? lastActiveDate,
    int? previousStreak,
    int? streakRestoresLeft,
    String? lastRestoreMonth,
    String? avatarUrl,
  }) {
    return UserModel(
      id: id ?? this.id,
      fullName: fullName ?? this.fullName,
      email: email ?? this.email,
      phoneNumber: phoneNumber ?? this.phoneNumber,
      password: password ?? this.password,
      coins: coins ?? this.coins,
      xp: xp ?? this.xp,
      isAdmin: isAdmin ?? this.isAdmin,
      streakCount: streakCount ?? this.streakCount,
      lastActiveDate: lastActiveDate ?? this.lastActiveDate,
      previousStreak: previousStreak ?? this.previousStreak,
      streakRestoresLeft: streakRestoresLeft ?? this.streakRestoresLeft,
      lastRestoreMonth: lastRestoreMonth ?? this.lastRestoreMonth,
      avatarUrl: avatarUrl ?? this.avatarUrl,
    );
  }

  String get level {
    if (xp >= 2000) return 'Master';
    if (xp >= 1000) return 'Expert';
    if (xp >= 500) return 'Advanced';
    if (xp >= 200) return 'Intermediate';
    return 'Beginner';
  }

  int get availableRestores {
    final today = DateTime.now();
    final currentMonth = "${today.year}-${today.month.toString().padLeft(2, '0')}";
    if (lastRestoreMonth != currentMonth) {
      return 5;
    }
    return streakRestoresLeft;
  }
}
