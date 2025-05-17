def get_wordcount(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()
        
    list_content = contents.split()
    num_of_words = len(list_content)
    print("Found " + str(num_of_words) + " total words")

def count_characters(string):
    lower_string = string.lower()
    characters = {}

    for character in  lower_string:
        if character in characters:
            characters[character] +=1
        else:
            characters[character] = 1
    
    return characters

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
