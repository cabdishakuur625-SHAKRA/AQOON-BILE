import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Af-Soomaali F4.pdf"
doc = fitz.open(pdf_path)
print("Rendering first 10 pages...")
for i in range(10):
    page = doc[i]
    pix = page.get_pixmap()
    output_path = f"scratch/page_{i+1}.png"
    pix.save(output_path)
    print(f"Saved {output_path}")
