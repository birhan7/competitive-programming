"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for employee in employees:
            graph[employee.id] = employee

        def dfs(node):
            total = 0
            for n in node.subordinates:
                total += dfs(graph[n])
            return total + node.importance
            
        return dfs(graph[id])
            


        