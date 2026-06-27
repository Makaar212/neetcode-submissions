class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        longest = 0
        current = 1

        for value in nums:
            if value - 1 not in numsSet:
                next = value + 1
                while next in numsSet:
                    current +=1
                    next += 1
                longest = max(current, longest)
                current = 1

        

        return max(current, longest)

        
            
