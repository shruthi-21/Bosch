def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage with runtime input
input_list = input("Enter elements separated by space: ")
arr = list(map(int, input_list.split()))

bubble_sort(arr)
print("Sorted list:", arr)
