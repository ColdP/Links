import os
import json

def generate_lyrics_data(directory="."):
    """
    Reads lyric lines from jp.txt, romaji.txt, en.txt, and zh.txt files
    in the specified directory and generates a JSON-formatted lyricsData array.

    Args:
        directory (str): The directory where the lyric files are located.
                         Defaults to the current directory.

    Returns:
        str: A JSON string representing the lyricsData array, suitable for
             direct insertion into the HTML/JavaScript.
    """
    file_names = {
        "jp": os.path.join(directory, "jp.txt"),
        "romaji": os.path.join(directory, "romaji.txt"),
        "en": os.path.join(directory, "en.txt"),
        "zh": os.path.join(directory, "zh.txt")
    }

    lyrics_content = {}
    max_lines = 0

    # Read each lyric file
    for key, file_path in file_names.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()] # Read non-empty lines
                lyrics_content[key] = lines
                if len(lines) > max_lines:
                    max_lines = len(lines)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}. Please ensure all four files exist.")
            return None
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
            return None

    # Ensure all files have the same number of lines for proper pairing
    for key, lines in lyrics_content.items():
        if len(lines) != max_lines:
            print(f"Warning: The number of lines in {key}.txt ({len(lines)}) "
                  f"does not match the maximum lines found ({max_lines}). "
                  "This might cause misalignment in lyrics.")
            # Optionally, you can choose to pad shorter lists or raise an error
            # For simplicity, we'll proceed but warn about potential misalignment.

    lyrics_data = []
    for i in range(max_lines):
        line_data = {
            "jp": lyrics_content.get("jp", [""])[i] if i < len(lyrics_content.get("jp", [])) else "",
            "romaji": lyrics_content.get("romaji", [""])[i] if i < len(lyrics_content.get("romaji", [])) else "",
            "en": lyrics_content.get("en", [""])[i] if i < len(lyrics_content.get("en", [])) else "",
            "zh": lyrics_content.get("zh", [""])[i] if i < len(lyrics_content.get("zh", [])) else ""
        }
        lyrics_data.append(line_data)

    # Return as a formatted JSON string that can be directly pasted into JS
    return json.dumps(lyrics_data, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    # Create dummy files for demonstration
    dummy_dir = "lyrics_files"
    os.makedirs(dummy_dir, exist_ok=True) # Create directory if it doesn't exist

    with open(os.path.join(dummy_dir, "jp.txt"), "w", encoding="utf-8") as f:
        f.write("周りに合わせる言語も知らねえ\n")
        f.write("守備力は弱いけど勘は鋭\n")
        f.write("一旦進められたら止まれ\n")

    with open(os.path.join(dummy_dir, "romaji.txt"), "w", encoding="utf-8") as f:
        f.write("Mawari ni awaseru gengo mo shiranē\n")
        f.write("Shubiryoku wa yowai kedo kan wa surudoi\n")
        f.write("Ittan susumeraretara tomare\n")

    with open(os.path.join(dummy_dir, "en.txt"), "w", encoding="utf-8") as f:
        f.write("Don't even know the language to fit in with others\n")
        f.write("My defense is weak, but my intuition is sharp\n")
        f.write("Once I start, I can't stop\n")

    with open(os.path.join(dummy_dir, "zh.txt"), "w", encoding="utf-8") as f:
        f.write("连融入周围的语言都不懂\n")
        f.write("防守力弱但直觉敏锐\n")
        f.write("一旦被推动就停不下来\n")


    print(f"Dummy lyric files created in '{dummy_dir}' for demonstration.")
    print("\n--- Generated lyricsData content (copy and paste into your HTML Canvas): ---")

    # Generate and print the lyrics data
    generated_json = generate_lyrics_data(dummy_dir)
    if generated_json:
        print(generated_json)
    else:
        print("Failed to generate lyrics data.")

    print("\n--------------------------------------------------------------------------")
    print("To use this script:")
    print("1. Save it as a Python file (e.g., `generate_lyrics.py`).")
    print("2. Create a folder (e.g., `lyrics_files`) in the same directory.")
    print("3. Place your `jp.txt`, `romaji.txt`, `en.txt`, and `zh.txt` files inside `lyrics_files`.")
    print("4. Run the script: `python generate_lyrics.py`.")
    print("5. Copy the output JSON array and paste it into the `lyricsData` variable in your HTML Canvas.")

