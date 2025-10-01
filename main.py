import sys
from stats import word_count
from stats import character_count
from stats import sorted_characters

def get_book_text(path_to_file)->str:
    with open(path_to_file) as file:
        contents = file.read()
    return contents

#filepath is a string

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    whereQ = sys.argv[1]
    book = get_book_text(whereQ)
    
    print("============ BOOKBOT ============ \n",
    f"Analyzing book found at {whereQ}... \n",
    "----------- Word Count ----------\n", 
    f"Found {word_count(book)} total words \n",
    "--------- Character Count -------")


    sorted_list = sorted_characters(character_count(book))
    for i in range(len(sorted_list)):

        char = sorted_list[i]["char"]

        if char.isalpha():
            print(f"{char}: {sorted_list[i]["num"]}")
    pass

main()