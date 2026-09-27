class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u,v, w in times:
            adj[u].append((w,v))
        visit = set()
        time = 0
        minheap = [(0,k)]
        

        while minheap:
            curWeight, cur = heapq.heappop(minheap)
            if cur in visit:
                continue
            visit.add(cur)
            time = curWeight

            for neiWeight, nei in adj[cur]:
                if nei in visit:
                    continue
                heapq.heappush(minheap, (neiWeight + curWeight, nei))
        return time if len(visit) == n else -1