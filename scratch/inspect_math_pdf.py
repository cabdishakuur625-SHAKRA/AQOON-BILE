import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/Maths F4.pdf"
    doc = fitz.open(pdf_path)
    print("Number of pages:", len(doc))
    
    non_empty = []
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text:
            non_empty.append((page_num + 1, len(text)))
            
    print(f"Total pages with text: {len(non_empty)}")
    if non_empty:
        print("Pages with text (first 20):")
        for p, l in non_empty[:20]:
            print(f"Page {p}: {l} characters")
    else:
        print("This PDF is entirely scanned images with no embedded text.")

if __name__ == "__main__":
    main()
