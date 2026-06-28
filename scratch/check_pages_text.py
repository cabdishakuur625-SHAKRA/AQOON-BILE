import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/English F4.pdf"
    doc = fitz.open(pdf_path)
    
    print("Page text statistics (showing non-empty pages):")
    has_text_count = 0
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text:
            has_text_count += 1
            if has_text_count <= 30 or page_num % 10 == 0:
                print(f"Page {page_num + 1}: {len(text)} chars | First 60 chars: {repr(text[:60])}")
    
    print(f"\nTotal pages with text: {has_text_count} out of {len(doc)}")

if __name__ == "__main__":
    main()
