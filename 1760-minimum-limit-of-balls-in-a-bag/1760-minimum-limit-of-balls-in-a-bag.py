class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_balls):
            ops=0
            for n in nums:
                ops+=ceil(n/max_balls)-1
                if ops>maxOperations:
                    return False
            return True
        l=1
        r=max(nums)
        res=r
        while l<r:
            mid=l+(r-l)//2
            if can_divide(mid):
                r=mid
                res=r
            else:
                l=mid+1
        return res
