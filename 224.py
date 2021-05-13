# Input: s = "1 + 1"
# Output: 2
# Input: s = " 2-1 + 2 "
# Output: 3
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
class Solution:
    def calculate(self, s):
        stack = []
        res = 0 # ongoing calculation
        sign = 1
        operand = 0

        for ch in s:
            if ch.isdigit():
                operand += 10 * operand + int(ch)
            if ch == "+":
                res += sign * operand
                sign = 1
                operand = 0
            if ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            if ch == "(":
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1
                # no operand reset?
            if ch == ")":
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + operand * sign # example "1 + 1"

