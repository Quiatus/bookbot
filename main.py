def open_book(path):
    with open(path) as f:
        file_content = f.read()
        return file_content
    

def count_words(book):
    words = book.split()
    return len(words)


def count_characters(book):
    book = book.lower()
    count = {}

    for char in book:
        if char.isalpha() == True:
            if char in count.keys():
                count[char] += 1
            else:
                count[char] = 1

    return count


def main(path):
    book = open_book(path)
    words = count_words(book)
    characters = count_characters(book)
    lst = list(characters.items())
    lst.sort(reverse=True, key = lambda x:x[1])
    
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    for items in lst:
        print(f"The '{items[0]}' character was found {items[1]} times")
    print("--- End report ---")

    
main("books/frankenstein.txt")