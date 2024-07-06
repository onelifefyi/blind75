# https://neetcode.io/problems/string-encode-and-decode


# Approach:
# Can't use normal delimiters, because it might be part of the given string
# The approach is to prefix each word with 2 things
# 1st: length of the word
# 2nd: a delimiter of choice (to know the actual lenght if in two digits or more)
# Then we keep kumping based on first letter (till delimiter) to jump

# Time O(n) | Space O(1) | where n is the total number of characters
def encode(strs):
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + ";" + s
    return encoded_string

# Time O(n) | Space O(size of nums) } where n is the total number of characters
def decode(s):
    res = []
    index = 0
    while index < len(s):
        length = ""
        while s[index] != ";":
            length += s[index]
            index += 1
        start = index + 1
        end = start + int(length)
        res.append(s[start: end])
        index = end
    return res


strs = ["what","do","you1;","24;"]
encoded_string = encode(strs)
print(encoded_string)
print(decode(encoded_string))
