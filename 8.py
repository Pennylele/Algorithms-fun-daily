# Input: s = "   -42"
# Output: -42
# Input: s = "4193 with words"
# Output: 4193
# Input: s = "words and 987"
# Output: 0
#/////////////////////////REGEX///////////////////////////
class Solution:
    # @return an integer
    def myAtoi(self, s):
        s = s.strip()
        pattern = "^[+-]?\d+" # This regex is imporant - I tend to mix up with the ? in Python regular expression
        result = re.match(pattern, s) # only match the 1st occurance which is enough for this case
        if not result: return 0
        result = int(result[0]) # see how we get the match
        
        if -2 ** 31 <= result < 2 ** 31 - 1:
            return result
        else:
            return -2 ** 31 if result < 0 else 2 ** 31 - 1
#/////////////////////////A different method///////////////////////////
# This is more trivial - pointer
class Solution:
    # @return an integer
    def myAtoi(self, s):
        s = s.strip()
        if not s: return 0 # don't forget this edge case - should be after the strip() method, just in case we meet " " as the edge case
        intMAX = 2147483647
        intMIN = -2147483648
        i = 0
        sign = 1
        if s[i] in "+-":
            i += 1
            sign = 1 if s[0] == "+" else -1
    
        num = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            num = num * 10 + (ord(s[i]) - ord('0')) # See how we add up the number from the first digit
            if num > intMAX:
                break
            i += 1
        return min(max(sign * num, intMIN), intMAX) # great line
