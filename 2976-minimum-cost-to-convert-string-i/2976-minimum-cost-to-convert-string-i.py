class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        graph = defaultdict(list)
        for i in range(n):
            graph[original[i]].append((cost[i], changed[i]))
        def shortest_path(start_node, end_node):
            heap = [(0, start_node)]
            distances = {chr(i + 97): float('inf') for i in range(26)}
            processed = set()
            while heap:
                curr_dist, curr_node = heappop(heap)
                if curr_node == end_node:
                    return distances[curr_node]
                if curr_node in processed:
                    continue
                processed.add(curr_node)
                for w, child in graph[curr_node]:
                    distance = w + curr_dist
                    if distance < distances[child]:
                        distances[child] = distance
                    heappush(heap, (distance, child))
            return -1
        ans = 0
        memo = {}
        for i in range(len(source)):
            src, trg = source[i], target[i]
            if src != trg:
                if (src, trg) in memo:
                    ans += memo[(src, trg)]
                else:
                    temp = shortest_path(src, trg)
                    if temp == -1:
                        return -1
                    else:
                        memo[(src, trg)] = temp
                        ans += temp
        return ans
        