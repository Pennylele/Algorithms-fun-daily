class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s)-1: # need to use "if", bc if the last element is a digit, we need to do the final calculation
                if sign == "+": # The sign is always the previous element's sign
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i] 
        return sum(stack)