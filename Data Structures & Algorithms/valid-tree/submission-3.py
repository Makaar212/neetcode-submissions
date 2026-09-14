class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check for cycles and if we've visited every node

        # make adjacency map

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for p in adj[node]:
                if p == prev:
                    continue
                if not dfs(p, node):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n