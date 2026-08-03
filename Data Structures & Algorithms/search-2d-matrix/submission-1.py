class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return self.binarySearch( matrix[m], target)
            elif target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
        return False

        

    def binarySearch(self, nums: list[int], target: int):
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r ) // 2 
            if target < nums[m]:
                r = m - 1 
            elif target > nums[m]:
                l = m + 1 
            elif target == nums[m]:
                return True
        return False
         
        