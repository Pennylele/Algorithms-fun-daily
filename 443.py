# chars = ["a","a","b","b","c","c","c"]
class Solution:
    def compress(self, chars: List[str]) -> int:
        walker, runner = 0, 0 # walker records the next element to make a change to; runner is the index we have processed to.
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1 # This is one round of counting repeated chars
            
            while runner + 1 < len(chars) and chars[runner] == chars[runner + 1]:
                runner += 1 # At the end, runner is at the last char of the current repeated chars
                count += 1
            
            if count > 1: # we don't want to write 1
                for c in str(count):
                    chars[walker + 1] = c # always pointing to the 2nd char of the current repeated chars, expect the one char. The interesting fact is that if the count is >1 digit long, then we'll process it like this ["a","1","0","b","2","c","3"], so that we can count the string length in total.
                    walker += 1
            
            walker += 1
            runner += 1
        
        return walker