# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        # What's going on here?

        # First we are trying to create a distance between the two points of exactly n distance
        # Why? because when r is at the end of the list that means the distance between
        # the end of the list and l is exactly n nodes. This is useful because that's how we can determine
        # what node to remove.

        # however if we want to remove that node we would need the node before to point to the next node
        # so create a dummy node first that points to the head.
        # then move r n spaces away from the front, then move both
        # remove then send back dummy node.
        
        