# https://leetcode.com/problems/valid-anagram/

# Brute;
# Sort both the strings (will give list) then compare index wise
# Time O(nlogn + mlogm) | Space O(m + n)

# Approach:
# Use hashmap to store the frequency of each character in s & t
# Then compare if all the freq equal or not
# Time O(n) | Space O(n)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq_s = {x:0 for x in s}
    freq_t = {x:0 for x in t}

    for i in range(len(s)):
        freq_s[s[i]] += 1
        freq_t[t[i]] += 1
    
    for ch in s:
        if freq_s[ch] != freq_t.get(ch, 0):
            return False

    return True

# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s, t))