class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # This is a problem that deals with subprobs
        if not nums:
            return [[]]
        # get all the permutations for the ones before 
        perms = self.permute(nums[1:])
        # then for every permutation for the ones before, put nums[0] in every position from 0 to i
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy)
        # add it to result


        return res