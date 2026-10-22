class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj = defaultdict(list)
        minheap = []
        time = 0
        visit = set()
        for u, v, w in times:
            adj[u].append((w,v))

        minheap = [(0, k)]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            time = max(w1, time)
            visit.add(n1)
            for w2, n2 in adj[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minheap, (w2 + w1, n2))

        return time if len(visit) == n else -1