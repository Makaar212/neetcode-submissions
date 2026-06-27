class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        longest = 0
        

        for value in nums:
            if value - 1 not in numsSet:
                current = 1
                while value + current in numsSet:
                    current +=1                   
                longest = max(current, longest)
                

        

        return longest

        
            
