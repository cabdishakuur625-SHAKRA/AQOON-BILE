import PyPDF2
import os

pdf_path = r'C:\flutterApp\Aqoon_Bile\F4 afsoomaali weydiimo _240515_174222.PDF'
out_path = r'C:\flutterApp\Aqoon_Bile\scratch\pdf_text.txt'

os.makedirs(os.path.dirname(out_path), exist_ok=True)

try:
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
                
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extraction complete.")
except Exception as e:
    print(f"Error: {e}")
