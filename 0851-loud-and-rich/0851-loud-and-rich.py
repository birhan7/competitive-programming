class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        graph = defaultdict(list)
        roots = set(quiet)
        for u,v in richer:
            graph[v].append(u)
            roots.discard(u)
            
        ans = [0] * length
        visited = set()
        def dfs(vertex):
            min_node = vertex
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(vertex)
                    node = dfs(neighbor)
                    quietness = quiet[min_node]
                    if quietness > quiet[node]:
                        min_node = node
                else:
                    if quiet[min_node] > quiet[ans[neighbor]]:
                        min_node = ans[neighbor]
            ans[vertex] = min_node
            
            return min_node
        for i in roots:
            visited.add(i)
            dfs(i)
        return ans

            
        