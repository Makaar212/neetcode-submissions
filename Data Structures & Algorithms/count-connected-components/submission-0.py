class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        
        visit = set()
        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node)
            for j in adj[node]:
                dfs(j)
        
        res = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        
        return res

                            