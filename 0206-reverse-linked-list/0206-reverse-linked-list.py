# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        p=None
        q=None
        while head!=None:
            q=head.next
            head.next=p
            p=head
            head=q
        return p
            


        
