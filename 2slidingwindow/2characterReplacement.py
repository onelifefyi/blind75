# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Brute:
# All possible substrings, 
# in each substring check if most frequently occuring char's length in that substring + k >= len(substring) + k
# if yes, keep track of max length
# Time O(n^2) | Space O(n)

# Approach:
# Have two pointers, have a hashmap to keep track of frequency of element
# If the window size becomes > maxFrequency + k, keep moving left till the prev condition fails
# keep track of max size
# Time O(26n) the 26 is to find the max frequent element from hashmap of max size 26 (english chars) | Space O(1) max 26

# Improvement:
# To reduce time complexity, have a variable maxFreq
# Each time a char is encountered, set the maxFreq to max(map[ch], maxFreq)
# This way we need not iterate through the hashmap to get max value
# Time O(n) | Space O(1)
def characterReplacement(s, k):
    freqMap = {}
    left = right = 0
    maxFreq = 0
    res = 0

    while right < len(s):
        freqMap[s[right]] = freqMap.get(s[right], 0) + 1
        maxFreq = max(maxFreq, freqMap[s[right]])
        while k < (right - left + 1) - maxFreq:
            # Note that we don't care about reducing the maxFreq, because the result is always going to be 
            # Something bigger (or equal) to the size before reducing the max frequency
            # And whenever something comes with more frequency than max, we update the maxFreq
            freqMap[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

s = "ABAB"
k = 2
print(characterReplacement(s, k))