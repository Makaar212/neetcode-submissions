class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a graph is a valid tree if all the nodes are connnected and there is no cycles
        # since this is an undirected graph that means that we can travel both ways on the grap

        # we can check if there is a cycle using cyclic dfs 
        # we can also check if every node has been visited by using a set to keep track of all the nodes
        # that we visited
        # because it's an undirected graph, we should be able to get to every single node using js one 
        # node

        # to start this problem we first need to build the adjacency list

        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # now we have to check for cycles and visit all the nodes from 0
        # this can be done by using cyclic dfs, the only problem is that when we visit a node,
        # we would typically remove it from the visited list that way we can avoid getting false positive
        # what's another way we could detect self positives
        # (a false positive would be if we go back to 0 (sicne it's undirected) and the dfs would think
        # it's a cycle)
        # we can solve this by using a prev var
        # when we are iterating through the edges for each node, if it's the previous js skip it
        # we know that one is green
        # if we all good js return True
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)