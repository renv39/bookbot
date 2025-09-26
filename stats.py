def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_number_of_words(text):
    return len(text.split())

def count_characters(text):
    found_characters = {}
    lower_text = text.lower()
    for character in lower_text:
        
        if character not in found_characters:
            
            found_characters[character] = 1
        else:
            found_characters[character] += 1
    
    return found_characters

def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    tmp_dict = {}
    list = []
    
    for character, count in char_dict.items():
        tmp_dict["char"] = character
        tmp_dict["num"] = count
        list.append(tmp_dict.copy())

    list.sort(reverse=True, key=sort_on)

    return list

