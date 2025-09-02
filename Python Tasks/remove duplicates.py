numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List after removing duplicates:", unique_numbers)
