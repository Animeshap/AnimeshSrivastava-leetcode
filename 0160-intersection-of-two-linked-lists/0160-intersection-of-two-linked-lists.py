# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        st=set()
        temp=head1
        while temp:
            st.add(temp)
            temp=temp.next
        while head2!=None:
            if head2 in st:
                return head2
            head2=head2.next
        return None
