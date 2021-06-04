# 58 = 50 + 8
# The easiest way is to use greedy
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        roman_digits = []
        for digit, symbol in digits:
            count, num = divmod(num, digit) # 487 => count, num = 4, 87
            roman_digits.append(count * symbol)
        return "".join(roman_digits)

# The first approach should be fine, and in-fact has the added bonus of being more flexible if we were to extend the Roman Numeral symbol set to have symbols over 1000. This second approach is only included for completeness. Do try to understand how we derived this approach, though.
        