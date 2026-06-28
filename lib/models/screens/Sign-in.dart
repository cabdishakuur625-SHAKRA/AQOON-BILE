import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/auth_service.dart';
import 'Sign-up.dart';
import 'HomeScreen.dart';

class SignInScreen extends StatefulWidget {
  const SignInScreen({super.key});

  @override
  State<SignInScreen> createState() => _SignInScreenState();
}

class _SignInScreenState extends State<SignInScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  
  bool _obscurePassword = true;
  bool _isLoading = false;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _handleSignIn() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      await AuthService.loginUser(
        email: _emailController.text.trim(),
        password: _passwordController.text,
      );

      if (mounted) {
        // Show success snackbar
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Row(
              children: [
                const Icon(Icons.verified_user_rounded, color: Colors.cyanAccent),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    'Welcome back, ${AuthService.currentUser?.fullName}!',
                    style: GoogleFonts.outfit(fontWeight: FontWeight.w600, color: Colors.white),
                  ),
                ),
              ],
            ),
            backgroundColor: const Color(0xFF312E81),
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
            elevation: 10,
          ),
        );

        // Transition smoothly to the HomeScreen
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => const HomeScreen()),
        );
      }
    } catch (e) {
      if (mounted) {
        // Show failure dialog
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            backgroundColor: const Color(0xFF1E1B4B),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(20),
              side: const BorderSide(color: Colors.redAccent, width: 1),
            ),
            title: Row(
              children: [
                const Icon(Icons.lock_person_rounded, color: Colors.redAccent),
                const SizedBox(width: 10),
                Text(
                  "Access Denied",
                  style: GoogleFonts.outfit(color: Colors.white, fontWeight: FontWeight.bold),
                ),
              ],
            ),
            content: Text(
              e.toString().replaceAll('Exception: ', ''),
              style: GoogleFonts.outfit(color: Colors.white70),
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: Text(
                  "TRY AGAIN",
                  style: GoogleFonts.outfit(color: Colors.cyanAccent, fontWeight: FontWeight.bold),
                ),
              ),
            ],
          ),
        );
      }
    } finally {
      if (mounted) {
        setState(() => _isLoading = false);
      }
    }
  }

  // Dynamic Password Recovery Modal
  void _showForgotPasswordDialog() {
    final recoveryEmailController = TextEditingController(text: _emailController.text.trim());
    final codeController = TextEditingController();
    final newPasswordController = TextEditingController();
    final confirmPasswordController = TextEditingController();

    final formKey1 = GlobalKey<FormState>();
    final formKey2 = GlobalKey<FormState>();
    final formKey3 = GlobalKey<FormState>();

    int step = 1; // 1 = Email, 2 = Code, 3 = Password, 4 = Success
    bool isLoading = false;
    String generatedCode = '';
    String enteredEmail = '';
    String errorMessage = '';

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setModalState) {
            return Container(
              padding: EdgeInsets.only(
                bottom: MediaQuery.of(context).viewInsets.bottom + 30,
                top: 25,
                left: 25,
                right: 25,
              ),
              decoration: const BoxDecoration(
                color: Color(0xFF1E1B4B),
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(30),
                  topRight: Radius.circular(30),
                ),
                border: Border(
                  top: BorderSide(color: Colors.cyanAccent, width: 1.5),
                ),
              ),
              child: SingleChildScrollView(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Center(
                      child: Container(
                        width: 50,
                        height: 5,
                        decoration: BoxDecoration(
                          color: Colors.white24,
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                    ),
                    const SizedBox(height: 25),
                    Text(
                      step == 4 ? "Success!" : "Recover Password",
                      style: GoogleFonts.outfit(
                        color: Colors.white,
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 10),
                    Text(
                      step == 1
                          ? "Enter your registered email below to generate a verification code."
                          : step == 2
                              ? "A verification code has been generated. Enter the code below to verify."
                              : step == 3
                                  ? "Enter your new secure account password below."
                                  : "Your account password has been successfully updated.",
                      style: GoogleFonts.outfit(color: Colors.white60, fontSize: 14),
                    ),
                    const SizedBox(height: 25),

                    if (step == 1) ...[
                      Form(
                        key: formKey1,
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              decoration: BoxDecoration(
                                color: Colors.white.withOpacity(0.06),
                                borderRadius: BorderRadius.circular(15),
                                border: Border.all(
                                  color: errorMessage.isNotEmpty
                                      ? Colors.redAccent.withOpacity(0.5)
                                      : Colors.white.withOpacity(0.12),
                                ),
                              ),
                              child: TextFormField(
                                controller: recoveryEmailController,
                                keyboardType: TextInputType.emailAddress,
                                style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                                validator: (value) {
                                  if (value == null || value.trim().isEmpty) {
                                    return 'Please enter your email address';
                                  }
                                  if (!RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$').hasMatch(value.trim())) {
                                    return 'Please enter a valid email address';
                                  }
                                  return null;
                                },
                                decoration: InputDecoration(
                                  prefixIcon: const Icon(Icons.email_outlined, color: Colors.white54, size: 22),
                                  hintText: "example@gmail.com",
                                  hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                                  border: InputBorder.none,
                                  contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                                ),
                              ),
                            ),
                            if (errorMessage.isNotEmpty) ...[
                              const SizedBox(height: 10),
                              Row(
                                children: [
                                  const Icon(Icons.error_outline_rounded, color: Colors.redAccent, size: 16),
                                  const SizedBox(width: 6),
                                  Expanded(
                                    child: Text(
                                      errorMessage,
                                      style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 13),
                                    ),
                                  ),
                                ],
                              ).animate().shake(),
                            ],
                            const SizedBox(height: 25),
                            SizedBox(
                              width: double.infinity,
                              height: 55,
                              child: ElevatedButton(
                                onPressed: isLoading
                                    ? null
                                    : () async {
                                        if (!formKey1.currentState!.validate()) return;

                                        setModalState(() {
                                          isLoading = true;
                                          errorMessage = '';
                                        });

                                        try {
                                          final email = recoveryEmailController.text.trim();
                                          final int randomCodeNum = (DateTime.now().millisecondsSinceEpoch % 900000) + 100000;
                                          final codeStr = randomCodeNum.toString();

                                          await AuthService.sendRecoveryCode(email, codeStr);

                                          setModalState(() {
                                            enteredEmail = email;
                                            generatedCode = codeStr;
                                            step = 2;
                                          });

                                          // Show simulated code toast for testing
                                          if (mounted) {
                                            ScaffoldMessenger.of(context).showSnackBar(
                                              SnackBar(
                                                content: Text(
                                                  "Simulation Code: $codeStr",
                                                  style: GoogleFonts.outfit(fontWeight: FontWeight.bold),
                                                ),
                                                backgroundColor: Colors.orangeAccent,
                                                duration: const Duration(seconds: 10),
                                              ),
                                            );
                                          }
                                        } catch (e) {
                                          setModalState(() {
                                            errorMessage = e.toString().replaceAll('Exception: ', '');
                                          });
                                        } finally {
                                          setModalState(() {
                                            isLoading = false;
                                          });
                                        }
                                      },
                                style: ElevatedButton.styleFrom(
                                  backgroundColor: Colors.cyanAccent,
                                  foregroundColor: Colors.black,
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(15),
                                  ),
                                ),
                                child: isLoading
                                    ? const SizedBox(
                                        width: 24,
                                        height: 24,
                                        child: CircularProgressIndicator(color: Colors.black, strokeWidth: 2),
                                      )
                                    : Text(
                                        "GENERATE CODE",
                                        style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 15),
                                      ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ] else if (step == 2) ...[
                      Form(
                        key: formKey2,
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              decoration: BoxDecoration(
                                color: Colors.white.withOpacity(0.06),
                                borderRadius: BorderRadius.circular(15),
                                border: Border.all(
                                  color: errorMessage.isNotEmpty
                                      ? Colors.redAccent.withOpacity(0.5)
                                      : Colors.white.withOpacity(0.12),
                                ),
                              ),
                              child: TextFormField(
                                controller: codeController,
                                keyboardType: TextInputType.number,
                                style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                                validator: (value) {
                                  if (value == null || value.trim().isEmpty) {
                                    return 'Please enter verification code';
                                  }
                                  return null;
                                },
                                decoration: InputDecoration(
                                  prefixIcon: const Icon(Icons.security_rounded, color: Colors.white54, size: 22),
                                  hintText: "Enter 6-digit Code",
                                  hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
                                  border: InputBorder.none,
                                  contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                                ),
                              ),
                            ),
                            if (errorMessage.isNotEmpty) ...[
                              const SizedBox(height: 10),
                              Row(
                                children: [
                                  const Icon(Icons.error_outline_rounded, color: Colors.redAccent, size: 16),
                                  const SizedBox(width: 6),
                                  Expanded(
                                    child: Text(
                                      errorMessage,
                                      style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 13),
                                    ),
                                  ),
                                ],
                              ).animate().shake(),
                            ],
                            const SizedBox(height: 25),
                            SizedBox(
                              width: double.infinity,
                              height: 55,
                              child: ElevatedButton(
                                onPressed: () {
                                  if (!formKey2.currentState!.validate()) return;
                                  
                                  final enteredCode = codeController.text.trim();
                                  if (enteredCode != generatedCode) {
                                    setModalState(() {
                                      errorMessage = "Invalid verification code.";
                                    });
                                    return;
                                  }

                                  setModalState(() {
                                    errorMessage = '';
                                    step = 3;
                                  });
                                },
                                style: ElevatedButton.styleFrom(
                                  backgroundColor: Colors.cyanAccent,
                                  foregroundColor: Colors.black,
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(15),
                                  ),
                                ),
                                child: Text(
                                  "VERIFY CODE",
                                  style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 15),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ] else if (step == 3) ...[
                      Form(
                        key: formKey3,
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            // New Password Input
                            Text("New Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                            const SizedBox(height: 8),
                            Container(
                              decoration: BoxDecoration(
                                color: Colors.white.withOpacity(0.06),
                                borderRadius: BorderRadius.circular(15),
                                border: Border.all(color: Colors.white.withOpacity(0.12)),
                              ),
                              child: TextFormField(
                                controller: newPasswordController,
                                obscureText: true,
                                style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                                validator: (value) {
                                  if (value == null || value.isEmpty) {
                                    return 'Please enter a new password';
                                  }
                                  if (value.length < 6) {
                                    return 'Password must be at least 6 characters';
                                  }
                                  if (!RegExp(r'[a-zA-Z]').hasMatch(value) || !RegExp(r'[0-9]').hasMatch(value)) {
                                    return 'Password must contain both letters and numbers';
                                  }
                                  return null;
                                },
                                decoration: const InputDecoration(
                                  prefixIcon: Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                                  border: InputBorder.none,
                                  contentPadding: EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                                ),
                              ),
                            ),
                            const SizedBox(height: 15),

                            // Confirm Password Input
                            Text("Confirm Password", style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13, fontWeight: FontWeight.bold)),
                            const SizedBox(height: 8),
                            Container(
                              decoration: BoxDecoration(
                                color: Colors.white.withOpacity(0.06),
                                borderRadius: BorderRadius.circular(15),
                                border: Border.all(color: Colors.white.withOpacity(0.12)),
                              ),
                              child: TextFormField(
                                controller: confirmPasswordController,
                                obscureText: true,
                                style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
                                validator: (value) {
                                  if (value == null || value.isEmpty) {
                                    return 'Please confirm password';
                                  }
                                  if (value != newPasswordController.text) {
                                    return 'Passwords do not match';
                                  }
                                  return null;
                                },
                                decoration: const InputDecoration(
                                  prefixIcon: Icon(Icons.lock_reset_rounded, color: Colors.white54, size: 22),
                                  border: InputBorder.none,
                                  contentPadding: EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                                ),
                              ),
                            ),
                            if (errorMessage.isNotEmpty) ...[
                              const SizedBox(height: 15),
                              Row(
                                children: [
                                  const Icon(Icons.error_outline_rounded, color: Colors.redAccent, size: 16),
                                  const SizedBox(width: 6),
                                  Expanded(
                                    child: Text(
                                      errorMessage,
                                      style: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 13),
                                    ),
                                  ),
                                ],
                              ).animate().shake(),
                            ],
                            const SizedBox(height: 25),
                            SizedBox(
                              width: double.infinity,
                              height: 55,
                              child: ElevatedButton(
                                onPressed: isLoading
                                    ? null
                                    : () async {
                                        if (!formKey3.currentState!.validate()) return;

                                        setModalState(() {
                                          isLoading = true;
                                          errorMessage = '';
                                        });

                                        try {
                                          await AuthService.resetPasswordWithCode(
                                            email: enteredEmail,
                                            code: generatedCode,
                                            newPassword: newPasswordController.text,
                                          );

                                          setModalState(() {
                                            step = 4;
                                          });
                                        } catch (e) {
                                          setModalState(() {
                                            errorMessage = e.toString().replaceAll('Exception: ', '');
                                          });
                                        } finally {
                                          setModalState(() {
                                            isLoading = false;
                                          });
                                        }
                                      },
                                style: ElevatedButton.styleFrom(
                                  backgroundColor: Colors.cyanAccent,
                                  foregroundColor: Colors.black,
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(15),
                                  ),
                                ),
                                child: isLoading
                                    ? const SizedBox(
                                        width: 24,
                                        height: 24,
                                        child: CircularProgressIndicator(color: Colors.black, strokeWidth: 2),
                                      )
                                    : Text(
                                        "RESET PASSWORD",
                                        style: GoogleFonts.outfit(fontWeight: FontWeight.bold, fontSize: 15),
                                      ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ] else ...[
                      // Step 4: Success Screen
                      Center(
                        child: Column(
                          children: [
                            const Icon(Icons.check_circle_rounded, color: Colors.cyanAccent, size: 60)
                                .animate()
                                .scale(duration: 500.ms, curve: Curves.easeOutBack),
                            const SizedBox(height: 15),
                            Text(
                              "Password Updated!",
                              style: GoogleFonts.outfit(
                                color: Colors.white,
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            const SizedBox(height: 10),
                            Text(
                              "Your password has been successfully reset. You can now use your new password to sign in.",
                              textAlign: TextAlign.center,
                              style: GoogleFonts.outfit(color: Colors.white70, fontSize: 13),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 25),
                      SizedBox(
                        width: double.infinity,
                        height: 55,
                        child: OutlinedButton(
                          onPressed: () => Navigator.pop(context),
                          style: OutlinedButton.styleFrom(
                            side: const BorderSide(color: Colors.cyanAccent),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(15),
                            ),
                          ),
                          child: Text(
                            "DONE",
                            style: GoogleFonts.outfit(
                              color: Colors.cyanAccent,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Color(0xFF1E1B4B),
              Color(0xFF312E81),
              Color(0xFF4338CA),
            ],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              physics: const BouncingScrollPhysics(),
              padding: const EdgeInsets.symmetric(horizontal: 25),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const SizedBox(height: 20),
                    // BRAND LOGO WIDGET
                    Container(
                      width: 110,
                      height: 110,
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(28),
                        border: Border.all(color: Colors.white.withOpacity(0.2), width: 2),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.cyanAccent.withOpacity(0.25),
                            blurRadius: 25,
                            spreadRadius: 2,
                          ),
                        ],
                      ),
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(26),
                        child: Image.asset(
                          "assets/images/app_logo.jpg",
                          fit: BoxFit.cover,
                        ),
                      ),
                    ).animate().scale(duration: 650.ms, curve: Curves.easeOutBack),
                    
                    const SizedBox(height: 25),
                    
                    Text(
                      "Aqoon Bile",
                      style: GoogleFonts.outfit(
                        fontSize: 32,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                        letterSpacing: 1.5,
                      ),
                    ).animate().fadeIn(delay: 150.ms, duration: 600.ms),
                    
                    Text(
                      "Your Gateway to Ultimate Knowledge",
                      style: GoogleFonts.outfit(
                        fontSize: 14,
                        color: Colors.white54,
                        letterSpacing: 0.5,
                      ),
                    ).animate().fadeIn(delay: 250.ms, duration: 600.ms),
                    
                    const SizedBox(height: 40),

                    // EMAIL FIELD
                    _buildInputField(
                      controller: _emailController,
                      icon: Icons.email_outlined,
                      hint: "Email Address",
                      keyboardType: TextInputType.emailAddress,
                      validator: (value) {
                        if (value == null || value.trim().isEmpty) {
                          return 'Please enter your email address';
                        }
                        if (!RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$').hasMatch(value.trim())) {
                          return 'Please enter a valid email address';
                        }
                        return null;
                      },
                    ).animate().fadeIn(delay: 350.ms).slideY(begin: 0.1),
                    
                    const SizedBox(height: 18),

                    // PASSWORD FIELD
                    _buildPasswordField().animate().fadeIn(delay: 450.ms).slideY(begin: 0.1),
                    
                    // FORGOT PASSWORD
                    Align(
                      alignment: Alignment.centerRight,
                      child: TextButton(
                        onPressed: _showForgotPasswordDialog,
                        child: Text(
                          "Forgot password?",
                          style: GoogleFonts.outfit(
                            color: Colors.cyanAccent,
                            fontSize: 14,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ).animate().fadeIn(delay: 500.ms),
                    
                    const SizedBox(height: 20),

                    // SIGN IN BUTTON
                    SizedBox(
                      width: double.infinity,
                      height: 55,
                      child: ElevatedButton(
                        onPressed: _isLoading ? null : _handleSignIn,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white,
                          foregroundColor: const Color(0xFF1E1B4B),
                          disabledBackgroundColor: Colors.white.withOpacity(0.3),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15),
                          ),
                          elevation: 6,
                          shadowColor: Colors.black.withOpacity(0.3),
                        ),
                        child: _isLoading
                            ? const SizedBox(
                                width: 24,
                                height: 24,
                                child: CircularProgressIndicator(
                                  color: Color(0xFF1E1B4B),
                                  strokeWidth: 2.5,
                                ),
                              )
                            : Text(
                                "SIGN IN",
                                style: GoogleFonts.outfit(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 16,
                                  letterSpacing: 1.1,
                                ),
                              ),
                      ),
                    ).animate().fadeIn(delay: 550.ms).scale(curve: Curves.easeOutBack),
                    
                    const SizedBox(height: 25),
                    
                    Row(
                      children: [
                        Expanded(child: Divider(color: Colors.white.withOpacity(0.15))),
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 15),
                          child: Text(
                            "OR",
                            style: GoogleFonts.outfit(color: Colors.white38, fontSize: 13),
                          ),
                        ),
                        Expanded(child: Divider(color: Colors.white.withOpacity(0.15))),
                      ],
                    ),
                    
                    const SizedBox(height: 25),

                    // CREATE ACCOUNT BUTTON
                    SizedBox(
                      width: double.infinity,
                      height: 55,
                      child: OutlinedButton(
                        onPressed: () {
                          Navigator.pushReplacement(
                            context,
                            MaterialPageRoute(builder: (context) => const SignUpScreen()),
                          );
                        },
                        style: OutlinedButton.styleFrom(
                          side: BorderSide(color: Colors.white.withOpacity(0.3), width: 1.5),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15),
                          ),
                        ),
                        child: Text(
                          "Create an account",
                          style: GoogleFonts.outfit(
                            color: Colors.white,
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ).animate().fadeIn(delay: 650.ms),
                    const SizedBox(height: 30),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildInputField({
    required TextEditingController controller,
    required IconData icon,
    required String hint,
    required TextInputType keyboardType,
    required String? Function(String?) validator,
  }) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.06),
        borderRadius: BorderRadius.circular(15),
        border: Border.all(color: Colors.white.withOpacity(0.12)),
      ),
      child: TextFormField(
        controller: controller,
        keyboardType: keyboardType,
        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
        validator: validator,
        decoration: InputDecoration(
          prefixIcon: Icon(icon, color: Colors.white54, size: 22),
          hintText: hint,
          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
          errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
        ),
      ),
    );
  }

  Widget _buildPasswordField() {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.06),
        borderRadius: BorderRadius.circular(15),
        border: Border.all(color: Colors.white.withOpacity(0.12)),
      ),
      child: TextFormField(
        controller: _passwordController,
        obscureText: _obscurePassword,
        style: GoogleFonts.outfit(color: Colors.white, fontSize: 16),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Please enter your password';
          }
          return null;
        },
        decoration: InputDecoration(
          prefixIcon: const Icon(Icons.lock_outline_rounded, color: Colors.white54, size: 22),
          hintText: "Password",
          hintStyle: GoogleFonts.outfit(color: Colors.white38, fontSize: 15),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
          errorStyle: GoogleFonts.outfit(color: Colors.redAccent, fontSize: 12),
          suffixIcon: IconButton(
            icon: Icon(
              _obscurePassword ? Icons.visibility_off_outlined : Icons.visibility_outlined,
              color: Colors.white54,
              size: 20,
            ),
            onPressed: () {
              setState(() {
                _obscurePassword = !_obscurePassword;
              });
            },
          ),
        ),
      ),
    );
  }
}
