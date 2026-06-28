import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/Carabi F4.pdf"
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    print("Table of Contents:")
    for item in toc:
        print(item)
    print("Total chapters in outline:", len(toc))

if __name__ == "__main__":
    main()
