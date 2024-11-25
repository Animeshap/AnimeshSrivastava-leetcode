# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
        # If the list is empty or has only one node, return None
            return None

        slow, fast = head, head
        prev = None

        # Traverse the list to find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        if prev:
            prev.next = slow.next

        return head