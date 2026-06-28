import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/Carabi F4.pdf"
    doc = fitz.open(pdf_path)
    for page_num in range(5):
        text = doc[page_num].get_text().strip()
        print(f"Page {page_num + 1} text: {repr(text)}")

if __name__ == "__main__":
    main()
