"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pairs = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            pairs[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            pairs[curr].next = pairs[curr.next]
            pairs[curr].random = pairs[curr.random]
            curr = curr.next
        
        return pairs[head]
        
        


        