class Solution:
    def reformat(self, s: str) -> str:
        alph, digit = [], []
        
        for ch in s:
            if ch.isdigit():
                digit.append(ch)
            else:
                alph.append(ch)
        
        D, A = len(digit), len(alph)
        if abs(D - A) > 1:
            return ""
        
        res = []
        while digit and alph:
            res += [digit.pop(), alph.pop()]
        
        return "".join(alph + res + digit) # This line is very smart - I didn't think of it...