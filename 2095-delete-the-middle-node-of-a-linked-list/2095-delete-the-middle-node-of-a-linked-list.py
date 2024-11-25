class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Handle edge cases (0 or 1 node)
            return None

        # Create a list of nodes for brute force
        res = []
        temp = head
        while temp:  # First pass to store all nodes in a list
            res.append(temp)
            temp = temp.next

        # Find the middle index
        mid = len(res) // 2

        # If there's a node before the middle, update its `next` pointer to skip the middle node
        if mid > 0:
            res[mid - 1].next = res[mid].next

        return head
