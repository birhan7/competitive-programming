# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        self.paths(root, "")
        return self.ans

    def paths(self, root, path):
        path = path + "->" + str(root.val) if path else str(root.val)
        if root.left == None and root.right == None:
            self.ans.append(path)
        if root.left:
            self.paths(root.left, path)
        if root.right:
            self.paths(root.right, path)



        