class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force solution would be to sort the array and return the (len - k)th element 

        # Optimize by using quick select since we really only need to have one thing sorted
        # and know where that is

        # we could also use a min heap where the size of the minheap is len k


        # brute force:

        # nums.sort()
        # return nums[len(nums) - k]

        # min heap:

        # minHeap = []
        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     while len(minHeap) > k:
        #         heapq.heappop(minHeap)
        
        # return heapq.heappop(minHeap)


        # quick sort:
        # partition, pivot, p, 
        k = len(nums) - k
        def quickSelect(l, r):
            
            pivot, p = nums[r], l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        return quickSelect(0, len(nums) - 1)