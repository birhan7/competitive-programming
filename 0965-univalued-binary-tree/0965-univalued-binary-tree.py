# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(node):
            visited = set([node])
            queue = deque([node])

            while queue:
                vertex = queue.popleft()
                if vertex.val != root.val:
                    return False
                if vertex.left:
                    visited.add(vertex.left)
                    queue.append(vertex.left)
                if vertex.right:
                    visited.add(vertex.right)
                    queue.append(vertex.right)
            return True
        return bfs(root)
        