def isBalanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}   
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return "NO"
        else:
            continue
    return "YES" if not stack else "NO"
# Example usage 
brackets_list = [
    "{[()]}",      # Balanced
    "{[(])}",      # Not balanced
    "{{[[(())]]}}",# Balanced
    "(((",         # Not balanced
    "[](){}",      # Balanced
    "][",          # Not balanced
]
for s in brackets_list:
    print(f"{s} --> {isBalanced(s)}")
