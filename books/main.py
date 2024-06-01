

def main():
    
    # Gets the path to the book
    book_path = "books/frankenstein.txt"
    
    # Gets the text from the book path. Calls get_book_text function
    book_text = get_book_text(book_path)

    # Counts the number of words sored in the text variable. 
    num_words = word_count(book_text)
    
    # Changes all the text to the lowercase.
    lowercase = lowercase_function(book_text)

    # Take lowercase book text and sort it in a dictionary.
    book_letter_count = dictionary_count(lowercase)
   
    # This calls the sort alpha function that removes anything that isn't in the alphabet.
    only_letters_dict = sort_alpha(book_letter_count)
   
    # Sort the dictionary based on the highest value, this turns the item into a tuple.
    sorted_dict = sorted(only_letters_dict.items(), key=lambda x:x[1], reverse=True)

    # Convert tuple back to a dictionary
    converted_dict = dict(sorted_dict)
    
    # Print ending statements 
    print("--- Begin report of", book_path,"---")
    print(num_words, "words found in the document\n")
    
    for letter in converted_dict:
        print(f"The '{letter}' character was found {converted_dict[letter]} times")
    
    print("--- End reprot ---")
    
def get_book_text(path):
    with open("/Users/karl/workspace/github.com/bigfreakydaddy/bookbot/books/frankenstien.txt") as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)
    #^ this prints len of words

def lowercase_function(text):
    book_lowercase = text
    lowercase_book = book_lowercase.lower()
    return lowercase_book

def dictionary_count(text):

    #letter_count = {}

    #for letter in text:
    #    letter_count[letter] = letter_count.setdefault(letter, 0) +1

    #return letter_count

    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_alpha(dict):
    sorted_dictionary = dict
    for i in list(sorted_dictionary):
        if i.isalpha() == False:
             sorted_dictionary.pop(i)
    return sorted_dictionary
            
main()