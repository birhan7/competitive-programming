class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        heap = [(0, -1, src)]
        distances = {node: float('inf') for node in range(n)}
        processed = set()
        while heap:
            curr_dist, stop, curr_node = heappop(heap)
            if curr_node == dst and stop <= k:
                return curr_dist
            if curr_node in processed or stop >= k:
                continue
            processed.add(curr_node)
            for nbr, weight in graph[curr_node]:
                distance = weight + curr_dist
                if distance < distances[nbr]:
                    distances[nbr] = distance
                    heappush(heap, (distance, stop + 1, nbr))
        return -1
        