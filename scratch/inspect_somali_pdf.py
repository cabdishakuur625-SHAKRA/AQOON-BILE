import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Af-Soomaali F4.pdf"
print("Opening PDF with fitz...")
doc = fitz.open(pdf_path)
print("Total pages:", len(doc))

print("Checking first 20 pages text:")
has_text_count = 0
for i in range(len(doc)):
    text = doc[i].get_text().strip()
    if text:
        has_text_count += 1
        if i < 20 or i % 10 == 0:
            print(f"Page {i+1}: {len(text)} chars | First 100 chars: {repr(text[:100])}")

print(f"\nTotal pages with text: {has_text_count} out of {len(doc)}")
