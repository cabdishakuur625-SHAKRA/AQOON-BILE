import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import '../../services/auth_service.dart';

class ChatScreen extends StatefulWidget {
  final String userName;
  final String? avatarUrl;
  final String userEmail;

  const ChatScreen({
    super.key,
    required this.userName,
    this.avatarUrl,
    required this.userEmail,
  });

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final DatabaseReference _dbRef = FirebaseDatabase.instanceFor(
    app: Firebase.app(),
    databaseURL: 'https://aqoonbile-3389f-default-rtdb.europe-west1.firebasedatabase.app',
  ).ref();

  final List<MessageData> _messages = [];
  StreamSubscription<DatabaseEvent>? _chatSubscription;
  StreamSubscription<DatabaseEvent>? _peerSubscription;
  StreamSubscription<DatabaseEvent>? _connectionSubscription;
  StreamSubscription<DatabaseEvent>? _peerPresenceSubscription;
  bool _isLoading = true;
  bool _isConnected = true;

  String? _peerAvatarUrl;
  String? _peerName;
  bool _isPeerOnline = false;

  final TextEditingController _controller = TextEditingController();

  String get _chatRoomId {
    final myEmail = AuthService.currentUser?.email ?? 'learner@gmail.com';
    final peerEmail = widget.userEmail;
    final keyA = AuthService.sanitizeEmail(myEmail);
    final keyB = AuthService.sanitizeEmail(peerEmail);
    return keyA.compareTo(keyB) < 0 ? "${keyA}_$keyB" : "${keyB}_$keyA";
  }

  @override
  void initState() {
    super.initState();
    _startConnectionListener();
    _startPeerListener();
    _startChatListener();
  }

  @override
  void dispose() {
    _chatSubscription?.cancel();
    _peerSubscription?.cancel();
    _connectionSubscription?.cancel();
    _peerPresenceSubscription?.cancel();
    _controller.dispose();
    super.dispose();
  }

  void _startConnectionListener() {
    _connectionSubscription = _dbRef.root.child('.info/connected').onValue.listen((event) {
      if (!mounted) return;
      final connected = event.snapshot.value as bool? ?? false;
      setState(() {
        _isConnected = connected;
      });
    });
  }

  void _startPeerListener() {
    _peerAvatarUrl = widget.avatarUrl;
    _peerName = widget.userName;

    final peerSanitized = AuthService.sanitizeEmail(widget.userEmail);
    _peerSubscription = _dbRef.child('Users/$peerSanitized').onValue.listen((event) {
      if (!mounted) return;
      final value = event.snapshot.value;
      if (value != null && value is Map) {
        setState(() {
          _peerAvatarUrl = value['avatarUrl'] as String?;
          _peerName = value['fullName'] as String? ?? widget.userName;
        });
      }
    });

    _peerPresenceSubscription = _dbRef.child('Users/$peerSanitized/presence').onValue.listen((event) {
      if (!mounted) return;
      final status = event.snapshot.value as String? ?? 'offline';
      setState(() {
        _isPeerOnline = status == 'online';
      });
      if (_isPeerOnline) {
        _markMyMessagesAsDelivered();
      }
    });
  }

  void _markMyMessagesAsDelivered() {
    final roomId = _chatRoomId;
    for (var msg in _messages) {
      if (msg.isMe && !msg.delivered) {
        final msgId = msg.timestamp.toString();
        _dbRef.child('Chats/$roomId/messages/$msgId/delivered').set(true);
      }
    }
  }

  void _startChatListener() {
    final roomId = _chatRoomId;
    _chatSubscription = _dbRef.child('Chats/$roomId/messages').onValue.listen((event) {
      if (!mounted) return;
      final Map<dynamic, dynamic>? data = event.snapshot.value as Map<dynamic, dynamic>?;
      final List<MessageData> temp = [];
      if (data != null) {
        data.forEach((key, value) {
          final msgMap = value as Map;
          final sender = msgMap['senderEmail'] as String? ?? '';
          final myEmail = AuthService.currentUser?.email ?? '';
          final isMe = sender.toLowerCase() == myEmail.toLowerCase();
          final isSeen = msgMap['seen'] == true;

          // If the message is from the peer and we haven't seen it yet, mark it as seen and delivered
          if (!isMe && !isSeen) {
            _dbRef.child('Chats/$roomId/messages/$key/seen').set(true);
            _dbRef.child('Chats/$roomId/messages/$key/delivered').set(true);
          }

          temp.add(MessageData(
            text: msgMap['text'] ?? '',
            time: msgMap['time'] ?? 'Now',
            isMe: isMe,
            timestamp: msgMap['timestamp'] ?? 0,
            seen: isSeen,
            delivered: isSeen || msgMap['delivered'] == true,
          ));
        });
        // Sort by timestamp asc
        temp.sort((a, b) => a.timestamp.compareTo(b.timestamp));
      }
      setState(() {
        _messages.clear();
        _messages.addAll(temp);
        _isLoading = false;
      });
    });
  }

