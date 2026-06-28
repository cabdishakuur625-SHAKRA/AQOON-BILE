import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import '../../services/auth_service.dart';
import 'ProfilePreviewScreen.dart';

class FindFriendsScreen extends StatefulWidget {
  const FindFriendsScreen({super.key});

  @override
  State<FindFriendsScreen> createState() => _FindFriendsScreenState();
}

class _FindFriendsScreenState extends State<FindFriendsScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  List<UserData> suggestedUsers = [];
  List<UserData> incomingRequests = [];
  List<UserData> sentRequests = [];
  List<UserData> friends = [];
  bool _isLoading = true;
  String _searchQuery = "";

  StreamSubscription<DatabaseEvent>? _usersSubscription;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
    _startUsersListener();
  }

  @override
  void dispose() {
    _tabController.dispose();
    _usersSubscription?.cancel();
    super.dispose();
  }

  /// Start a real-time listener on the Users node to keep relationship statuses synced instantly
  void _startUsersListener() {
    if (AuthService.currentUser == null) return;

    final myEmail = AuthService.currentUser!.email;
    final myKey = AuthService.sanitizeEmail(myEmail);

    _usersSubscription = _dbRef.child('Users').onValue.listen((event) {
      if (!mounted) return;

      final value = event.snapshot.value;
      if (value == null) {
        setState(() {
          suggestedUsers = [];
          incomingRequests = [];
          sentRequests = [];
          friends = [];
          _isLoading = false;
        });
        return;
      }

      final Map<dynamic, dynamic> allUsersMap = value as Map<dynamic, dynamic>;

      // Fetch my relationships
      final myUserMap = allUsersMap[myKey] as Map<dynamic, dynamic>? ?? {};
      final Map<dynamic, dynamic> myFriendsKeysMap = myUserMap['friends'] as Map<dynamic, dynamic>? ?? {};
      final Map<dynamic, dynamic> myFriendRequestsKeysMap = myUserMap['friendRequests'] as Map<dynamic, dynamic>? ?? {};
      final Map<dynamic, dynamic> mySentRequestsKeysMap = myUserMap['sentRequests'] as Map<dynamic, dynamic>? ?? {};

      final List<UserData> tempFriends = [];
      final List<UserData> tempIncomingRequests = [];
      final List<UserData> tempSentRequests = [];
      final List<UserData> tempSuggested = [];

      allUsersMap.forEach((key, value) {
        final userMap = value as Map<dynamic, dynamic>;
        final String email = userMap['email'] ?? '';
        final String fullName = userMap['fullName'] ?? 'User';
        final String xp = (userMap['xp'] ?? 0).toString();

        // Skip current user
        if (email.toLowerCase() == myEmail.toLowerCase()) {
          return;
        }

        final sanitizedEmail = AuthService.sanitizeEmail(email);
        final String? avatarUrl = userMap['avatarUrl'] as String?;

        final userData = UserData(
          name: fullName,
          xp: xp,
          isAdded: mySentRequestsKeysMap.containsKey(sanitizedEmail),
          avatarUrl: avatarUrl,
          email: email,
        );

        if (myFriendsKeysMap.containsKey(sanitizedEmail)) {
          tempFriends.add(userData);
        } else if (myFriendRequestsKeysMap.containsKey(sanitizedEmail)) {
          tempIncomingRequests.add(userData);
        } else if (mySentRequestsKeysMap.containsKey(sanitizedEmail)) {
          tempSentRequests.add(userData);
        } else {
          tempSuggested.add(userData);
        }
      });

      setState(() {
        friends = tempFriends;
        incomingRequests = tempIncomingRequests;
        sentRequests = tempSentRequests;
        suggestedUsers = tempSuggested;
        _isLoading = false;
      });
    }, onError: (e) {
      debugPrint("Error loading friends data: $e");
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    });
  }

  List<UserData> _getFilteredUsers(List<UserData> list) {
    if (_searchQuery.isEmpty) return list;
    return list.where((u) => u.name.toLowerCase().contains(_searchQuery)).toList();
  }

  Future<void> _handleSendRequest(UserData user) async {
    try {
      await AuthService.sendFriendRequest(user.email);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Friend request sent to ${user.name}!"),
          backgroundColor: Colors.cyan,
        ),
      );
    } catch (e) {
      debugPrint("Error sending friend request: $e");
    }
  }

  Future<void> _handleCancelRequest(UserData user) async {
    try {
      await AuthService.cancelFriendRequest(user.email);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Cancelled request to ${user.name}"),
          backgroundColor: Colors.orangeAccent,
        ),
      );
    } catch (e) {
      debugPrint("Error cancelling friend request: $e");
    }
  }

  Future<void> _handleAcceptRequest(UserData user) async {
    try {
      await AuthService.acceptFriendRequest(user.email);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Accepted friend request from ${user.name}!"),
          backgroundColor: Colors.green,
        ),
      );
    } catch (e) {
      debugPrint("Error accepting friend request: $e");
    }
  }

  Future<void> _handleDeclineRequest(UserData user) async {
    try {
      await AuthService.declineFriendRequest(user.email);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Declined request from ${user.name}."),
          backgroundColor: Colors.redAccent,
        ),
      );
    } catch (e) {
      debugPrint("Error declining friend request: $e");
    }
  }

  Future<void> _handleUnfriend(UserData user) async {
    try {
      await AuthService.unfriend(user.email);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Removed ${user.name} from friends."),
          backgroundColor: Colors.orangeAccent,
        ),
      );
    } catch (e) {
      debugPrint("Error unfriending: $e");
    }
  }

  Widget _buildRequestsTab() {
    final filteredIncoming = _getFilteredUsers(incomingRequests);
    final filteredSent = _getFilteredUsers(sentRequests);

    if (filteredIncoming.isEmpty && filteredSent.isEmpty) {
      return Center(
        child: Text(
          "No requests found",
          style: GoogleFonts.outfit(color: Colors.white24, fontSize: 16),
        ),
      );
    }

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.only(top: 10),
      children: [
        if (filteredIncoming.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 5),
            child: Text(
              "Received Requests (${filteredIncoming.length})",
              style: GoogleFonts.outfit(
                color: Colors.cyanAccent,
                fontSize: 14,
                fontWeight: FontWeight.bold,
                letterSpacing: 1.0,
              ),
            ),
          ),
          ...List.generate(filteredIncoming.length, (index) {
            return _buildUserCard(filteredIncoming, index, 1); // 1 = Received/Incoming Request
          }),
          const SizedBox(height: 20),
        ],
        if (filteredSent.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 5),
            child: Text(
              "Sent Requests (${filteredSent.length})",
              style: GoogleFonts.outfit(
                color: Colors.white70,
                fontSize: 14,
                fontWeight: FontWeight.bold,
                letterSpacing: 1.0,
              ),
            ),
          ),
          ...List.generate(filteredSent.length, (index) {
            return _buildUserCard(filteredSent, index, 3); // 3 = Sent/Outgoing Request
          }),
        ],
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E1B4B), Color(0xFF312E81)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              _buildAppBar(context),
              _buildTabs(),
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: Column(
                    children: [
                      const SizedBox(height: 20),
                      _buildSearchBar(),
                      const SizedBox(height: 20),
                      Expanded(
                        child: TabBarView(
                          controller: _tabController,
                          children: [
                            _isLoading
                                ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                                : _buildUserList(_getFilteredUsers(suggestedUsers), 0),
                            _isLoading
                                ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                                : _buildRequestsTab(),
                            _isLoading
                                ? const Center(child: CircularProgressIndicator(color: Colors.cyanAccent))
                                : _buildUserList(_getFilteredUsers(friends), 2),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildAppBar(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          IconButton(
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            style: IconButton.styleFrom(
              backgroundColor: Colors.white.withOpacity(0.1),
              padding: const EdgeInsets.all(12),
            ),
          ),
          Text(
            "Find Friends",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(width: 48),
        ],
      ),
    ).animate().fadeIn().slideY(begin: -1);
  }

  Widget _buildTabs() {
    return TabBar(
      controller: _tabController,
      dividerColor: Colors.transparent,
      indicatorColor: Colors.cyanAccent,
      indicatorWeight: 3,
      labelColor: Colors.cyanAccent,
      unselectedLabelColor: Colors.white38,
      labelStyle: GoogleFonts.outfit(fontWeight: FontWeight.bold),
      tabs: const [
        Tab(text: "Suggested"),
        Tab(text: "Requests"),
        Tab(text: "Friends"),
      ],
    ).animate().fadeIn(delay: 200.ms);
  }

  Widget _buildSearchBar() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.08),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: TextField(
        onChanged: (val) {
          setState(() {
            _searchQuery = val.trim().toLowerCase();
          });
        },
        style: const TextStyle(color: Colors.white),
        decoration: InputDecoration(
          icon: const Icon(Icons.search_rounded, color: Colors.white54),
          hintText: "Search by name...",
          hintStyle: GoogleFonts.outfit(color: Colors.white38),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 18),
        ),
      ),
    ).animate().fadeIn(delay: 400.ms).slideX(begin: 0.1);
  }

  Widget _buildUserList(List<UserData> users, int tabIndex) {
    if (users.isEmpty) {
      return Center(
        child: Text(
          "No users found",
          style: GoogleFonts.outfit(color: Colors.white24),
        ),
      );
    }
    return ListView.builder(
      physics: const BouncingScrollPhysics(),
      itemCount: users.length,
      padding: const EdgeInsets.only(top: 10),
      itemBuilder: (context, index) {
        return _buildUserCard(users, index, tabIndex);
      },
    );
  }

  Widget _buildUserCard(List<UserData> users, int index, int tabIndex) {
    final user = users[index];
    return GestureDetector(
      onTap: tabIndex == 2
          ? () async {
              final result = await Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ProfilePreviewScreen(
                    name: user.name,
                    avatarUrl: user.avatarUrl,
                    xp: int.tryParse(user.xp),
                    email: user.email,
                  ),
                ),
              );
              if (result == 'unfriend') {
                _handleUnfriend(user);
              }
            }
          : null,
      child: Container(
        margin: const EdgeInsets.only(bottom: 15),
        padding: const EdgeInsets.all(15),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.05),
          borderRadius: BorderRadius.circular(25),
          border: Border.all(color: Colors.white.withOpacity(0.1)),
        ),
        child: Row(
          children: [
            CircleAvatar(
              radius: 28,
              backgroundColor: Colors.cyanAccent.withOpacity(0.2),
              backgroundImage: AuthService.getAvatarProvider(user.avatarUrl),
              child: user.avatarUrl == null || user.avatarUrl!.isEmpty
                  ? Text(
                      user.name.split(' ').map((e) => e[0]).join(),
                      style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold),
                    )
                  : null,
            ),
            const SizedBox(width: 15),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    user.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: GoogleFonts.outfit(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  Text(
                    "XP: ${user.xp}",
                    style: GoogleFonts.outfit(color: Colors.white38, fontSize: 13),
                  ),
                ],
              ),
            ),
            _buildActionWidget(user, tabIndex),
          ],
        ),
      ),
    ).animate().fadeIn(delay: (200 + index * 50).ms).slideY(begin: 0.1);
  }

  Widget _buildActionWidget(UserData user, int tabIndex) {
    if (tabIndex == 2) {
      // Friends tab - Unfriend button
      return IconButton(
        onPressed: () => _handleUnfriend(user),
        icon: const Icon(Icons.person_remove_alt_1_rounded, color: Colors.redAccent),
        style: IconButton.styleFrom(
          backgroundColor: Colors.redAccent.withOpacity(0.1),
          padding: const EdgeInsets.all(12),
        ),
      );
    } else if (tabIndex == 1) {
      // Requests tab - Accept / Decline buttons
      return Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          ElevatedButton(
            onPressed: () => _handleAcceptRequest(user),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.greenAccent,
              foregroundColor: Colors.black,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              elevation: 0,
            ),
            child: Text(
              "Accept",
              style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 12),
            ),
          ),
          const SizedBox(width: 8),
          ElevatedButton(
            onPressed: () => _handleDeclineRequest(user),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.redAccent.withOpacity(0.2),
              foregroundColor: Colors.redAccent,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              elevation: 0,
              side: const BorderSide(color: Colors.redAccent, width: 1.5),
            ),
            child: Text(
              "Decline",
              style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 12),
            ),
          ),
        ],
      );
    } else if (tabIndex == 3) {
      // Sent Requests tab - Cancel button
      return ElevatedButton(
        onPressed: () => _handleCancelRequest(user),
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.redAccent.withOpacity(0.2),
          foregroundColor: Colors.redAccent,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
          elevation: 0,
          side: const BorderSide(color: Colors.redAccent, width: 1.5),
        ),
        child: Text(
          "Cancel",
          style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 12),
        ),
      );
    } else {
      // Suggested tab - Add / Cancel button
      return ElevatedButton(
        onPressed: () {
          if (user.isAdded) {
            _handleCancelRequest(user);
          } else {
            _handleSendRequest(user);
          }
        },
        style: ElevatedButton.styleFrom(
          backgroundColor: user.isAdded ? Colors.redAccent.withOpacity(0.2) : Colors.cyanAccent,
          foregroundColor: user.isAdded ? Colors.redAccent : Colors.black,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
          elevation: 0,
          side: user.isAdded ? const BorderSide(color: Colors.redAccent, width: 1.5) : null,
        ),
        child: Text(
          user.isAdded ? "Cancel" : "Add",
          style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
        ),
      );
    }
  }
}

class UserData {
  final String name;
  final String xp;
  final bool isAdded;
  final String? avatarUrl;
  final String email;

  UserData({
    required this.name,
    required this.xp,
    required this.isAdded,
    this.avatarUrl,
    required this.email,
  });
}
