# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        temp=head
        while temp:
            r.append(temp.val)
            temp=temp.next
        r=sorted(r)
        i=0
        temp=head
        while i<len(r) and temp:
            temp.val=r[i]
            temp=temp.next
            i+=1
        return head