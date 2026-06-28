import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_application_22/models/user_model.dart';

void main() {
  group('UserModel Tests', () {
    test('Level calculation should be correct based on XP', () {
      final userBeginner = UserModel(id: '1', fullName: 'Alice', email: 'alice@example.com', phoneNumber: '123', password: 'password', xp: 50);
      final userIntermediate = UserModel(id: '1', fullName: 'Alice', email: 'alice@example.com', phoneNumber: '123', password: 'password', xp: 200);
      final userAdvanced = UserModel(id: '1', fullName: 'Alice', email: 'alice@example.com', phoneNumber: '123', password: 'password', xp: 500);
      final userExpert = UserModel(id: '1', fullName: 'Alice', email: 'alice@example.com', phoneNumber: '123', password: 'password', xp: 1000);
      final userMaster = UserModel(id: '1', fullName: 'Alice', email: 'alice@example.com', phoneNumber: '123', password: 'password', xp: 2500);

      expect(userBeginner.level, 'Beginner');
      expect(userIntermediate.level, 'Intermediate');
      expect(userAdvanced.level, 'Advanced');
      expect(userExpert.level, 'Expert');
      expect(userMaster.level, 'Master');
    });

    test('availableRestores handles reset of month correctly', () {
      final today = DateTime.now();
      final currentMonthStr = "${today.year}-${today.month.toString().padLeft(2, '0')}";
      final dynamicMonthAgo = today.month == 1 ? "${today.year - 1}-12" : "${today.year}-${(today.month - 1).toString().padLeft(2, '0')}";

      // If lastRestoreMonth is not set / null, it should return 5
      final user1 = UserModel(
        id: '1',
        fullName: 'Alice',
        email: 'alice@example.com',
        phoneNumber: '123',
        password: 'password',
        streakRestoresLeft: 2,
        lastRestoreMonth: null,
      );
      expect(user1.availableRestores, 5);

      // If lastRestoreMonth is not current month, it should return 5
      final user2 = UserModel(
        id: '2',
        fullName: 'Bob',
        email: 'bob@example.com',
        phoneNumber: '123',
        password: 'password',
        streakRestoresLeft: 2,
        lastRestoreMonth: dynamicMonthAgo,
      );
      expect(user2.availableRestores, 5);

      // If lastRestoreMonth is current month, it should return the actual streakRestoresLeft
      final user3 = UserModel(
        id: '3',
        fullName: 'Charlie',
        email: 'charlie@example.com',
        phoneNumber: '123',
        password: 'password',
        streakRestoresLeft: 3,
        lastRestoreMonth: currentMonthStr,
      );
      expect(user3.availableRestores, 3);
    });

    test('toMap and fromMap should work correctly', () {
      final original = UserModel(
        id: '123',
        fullName: 'Jane Doe',
        email: 'jane@example.com',
        phoneNumber: '987654321',
        password: 'secretpassword',
        coins: 100,
        xp: 1500,
        isAdmin: true,
        streakCount: 5,
        lastActiveDate: '2026-06-12',
        previousStreak: 4,
        streakRestoresLeft: 3,
        lastRestoreMonth: '2026-06',
      );

      final map = original.toMap();
      
      expect(map['id'], '123');
      expect(map['fullName'], 'Jane Doe');
      expect(map['email'], 'jane@example.com');
      expect(map['phoneNumber'], '987654321');
      expect(map['password'], 'secretpassword');
      expect(map['coins'], 100);
      expect(map['xp'], 1500);
      expect(map['isAdmin'], true);
      expect(map['streakCount'], 5);
      expect(map['lastActiveDate'], '2026-06-12');
      expect(map['previousStreak'], 4);
      expect(map['streakRestoresLeft'], 3);
      expect(map['lastRestoreMonth'], '2026-06');

      final reconstructed = UserModel.fromMap('123', map);
      expect(reconstructed.id, '123');
      expect(reconstructed.fullName, 'Jane Doe');
      expect(reconstructed.email, 'jane@example.com');
      expect(reconstructed.phoneNumber, '987654321');
      expect(reconstructed.password, 'secretpassword');
      expect(reconstructed.coins, 100);
      expect(reconstructed.xp, 1500);
      expect(reconstructed.isAdmin, true);
      expect(reconstructed.streakCount, 5);
      expect(reconstructed.lastActiveDate, '2026-06-12');
      expect(reconstructed.previousStreak, 4);
      expect(reconstructed.streakRestoresLeft, 3);
      expect(reconstructed.lastRestoreMonth, '2026-06');
    });

    test('copyWith works correctly', () {
      final user = UserModel(
        id: '1',
        fullName: 'Alice',
        email: 'alice@example.com',
        phoneNumber: '123',
        password: 'password',
        streakCount: 2,
      );

      final copied = user.copyWith(
        streakCount: 5,
        lastActiveDate: '2026-06-12',
      );

      expect(copied.id, '1');
      expect(copied.fullName, 'Alice');
      expect(copied.streakCount, 5);
      expect(copied.lastActiveDate, '2026-06-12');
    });
  });
}
