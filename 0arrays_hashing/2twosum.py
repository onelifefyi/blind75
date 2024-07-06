# https://leetcode.com/problems/two-sum/description/

# Brute:
# Check all possible number pairs combination, if sum == target return True
# Time O(n^2) | Space O(1)

# Approach:
# Create a hashmap storing the target - num as key & index as value
# Everytime you check a num, see if target exists, if it does return the index & hashmap[num]
# Time O(n) | Space O(n)
def twoSum(nums, target):
    targetmap = {}
    for index, num in enumerate(nums):
        if num in targetmap:
            return [index, targetmap[num]]
        targetmap[target - num] = index
    return -1

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))