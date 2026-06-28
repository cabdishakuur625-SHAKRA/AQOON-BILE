import fitz
import re

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/English F4.pdf"
    doc = fitz.open(pdf_path)
    
    # regex matches unit followed by optional spaces then digits
    unit_pattern = re.compile(r'\bunit\s*(\d+)', re.IGNORECASE)
    
    print("Scanning entire text of all pages for Unit mentions:")
    found_units = {}
    
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        matches = unit_pattern.findall(text)
        if matches:
            for m in matches:
                unit_num = int(m)
                if unit_num not in found_units:
                    found_units[unit_num] = []
                found_units[unit_num].append(page_num + 1)
                
    for u in sorted(found_units.keys()):
        pages = found_units[u]
        print(f"Unit {u} mentioned on pages: {pages}")
        
        # Let's inspect the first page it's mentioned on
        first_page = pages[0]
        page_text = doc[first_page - 1].get_text()
        lines = [line.strip() for line in page_text.split('\n') if line.strip()]
        # find the line containing Unit and print it and subsequent lines
        for idx, line in enumerate(lines):
            if re.search(r'\bunit\s*' + str(u) + r'\b', line, re.IGNORECASE):
                print(f"   --> Page {first_page} line: '{line}'")
                print(f"       Context lines: {lines[max(0, idx-1):min(len(lines), idx+5)]}")
                break

if __name__ == "__main__":
    main()
