class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            indegree[courses[0]] += 1
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        print(queue,graph)
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return list(order) if len(order) == numCourses else []
                
        
