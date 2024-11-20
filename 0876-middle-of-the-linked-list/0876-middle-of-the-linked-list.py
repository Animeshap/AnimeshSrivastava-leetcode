# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        total=0
        while temp!=None:
            total+=1
            temp=temp.next
        #find the middlenode
        midnode=(total//2)+1
        temp=head
        while temp!=None:
            midnode=midnode-1
            if midnode==0:
                break
            temp=temp.next
        return temp
        
        
            