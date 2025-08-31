def find_largest_smallest(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1], sorted_numbers[0]
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
largest, smallest = find_largest_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
