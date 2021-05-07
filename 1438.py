# can we use 2 heaps to keep track? or 2 monotonic stacks.
class Solution:
    def longestSubarray(self, nums, limit):
        # initialte 2 decks - one decreasing and one increasing
        maxdeque = collections.deque()
        mindeque = collections.deque()

        left, ans = 0, 0
        for idx, num in enumerate(nums):
            while maxdeque and num > maxdeque[-1]:
                maxdeque.pop()
            while mindeque and num < mindeque[-1]:
                mindeque.pop()
            maxdeque.append(num)
            mindeque.append(num)

            while maxdeque[0] - mindeque[0] > limit:
                if nums[left] == maxdeque[0]: maxdeque.popleft()
                if nums[left] == mindeque[0]: mindeque.popleft()
                left += 1
            
            ans = max(ans, idx - left + 1)
        return ans

