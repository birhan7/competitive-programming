class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b,values[i]))
            graph[b].append((a,1 / values[i]))

        def dfs(vertex, destination, visited):
            if destination not in graph or vertex not in graph:
                return -1
            elif vertex == destination:
                return 1
            visited.add(vertex)
            total = 0
            for neighbor in graph[vertex]:
                node, weight = neighbor
                if node == destination:
                    return weight
                elif node not in visited:
                    total = max(total,dfs(node, destination, visited) * weight)

            return total 


        ans = []
        for i in range(len(queries)):
            a, b = queries[i]
            val = dfs(a,b,set())
            val = val if val != 0 else -1
            ans.append(val)

        return ans
        