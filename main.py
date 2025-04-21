from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys
def get_book_text(path):
     with open(path) as f:
          return f.read()

def main ():
     if len(sys.argv)!=2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit[1]
     
     path=sys.argv[1]
     
     

     text = get_book_text(path)
     word_count=count_words(text)
     char_counts=count_characters(text)
     sorted_chars=sort_characters(char_counts)
     print("============ BOOKBOT ============")
     print("Analyzing book found at books/frankenstein.txt...")
     print("----------- Word Count ----------")
     print(f"Found {word_count} total words")
     print("--------- Character Count -------")
     for char_dict in sorted_chars:
          if char_dict["char"].isalpha():
               print(f"{char_dict['char']}: {char_dict['count']}")

     print("============= END ===============")          

if __name__=="__main__":
     main()

