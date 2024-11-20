class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # The start of the cycle
