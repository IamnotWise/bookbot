from stats import num_words, char_count, sort_on
import sys

if len(sys.argv) != 2:
    print(sys.argv)
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filename = sys.argv[1]


def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
        #print(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filename}")
        print("----------- Word Count ----------")
        num_words(file_contents)
        counts = char_count(file_contents)
        #print(counts)
        print("------- Character Count ---------")
        sort_on(counts)

get_book_text(filename)


