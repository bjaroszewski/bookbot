book_path = "books/frankenstein.txt"

def count_words(text):
    words_count = 0
    words = text.split()
    for word in words:
        words_count += 1

    return words_count

def count_chars(text):
    chars_count = {}
    
    for char in text.lower():
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1
    return chars_count

def sort_on(d):
    return d["num"]

    

def main():
    
    with open(book_path, "r") as f:
        f_content = f.read()    
        chars_summary = count_chars(f_content)
       
        new_d = [{"num": value, "letter": key} for key, value in chars_summary.items() if key.isalpha()]
        new_d.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {book_path} ---")
        print(f"{count_words(f_content)} words found in the document")
        for i in new_d:
            print(f"The '{i["letter"]}' character was found {i["num"]} times")
        print("--- End report ---")
main()