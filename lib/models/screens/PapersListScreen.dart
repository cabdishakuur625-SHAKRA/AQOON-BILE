import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../../services/firebase_service.dart';
import '../subject.dart';
import '../paper.dart';
import 'PaperViewScreen.dart';

class PapersListScreen extends StatefulWidget {
  const PapersListScreen({super.key});

  @override
  State<PapersListScreen> createState() => _PapersListScreenState();
}

class _PapersListScreenState extends State<PapersListScreen> {
  final FirebaseService _firebaseService = FirebaseService();
  
  String _searchQuery = '';
  String? _selectedYear; // Null means 'All'

  final List<String> _years = ['All', '2021', '2022', '2023', '2024', '2025'];

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
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildAppBar(context),
              
              // Search Bar
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: _buildSearchBar(),
              ),
              const SizedBox(height: 16),
              
              // Years filter list
              _buildYearsFilter(),
              const SizedBox(height: 16),
              
              // Header
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Text(
                  "Available Papers",
                  style: GoogleFonts.outfit(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 12),
              
              // Papers List
              Expanded(
                child: StreamBuilder<List<Paper>>(
                  stream: _firebaseService.getPapers(),
                  builder: (context, snapshot) {
                    final firebasePapers = snapshot.data ?? [];
                    
                    final List<Paper> localPapers = [
                      Paper(
                        id: 'local_2021',
                        title: 'Exam F4 2021',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2021',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2021.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2022',
                        title: 'Exam F4 2022',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2022',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2022.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2023',
                        title: 'Exam F4 2023',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2023',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2023.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2024',
                        title: 'Exam F4 2024',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2024',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2024.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                    final List<Paper> localPapers = [
                      Paper(
                        id: 'local_2021',
                        title: 'Exam F4 2021',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2021',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2021.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2022',
                        title: 'Exam F4 2022',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2022',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2022.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2023',
                        title: 'Exam F4 2023',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2023',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2023.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2024',
                        title: 'Exam F4 2024',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2024',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2024.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                      Paper(
                        id: 'local_2025',
                        title: 'Exam F4 2025',
                        subjectId: 'general',
                        subjectName: 'General Exam',
                        year: '2025',
                        pdfUrl: 'Past Exam Pepars/Exam F4 2025.pdf',
                        uploadedAt: 0,
                        isAsset: true,
                      ),
                    ];

                    final allPapers = [...localPapers, ...firebasePapers];
                    
                    // Filter papers based on search query and year
                    final filteredPapers = allPapers.where((paper) {
                      final matchesSearch = paper.title.toLowerCase().contains(_searchQuery.toLowerCase());
                      final matchesYear = _selectedYear == null || paper.year == _selectedYear;
                      return matchesSearch && matchesYear;
                    }).toList();

                    // Sort: order by exam year ascending: 2021, 2022, 2023, 2024, 2025
                    filteredPapers.sort((a, b) => a.year.compareTo(b.year));

                    if (filteredPapers.isEmpty) {
                      return Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.find_in_page_outlined, size: 72, color: Colors.white.withOpacity(0.3)),
                            const SizedBox(height: 16),
                            Text(
                              "No papers found",
                              style: GoogleFonts.outfit(color: Colors.white70, fontSize: 18, fontWeight: FontWeight.w500),
                            ),
                            const SizedBox(height: 8),
                            Text(
                              "Try adjusting your filters or search query.",
                              style: GoogleFonts.outfit(color: Colors.white38, fontSize: 14),
                            ),
                          ],
                        ),
                      );
                    }

                    return ListView.builder(
                      physics: const BouncingScrollPhysics(),
                      padding: const EdgeInsets.symmetric(horizontal: 20),
                      itemCount: filteredPapers.length,
                      itemBuilder: (context, index) {
                        final paper = filteredPapers[index];
                        return _buildPaperCard(paper, index);
                      },
                    );
                  },
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
            "Past Papers",
            style: GoogleFonts.outfit(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          // Clear filters button as right action if any filter is active
          if (_selectedYear != null || _searchQuery.isNotEmpty)
            IconButton(
              onPressed: () {
                setState(() {
                  _selectedYear = null;
                  _searchQuery = '';
                });
              },
              icon: const Icon(Icons.filter_alt_off_rounded, color: Colors.cyanAccent),
              style: IconButton.styleFrom(
                backgroundColor: Colors.white.withOpacity(0.1),
                padding: const EdgeInsets.all(12),
              ),
            )
          else
            const SizedBox(width: 48), // Spacer to center title
        ],
      ),
    ).animate().slideY(begin: -1, duration: 600.ms);
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
        style: const TextStyle(color: Colors.white),
        onChanged: (val) {
          setState(() {
            _searchQuery = val;
          });
        },
        decoration: InputDecoration(
          icon: const Icon(Icons.search_rounded, color: Colors.white54),
          hintText: "Search exam papers...",
          hintStyle: GoogleFonts.outfit(color: Colors.white38),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 18),
        ),
      ),
    ).animate().fadeIn(duration: 800.ms).slideX(begin: 0.1);
  }

  Widget _buildYearsFilter() {
    return SizedBox(
      height: 40,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        padding: const EdgeInsets.symmetric(horizontal: 20),
        itemCount: _years.length,
        itemBuilder: (context, index) {
          final yearStr = _years[index];
          final isAll = yearStr == 'All';
          
          final isSelected = isAll 
              ? _selectedYear == null 
              : _selectedYear == yearStr;

          return Padding(
            padding: const EdgeInsets.only(right: 8),
            child: FilterChip(
              label: Text(isAll ? 'All Years' : 'Year $yearStr'),
              selected: isSelected,
              checkmarkColor: Colors.purpleAccent,
              color: WidgetStateProperty.resolveWith<Color?>((states) {
                if (states.contains(WidgetState.selected)) {
                  return Colors.purpleAccent.withOpacity(0.2);
                }
                return Colors.white.withOpacity(0.06);
              }),
              surfaceTintColor: Colors.transparent,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
                side: BorderSide(
                  color: isSelected ? Colors.purpleAccent.withOpacity(0.5) : Colors.white12,
                ),
              ),
              labelStyle: GoogleFonts.outfit(
                color: isSelected ? Colors.purpleAccent : Colors.white70,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                fontSize: 13,
              ),
              onSelected: (selected) {
                setState(() {
                  _selectedYear = isAll ? null : yearStr;
                });
              },
            ),
          );
        },
      ),
    ).animate().fadeIn(delay: 150.ms);
  }

  Widget _buildPaperCard(Paper paper, int index) {
    // Determine card styling based on Subject ID using unified model helpers
    final IconData iconData = Subject.getIconForId(paper.subjectId);
    final List<Color> gradientColors = Subject.getGradientColorsForId(paper.subjectId);

    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => PaperViewScreen(paper: paper),
          ),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(25),
          border: Border.all(color: Colors.white.withOpacity(0.08)),
        ),
        child: Row(
          children: [
            // Subject Gradient Icon
            Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                gradient: LinearGradient(
                  colors: gradientColors,
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
              ),
              child: Icon(iconData, color: Colors.white, size: 28),
            ),
            const SizedBox(width: 16),
            
            // Text info
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    paper.title,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: GoogleFonts.outfit(
                      color: Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          paper.subjectName,
                          style: GoogleFonts.outfit(
                            color: Colors.cyanAccent,
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          "Year ${paper.year}",
                          style: GoogleFonts.outfit(
                            color: Colors.purpleAccent,
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            const SizedBox(width: 8),
            
            // Go Arrow
            Icon(
              Icons.chevron_right_rounded,
              color: Colors.white.withOpacity(0.4),
              size: 28,
            ),
          ],
        ),
      ).animate().fadeIn(delay: (index * 50).ms, duration: 400.ms).slideY(begin: 0.1),
    );
  }
}
