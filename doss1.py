import sys
def reverseArray(A):
    return A[::-1]
data = sys.stdin.read().split()
N = int(data[0])  # Read the number of integers
A = list(map(int, data[1:]))  # Read the space-separated integers into a list
reversed_array = reverseArray(A) # Reverse the array
print(A)
print(' '.join(map(str, reversed_array))) 