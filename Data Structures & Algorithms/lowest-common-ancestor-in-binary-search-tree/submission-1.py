# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # a node is an ancestor if it has btoh p and q as it's descendants
        queue = deque()
        queue.append(root)
        res = root

        # meaning that for every node we can check if it's an ancesetor, if it is, update result
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if self.isAncestor(node, p, q) >= 2:
                res = node
            queue.append(node.left)
            queue.append(node.right)
        
        return res


    def isAncestor(self, node, p, q):
        queue = deque()
        queue.append(node)
        found = 0

        while queue:
            node = queue.popleft()
            if not node:
                continue
            if node.val == p.val or node.val == q.val:
                found += 1
            queue.append(node.left)
            queue.append(node.right)
        return found
        
        
        # since we will be using bfs to traverse the tree, then there is no need to do a min/max type
        # check

