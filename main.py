def count_words(text):
    words = text.split()
    count = len(words)
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)


main()

