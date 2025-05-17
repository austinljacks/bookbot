def get_wordcount(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()
        
    list_content = contents.split()
    num_of_words = len(list_content)
    print(str(num_of_words) + " words found in the document")