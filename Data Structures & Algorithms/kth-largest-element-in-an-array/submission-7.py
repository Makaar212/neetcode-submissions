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

        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)