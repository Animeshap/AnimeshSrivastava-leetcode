class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')
        for i in range(len(nums)):
            cur=0
            cur_len=0
            for j in range(i,len(nums)):
                cur+=nums[j]
                cur_len+=1
                if cur_len>=l and cur_len<=r and cur>0:
                    ans=min(ans,cur)
        if (ans==float('inf')):
            return -1
        return ans
