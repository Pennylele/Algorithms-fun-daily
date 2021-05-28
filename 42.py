# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        l_max = r_max = 0
        ans = 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            if l_max <= r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1
        return ans
