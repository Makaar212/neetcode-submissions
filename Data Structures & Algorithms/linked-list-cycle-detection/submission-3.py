# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        # Implement floyd's fast and slow

        # start with fast already set two ahead and curr in base, if from before
        # to prevent curr.next.next throwing error. 
        s = head
        f = head.next.next
        # while s
        # if s == f
        # return true
        # if f == None
        #return false

        while s:
            if s == f:
                return True
            if not f or not f.next:
                return False
            f = f.next.next
            s = s.next
        



        