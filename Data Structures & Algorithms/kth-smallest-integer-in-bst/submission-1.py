# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # keep traveling to the left as much as you can, everytime you move to the left 

        # add node to the stack, if left is null pop stack and process node, go right then keep going left

        stack = []
        cur = root
        arr = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left 
            
            node = stack.pop()
            arr.append(node.val)
            cur = node.right
        
        return arr[k - 1]

        