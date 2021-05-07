# a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR"
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# The first rule is that the sequence of R and L should stsay the same after the conversion
# The second rule is that the converted "L"'s position should be smaller than or equal to the original "L"; while the converted "R"'s position should be bigger than or equal to the original "R", following the sequence.
class Solution:
    def canTransform(self, start, end):
        if len(start) != len(end): return False
        S = [(s, i) for i, s in enumerate(start) if s == 'L' or s == 'R']
        E = [(e, j) for j, e in enumerate(end) if e == 'L' or e == 'R']

        if len(S) != len(E): return False # Don't forget about this edge case. e.g. "X" -> "L"

        for (s, i), (e, j) in zip(S, E):
            if s != e: return False
            if s == 'L' and i < j:
                return False
            if s == 'R' and i > j:
                return False
        return True

    