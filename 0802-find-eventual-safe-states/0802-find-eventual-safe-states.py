class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        colors = [0] * length
        stack = []
        def topsort(vertex):
            colors[vertex] = 1
            for neighbor in graph[vertex]:
                if colors[neighbor] == 1:
                    return False
                elif colors[neighbor] == 0:
                    colors[neighbor] = 1
                    if not topsort(neighbor):
                        return False
            colors[vertex] = 2
            stack.append(vertex)
            return True

        ans = []
        for i in range(length):
            if colors[i] == 0:
                if not topsort(i):
                    ans.extend(stack)
                    stack = []  
        ans.extend(stack)   
        ans.sort()
        return ans


        
        