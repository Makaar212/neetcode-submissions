class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cur = 0


        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            maxSub = max(cur, maxSub)
        return maxSub