# https://leetcode.com/problems/container-with-most-water/description/

# Brute:
# Check all possible end points
# Time O(n^2) | Space O(1)

# Approach:
# Maintain maxWater 
# Have two pointers, left end and right end, at a time keep decreasing the least one (updating max)
# Time O(n) | Space O(1)
def maxArea(height):
    left, right = 0, len(height) - 1
    maxWater = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        maxWater = max(maxWater, water)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxWater
        

# height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
height = [2,3,4,5,18,17,6]
print(maxArea(height))