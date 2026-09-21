class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search question due to time comp

        # The array was rotated n times
        # if it was rotated then it was shifted to the left

        l, r = 0, len(nums) - 1 

        m = (l + r) // 2
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m - 1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
        m = r
        return nums[m]