class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
            else:
                continue
        res=[0]*n
        i=0
        for x in nums:
            if x!=0:
                res[i]=x
                i+=1   
        return res
