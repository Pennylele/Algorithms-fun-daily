# Robin-karp is a rolling hash algorithm, for pattern detection.
# We use the previous calculated hash to calculate the current hash value.
# 1. First assign all different chars into numerical values
# 2. Then create a list that contains all the values for the whole string, mapped from the assignments.
# 3. We need to calcuate the first N required sequence letters into a hash value 
# 4. Then we can use the original hashed value to calculate the next N sequenced letters.
#The Naiive way of doing it is the same idea as the Robin-Karp, however, the original idea uses the string to comparison, which could be kinda inefficient. The more optimized way is to use hash values for store and comparison
class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10: return []
        assignment = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        nums = [assignment[i] for i in s]
        store, ans = set(), set()
        base, hash_value = 4, 0

        for i in range(len(s) - 9):
            if i != 0:
                hash_value = hash_value * base - nums[i-1] * pow(base, 10) + nums[i+9] # example on the base 10 system: how do we get 234 from the hash value of 123? Let's say the original hashed string should be 1234, so the length of the sequence is 4. We can do: 123 * 10 - 10 ** 4 + 4 = 234
            else:
                for j in range(10):
                    hash_value = hash_value * base + nums[j] # example on the base 10 system: how do we get 123 => 1 * 10 + 2 = 12; 12 * 10 + 3 - 123
            
            if hash_value in store:
                ans.add(s[i:i+10])
            store.add(hash_value)
        return ans
