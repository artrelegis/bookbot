def main():
    file_content = get_file_contents("books/frankenstein.txt")
    #count_words(file_content)
    count_chars(file_content)

def count_words(text):
    words = text.split()
    print(len(words))

def count_chars(text):
    words = text.split()
    char_list = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char not in char_list:
                char_list[char] = 1
            else:
                char_list[char] = char_list[char] + 1
    print(char_list)
    
def get_file_contents(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()