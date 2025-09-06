def get_word_count(string):
    word_array = string.split()
    return len(word_array)

def get_char_dict(string):
    char_count_dict = {}
    string = string.lower()
    for char in string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(items):
    return items["num"]

def get_sorted_dict(char_count_dict):
    char_list = []
    for char, occurences in char_count_dict.items():
        char_list.append({"char": char, "num": occurences})
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list