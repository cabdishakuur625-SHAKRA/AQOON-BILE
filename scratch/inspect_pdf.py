import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/English F4.pdf"
    doc = fitz.open(pdf_path)
    print("Number of pages:", len(doc))
    
    print("\n--- Searching first 15 pages for Unit / Table of Contents ---")
    for page_num in range(min(15, len(doc))):
        text = doc[page_num].get_text()
        print(f"--- Page {page_num + 1} ---")
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines[:30]:  # print first 30 lines of each page
            print(line)

if __name__ == "__main__":
    main()
