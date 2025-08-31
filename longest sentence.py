def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
# Runtime input
sentence = input("Enter a sentence: ")
longest = find_longest_word(sentence)
print("Longest word:", longest)
