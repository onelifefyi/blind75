# https://leetcode.com/problems/3sum/description/

# Brute:
# All possible combinations of triplets (might get duplicates, need to sort & store)
# Time O(n^3) | Space O(n) 

# Approach
# Sort the array
# For each element (except duplicate), perform two pointer (index+1, len1-1) (two sum 2 (sorted array)) to find the solution
# Be sure to skip if it's the same as previous for both index & left to avoid duplicate (or use set as result)
# Time O(nlog + n^2) = O(n^2) | Space O(n) for result/sorting

def threeSum(nums):
    res = []
    nums.sort()
    index = 0
    prevNum = None
    while index < len(nums) - 2:
        if nums[index] == prevNum:
            index += 1
            continue
        left, right = index+1, len(nums)-1
        while left < right:
            totalSum = nums[left] + nums[right] + nums[index]
            if totalSum < 0:
                left += 1
            elif totalSum > 0:
                right -= 1
            else:
                res.append([nums[index], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
        prevNum = nums[index]
        index += 1
        
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))