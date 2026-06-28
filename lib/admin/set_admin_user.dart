import 'package:flutter/widgets.dart';
import 'package:firebase_core/firebase_core.dart';
import '../services/auth_service.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  const String targetEmail = 'cabdishakuur625@gmail.com';
  await AuthService.setUserAdmin(email: targetEmail, isAdmin: true);
  print('✅ $targetEmail has been promoted to admin');
}
