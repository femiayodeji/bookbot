from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")
    print(f"{count_characters(book_text)}")

main()