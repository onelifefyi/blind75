# https://leetcode.com/problems/top-k-frequent-elements/

# Brute:
# Store freq in hashmap
# Form an array sorted based on frequency (this can be done bys using tuple (freq, val) & sorting it)
# Return the last k elements
# Time O(nlogn) | space O(n)

# Approach:
# Bucket sort (kind of)
# First, Iterate through nums storing the frequency in a hashmap
# Create an array (of list) of size nums
# And for each element in the hashmap, put it in the index of hashmap[element]
# Now iterate through the array, from back (cos most frequent)
# Time O(n) | Space O(n)

def topKFrequent(nums, k):
    freq_table = {}
    for num in nums:
        freq_table[num] = freq_table.get(num, 0) + 1

    # Note that we can't just have [[]] * len(nums), cos it will be the same list
    position_arr = [[] for _ in range(len(nums) + 1)]
    for num in freq_table:
        position_arr[freq_table[num]].append(num)
    
    res = []
    index = len(position_arr) - 1
    # print(freq_table)
    # print(position_arr)
    
    while index > 0:
        if not position_arr[index]:
            index -= 1
            continue 
        res.append(position_arr[index].pop())
        if len(res) == k:
            return res
    return -1


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))