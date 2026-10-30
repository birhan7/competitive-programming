# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node.left and not node.right:
                ans = max(ans, node.val)
                return node.val
            right, left = float('-inf'), float('-inf')
            if node.right:
                right = dfs(node.right)
            if node.left:
                left = dfs(node.left)
            local_max = node.val + left + right
            ans = max(local_max, right, left, node.val, ans)
            return max(right + node.val, left + node.val, node.val)
        res = dfs(root)
        return max(ans, res)
        