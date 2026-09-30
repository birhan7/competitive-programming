# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or head.next == None:
            return head
        node = self.reverseList(head.next)
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = head
        head.next = None
        return node
        
    
        