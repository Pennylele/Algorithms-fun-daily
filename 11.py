class Solution:
    def maxArea(self, height):
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            ans = max(ans, area)
        return ans