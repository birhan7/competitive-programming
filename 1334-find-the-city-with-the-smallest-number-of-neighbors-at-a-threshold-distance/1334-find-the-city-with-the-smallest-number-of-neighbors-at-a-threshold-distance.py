class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v, w = edges[i]
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def nodes(start_node, max_dist):
            processed = set()
            heap = [(0, start_node)]
            count = set()
            while heap:
                curr_dist, curr_node = heappop(heap)
                if curr_node in processed:
                    continue
                processed.add(curr_node)
                for child, w in graph[curr_node]: 
                    distance = w + curr_dist
                    if distance <= max_dist and child not in processed:
                        count.add(child)
                        heappush(heap, (distance, child))
            return len(count)
        ans = {}
        for i in range(n):
            ans[i] = nodes(i, distanceThreshold)
        res = min(ans.values())
        index = 0
        for k, v in ans.items():
            if v == res and k > index:
                index = k
        return index

        