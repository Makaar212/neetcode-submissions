class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        for i in range(len(nums) - 1, -1, -1 ):
            if i + 1 >= len(nums):
                continue
            elif i + 2 >= len(nums):
                nums[i] = max(nums[i], nums[i + 1])
            else:
                nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        return max(nums)