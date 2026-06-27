class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        startingPoints = set()
        numsSet = set(nums)
        longest = 0
        current = 1

        for value in nums:
            if value in startingPoints:
                continue
            elif value+1 in numsSet:
                next = value+1
                while True:
                    if next not in numsSet:
                        longest = max(longest, current)
                        current = 1
                        break
                    else:
                        current += 1
                        next += 1
                startingPoints.add(value)

        

        return max(current, longest)

        
            
