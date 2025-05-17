from stats import get_wordcount, count_characters, chars_dict_to_sorted_list

book_path = "./books/frankenstein.txt"

def get_book_text(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()

    return contents

character_count = count_characters(get_book_text(book_path))



print("============ BOOKBOT ============")
print("Analyzing book found at " + book_path + "...")
print("----------- Word Count ----------")
get_wordcount(book_path)
print("--------- Character Count -------")
print(chars_dict_to_sorted_list(count_characters(get_book_text(book_path))))
    