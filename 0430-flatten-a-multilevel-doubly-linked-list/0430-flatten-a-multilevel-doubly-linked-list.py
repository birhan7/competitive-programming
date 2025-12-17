"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node.child:
                if not node.next:
                    return node
                return dfs(node.next)
            else:
                last_node = dfs(node.child)
                last_node.next = node.next
                if node.next:
                    node.next.prev = last_node 
                node.next = node.child
                node.next.prev = node
                node.child = None
                return dfs(last_node)
        if head:
            dfs(head)
        return head
        