# Euclidean algorithm
# Main article: Euclidean algorithm
# File:The Great Common Divisor of 62 and 36 is 2.ogv
# Animation showing an application of the Euclidean algorithm to find the greatest common divisor of 62 and 36, which is 2.
# A more efficient method is the Euclidean algorithm, a variant in which the difference of the two numbers a and b is replaced by the remainder of the Euclidean division (also called division with remainder) of a by b.

# Denoting this remainder as a mod b, the algorithm replaces (a, b) by (b, a mod b) repeatedly until the pair is (d, 0), where d is the greatest common divisor.

# For example, to compute gcd(48,18), the computation is as follows:
# (48,18) => (18,48 % 18) = (18,12)
#         => (12,18 % 12) = (12,6)
#         => (6,12 % 6) = (6,0)
# This again gives gcd(48, 18) = 6.
# basic idea is that the targetCapacity should be a multiple of gcd(jug1Capacity, jug2Capacity).
# jug1Capacity + jug2Capacity should be >= targetCapacity as well, otherwise even if we fill the 2 jugs full, we can't get the targetCapacity
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if (jug1Capacity + jug2Capacity < targetCapacity): return False
        
        def gcd(x, y):
            if x < y:
                x, y = y, x
            
            while x != y and y != 0:
                remainder = x % y
                x, y = y, remainder
            return x
        
        g = gcd(jug1Capacity, jug2Capacity)
        
        if g == 0: 
            return targetCapacity == 0
        else:
            return targetCapacity % g == 02 ** 15