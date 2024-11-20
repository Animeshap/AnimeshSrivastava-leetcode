# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        node_set=set()
        while temp!=None:
            node_set.add(temp)
            temp=temp.next
            if temp in node_set:
                return temp
        return None