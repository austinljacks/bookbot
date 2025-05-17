def get_book_text(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()

    return contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
    