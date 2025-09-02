class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: (x[0] - x[1]))
        n = len(costs)
        cost = 0
        for i in range(n):
            if i < n // 2:
                cost += costs[i][0]
            else:
                cost += costs[i][1]
        return cost
            

            
            
        