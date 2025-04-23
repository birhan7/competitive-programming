class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
        colors = ["W"] * numCourses
        stack = []
        def dfs(vertex):
            colors[vertex] = "G"
            for neighbor in graph[vertex]:
                if colors[neighbor] == "G":
                    return False
                elif colors[neighbor] == "W":
                    colors[neighbor] = "G"
                    if not dfs(neighbor):
                        return False
            stack.append(vertex)
            colors[vertex] = "B"
            return True
            
        for node in range(numCourses):
            if colors[node] == "W":
                if not dfs(node):
                    return []
        stack.reverse()
        return stack


                
        
