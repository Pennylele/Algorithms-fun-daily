# distances is a 2D list, where its inner list index corresponds to the worker ID; But each list is sorted based the distance between the worker and all bikes in an descending manner.
# Then another sorted of process after the above, is to place all the popped out smallest distance for each worker to a heap. 
# The above distances list is still useful in that whenever we have a conflict for a user, we can find the next best option for the current user.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # get the minimum distance from each worker to each bike
        W = len(workers)
        B = len(bikes)
        distances = []
        
        for i in range(W):
            distances.append([])
            for j in range(B):
                m_distance = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
                distances[-1].append((m_distance, i, j))
            distances[-1].sort(reverse=True)

        
        min_distances = [distances[i].pop() for i in range(W)]
        
        # use heap to assign bikes to the workers
        heapq.heapify(min_distances) # Please don't forget to heapify the list first before operating the heap methods
        assigned_bikes = set()
        ans = [0] * W
        
        while len(assigned_bikes) < W:
            smallest_dis, worker, bike = heapq.heappop(min_distances)

            if bike not in assigned_bikes:
                assigned_bikes.add(bike)
                ans[worker] = bike
            else:
                heapq.heappush(min_distances, distances[worker].pop())
        
        return ans
                