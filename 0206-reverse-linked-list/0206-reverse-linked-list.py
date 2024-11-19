class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        reversed_head = self.reverseList(head.next)

        # Reverse the current node's link
        head.next.next = head
        head.next = None

        return reversed_head
