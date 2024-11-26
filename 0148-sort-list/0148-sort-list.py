class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: empty list or single node is already sorted
        
        # Step 1: Extract values into a list
        res = []
        temp = head
        while temp:
            res.append(temp.val)  # Append the value, not the entire node
            temp = temp.next
        
        # Step 2: Sort the values
        res.sort()
        
        # Step 3: Reassign sorted values back to the linked list
        temp = head
        i = 0
        while temp:
            temp.val = res[i]
            i += 1
            temp = temp.next
        
        return head
