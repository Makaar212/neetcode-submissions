class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((w,v))


        minheap = [(0,k)]

        visit = set()
        t = 0
        while minheap:
            currWeight, curr = heapq.heappop(minheap)
            if curr in visit:
                continue
            visit.add(curr)
            t = currWeight
            for neiWeight, nei in adj[curr]:
                if nei in visit:
                    continue
                heapq.heappush(minheap, (neiWeight + currWeight, nei))
        return t if len(visit) == n else -1
        
