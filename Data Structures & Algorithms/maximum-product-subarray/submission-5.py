class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                curMax = 0
                curMin = 0
                continue
            tmp = curMax *n
            curMax = max(curMax * n, n, n * curMin)
            curMin = min(tmp, n, curMin * n)
            res = max(res, curMax)
        return res