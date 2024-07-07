# https://leetcode.com/problems/valid-parentheses/description/

# Approach:
# Take a stack (list), iterate through the string
# If it's opening bracket, push to stack,
# If it's closing, pop from stack & see if it's valid 
# If stack empty, return False
# Time O(n) | Space O(n)
def isValidParentheses(s):
    bracketMap = {"}": "{", ")": "(", "]": "["}
    stack = []
    for x in s:
        if x in bracketMap:
            if (not stack) or (stack.pop() != bracketMap[x]):
                return False
        else:
            stack.append(x)
    return False if stack else True


# s = "()[]{}"
# s = "(]"
s = "("
print(isValidParentheses(s))