# Clearly hashmap is easier to think of for this problem
# So we are going to use the bit manipulation which only requires one pass O(n)
class Solution:
    def singleNumber(self, nums):
        start = 0
        for num in nums:
            start ^= num
        return start
# If we take XOR of zero and some bit, it will return that bit
# a ^ 0 = a
# If we take XOR of two same bits, it will return 0
# a ^ a = 0
# a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
# So we can XOR all bits together to find the unique number.