import pdfplumber
import os

base_dir = r"C:\Users\cabdi\OneDrive\Desktop\12 maado\12 maado"
output_dir = r"c:\flutterApp\Aqoon_Bile\scratch\extracted_texts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = [
    "Biology Chapter Questions and answers Form Four.pdf",
    "Chemistry Quiz One F4.pdf",
    "F4 afsoomaali weydiimo _240515_174222.PDF",
    "Taariikh weydiimo iyo warcilin.pdf",
    "TarbiyoDhameystiran-Reduced.pdf",
    "buug Juqraafi S&J.pdf",
    "physics practice all chapter.pdf"
]

for filename in files:
    pdf_path = os.path.join(base_dir, filename)
    print(f"Processing {filename}...")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
        
        output_name = filename.replace(".pdf", ".txt").replace(".PDF", ".txt")
        with open(os.path.join(output_dir, output_name), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  Saved to {output_name}")
    except Exception as e:
        print(f"  Error processing {filename}: {e}")
