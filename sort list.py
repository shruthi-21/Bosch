def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_list = bubble_sort(numbers)
print("Sorted list:", sorted_list)
