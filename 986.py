# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# [[0,2],[5,10],[13,23],[24,25]]
# [[1,5],[8,12],[15,24],[25,26]]
class Solution:
    def intervalIntersection(self, firstList, secondList):
        F, S = len(firstList), len(secondList)
        i = j = 0
        res = []

        while i < F and j < S:
            if secondList[j][0] <= firstList[i][1] and secondList[j][1] >= firstList[i][0]:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if secondList[j][1] > firstList[i][1]:
                i += 1
            else:
                j += 1
        return res




