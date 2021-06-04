# 1. select the tasks that need the least processing time
# 2. choose the task that has the smallest enqueue time to start with
# 3. Forgot about we also want to reduce the CPU idle time. So we should push into the heap the tasks that start the earliest. Then at the second round, we recalculate the CPU's next idle time; and the next elements popped in, as long as their enqueue time is <= the CPU's next idle time, we pick the one with the shortest processing time; if 
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the tasks based on their starting time
        tasks = sorted([(t[0], t[1], idx) for idx, t in enumerate(tasks)])
        
        # start the heap operations: 1. select and push the tasks that have the desired start time into the heap; 2. pop out the tasks that have the shortest processing time among them.
        res = []
        heap = []
        i = 0
        T = len(tasks)
        time = tasks[0][0]
        while len(res) < T:
            while i < T and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2])) # processingTime, index
                i += 1
            
            if heap: 
                processingTime, idx = heapq.heappop(heap)
                time += processingTime
                res.append(idx)
            elif i < T:# if heap is empty (i.e. rest of the tasks would all give CPU some idle time), we chose the next enqueue time as the bar. Otherwise, we just process the existing tasks inside the heap to avoid idle time.
                time = tasks[i][0]
        return res