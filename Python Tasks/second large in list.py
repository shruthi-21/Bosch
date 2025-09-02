def second_largest(numbers):
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
