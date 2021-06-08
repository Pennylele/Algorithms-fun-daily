# Time complexity: O(4^N⋅N), where N is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.

# The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to N to build the combination. This problem can be generalized to a scenario where numbers correspond with up to M digits, in which case the time complexity would be O(M^N⋅N). For the problem constraints, we're given, M=4, because of digits 7 and 9 having 4 letters each.


class Solution:
    def letterCombinations(self, digits):
        def backtrack(idx, path):
            if len(path) == D:
                res.append("".join(path))
                return # return here is important, so taht we don't continue adding in the idx, which would generate the index error.
            # Get the letters that the current digit maps to, and loop through them
            chars = self.digitToLetters(digits[idx]) # This is to fix the first level keys
            for ch in chars: # Then try to add more chars after each of them.
                path += ch
                backtrack(idx+1, path)
                path.pop()
        
        if len(digits) == 0: return []
        D = len(digits)
        res = []
        backtrack(0, [])
        return res
    
    def digitToLetters(self, digit):
        mapping = {"2":"abc", 
                   "3":"def",
                   "4":"ghi", 
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv", 
                   "9":"wxyz"}
        return mapping[digit] 