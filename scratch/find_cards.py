from PIL import Image

img = Image.open('scratch/screen.png')
w, h = img.size
print(f"Image dimensions: {w}x{h}")

for col_name, x in [("Col 1 (Left)", 360), ("Col 2 (Right)", 1080)]:
    print(f"\n--- Analysis for {col_name} at X={x} ---")
    in_card = False
    start_y = 0
    for y in range(0, h, 10):
        r, g, b = img.getpixel((x, y))[:3]
        is_bright = r > 50
        
        if is_bright and not in_card:
            in_card = True
            start_y = y
        elif not is_bright and in_card:
            in_card = False
            card_h = y - start_y
            if card_h > 150: # Only count reasonably large components (cards)
                cy = start_y + card_h // 2
                print(f"Detected Card: Y={start_y} to Y={y} (height={card_h}), Center Y={cy}")
