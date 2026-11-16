from stats import find_word_count, find_char_count
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    leng = find_word_count(text)
    book_report(book_path, leng, text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def book_report(book_path, word_count, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    parsed = find_char_count(text)
    for char in parsed:
        print(f"{char}: ", end="")
        print(parsed[char])

main()
