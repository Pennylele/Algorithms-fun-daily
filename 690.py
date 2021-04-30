class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
#//////////////////////////////////////
# I think this problem is to understand that each employee is an object, so we can create a map with the employee id as the key and the employee object as the value.
# Time Complexity: O(n); Space Complexity: O(n)

class Solution:
    def getImportance(self, employees, id):

        def helper(id):
            self.ans += employeeMap[id].importance
            for sub in employeeMap[id].subordinates:
                helper(sub)
            return self.ans

        # Need to place the Employee subordination relationships into a data structure for the later dfs. e.g. {id: [sub1_id, sub2_id]}
        
        employeeMap = collections.defaultdict()
        for employee in employees:
            employeeMap[employee.id] = employee

        self.ans = 0
        self.visited = set()
        helper(id)
        return self.ans 

