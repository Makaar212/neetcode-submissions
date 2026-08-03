# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # global res value
        res = 0


        # for every node check diameter byh adding left child height right child height
        def dfs(root):
            if not root:
                return 0
            nonlocal res


            left = dfs(root.left)
            right = dfs(root.right)

            res = max(left + right, res)

        # update res
            return 1 + max(left, right)
        dfs(root)

        return res

        # return height of value
        