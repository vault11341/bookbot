def count_words(text):
     num_words=len(text.split())
     return num_words



def count_characters(text):
     characters={}
     words=text.lower()
     for char in words:
          if char.isalpha():
               if char in characters:
                    characters[char]+=1
               else:
                    characters[char]=1
     return characters


def sort_characters(char_dict):
     char_list=[]

     for char,count in char_dict.items():
          char_list.append({"char":char,"count":count})
     def sort_on(dict):
          return dict["count"]
     char_list.sort(reverse=True,key=sort_on)

     return char_list