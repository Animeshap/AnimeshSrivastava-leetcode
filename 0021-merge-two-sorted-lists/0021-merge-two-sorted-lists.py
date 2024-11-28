class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create an empty list to store the values of both linked lists
        res = []
        
        # Traverse the first list and append its values to the res list
        temp1 = list1
        while temp1:
            res.append(temp1.val)
            temp1 = temp1.next
        
        # Traverse the second list and append its values to the res list
        temp2 = list2
        while temp2:
            res.append(temp2.val)
            temp2 = temp2.next
        
        # Sort the combined values
        res.sort()
        
        # Create a dummy node to build the merged linked list
        dummy = ListNode()
        current = dummy
        
        # Iterate through the sorted values and create new nodes in the linked list
        for val in res:
            current.next = ListNode(val)
            current = current.next
        
        # Return the merged linked list, starting from dummy.next
        return dummy.next
