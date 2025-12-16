import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(book_path):
    with open(book_path, "r") as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)    
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")
    
if __name__ == "__main__":
    main()