class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # for this one the actual letters dont matter. Why? because what we're returning has nothing to
        # do with the letters 

        # so what do we want to do,

        # first we want to count the number of occurrences for all of the letters. 
        count = Counter(tasks)

        # after we count the occurrences we can use a maxheap to get rid of the highest occuring
        # characters first. 

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)


        # once we've created the maxHeap we should also keep a queue to keep track of when the 
        # occurrences are allowed to be in maxHeap again, when they're allowed to be processed again

        q = deque()
        time = 0

        # now, while maxHeap or q since that means we have occurrences left.  
        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 