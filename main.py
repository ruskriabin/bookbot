import sys
from stats import get_book_text, count_words, count_characters, sort_characters_dictionary

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    sorted_characters_dictionary = sort_characters_dictionary(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters_dictionary:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()
