# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        rm = len(nodes) - n

        if rm == 0:
            return head.next
            
        
        nodes[rm - 1].next = nodes[rm - 1].next.next

        return head


        