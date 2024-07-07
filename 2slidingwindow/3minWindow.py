# https://leetcode.com/problems/minimum-window-substring/

# Brute:
# All possible substrings, check if it contains all the characters from 't'
# Time O(n^3) | Space O(len(m)) where m is len(t)

# Approach:
# Kindof Greedy
# Have two pointers at 0, keep moving r till all the elements from t are found (using hashmap)
# keep a minLen list to store: 1) min length so far & the [left, right] for that
# Have two hashmaps, 1st requiredMap, 2nd currentMap
# for each key:value in requiredMap <= currentMap, keep moving left forward, reducing the frequency. (again tracking minFreq)
# Time O(n*m) | Space O(n + m) 

# Optimization
# Before we were iterating through each key in reqMap to see if it satisfies the condition or not
# Instead of that we can have an int variable, which keeps track of number of satisfied conditions
# explained: whenever a new item is added in currMap, we check if it's freq is >= freq in required
# instead, we can have a variable 'required' storing (#keys in required)
# another variable called 'current', whenever something is inserted check if it passes required or not
# if >= required + 1 else required - 1

# Time O(n) | Space O(n + m)
def minWindow(s, t):
    if not s or not t:
        return ""
    left, right = 0, 0
    requiredMap = {x:0 for x in t}
    for ch in t:
        requiredMap[ch] += 1
    required = len(requiredMap)
    
    currMap = {}
    current = 0
    res = [float("inf"), [0, 0]]
    while right < len(s):
        currMap[s[right]] = currMap.get(s[right], 0) + 1
        if s[right] in requiredMap:
            if currMap[s[right]] == requiredMap[s[right]]: current += 1 
        while required == current:
            if res[0] > right - left + 1:
                res = [right - left + 1, [left, right]]
            currMap[s[left]] -= 1
            if s[left] in requiredMap:
                if currMap[s[left]] < requiredMap[s[left]]: 
                    current -= 1
            left += 1
        
        right += 1
    return "" if res[0] == float("inf") else s[res[1][0]:res[1][1] + 1]



# s = "ADOBECODEBANC"
# t = "ABC"
# s = "a"
# t = "a"
# s = "abc"
# t = "xv"
s = "a"
t = "aa"
print(minWindow(s, t))