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
        if not head:
            return head

        def flatten_node(prev, curr):
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            
            curr_next = curr.next
            tail = flatten_node(curr, curr.child)
            curr.child = None
            return flatten_node(tail, curr_next)

        dummyNode = Node(0, None, head, None)     
        flatten_node(dummyNode, head)
        dummyNode.next.prev = None
        return dummyNode.next  