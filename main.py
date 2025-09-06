import sys
from stats import get_word_count, get_char_dict, get_sorted_dict
from printers import print_title,print_word_count,print_char_count,print_end


def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookpath = sys.argv[1]
    book_as_string = get_book_text(bookpath)
    word_count = get_word_count(book_as_string)
    char_dict = get_char_dict(book_as_string)
    sorted_char_list = get_sorted_dict(char_dict)

    print_title(bookpath)
    print_word_count(word_count)
    print_char_count(sorted_char_list)
    print_end()

def get_book_text (filepath):
    file_as_string = ""

    with open(filepath) as file:
        file_as_string = file.read()

    return file_as_string


main()