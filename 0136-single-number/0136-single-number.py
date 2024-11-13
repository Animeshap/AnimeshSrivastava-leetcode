class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:  # Check if the count of `num` is 1
                return num