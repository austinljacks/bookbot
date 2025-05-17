from stats import get_word_count, count_characters, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
     return f.read()

book_path = "./books/frankenstein.txt"
text = get_book_text(book_path)
num_of_words = get_word_count(text)
chars_dict = count_characters(text)
chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

def print_report(book_path, num_of_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_of_words) + " total words")
    print("--------- Character Count -------")
    
    for item in chars_sorted_list:
       if not item["char"].isalpha():
          continue
       print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

print_report(book_path, num_of_words, chars_sorted_list)
    
