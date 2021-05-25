# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

# Guess the math method is the fastest
class Solution:
    def leastInterval(self, tasks, n):
        values = list(collections.Counter(tasks).values())
        max_task_count = max(values)
        max_count_tasks = values.count(max_task_count)
        return max(len(tasks), (max_task_count - 1) * (n + 1) + max_count_tasks)


