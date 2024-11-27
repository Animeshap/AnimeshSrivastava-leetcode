# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        temp=head
        while temp:
            res.append(temp.val)
            temp=temp.next
        # Remove duplicates from the list
        nums=[]
        for i in range(len(res)):
            if res[i-1]!=res[i]:
                nums.append(res[i])
        
        # Rebuild the linked list with unique values
        i=0
        temp=head
        while temp and i<len(nums):
            temp.val=nums[i]
            if i<len(nums)-1:
                if temp.next==None:
                    temp.next=listnode()
                temp=temp.next
            i+=1
        
        # Ensure the new list ends correctly
        if temp:
            temp.next=None
        return head