class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        comp=[]
        for i in range(1,len(nums),2):
            freq=nums[i-1]
            val=nums[i]
            comp.extend([val]*freq)
        return comp
