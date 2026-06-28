import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/Carabi F4.pdf"
    doc = fitz.open(pdf_path)
    
    print(f"Total pages: {len(doc)}")
    
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        non_cs_lines = [line for line in lines if "camscanner" not in line.lower()]
        
        if non_cs_lines:
            print(f"Page {page_num + 1} has non-CamScanner text:")
            for line in non_cs_lines:
                print(f"  {repr(line)}")
            if page_num > 20:
                # Limit output
                pass

if __name__ == "__main__":
    main()
