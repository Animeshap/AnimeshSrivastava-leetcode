class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []  # Create a new list to store the sorted elements
        for num in nums:
            if num % 2 == 0:
                result.insert(0, num)  # Place even numbers at the front
            else:
                result.append(num)  # Place odd numbers at the back
        return result
