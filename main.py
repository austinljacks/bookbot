from stats import get_word_count, count_characters, chars_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
     return f.read()

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
    
