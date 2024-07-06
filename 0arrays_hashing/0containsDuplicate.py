# https://leetcode.com/problems/contains-duplicate/

# Brute: 
# Check all possible pairs, see if they match
# Time O(n^2) | Space O(1)

# Approach:
# Use a hash set, keep inserting, if already present return True
# Time O(n) | Space O(n)
def containsDuplicate(nums):
    visited = set()
    for num in nums:
        if num in visited:
            return True
        visited.add(num)
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))