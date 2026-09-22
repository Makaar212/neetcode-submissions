class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for recursion at every step we have the choice of taking this one and moving on or not taking 
        # this one and moving on, so let's keep track of index and current amout, and return the max of 
        # it
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
        