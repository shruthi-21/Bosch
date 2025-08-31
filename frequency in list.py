from collections import Counter
input_str = input("Enter elements separated by space: ")
elements = input_str.split()
frequency = Counter(elements)
print("Frequency of each element:")
for element, count in frequency.items():
    print(f"{element}: {count}")
