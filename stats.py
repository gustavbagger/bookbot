def word_count(book_text:str) -> int:
    return len(book_text.split( ))

def character_count(book_text:str) -> dict:
    characters = dict()
    book_text = book_text.lower()
    for char in book_text:
        if char in characters:
            characters[char] += 1
            continue
        characters[char] = 1
    return characters

def dictify_key_pair(key:str,characters:dict) -> int:
    return {"char":key,"num":characters[key]}

def sorting_function(key_pair:dict) -> int:
    return key_pair["num"]

def sorted_characters(characters:dict) -> list:
    sorted_list = list()
    for char in characters:
        sorted_list.append(dictify_key_pair(char,characters))
    sorted_list.sort(reverse=True,key=sorting_function)
    return sorted_list

