# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
class Solution:
    def canCompleteCircuit(self, gas, cost):
        cur_tank, total_tank = 0, 0 # one for finding the starting gas station, and the other to check whether we can finish the whole trip
        starting_station = 0

        for i in gas:
            cur_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]

            if cur_tank > 0:
                cur_tank = 0
                starting_station += 1
        
        if total_tank >= 0:
            return starting_station
        else:
            return -1

        