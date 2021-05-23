# If using pointers
class Solution:
    def addStrings(self, num1, num2):
        p1, p2 = len(num1) - 1, len(num2) - 1
        ans = []
        carry = 0
        while p1 >= 0 or p2 >= 0):
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            total = n1 + n2 + carry
            cur = total % 10
            carry = total // 10

            ans.append(cur)
            p1 -= 1
            p2 -= 1
        
        if carry: ans.append(carry)
        return ''.join(str(i) for i in ans[::-1])

# Using stack...
# class Solution:
#     def addStrings(self, num1, num2):
#         num1, num2 = list(num1), list(num2)
#         ans = []
#         carry = 0
#         while num1 or num2:
#             n1 = ord(num1.pop()) - ord('0') if num1 else 0
#             n2 = ord(num2.pop()) - ord('0') if num2 else 0

#             total = n1 + n2 + carry
#             cur = total % 10
#             carry = total // 10

#             ans.append(cur)
        
#         if carry: ans.append(carry)
#         return ''.join(str(i) for i in ans[::-1])

obj = Solution()
print(obj.addStrings('11', '123'))
print(obj.addStrings('584', '18'))


