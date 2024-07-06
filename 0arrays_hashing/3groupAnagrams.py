# https://leetcode.com/problems/group-anagrams/description/

# Brute:
# ...

# Approach:
# Have a hashmap, with key as the sorted word & val as [word]
# For each word, put that in the hashmap & finally return the hashmap.values() appended to a list
# Time O(n * mlogm) | O(n)

# Optimization:
# Since it's going to be lower english characters, we can use the char frequency tuple as key
# That way no need to sort, for each word insert in the hashmap
# return the hashmap.values() converted to a list
# Time O(n*m) where m is the avg len of word | Space O(n)
def groupAnagrams(strs):
    anagram_map = {}
    for word in strs:
        freq_list = [0] * 26
        for ch in word:
            freq_list[ord(ch) - ord('a')] += 1
        anagram_map[tuple(freq_list)] = anagram_map.get(tuple(freq_list), []) + [word]
    return [anagram_list for anagram_list in anagram_map.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))