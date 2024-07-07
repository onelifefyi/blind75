# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Brute:
# All possible substrings, check if repeates. can have a hashset to check for repeats
# Time O(n^2) | Space O(n)

# Approach:
# keep track of max length
# have two pointers left, right at 0, 1
# have a hashmap of repeating chars & it's index set(s[0]: 0)
# keep moving the right till not repeating, if repeated, move left to s[right] + 1 & continue
# Time O(n) | Space O(n)
# NOTE!!! This won't work, because we need to pop everything till the duplicate is removed
# And we while using hashmap we are just jumping, not removing the items from skipped substring


# Approach:
# keep track of max length
# have two pointers left, right at 0, 1
# have a set of repeating chars
# keep moving the right till not repeating adding to the set,
# if repeated, keep removing from set, s[left] till duplicate is removed incrementing left each time
# if no duplicate, add to the set s[right]
# Time O(n) | Space O(n)
def lengthOfLongestSubstring(s):
    repeatedSet = set()
    left, right = 0, 0
    maxLen = 0
    while right < len(s):
        if s[right] in repeatedSet:
            while s[right] in repeatedSet:
                repeatedSet.remove(s[left])
                left += 1
        repeatedSet.add(s[right])
        maxLen = max(maxLen, right - left + 1)
        right += 1
    return maxLen

# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "abba"
s = ""
print(lengthOfLongestSubstring(s))