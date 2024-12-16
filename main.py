from collections import Counter

def character_count(text):
    return Counter(map(lambda x: x.lower(), filter(lambda x: x.isalpha(), list(text))))

def word_count(text):
    return len(text.split())

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count(file_contents)} words found in the document")
        for ch, count in character_count(file_contents).items():
            print(f"The '{ch}' character was found {count} time")
        print(f"--- End report ---")

main()

