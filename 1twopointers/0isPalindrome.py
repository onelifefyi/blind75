# https://leetcode.com/problems/valid-palindrome/

# Brute
# Clean the string then sort the string
# BIG NOTE! Sorting a string gives a list
# Check if reversed(s) == s or not
# Time O(nlogn) | Space O(n) for cleaned string

# Approach:
# Have to pointers, left and right, pointing to start & end resp
# check if each char is equal or not moving left & right towards the center (checking if alphanum or not)
# Time O(n) | Space O(1)
def isPalindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and right > left:            
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))