def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for o in chars_dict:
      print(f"The '{o['char']}' character was found {o['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = []
    added_chars = ""
    lowered_text = text.lower()
    for c in lowered_text:
        if c not in added_chars and c.isalpha():
            chars.append({"char": c, "num": 0})
            added_chars += c
        for o in chars:
            if o["char"] == c:
                o["num"] += 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["num"]


main()
