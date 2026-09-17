class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr1(n):
            rob1, rob2 = 0,0
            for num in n:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        

        res = 0

        res = max(nums[0], hr1(nums[0:len(nums) - 1]), hr1(nums[1:len(nums)]))
        return res