class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        # create the minheap

        # check len of minheap if < 2 return minheap
        while len(minHeap) > 1:

        # pop first two things, make positive
            first = -heapq.heappop(minHeap)
            second = -heapq.heappop(minHeap)
        # if equal don't do anything
            if first != second:
                heapq.heappush(minHeap, -(first - second))

        # else  push difference 
        return -minHeap[0] if minHeap else  0

        
            

        