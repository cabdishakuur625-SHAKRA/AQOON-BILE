import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Af-Soomaali F4.pdf"
doc = fitz.open(pdf_path)
total = len(doc)
print(f"Total pages: {total}")
print("Rendering last 6 pages...")
for i in range(total - 6, total):
    page = doc[i]
    pix = page.get_pixmap()
    output_path = f"scratch/page_{i+1}.png"
    pix.save(output_path)
    print(f"Saved {output_path}")
