class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        res = []
        # thikn of this as a subprob

        # gimme the permutations of everything below me
        preperms = self.permute(nums[1:])
        # for every preperm insert nums[0] at every position from 0 <= len(preperm)
        for previous in preperms:
            for i in range(len(previous) + 1):
                previousCopy = previous.copy()
                previousCopy.insert(i, nums[0])
                res.append(previousCopy)
        # add that to res
        return res
        #return res