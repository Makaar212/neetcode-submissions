class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i, value in enumerate(nums):
            if value in mySet: 
                return True

        
            mySet.add(value)

        return False
        