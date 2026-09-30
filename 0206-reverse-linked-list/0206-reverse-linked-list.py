# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head:
            node = self.reverse(head)
            node.next = None
        return self.head
        

    def reverse(self, head):
        if head.next == None:
            self.head = head
            return head
        node = self.reverse(head.next)
        node.next = head
        return head

        
    
        