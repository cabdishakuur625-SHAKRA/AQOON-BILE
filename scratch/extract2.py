import fitz # PyMuPDF
import os

pdf_path = r'C:\flutterApp\Aqoon_Bile\F4 afsoomaali weydiimo _240515_174222.PDF'
out_path = r'C:\flutterApp\Aqoon_Bile\scratch\pdf_text.txt'

try:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
        
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Extraction complete. Characters extracted: {len(text)}")
except Exception as e:
    print(f"Error: {e}")
