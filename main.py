def main():
    print_report("books/frankenstein.txt")

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    words = text.split()
    char_dict = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] = char_dict[char] + 1
    return char_dict

def print_report(bookpath):
    book_content = get_file_contents(bookpath)
    print(f"--- Begin report of {bookpath} ---")
    print(f"{count_words(book_content)} words found in the document")
    print("\n")
    char_list = []
    char_dict = count_chars(book_content)
    for key in char_dict:
        tmp_dict = {}
        tmp_dict["char"] = key
        tmp_dict["num"] = char_dict[key]
        if key.isalpha():
            char_list.append(tmp_dict)

    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    
    for chars in char_list:
        print(f"The '{chars["char"]}' character was found {chars["num"]} times")
    print("-- End report ---")
    
def get_file_contents(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()