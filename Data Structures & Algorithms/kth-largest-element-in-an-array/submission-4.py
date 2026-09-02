class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Why is this being done. Because we want to know where the kth largest element is. In a 
        # sorted array that would mean len - k is the kth largest number in th array.
        # when using quick select we are sorting the array one at a time until the p pointer equals len -
        # k so then that's why it's more convenient to jus switch it out like so.
        k = len(nums) - k 
        
        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:   return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]
        return quickSelect(0, len(nums) - 1)