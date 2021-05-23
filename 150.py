class Solution:
    def evalRPN(self, tokens):
        stack = []

        def math(num1, num2, operator):
            if operator == "+":
                return int(num1) + int(num2)
            if operator == "-":
                return int(num2) - int(num1)
            if operator == "*":
                return int(num1) * int(num2)
            if operator == "/":
                return int(int(num2)/int(num1))

        for i in tokens:
            if i in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math(num1, num2, i))
            else:
                stack.append(i)
        return stack[0]

obj = Solution()
print(obj.evalRPN(["4","13","5","/","+"]))