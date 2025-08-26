import sys
from stats import word_count 
from stats import char_count_per_letter
from stats import sorted_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book


def main():
    book = sys.argv[1]
    words = word_count(get_book_text(book))
    chars = char_count_per_letter(get_book_text(book))
    chars_list = sorted_characters(chars)
    #print(f"{words} words found in the document")
    #print(f"{report}")
    print("==== BOOKBOT ====")
    print(f"Analyzing book found at {book}...")
    print("-------- Word Count --------")
    print(f"Found {words} total words")
    print("-------- Character Count -------")
    for dictionary in chars_list:
        print(f"{dictionary['letter']}: {dictionary['num']}")
#        for key, value in dictionary:
#            print(f"{key} : {value}")
    print("======== END ========")

main()
