# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                curr = queue.pop()
                temp.append(curr.val)
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            ans.append(temp)
        return ans
            

        