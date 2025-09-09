def rotateLeft(d, arr):
    n = len(arr)
    d %= n 
    return arr[d:] + arr[:d]
# Example usage
arr = [1, 2, 3, 4, 5]  
d = 2                
result = rotateLeft(d, arr)
print("Rotated Array:", result)
