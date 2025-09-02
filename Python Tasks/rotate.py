def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle rotations greater than list length
    return lst[-k:] + lst[:-k]
input_list = input("Enter list elements separated by space: ")
lst = input_list.split()  # keeps elements as strings; use map(int, ...) if numbers

k = int(input("Enter number of positions to rotate: "))

rotated = rotate_list(lst, k)
print("Rotated list:", rotated)
