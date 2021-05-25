# This problem can be solved in a lot of diferent ways, here is just one of them: we will use that 3 is prime number, so if we take number 3^19, then it is divisible by powers of 3 and by only them. Why we choose 3^19? Because it is the biggest power of 3, which fits in int32.
class Solution:
    def isPowerOfThree(self, n):
        return 0 if n <= 0 else 1162261467 % n == 0