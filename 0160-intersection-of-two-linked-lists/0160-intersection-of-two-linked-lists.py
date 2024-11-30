class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        if not head1 or not head2:  # Check if either list is empty
            return None

        temp1, temp2 = head1, head2

        # Traverse both lists
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else head2  # Switch to head2 when temp1 reaches the end
            temp2 = temp2.next if temp2 else head1  # Switch to head1 when temp2 reaches the end

        return temp1  # Returns the intersection node or None
