import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Physics F4.pdf"
doc = fitz.open(pdf_path)
print("Page count of Physics F4.pdf:", len(doc))

print("Checking first 15 pages for text...")
has_text_count = 0
for i in range(len(doc)):
    text = doc[i].get_text().strip()
    if text:
        has_text_count += 1
        if i < 15 or i % 20 == 0:
            print(f"Page {i+1}: {len(text)} chars | First 120 chars: {repr(text[:120])}")

print(f"\nTotal pages with text: {has_text_count} out of {len(doc)}")
