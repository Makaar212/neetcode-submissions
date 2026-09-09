class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        minHeap = [-cnt for cnt in counter.values()]

        heapq.heapify(minHeap)
        q = deque()
        time = 0 
        while minHeap or q:
            time += 1
            if minHeap:
                curr = heapq.heappop(minHeap) + 1
                if curr:
                    q.append([curr, n + time])
            if q and q[0][1] == time:
                heapq.heappush(minHeap, q.popleft()[0])
        return time