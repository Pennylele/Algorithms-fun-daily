# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [] # monotomous descending stack
        T = len(temperatures)
        ans = [0] * T
        for i in range(T):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

obj = Solution()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))