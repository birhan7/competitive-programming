class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        shortest_path = float('inf')
        allvisited = (1 << n) - 1

        for u in range(n):
            queue = [(u, (1 << u))]
            seen = set(queue)
            level = 0
            while queue:
                if any(allvisited == nodevisited for _, nodevisited in queue):
                    shortest_path = min(shortest_path, level)
                    break
                queue, level = [(v, (nodevisited | 1 << v)) for u, nodevisited in queue for v in graph[u] if (v, (nodevisited | 1 << v)) not in seen and not seen.add((v, (nodevisited | 1 << v))) ], level + 1
        return shortest_path




        