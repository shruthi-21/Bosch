def is_palindrome(s):
    return s == s[::-1]
input_string = input("Enter a string: ").replace(" ", "").lower()
print(f"'{input_string}' is a palindrome.") if is_palindrome(input_string) else print(f"'{input_string}' is not a palindrome.")
