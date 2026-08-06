# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # For this problem i'm thinking we would do some dfs just to go down each branch

        # for each branch you would keep track of the largest at that point, 

        # if anything is larger, update largest

        # base case should probably if not node return 0

        # we should pass down a largest number as a parameter for the dfs as well

        if not root:
            return 0
        res = 0

        def dfs(root, largest):
            if not root:
                return 0
            if root.val >= largest:
                
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, largest) + dfs(root.right, largest)
        res = dfs(root, -101)

        return res
            

        