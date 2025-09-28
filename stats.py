

def get_book_words(book_text):
    count=0
    words=book_text.split()
    count=len(words)
    
    return count

def get_book_text(book_text):
    with open(book_text)as f:
        contents = f.read()

    return contents


def character_count(book_text):
    char_dictionary={}
    dictionary_list=[]
    lower_char_count=book_text.lower()
    for item in lower_char_count:
        if item in char_dictionary:
            char_dictionary[item]+=1
        else:
            char_dictionary[item]=1

    return char_dictionary

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(target_book, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {target_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")