class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # helpful to think of this problem in a way where for every perm, js take nums[0] and move it every around it 
        # that's how we would do it by hand for every number just move it to every position 
        
        # for every perm before

        if not nums:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(nums)):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy)
        return res