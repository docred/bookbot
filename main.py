from stats import *
import sys
 
if len(sys.argv)!=2:
    Print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


target_book=sys.argv[1]



def main():
    book_content=get_book_text(target_book)
    word_count=get_book_words(book_content)
    chars_dict=character_count(book_content)
    chars_sorted_list=chars_dict_to_sorted_list(chars_dict)
    print_report(target_book,word_count,chars_sorted_list)

    
    
main()


