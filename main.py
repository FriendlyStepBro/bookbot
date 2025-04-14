from stats import *
from sys import argv, exit

def get_book_text(book_path):
    with open(book_path) as file:
        book_contents = file.read()
    return book_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book_contents = get_book_text(argv[1])
    print("============ BOOTBOT ============")
    print(f"Analyzing book found at {argv[1]}")

    print("----------- Word Count -----------")
    print(f"Found {get_num_words(book_contents)} total words")

    print("--------- Character Count -------")
    for key, value in dictionary_to_list(symbol_count(book_contents)):
        if isinstance(key, str) and key.isalpha():  # Ensure key is a string before calling isalpha()
            print(f"{key}: {value}")

    print("============= END ===============")

main()
