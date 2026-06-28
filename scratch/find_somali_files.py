import os

print("Searching for files with 'somaal' or 'weydiimo' or 'som' in name:")
for root, dirs, files in os.walk("c:\\flutterApp\\Aqoon_Bile"):
    if ".git" in root or ".dart_tool" in root or "build" in root:
        continue
    for f in files:
        f_lower = f.lower()
        if "somaal" in f_lower or "weydiimo" in f_lower or "somali" in f_lower:
            print(os.path.join(root, f))
