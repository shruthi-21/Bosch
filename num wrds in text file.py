def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
filename = input("Enter the filename: ")
word_count = count_words_in_file(filename)

if word_count is not None:
    print(f"The file '{filename}' contains {word_count} words.")
