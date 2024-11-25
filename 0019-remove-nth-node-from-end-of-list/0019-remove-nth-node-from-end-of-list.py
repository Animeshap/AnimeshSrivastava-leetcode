# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
        if head is None:
            return None
        cnt = 0
        temp = head

        # Count the number of nodes in the linked list
        while temp is not None:
            cnt += 1
            temp = temp.next

        # If N equals the total number of nodes, delete the head
        if cnt == N:
            newhead = head.next
            head = None
            return newhead

        # Calculate the position of the node to delete (res)
        res = cnt - N
        temp = head

        # Traverse to the node just before the one to delete
        while temp is not None:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        # Delete the Nth node from the end
        delNode = temp.next
        temp.next = temp.next.next
        delNode = None
        return head