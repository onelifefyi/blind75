# https://leetcode.com/problems/longest-consecutive-sequence/

# Brute:
# Sort the array, return the longest subsequence
# Time O(nlogn) | Space O(1)

# Approach:
# Put all the numbers in a hashset
# Now for each element in num, check if it's start of a sequence
# To know this, check the hashset if num - 1 exisit, if it does, it's not the start
# If it's the start, start a while loop to keep checking if num + 1, num + 2.... exists maintaining max
# Time O(n) | Space O(n)
def longestConsecutive(nums):
    num_set = set([num for num in nums])
    maxLen = 0
    for num in nums:
        if (num - 1) not in num_set:
            count = 0
            start = num
            while start in num_set:
                count += 1
                start += 1
            maxLen = max(maxLen, count)
    return maxLen
        

# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))