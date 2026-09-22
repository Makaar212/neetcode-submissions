class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Can start on 0, if we start on 0 it's not possible
        # js get to the last index, not out of bounds

        # 
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        dp = [0] * len(nums)
        dp[-1] = 1


        for i in range(len(nums) - 1, -1, -1):
            # checking to see if from the current index to the choices do we have a valid path 
            cur = nums[i] 
            for j in range(i, i + cur + 1):
                if j < len(nums) and dp[j] == 1:
                    dp[i] = 1
        

        return dp[0] == 1


        """
        [0,2,0,1,0]

        dp = [1, 1, 0, 1, 1]

        i = 0
        iterateTo = 2
        cur = 1 
        j = 

        """
            