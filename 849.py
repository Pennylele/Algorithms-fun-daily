# This one is so clean...
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, last, S = 0, -1, len(seats)
        MAX = float('-inf')
        for j in range(S):
            if seats[j] == 1:
                if last == -1:
                    MAX = max(MAX, j)
                else:
                    MAX = max(MAX, (j - last)//2)
                last = j
        return max(MAX, S-1-last)
# My own version...
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # if the first index element is 0, then we try to record the length to the first 1
        candidate_left = 0
        i, S = 0, len(seats)
        if seats[i] == 0:
            while i < S and seats[i] != 1:
                i += 1
        candidate_left = i - 0
        
        # if the last index element is 0, then we try to record the length to the last 1
        candidate_right = 0
        j = S-1
        if seats[-1] == 0:
            while j > 0 and seats[j] != 1:
                j -= 1
        candidate_right = S - 1 - j

        # if the first 1 and the last 1 is not at the same index, we record the length between them and any 1s inside that range.
        if i == j:
            return max(candidate_left, candidate_right)
        candidate_middle = 0
        x = start = i
        max_middle = float('-inf')
        while x <= j:
            if seats[x] == 1:
                max_middle = max(max_middle, x - start)
                start = x
            x += 1
                
        # final comparison
        return max(candidate_left, candidate_right, max_middle // 2)