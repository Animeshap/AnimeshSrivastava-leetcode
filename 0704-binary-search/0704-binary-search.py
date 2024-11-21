class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        while low<high:
            if nums[low]==target:
                return low
            elif nums[low]<target:
                low+=1
            else:
                high-=1
        return -1
