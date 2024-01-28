def open_book():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        return file_content
    
def count_words():
    book = open_book()
    words = book.split()
    print(f"This book has {len(words)} words")

def main():
    count_words()
    book = open_book().lower()
    count = {}

    for char in book:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1

    print(count)

    
main()