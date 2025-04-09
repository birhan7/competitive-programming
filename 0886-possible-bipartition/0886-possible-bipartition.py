class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colored = [-1] * (n+1)
        aj_list = defaultdict(list)
        for a,b in dislikes:
            aj_list[a].append(b)
            aj_list[b].append(a)
        
        def dfs(node):
            for n in aj_list[node]:
                if colored[n] == -1:
                    colored[n] = 1 - colored[node]
                    if not dfs(n):
                        return False
                else:
                    if colored[n] == colored[node]:
                        return False
            return True

        for i in range(1,n):
            if colored[i] == -1:
                colored[i] = 1
            if not dfs(i):
                return False
        return True
        