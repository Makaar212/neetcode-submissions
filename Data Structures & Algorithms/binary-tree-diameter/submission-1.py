# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # init a constant res to track the diameter of left + right subtrees

        # for this node, get height left height right add them togehter
        
        # then see max(res, left + right)

        # after that you want to return the height of this node up to the next one

        res = 0 

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res
            
        