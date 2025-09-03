# Function to count vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"  
    vowels_count = 0
    consonants_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    
    return vowels_count, consonants_count
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
