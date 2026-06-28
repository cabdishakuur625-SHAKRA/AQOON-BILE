import json
import re
import os

JSON_FILE = r'c:\flutterApp\Aqoon_Bile\scratch\full_seed_data.json'
DART_FILE = r'c:\flutterApp\Aqoon_Bile\lib\services\seed_data.dart'

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    original_json = f.read()

with open(DART_FILE, 'r', encoding='utf-8') as f:
    dart_content = f.read()

json_match = re.search(r"fullSeedJson = r'''(.*?)'''", dart_content, re.DOTALL)
if json_match:
    new_dart_content = dart_content.replace(json_match.group(1).strip(), original_json.strip())
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(new_dart_content)
    print("Successfully restored original seed data.")
else:
    print("Could not find fullSeedJson in seed_data.dart")
