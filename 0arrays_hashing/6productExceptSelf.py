# https://leetcode.com/problems/product-of-array-except-self/

# Brute:
# Get the total_product in first pass
# In second pass replace each num by total_product/num
# Time O(n) | Space O(1)

# Approach:
# Where we can't use divide. Create a result array of same size
# In first pass keep storing the product so far (not including the num)
# In second pass, go in the reverse order, multiplying by product so far (reversed)
# return the array
# Time O(n) | Space O(n)
def productExceptSelf(nums):
    result = [0] * len(nums)
    i = 0
    prod_so_far = 1
    while i < len(nums):
        result[i] = prod_so_far
        prod_so_far *= nums[i]
        i += 1
    
    i = len(nums) - 1
    prod_so_far = 1
    while i >= 0:
        result[i] *= prod_so_far
        prod_so_far *= nums[i]
        i -= 1
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))