  void _sendMessage() async {
    if (!_isConnected) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("No internet connection. Message cannot be sent."),
          backgroundColor: Colors.redAccent,
        ),
      );
      return;
    }

    final text = _controller.text.trim();
    if (text.isEmpty) return;
    _controller.clear();

    final myEmail = AuthService.currentUser?.email ?? '';
    final myName = AuthService.currentUser?.fullName ?? 'Learner';
    final peerEmail = widget.userEmail;
    final roomId = _chatRoomId;
    final timestamp = DateTime.now().millisecondsSinceEpoch;

    final date = DateTime.fromMillisecondsSinceEpoch(timestamp);
    final hour = date.hour > 12 ? date.hour - 12 : (date.hour == 0 ? 12 : date.hour);
    final min = date.minute.toString().padLeft(2, '0');
    final period = date.hour >= 12 ? "PM" : "AM";
    final timeStr = "$hour:$min $period";

    final msgId = timestamp.toString();
    await _dbRef.child('Chats/$roomId/messages/$msgId').set({
      'text': text,
      'senderEmail': myEmail,
      'senderName': myName,
      'timestamp': timestamp,
      'time': timeStr,
      'seen': false,
      'delivered': _isPeerOnline,
    });

    // Write real-time notification to the peer
    final peerSanitized = AuthService.sanitizeEmail(peerEmail);
    final notificationId = timestamp.toString();
    await _dbRef.child('Users/$peerSanitized/notifications/$notificationId').set({
      'id': notificationId,
      'type': 'new_message',
      'title': 'New Message',
      'message': '$myName: $text',
      'timestamp': timestamp,
      'isRead': false,
      'senderEmail': myEmail,
      'senderName': myName,
      'roomId': roomId,
      'msgId': msgId,
    });
  }

  String _getMessageDateString(int timestamp) {
    final date = DateTime.fromMillisecondsSinceEpoch(timestamp);
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final yesterday = today.subtract(const Duration(days: 1));
    final checkDate = DateTime(date.year, date.month, date.day);

    if (checkDate == today) {
      return "Today";
    } else if (checkDate == yesterday) {
      return "Yesterday";
    } else {
      const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      final monthStr = date.month > 0 && date.month <= 12 ? months[date.month - 1] : "";
      return "$monthStr ${date.day}, ${date.year}";
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(kToolbarHeight),
        child: _buildAppBar(context),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: _isLoading
                  ? const Center(child: CircularProgressIndicator(color: Color(0xFF3B82F6)))
                  : _messages.isEmpty
                      ? Center(
                          child: Text(
                            "No messages yet.\nSay hello!",
                            style: GoogleFonts.outfit(color: Colors.black38, fontSize: 16),
                          ),
                        )
                      : ListView.builder(
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                          itemCount: _messages.length,
                          itemBuilder: (context, index) {
                            final msg = _messages[index];
                            final showDateHeader = index == 0 ||
                                _getMessageDateString(msg.timestamp) !=
                                    _getMessageDateString(_messages[index - 1].timestamp);

                            if (showDateHeader) {
                              return Column(
                                crossAxisAlignment: CrossAxisAlignment.stretch,
                                children: [
                                  _buildDateSeparator(_getMessageDateString(msg.timestamp)),
                                  _buildMessageBubble(msg),
                                ],
                              );
                            }
                            return _buildMessageBubble(msg);
                          },
                        ),
            ),
            _buildInputArea(),
          ],
        ),
      ),
    );
  }

  Widget _buildAppBar(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.white,
      elevation: 0,
      scrolledUnderElevation: 0,
      leading: IconButton(
        icon: const Icon(Icons.arrow_back, color: Colors.black),
        onPressed: () => Navigator.pop(context),
      ),
      titleSpacing: 0,
      title: Row(
        children: [
          CircleAvatar(
            radius: 20,
            backgroundColor: Colors.blue.shade100,
            backgroundImage: AuthService.getAvatarProvider(_peerAvatarUrl),
            child: _peerAvatarUrl == null || _peerAvatarUrl!.isEmpty
                ? Text(
                    (_peerName ?? widget.userName).isNotEmpty ? (_peerName ?? widget.userName)[0].toUpperCase() : "?",
                    style: GoogleFonts.outfit(color: Colors.blue.shade800, fontWeight: FontWeight.bold, fontSize: 16),
                  )
                : null,
          ),
          const SizedBox(width: 12),
          Text(
            _peerName ?? widget.userName,
            style: GoogleFonts.outfit(
              color: Colors.black,
              fontSize: 18,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDateSeparator(String date) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 16),
      child: Center(
        child: Text(
          date,
          style: GoogleFonts.outfit(
            color: Colors.black38,
            fontSize: 13,
            fontWeight: FontWeight.w500,
          ),
        ),
      ),
    );
  }

  Widget _buildMessageBubble(MessageData msg) {
    final bubbleColor = msg.isMe ? const Color(0xFF3B82F6) : const Color(0xFFECECEC);
    final textColor = msg.isMe ? Colors.white : Colors.black87;
    final timeColor = msg.isMe ? Colors.white.withOpacity(0.7) : Colors.black45;

    return Align(
      alignment: msg.isMe ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        constraints: BoxConstraints(
          maxWidth: MediaQuery.of(context).size.width * 0.75,
        ),
        decoration: BoxDecoration(
          color: bubbleColor,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Wrap(
          alignment: WrapAlignment.end,
          crossAxisAlignment: WrapCrossAlignment.end,
          spacing: 8,
          runSpacing: 4,
          children: [
            Text(
              msg.text,
              style: GoogleFonts.outfit(
                color: textColor,
                fontSize: 15,
                fontWeight: FontWeight.w400,
              ),
            ),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  msg.time,
                  style: GoogleFonts.outfit(
                    color: timeColor,
                    fontSize: 10,
                  ),
                ),
                if (msg.isMe) ...[
                  const SizedBox(width: 4),
                  Icon(
                    msg.seen
                        ? Icons.done_all
                        : (msg.delivered ? Icons.done_all : Icons.done),
                    size: 14,
                    color: msg.seen ? Colors.cyanAccent : timeColor,
                  ),
                  const SizedBox(width: 2),
                  Text(
                    msg.seen
                        ? "Seen"
                        : (msg.delivered ? "Delivered" : "Sent"),
                    style: GoogleFonts.outfit(
                      color: msg.seen ? Colors.cyanAccent : timeColor,
                      fontSize: 9,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ],
            ),
          ],
        ),
      ),
    ).animate().fadeIn(duration: 250.ms).slideX(begin: msg.isMe ? 0.05 : -0.05);
  }

  Widget _buildInputArea() {
    return Container(
      color: Colors.white,
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      child: Row(
        children: [
          Expanded(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              decoration: BoxDecoration(
                color: const Color(0xFFF3F4F6),
                borderRadius: BorderRadius.circular(24),
              ),
              child: TextField(
                controller: _controller,
                enabled: _isConnected,
                style: GoogleFonts.outfit(color: Colors.black87),
                decoration: InputDecoration(
                  hintText: _isConnected ? "Message..." : "Waiting for connection...",
                  hintStyle: GoogleFonts.outfit(color: Colors.black38),
                  border: InputBorder.none,
                  contentPadding: const EdgeInsets.symmetric(vertical: 10),
                ),
              ),
            ),
          ),
          const SizedBox(width: 12),
          GestureDetector(
            onTap: _sendMessage,
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: _isConnected ? const Color(0xFF3B82F6) : Colors.grey,
                shape: BoxShape.circle,
              ),
              child: const Icon(
                Icons.send_rounded,
                color: Colors.white,
                size: 20,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class MessageData {
  final String text;
  final String time;
  final bool isMe;
  final int timestamp;
  final bool seen;
  final bool delivered;

  MessageData({
    required this.text,
    required this.time,
    required this.isMe,
    required this.timestamp,
    required this.seen,
    required this.delivered,
  });
}
