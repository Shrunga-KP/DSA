#4. Match the parentheses using Stack

def are_parentheses_matched(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

# Test the function
test_cases = [
    "()",          # Balanced
    "{[()]}",      # Balanced
    "{[()()]}",    # Balanced
    "{[(])}",      # Not balanced
    "(",           # Not balanced
    "())",         # Not balanced
]

for test_case in test_cases:
    if are_parentheses_matched(test_case):
        print(f"'{test_case}' is balanced.")
    else:
        print(f"'{test_case}' is not balanced.")
