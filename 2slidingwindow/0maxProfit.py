# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Brute:
# For each day & a later day calculate profit keeping track of max profit
# Time O(n^2) | Space O(1)

# Approach:
# Two pointers, left, right = 0, 1, keep going right tracking max profit
# if val at right < val at left, move the left to right
def maxProfit(prices):
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        maxProfit = max(maxProfit, profit)
        if profit < 0:
            left = right
        right += 1
    return maxProfit
 

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(maxProfit(prices))