class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0 
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cur = heapq.heappop(maxHeap) + 1
                if cur:
                    q.append([cur, time + n])
            
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time