# Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
# Output: 3
# atan2 - atan2(y, x) returns value of atan(y/x) in radians. The atan2() method returns a numeric value between –pi and pi representing the angle \theta of a (x, y) point and positive x-axis.
# This problem is interesting in that:
# 1. we use the relative degree from each point to the location (see the drawing)
# 2. See why we should add 360 to the points
# 3. Adding 360 to other positive points wouldn't create duplicate max values.

#Atan2 result is always between -pi and pi.

class Solution:
    def visiblePoints(self, points, angle, location):
        extra = 0
        atan_values = []
        # calculate all atans values from all points
        for x, y in points:
            if x == location[0] and y == location[1]:
                extra += 1 # I think no matter where the person moves, this exact same point needs to be added to the final answer. 
                continue
            atan_values.append(math.atan2(y - location[1], x - location[0]))
        
        # add 360 to all the current points
        atan_values.sort()
        new_atan2 = atan_values + [i + 2 * math.pi for i in atan_values] # This is to add 360 degrees to all the values in case we miss any points. Example: location = [1,1], points = [[0,2],[0,0]], degree = 90
        degree_radiance = angle * math.pi / 180
        
        # Using sliding window to find all the points that were within the angle.
        l = 0
        ans = 0
        for r in range(len(new_atan2)):
            while new_atan2[r] - new_atan2[l] > degree_radiance:
                l += 1
            ans = max(ans, r - l + 1)
        return ans + extra
