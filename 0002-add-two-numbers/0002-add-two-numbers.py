# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        carry=0
        while (l1!=None  or l2!=None)or carry:
            sum=0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            sum+=carry
            num=sum%10
            carry=sum//10
            node=ListNode(num)
            current.next=node
            current=current.next
        return dummy.next
