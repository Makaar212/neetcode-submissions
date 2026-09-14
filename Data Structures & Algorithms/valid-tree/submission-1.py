class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # adjacency list:
        # 0 : [1,2,3]
        # 1: [0,4]
        # 2: [0]
        # 3: [0]
        # 4: [1]

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)