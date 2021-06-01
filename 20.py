# Input: s = "()[]{}"
# Output: true
# Input: s = "([)]"
# Output: false
class Solution:
    def isValid(self, s):
        d = {"]":"[", ")":"(", "}":"{"}
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack:
                    pair = stack.pop()
                    if pair != d[i]:
                        return False
                else:
                    return False
        return len(stack) == 0
                
