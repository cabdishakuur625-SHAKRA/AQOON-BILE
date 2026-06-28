import fitz

pdf_path = r"C:\flutterApp\Aqoon_Bile\Af-Soomaali F4.pdf"
doc = fitz.open(pdf_path)
print("Page count:", len(doc))

# Let's inspect page 15, for example
page = doc[14]
image_list = page.get_images(full=True)
print("Number of images on page 15:", len(image_list))
for img_index, img in enumerate(image_list):
    xref = img[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    image_ext = base_image["ext"]
    print(f"Image {img_index+1}: xref {xref}, extension {image_ext}, size {len(image_bytes)} bytes")
