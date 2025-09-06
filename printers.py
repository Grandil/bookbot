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