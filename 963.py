class Solution:
    def minAreaFreeRect(self, points):
        # function to calculate the distance between 2 points
        def distance(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        # try out all combinations for their diagonal center point. Then the center point can be stored into a dictionary with values being an integer.
        diagonal_dict = collections.defaultdict(list)
        P = len(points)
        for i in range(P):
            for j in range(i+1, P):
                p1, p2 = points[i], points[j]
                center_x = (p1[0] + p2[0])/2
                center_y = (p1[1] + p2[1])/2
                center_length = distance(i, j) # we use the distance to make sure the rectangles are rectangles
                diagonal_dict[(center_x, center_y, center_length)].append((p1, p2))

        # Loop through the dictionary - if the value is > 1, then calculate the area and find min
        ans = float('inf')
        for i in diagonal_dict:
            D = len(diagonal_dict)
            if D > 1:
                for i in range(D):
                    for j in range(i+1, D):
                        p1 = diagonal_dict[i][0]
                        p2 = diagonal_dict[i][1]
                        p3 = diagonal_dict[j][0]
                        p4 = diagonal_dict[j][1]
                        area = sqrt(distance(p1, p3)) * sqrt(distance(p1, p4))
                        ans = min(ans, area)
        if ans == float('inf') : 
            return 0
        else: 
            return ans

