# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()

        # the right side view of a tree is alwasy going to be the last node in a 
        # bfs algorithim. 

        # so what you need to do is go through a tree level by level, print out the last node
        # or add it to the result list

        q.append(root)
        res = []


        while q:
            recent = None
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    recent = node

            
            
            if recent:
                res.append(recent.val)
    
        return res
        