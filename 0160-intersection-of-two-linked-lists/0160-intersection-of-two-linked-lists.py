# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getdifference(self, temp1, temp2):
        # Initialize lengths for both linked lists
        l1 = 0
        l2 = 0

        # Calculate the length of the first linked list
        while temp1:
            l1 += 1
            temp1 = temp1.next

        # Calculate the length of the second linked list
        while temp2:
            l2 += 1
            temp2 = temp2.next

        # Return the difference in lengths
        return l1 - l2

    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        # Get the difference in lengths of the two linked lists
        diff = self.getdifference(head1, head2)

        # Assign temp1 and temp2 to the heads of the linked lists
        temp1 = head1
        temp2 = head2

        # Adjust temp1 or temp2 to align both linked lists
        if diff > 0:
            while diff:
                temp1 = temp1.next
                diff -= 1
        else:
            while diff < 0:
                temp2 = temp2.next
                diff += 1

        # Traverse both linked lists together to find the intersection point
        while temp1 and temp2:
            if temp1 == temp2:  # Intersection found
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next

        # If no intersection is found, return None
        return None
