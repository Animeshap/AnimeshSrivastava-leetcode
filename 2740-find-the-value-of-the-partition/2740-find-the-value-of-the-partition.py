class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        mini=float('inf')
        for i in range(0,len(nums)-1):
            mini=min(mini,nums[i+1]-nums[i])
        return mini