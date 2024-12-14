from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        
        # Find the first occurrence of the target
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        
        # Find the last occurrence of the target
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                end = i
                break
        
        return [start, end]
