from stats import get_wordcount

def get_book_text(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()

    return contents

def main():
    get_wordcount("./books/frankenstein.txt")

main()


    