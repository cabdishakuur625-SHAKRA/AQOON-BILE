import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Af-Soomaali F4.pdf"
doc = fitz.open(pdf_path)
toc = doc.get_toc()
print("Table of Contents / Outline:")
print(toc)
