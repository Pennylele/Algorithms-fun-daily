# This is a problem which we can solve by using a stack
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# stack = [(1, ""),(3, a), (2, c)]
class Solution:
    def decodeString(self, s):
        stack = [[1, ""]]
        integer = ""
        for i in s:
            if i in "0123456789": # 0 should be here too..
                integer += i
            elif i == "[":
                stack.append([int(integer), ""])
                integer = ""
            elif i == "]":
                num, char = stack.pop()
                stack[-1][1] += num * char
            else:
                stack[-1][1] += i
        return stack[-1][1]




obj = Solution()
# s = "3[a2[c]]"
string = "100[leetcode]"
print(obj.decodeString(string))
