import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';
import 'package:url_launcher/url_launcher.dart';
import '../paper.dart';

class PaperViewScreen extends StatefulWidget {
  final Paper paper;

  const PaperViewScreen({super.key, required this.paper});

  @override
  State<PaperViewScreen> createState() => _PaperViewScreenState();
}

class _PaperViewScreenState extends State<PaperViewScreen> {
  late PdfViewerController _pdfViewerController;
  bool _isLoading = true;
  bool _hasError = false;
  String _errorMessage = '';
  
  int _pageCount = 0;
  int _currentPage = 0;
  double _zoomLevel = 1.00;

  @override
  void initState() {
    super.initState();
    _pdfViewerController = PdfViewerController();
  }

  @override
  void dispose() {
    _pdfViewerController.dispose();
    super.dispose();
  }

  Future<void> _openExternal() async {
    final Uri url = Uri.parse(widget.paper.pdfUrl);
    try {
      if (await canLaunchUrl(url)) {
        await launchUrl(url, mode: LaunchMode.externalApplication);
      } else {
        throw 'Could not launch $url';
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Could not open external browser: $e')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1B4B),
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              widget.paper.title,
              style: GoogleFonts.outfit(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
            ),
            Text(
              '${widget.paper.subjectName} • ${widget.paper.year}',
              style: GoogleFonts.outfit(color: Colors.cyanAccent, fontSize: 12, fontWeight: FontWeight.w500),
            ),
          ],
        ),
        backgroundColor: const Color(0xFF1E1B4B),
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
        actions: [
          IconButton(
            icon: const Icon(Icons.open_in_browser_rounded, color: Colors.cyanAccent),
            tooltip: 'Open in Browser',
            onPressed: _openExternal,
          ),
        ],
      ),
      body: Container(
        color: Colors.white, // Standard white background for PDF page rendering contrast
        child: Stack(
          children: [
            if (!_hasError)
              widget.paper.isAsset
                  ? SfPdfViewer.asset(
                      widget.paper.pdfUrl,
                      controller: _pdfViewerController,
                      canShowScrollHead: true,
                      canShowScrollStatus: true,
                      onDocumentLoaded: (PdfDocumentLoadedDetails details) {
                        setState(() {
                          _isLoading = false;
                          _pageCount = details.document.pages.count;
                          _currentPage = _pdfViewerController.pageNumber;
                        });
                      },
                      onPageChanged: (PdfPageChangedDetails details) {
                        setState(() {
                          _currentPage = details.newPageNumber;
                        });
                      },
                      onDocumentLoadFailed: (PdfDocumentLoadFailedDetails details) {
                        setState(() {
                          _isLoading = false;
                          _hasError = true;
                          _errorMessage = details.description;
                        });
                      },
                    )
                  : SfPdfViewer.network(
                      widget.paper.pdfUrl,
                      controller: _pdfViewerController,
                      canShowScrollHead: true,
                      canShowScrollStatus: true,
                      onDocumentLoaded: (PdfDocumentLoadedDetails details) {
                        setState(() {
                          _isLoading = false;
                          _pageCount = details.document.pages.count;
                          _currentPage = _pdfViewerController.pageNumber;
                        });
                      },
                      onPageChanged: (PdfPageChangedDetails details) {
                        setState(() {
                          _currentPage = details.newPageNumber;
                        });
                      },
                      onDocumentLoadFailed: (PdfDocumentLoadFailedDetails details) {
                        setState(() {
                          _isLoading = false;
                          _hasError = true;
                          _errorMessage = details.description;
                        });
                      },
                    ),
            
            // Loading Overlay
            if (_isLoading)
              Container(
                color: const Color(0xFF1E1B4B).withOpacity(0.9),
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const CircularProgressIndicator(color: Colors.cyanAccent),
                      const SizedBox(height: 20),
                      Text(
                        "Loading PDF document...",
                        style: GoogleFonts.outfit(color: Colors.white70, fontSize: 16),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        "Please make sure you have internet connection.",
                        style: GoogleFonts.outfit(color: Colors.white38, fontSize: 12),
                      ),
                    ],
                  ),
                ),
              ),

            // Error Overlay
            if (_hasError)
              Container(
                color: const Color(0xFF1E1B4B),
                padding: const EdgeInsets.all(24),
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(Icons.error_outline_rounded, size: 72, color: Colors.redAccent),
                      const SizedBox(height: 24),
                      Text(
                        "Unable to Load PDF",
                        style: GoogleFonts.outfit(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 12),
                      Text(
                        _errorMessage.isNotEmpty 
                            ? _errorMessage 
                            : "The PDF could not be fetched. If this is an uploaded paper, please make sure your Firebase Storage security rules allow public reads.",
                        textAlign: TextAlign.center,
                        style: GoogleFonts.outfit(color: Colors.white70, fontSize: 14),
                      ),
                      const SizedBox(height: 30),
                      ElevatedButton.icon(
                        onPressed: _openExternal,
                        icon: const Icon(Icons.open_in_new_rounded),
                        label: const Text("Open PDF in Browser"),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.blueAccent,
                          foregroundColor: Colors.white,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                        ),
                      ),
                      const SizedBox(height: 12),
                      TextButton(
                        onPressed: () {
                          setState(() {
                            _isLoading = true;
                            _hasError = false;
                            _errorMessage = '';
                          });
                        },
                        child: Text(
                          "Retry Loading",
                          style: GoogleFonts.outfit(color: Colors.cyanAccent),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
          ],
        ),
      ),
      
      // Bottom toolbar for Navigation & Zoom controls (only active when PDF loads successfully)
      bottomNavigationBar: (!_isLoading && !_hasError)
          ? Container(
              height: 60,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              color: const Color(0xFF1E1B4B),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Page Indicators
                  Text(
                    'Page $_currentPage of $_pageCount',
                    style: GoogleFonts.outfit(color: Colors.white, fontSize: 14, fontWeight: FontWeight.w500),
                  ),
                  
                  // Zoom Controls
                  Row(
                    children: [
                      IconButton(
                        icon: const Icon(Icons.zoom_out_rounded, color: Colors.white70),
                        onPressed: () {
                          if (_zoomLevel > 1.0) {
                            setState(() {
                              _zoomLevel = (_zoomLevel - 0.25).clamp(1.0, 3.0);
                              _pdfViewerController.zoomLevel = _zoomLevel;
                            });
                          }
                        },
                      ),
                      Text(
                        '${(_zoomLevel * 100).toInt()}%',
                        style: GoogleFonts.outfit(color: Colors.white70, fontSize: 12),
                      ),
                      IconButton(
                        icon: const Icon(Icons.zoom_in_rounded, color: Colors.white70),
                        onPressed: () {
                          if (_zoomLevel < 3.0) {
                            setState(() {
                              _zoomLevel = (_zoomLevel + 0.25).clamp(1.0, 3.0);
                              _pdfViewerController.zoomLevel = _zoomLevel;
                            });
                          }
                        },
                      ),
                    ],
                  ),
                  
                  // Page Jump Buttons
                  Row(
                    children: [
                      IconButton(
                        icon: const Icon(Icons.keyboard_arrow_up_rounded, color: Colors.white),
                        onPressed: _currentPage > 1
                            ? () => _pdfViewerController.previousPage()
                            : null,
                      ),
                      IconButton(
                        icon: const Icon(Icons.keyboard_arrow_down_rounded, color: Colors.white),
                        onPressed: _currentPage < _pageCount
                            ? () => _pdfViewerController.nextPage()
                            : null,
                      ),
                    ],
                  ),
                ],
              ),
            )
          : null,
    );
  }
}
