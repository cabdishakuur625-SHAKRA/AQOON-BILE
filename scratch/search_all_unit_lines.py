import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/English F4.pdf"
    doc = fitz.open(pdf_path)
    
    print("Printing lines containing 'unit':")
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines:
            if "unit" in line.lower():
                print(f"Page {page_num + 1}: '{line}'")

if __name__ == "__main__":
    main()
