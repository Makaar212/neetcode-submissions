class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = (len(nums) - 1) // 2
        l, r = 0, len(nums)- 1

        while l <= r:
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                mid = (r + l) // 2
            elif nums[mid] > target:
                r = mid - 1
                mid = (r + l) // 2
        return -1
        
        