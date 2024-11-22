# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head:ListNode)->ListNode:
        p=None
        q=None
        while head!=None:
            q=head.next
            head.next=p
            p=head
            head=q
        return p

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        prev=None
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        rev=self.reverse(slow)
        while rev!=None:
            if head.val!=rev.val:
                return False
            head=head.next
            rev=rev.next
        return True