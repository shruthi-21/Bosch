def sum_kwargs(**kwargs):
    return sum(kwargs.values())
result = sum_kwargs(a=10, b=20, c=30)
print("Sum of values:", result)
