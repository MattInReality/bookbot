def main():
    book = "books/frankenstein.txt"
    text = read_book(book)
    words = count_words(text)
    counted = count_letters(text)
    sorted = sort_letters(counted)
    print_report(book, words, sorted)


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    letter_dict = {}
    for letter in text.lower():
        letter_num = ord(letter)
        if letter_num < 97 or letter_num > 122:
            continue
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_letters(letter_dict):
    letter_list = []
    for k, v in letter_dict.items():
        print(f"{k}, {v}")
        letter_list.append({"letter": k, "count": v})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


def sort_on(dict):
    return dict["count"]


def print_report(book_path, words, sorted_letter_count):
    print(f"--- Begin report of {book_path}---")
    print(f"{words} found in the document\n")
    for item in sorted_letter_count:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
