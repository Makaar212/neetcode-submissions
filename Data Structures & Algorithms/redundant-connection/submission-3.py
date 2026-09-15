class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Iterate through the edges, 
        # the dfs should return true, every time it returns true res should be updated
        # this is similar to finding out if a graph is a tree 

        # idea 1:
            # for every edge, remove it
            # then check if the graph is a tree
            # if it is, return the edge and move on to the next node

        # how to check if a graph is a valid tree
        # 2 things. 1: completely connected, 2: no cycles
        # how can we do that? by using cyclical dfs using a prev var and a set to see what we've visited
        # we need an adj list

        n = len(edges)
        adj = {i:set() for i in range(1,n + 1)}

        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)

        visit = set()

        def isTree(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for j in adj[node]:
                if j == prev:
                    continue
                if not isTree(j, node):
                    return False
            return True
        
        # now that we have defined the isTree function that works in dfs, we continue with the algorithim

        # for every edge
        res = []

        for i in range(len(edges)):
            n1, n2 = edges[i]
            
            # remove it from edge list
            adj[n1].remove(n2)
            adj[n2].remove(n1)
            
            # if isTree(1):
            visit = set()
            if isTree(1, 0) and len(visit) == n:
                # res = [edge]
                res = [n1,n2]
            # add edge back, 
            adj[n1].add(n2)
            adj[n2].add(n1)
                # make sure that we've marked that we've seen this already
        return res
            
            