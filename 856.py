# stack solution - using stacks to register the levels
# "(()(()))"
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for i in s:
            if i == "(":
                stack.append(0) 
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1) # This one is little bit tricky. But the popped value is replaced by the max(2*v, 1), we just add it to the stack[-1] for the total.
        return stack.pop()
#//////////////////////////////////////////
# Another elegant solution
class Solution:
    def scoreOfParentheses(self, s):
        ans = bal = 0
        
        for i, x in enumerate(s):
            if x == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    ans += 1 << bal # Just to count level. 1 <<  bal == 2 ** bal
        return ans