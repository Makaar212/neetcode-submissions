class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # given a list of integers that are sorted,
        # remove all the duplicates from a sorted array, like remove them, 
        # then return the number of unique elements denoted as k

        # What's interesting about this problem is that the first k elements of nums must
        # contain unique elements, meaning we can js swap all the duplicates and put them at the end. 

        # another method is to use extra space and put unique elements in there, then js make nums
        # follow that spaced out array


        res = []
        seen = set()
        i = 0

        while i < len(nums):
            if nums[i] not in seen:
                res.append(nums[i])
                seen.add(nums[i])
            i += 1 
        
        for i in range(len(res)):
            nums[i] = res[i]
        
        while len(nums) > len(res):
            nums.pop(-1)
        return len(res)