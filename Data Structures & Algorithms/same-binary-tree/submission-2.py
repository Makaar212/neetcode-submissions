# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # couple approaches that we could do here, first is dfs where for every node in each we would check equality and return True, IF ANYTHING ISN"T THE SAME everythign should be false

        # BFS where we would just run through both at the same time, 

        # dfs could be done recursively and iteratively. for this problem i'll do it recursively. 

        # if q left sub tree = p sub tree return true, if q right sub tree = p right sub tree return true

        # btoh branches should be explored at the same time 

        # if not P and q return true
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

        # if not p or q return false because if both of them aren't null and one of them is, it's not equal

        # if p.val != q.val return true

        # return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        