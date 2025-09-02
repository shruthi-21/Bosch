def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Target not found

# Example usage with runtime input
input_list = input("Enter sorted elements separated by space: ")
arr = list(map(int, input_list.split()))

target = int(input("Enter the target value to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
