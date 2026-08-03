# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Here is the bfs solution

        # we can keep a queue for both q and p and do this iteratively
        first = deque()
        second = deque()

        # add roots to stacks, (2 stacks)
        first.append(p)
        second.append(q)
        # while loop, for every iteration pop from both stacks
        while first and second:
            f, s = first.popleft(), second.popleft()
        # null check btoh, value check btoh, add children
            if not f and not s:
                continue
            if not f or not s:
                return False
            if f.val != s.val:
                return False

            first.append(f.left)
            second.append(s.left)
            first.append(f.right)
            second.append(s.right)
        # if while condition fails, check if either tree list is still having nodes, then return true
        if first or second:
            return False
        else:
            return True