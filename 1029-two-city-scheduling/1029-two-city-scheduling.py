class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0] - x[1]))
        half = len(costs) // 2
        ans = 0
        for i in range(len(costs)):
            if half:
                ans += costs[i][0]
                half -= 1
            else:
                ans += costs[i][1]
        return ans
            

            
            
        