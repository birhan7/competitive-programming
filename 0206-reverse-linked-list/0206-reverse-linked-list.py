# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        Prev, Next = None, None
        curr = head
        while curr:
            Next = curr.next
            curr.next = Prev
            Prev = curr
            curr = Next
        return Prev
        
        

    

        
    
        