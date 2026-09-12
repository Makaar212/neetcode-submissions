"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # for dfs we should create a hashmap
        # then for every node go to it's neighbor create a copy of it and append it to cur neighbor list
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
        