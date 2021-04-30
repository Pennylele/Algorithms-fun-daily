# target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# can get how much time each fleet needs to reach the destination.

# [1, 1, 12, 7, 3]
# [10, 8, 0, 5, 3]
# SORTED
# [0,  3, 5, 8, 10]
# [12, 3, 7, 1, 1]
# Time Complexity O(NlogN), Space Complexity: O(n)
class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        timeToDes = [(target - p)/s for p, s in cars]
        # timeToDes was sorted based on the position of each car in an ascending order

        fleets = 0
        while len(timeToDes) > 1:
            lead = timeToDes.pop()
            if lead < timeToDes[-1]:
                fleets += 1
            else:
                timeToDes[-1] = lead
        return fleets + len(timeToDes)

s = Solution()
target, position, speed = 12, [10,8,0,5,3], [2,4,1,1,3]
print(s.carFleet(target, position, speed))