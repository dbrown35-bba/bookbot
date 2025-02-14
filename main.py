def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_content = f.read()
        word_count = count_words(file_content)
        char_dict = count_characters(file_content)
        print(file_content)
        print(f"There are {word_count} words in this book!")
        print(char_dict)
        generate_book_report(book_path, word_count, char_dict)


def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def count_characters(book):
    book = book.lower()
    char_count = {}
    for char in book:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def generate_book_report(file_path, word_count, char_dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words were found in the document\n\n")
    for char in char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {char_dict[char]} times")

if __name__ == "__main__":
    main()

