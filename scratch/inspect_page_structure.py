import fitz

def main():
    pdf_path = "C:/flutterApp/Aqoon_Bile/English F4.pdf"
    doc = fitz.open(pdf_path)
    
    for page_idx in [5, 10, 20, 50, 100]:
        page = doc[page_idx]
        print(f"\n--- Page {page_idx + 1} ---")
        images = page.get_images()
        text = page.get_text()
        rects = page.get_drawings()
        print(f"Number of images: {len(images)}")
        print(f"Text length: {len(text)}")
        print(f"Number of vector graphics (drawings): {len(rects)}")
        
        # If there are images, let's print their details
        if images:
            for img in images[:3]:
                print(f"  Image info: xref={img[0]}, width={img[2]}, height={img[3]}")

if __name__ == "__main__":
    main()
