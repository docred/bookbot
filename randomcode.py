#BOOKBOT
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

def get_book_words(book_text):
    count=0
    words=book_text.split()
    count=len(words)
    
    return count


def get_book_text(book_text):
    with open(book_text)as f:
        contents = f.read()

    return contents




"""
def get_char_count(book_text):
    char_dictionary=dict()
    lower_char_count=book_text.lower()
    total_chars=len(lower_char_count)
    for item in lower_char_count:
        if item in char_dictionary:
            char_dictionary[item]+=1
        else:
            char_dictionary[item]=1

    return char_dictionary
"""



from stats import get_book_words
#from stats import get_char_count
from stats import get_book_text
from stats import character_count

target_book="books/frankenstein.txt"


def main():
    book_content=get_book_text(target_book)
    word_count=get_book_words(book_content)
    charcount=character_count(book_content)
    print(f"Found {word_count} total words")
    print (charcount)

    #print(f"Total characters : {charcount}")

main()



