class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap = []

        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((w,v))
        


        minheap.append((0,k))
        total = 0
        visit = set()
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            total = max(total, w1)
            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w2 + w1, n2))
        return total if len(visit) == n else -1 
