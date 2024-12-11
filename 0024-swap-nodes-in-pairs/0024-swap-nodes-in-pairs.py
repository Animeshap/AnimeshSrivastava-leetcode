# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        res = []
        temp = head
        
        # Collect all values from the linked list
        while temp:
            res.append(temp.val)
            temp = temp.next
        
        # Swap adjacent pairs
        for i in range(0, len(res) - 1, 2):  # Ensure `i+1` is within bounds
            res[i], res[i + 1] = res[i + 1], res[i]
        
        # Rebuild the linked list from the swapped values
        dummy = ListNode()
        temp = dummy
        for value in res:
            temp.next = ListNode(value)
            temp = temp.next
        
        return dummy.next
