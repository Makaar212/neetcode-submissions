class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        countZeros = 0
        totalProd = 1
        for i, value in enumerate(nums):
            if value == 0:
                countZeros += 1
            else:
                totalProd *= value

        if countZeros >= 2:
            return [0] * len(nums)

        elif countZeros == 1:
            for i, value in enumerate(nums):
                if value != 0:
                    nums[i] = 0
                else:
                    nums[i] = totalProd

        else:
            for i, value in enumerate(nums):
                nums[i] = totalProd // nums[i]

        return nums
        