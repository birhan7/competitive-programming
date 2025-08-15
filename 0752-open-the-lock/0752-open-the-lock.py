class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        graph = defaultdict(list)
        exclude = set(deadends)
        queue = deque([(target, 0)])
        visited = set(target)
        if "0000" in exclude:
            return -1

        def neighbors(node,dist):
            for i in range(len(node)):
                num = int(node[i]) + 10
                nbr1, nbr2 = node[:i] + str((num + 1) % 10)  + node[i+1:], node[:i] + str((num - 1) % 10)  + node[i+1:]
                if nbr1 not in exclude and nbr1 not in visited:
                    visited.add(nbr1)
                    queue.append((nbr1,dist+1))
                if nbr2 not in exclude and nbr2 not in visited:
                    visited.add(nbr2)
                    queue.append((nbr2,dist+1))
 
        while queue:
            node, distance = queue.popleft()
            if node == "0000":
                return distance
            neighbors(node,distance)
        return -1
            