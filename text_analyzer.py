def read_file(path):
    """Return the contents of the file at 'path' as a single string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_basic_stats(text):
    """Return a tuple: (num_characters, num_words, num_lines)."""
    num_characters = len(text)
    num_words = len(text.split())
    num_lines = text.count("\n") + 1
    return num_characters, num_words, num_lines
def get_most_common_words(text, n=10):
    """Return a list of (word, count) pairs for the n most common words."""
    words = text.lower().split()
    cleaned_words = []
    for w in words:
        w = w.strip(".,!?;:\"'()[]")
        if w:
            cleaned_words.append(w)
    freq = {}
    for w in cleaned_words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]


def main():
    file_path = input("Enter the path to a text file: ")
    contents = read_file(file_path)
    print("\n========== TEXT ANALYZER REPORT ==========\n")

    chars, words, lines = get_basic_stats(contents)

    print(f"\nCharacters: {chars}")
    print(f"Words: {words}")
    print(f"Lines: {lines}")

    common_words = get_most_common_words(contents, n=10)

    print("\n--- Most Common Words ---")

    for word, count in common_words:
        print(f"{word}: {count}")
    print("\n--- File preview (first 300 characters) ---")
    print(contents[:300])
    print("\nAnalysis complete.")
    save = input("\nSave results to a file? (y/n): ").strip().lower()

    if save == "y":
        with open("analysis_report.txt", "w", encoding="utf-8") as f:
            f.write("TEXT ANALYZER REPORT\n\n")
            f.write(f"Characters: {chars}\n")
            f.write(f"Words: {words}\n")
            f.write(f"Lines: {lines}\n\n")

            f.write("Most Common Words:\n")
            for word, count in common_words:
                f.write(f"{word}: {count}\n")

        print("Report saved as analysis_report.txt")




if __name__ == "__main__":
    main()



