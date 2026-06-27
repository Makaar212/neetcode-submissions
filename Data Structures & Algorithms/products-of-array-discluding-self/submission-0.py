class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        for i, value in enumerate(nums):
            currentValue = 1
            for j, v in enumerate(nums):
                if j == i:
                    continue
                else: 
                    currentValue *= v
            copy[i] = currentValue
            currentValue = 1
        
        return copy

        