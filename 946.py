# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
class Solution:
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        m = len(popped)

        for x in pushed:
            stack.append(x)
            while j < m and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return j == m

obj = Solution()
print(obj.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))