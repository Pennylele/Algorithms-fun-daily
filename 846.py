# O(MlogM + N), where M is the number of different cards.
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        start = collections.deque()
        
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or (opened > 0 and i > last_checked + 1):
                return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == groupSize: 
                opened -= start.popleft()
        return opened == 0