class Solution:
    def subarraySum(self, nums, k):
        hashmap = {0: 1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num # rolling sum
            count += hashmap.get(prefix_sum - k, 0) # adding how many prefix_sum in hashmap equals to prefix_sum - k.
            # !!IMPORTANT!! This line needs ot be before the next line
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1 # writing the rolling sum into the hashmap
        return count