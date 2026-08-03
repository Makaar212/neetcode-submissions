# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Since this is a binary search tree then there is the useful property of smaller > node > 
        # greater

        # with this property we can create an alogrithim that would allow us to check if both nodes are less than the current one
        # if both nodes are greater than the current one, go right

        # if nodes are split, and this node is the split point then this is the LCA

        if not root:
            return 
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    
        