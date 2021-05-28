# Input: nums = [3,2,3]
# Output: [3]
# Boyer-Moore Voting Algorithm to keep the space O(1)
# Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements, we are safe in discarding the prefix and attempting to recursively solve the majority element problem for the suffix. Eventually, a suffix will be found for which count does not hit 0, and the majority element of that suffix will necessarily be the same as the majority element of the overall array.

class Solution:
    def majorityElement(self, nums):
        countA, countB, candidateA, candidateB = 0, 0, None, None
        for num in nums:
            if candidateA == num:
                countA += 1
            elif candidateB == num:
                countB += 1
            elif countA == 0:
                candidateA = num
                countA += 1
            elif countB == 0:
                candidateB = num
                countB += 1
            else:
                countA -= 1
                countB -= 1
    
        ans = []
        majority = len(nums) // 3
        for i in [candidateA, candidateB]:
            if nums.count(i) > majority:
                ans.append(i)
        return ans
