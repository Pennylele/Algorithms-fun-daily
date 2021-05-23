# Sort the balloons by their end value
# Then only update the end variable when the new balloon starts after the current balloon's end (no overlap). It means that we need a new arrow for the new balloon. 
# And after the current balloon, even if we come across a balloon whose start is less than the previous ends, we don't need to add another arrow.
# Maybe think about it in a greedy way. We only need 1 more arrow if the current ballon has no overlap with the previous one.
class Solution:
    def findMinArrowShots(self, points):
        prev = float('-inf')
        arrow = 0

        for start, end in points:
            if start > prev:
                arrow += 1
                prev = end 
        return arrow