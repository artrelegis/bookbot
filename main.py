def main():
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(len(words))

main()