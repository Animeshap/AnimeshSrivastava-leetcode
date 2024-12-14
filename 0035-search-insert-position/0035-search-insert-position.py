class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)
        while l<h:
            mid =l+(h-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l+=1
            else:
                h-=1
                
        return l