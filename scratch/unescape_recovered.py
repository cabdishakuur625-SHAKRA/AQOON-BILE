import json

def main():
    recovered_path = "scratch/recovered_write_1_write_to_file.py"
    target_path = "scratch/generate_arabic_subject_recovered.py"
    
    with open(recovered_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
    # Check if the content is a JSON-serialized string (starts and ends with quotes)
    if content.startswith('"') and content.endswith('"'):
        try:
            # We wrap it in a list or just use json.loads to decode it
            decoded = json.loads(content)
            print("Successfully decoded using json.loads")
        except Exception as e:
            # If that fails, let's try evaluating it or using ast.literal_eval
            import ast
            try:
                decoded = ast.literal_eval(content)
                print("Successfully decoded using ast.literal_eval")
            except Exception as e2:
                print(f"Error decoding: {e}, {e2}")
                decoded = content
    else:
        # If it doesn't have quotes, maybe it's already decoded but has literal escape characters
        # Let's try to decode it by wrapping it in quotes and parsing
        try:
            decoded = json.loads('"' + content.replace('"', '\\"') + '"')
            print("Decoded by wrapping in quotes")
        except Exception as e:
            print("No quotes, using content as-is")
            decoded = content
            
    with open(target_path, "w", encoding="utf-8") as out:
        out.write(decoded)
        
    print(f"Saved unescaped script to {target_path} (length {len(decoded)})")

if __name__ == "__main__":
    main()
