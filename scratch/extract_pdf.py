import pdfplumber

pdf_path = r"C:\Users\cabdi\OneDrive\Desktop\12 maado\12 maado\Biology Chapter Questions and answers Form Four.pdf"
output_path = r"c:\flutterApp\Aqoon_Bile\scratch\biology_test_extract.txt"

with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages[:10]: # Just first 10 pages for now
        text += page.extract_text() + "\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted text to {output_path}")
