class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        heapify(heap)
        visited = set()
        res = 0
        while heap:
            w, node = heappop(heap)
            visited.add(node)
            if len(visited) == n:
                res = max(res,w)
                return res

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heappush(heap,(weight + w,neighbor))
        return -1 
        

                    

        