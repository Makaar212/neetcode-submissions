class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        
        for u,v,w in times:
            adj[u].append((w,v))
        visit = set()
        minheap = [(0,k)]
        t = 0 

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for w2, n2 in adj[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minheap, (w2 + w1, n2))
        return t if len(visit) == n else -1