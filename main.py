from stats import get_word_count, get_char_dict, get_sorted_dict

def main(bookpath):
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

def print_title(bookpath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")

def print_word_count(word_count):
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

def print_char_count(sorted_char_list):
    print("--------- Character Count -------")
    for entry in sorted_char_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    

def print_end():
    print("============= END ===============")

main("./books/frankenstein.txt")