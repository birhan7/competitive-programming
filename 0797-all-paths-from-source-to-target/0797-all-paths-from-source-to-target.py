class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in range(len(graph)):
            dic[i] = graph[i]

        result = []  

        def dfs(node,path):

            if node == len(graph)-1:
                result.append(path.copy())
            
            for neigh in dic[node]:
                path.append(neigh)
                dfs(neigh,path)
                path.pop()
   
        dfs(0,[0])

        return result