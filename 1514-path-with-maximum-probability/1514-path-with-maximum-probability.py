class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        distances = {node: -float('inf') for node in range(n)}
        processed = set()
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
            
        heap = [(1, start_node)]
        while heap:
            curr_dist, curr_node = heappop(heap)
            if curr_node in processed:
                continue
            if curr_node == end_node:
                return abs(curr_dist)
            processed.add(curr_node)
            for child, w in graph[curr_node]:
                distance = w * abs(curr_dist)
                if distance > distances[child]:
                    distances[child] = distance
                    heappush(heap, (-distance, child))
        return 0
        