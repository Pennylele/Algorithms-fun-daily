class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        left = 0
        ans = []
        
        for right in range(len(nums)):
            while q and nums[right] > q[-1]:
                q.pop()
            q.append(nums[right])
            
            if right - left == k-1:
                ans.append(q[0])
                if q[0] == nums[left]:
                    q.popleft()
                left += 1
        return ans