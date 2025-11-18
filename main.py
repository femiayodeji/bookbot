import sys
from stats import count_words, count_characters, sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("-------- Character Count --------")
    char_count = count_characters(book_text)
    sorted_char_count = sort_list(char_count)
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()