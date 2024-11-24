# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        temp=head
        #handle odd cases
        list_val=[]
        while temp!=None and temp.next!=None:
            list_val.append(temp.val)
            temp=temp.next.next
        if temp!=None:
            list_val.append(temp.val)
        #handle even cases
        temp=head.next
        while temp!=None and temp.next!=None:
            list_val.append(temp.val)
            temp=temp.next.next
        if temp!=None:
            list_val.append(temp.val)
        #append all values arr to linked list
        i=0
        temp=head
        while temp:
            temp.val = list_val[i]
            temp = temp.next
            i += 1
        return head
