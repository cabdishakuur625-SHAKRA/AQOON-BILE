import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../models/user_model.dart';
import '../services/auth_service.dart';

class ManageUserPointsScreen extends StatefulWidget {
  const ManageUserPointsScreen({super.key});

  @override
  State<ManageUserPointsScreen> createState() => _ManageUserPointsScreenState();
}

class _ManageUserPointsScreenState extends State<ManageUserPointsScreen> {
  List<UserModel> _users = [];
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadUsers();
  }

  Future<void> _loadUsers() async {
    setState(() => _loading = true);
    try {
      final users = await AuthService.getAllUsers();
      setState(() => _users = users);
    } catch (e) {
      debugPrint('Error loading users: $e');
    }
    setState(() => _loading = false);
  }

  void _editUser(UserModel user) async {
    final xpController = TextEditingController(text: user.xp.toString());
    final coinsController = TextEditingController(text: user.coins.toString());
    final streakController = TextEditingController(text: user.streakCount.toString());
    bool localIsAdmin = user.isAdmin;

    final result = await showDialog<bool>(
      context: context,
      builder: (context) => StatefulBuilder(
        builder: (context, setStateDialog) => AlertDialog(
          title: const Text('Edit User'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text('User: ${user.fullName}', style: const TextStyle(fontWeight: FontWeight.bold)),
              const SizedBox(height: 12),
              TextField(
                controller: xpController,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'XP'),
              ),
              TextField(
                controller: coinsController,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'Coins'),
              ),
              TextField(
                controller: streakController,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'Streak Count'),
              ),
              const SizedBox(height: 12),
              CheckboxListTile(
                title: const Text('Is Admin?'),
                value: localIsAdmin,
                activeColor: Colors.indigo,
                contentPadding: EdgeInsets.zero,
                onChanged: (val) {
                  if (val != null) {
                    setStateDialog(() {
                      localIsAdmin = val;
                    });
                  }
                },
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () async {
                // Reset to zero & remove admin
                await AuthService.setUserXp(email: user.email, xp: 0);
                await AuthService.setUserCoins(email: user.email, coins: 0);
                await AuthService.setUserAdmin(email: user.email, isAdmin: false);
                await AuthService.setUserStreakAdmin(email: user.email, streakCount: 0);
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('User reset to defaults')),
                  );
                }
                Navigator.of(context).pop(true);
              },
              child: const Text('Reset'),
            ),
            TextButton(
              onPressed: () => Navigator.of(context).pop(false),
              child: const Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () async {
                final int? newXp = int.tryParse(xpController.text);
                final int? newCoins = int.tryParse(coinsController.text);
                final int? newStreak = int.tryParse(streakController.text);
                if (newXp == null || newCoins == null || newStreak == null) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Please enter valid numbers')),
                  );
                  return;
                }
                await AuthService.setUserXp(email: user.email, xp: newXp);
                await AuthService.setUserCoins(email: user.email, coins: newCoins);
                await AuthService.setUserAdmin(email: user.email, isAdmin: localIsAdmin);
                await AuthService.setUserStreakAdmin(email: user.email, streakCount: newStreak);
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('User details updated')),
                  );
                }
                Navigator.of(context).pop(true);
              },
              child: const Text('Save'),
            ),
          ],
        ),
      ),
    );

    if (result == true) {
      _loadUsers();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Manage Users & Points', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      backgroundColor: const Color(0xFF1E1B4B),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : Container(
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [Color(0xFF1E1B4B), Color(0xFF312E81)],
                ),
              ),
              child: ListView.builder(
                itemCount: _users.length,
                itemBuilder: (context, index) {
                  final user = _users[index];
                  return ListTile(
                    title: Row(
                      children: [
                        Expanded(
                          child: Text(
                            user.fullName,
                            style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w600),
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                        if (user.isAdmin) ...[
                          const SizedBox(width: 8),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                            decoration: BoxDecoration(
                              color: Colors.redAccent.withOpacity(0.2),
                              borderRadius: BorderRadius.circular(6),
                              border: Border.all(color: Colors.redAccent.withOpacity(0.5)),
                            ),
                            child: const Text(
                              'ADMIN',
                              style: TextStyle(
                                color: Colors.redAccent,
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                letterSpacing: 0.5,
                              ),
                            ),
                          ),
                        ],
                      ],
                    ),
                    subtitle: Text('XP: ${user.xp} • Coins: ${user.coins} • Streak: ${user.streakCount}d', style: const TextStyle(color: Colors.white70)),
                    trailing: IconButton(
                      icon: const Icon(Icons.edit, color: Colors.amber),
                      onPressed: () => _editUser(user),
                    ),
                  ).animate().fadeIn(duration: 300.ms);
                },
              ),
            ),
    );
  }
}
