"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # for bfs it's similar to dfs, first we need a q holding the ifrst node

        # then for every node in q, check if neighbor copy node has been created, if not create it
        # then connect them

        if not node: return None

        q = deque()
        q.append(node)
        otn = {} # old to new hashmap
        otn[node] = Node(node.val)
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in otn:
                    otn[nei] = Node(nei.val)
                    q.append(nei)
                otn[n].neighbors.append(otn[nei])
                
        return otn[node]

        