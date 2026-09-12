"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # for dfs how would we do this

        # use hashmaps for copies 
        # for every node create a copy then go to neighbors
        # dfs would return a copy 
        if not node: return None
        otn = {} # old to new
        def dfs(node):
            if node in otn:
                return otn[node]
            
            copy = Node(node.val)
            otn[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
