import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    with open("scratch/extracted_classified.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for k in sorted(data.keys()):
        val = data[k]
        print(f"Key {k} (length {len(val)}):")
        if val:
            print("  First Q:", val[0])
        else:
            print("  Empty")

if __name__ == "__main__":
    main()
