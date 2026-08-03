# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         # Since this is just like adding back in elementary school, that's how we will handle
         # the problem


         # PSUEDOCODE

         # From left to right add both values together
        prev = False
        dummy = current = ListNode(0)
        while l1 and l2:
         # if greater than 10, Node( sum % 10), if prev + 1
            current.next = ListNode((l1.val + l2.val) % 10) if not prev else ListNode((l1.val + l2.val + 1) % 10)
            prev = l1.val + l2.val >= 10
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        restOf = l1 or l2

        while restOf:
            current.next = ListNode((restOf.val + 1)  % 10 ) if prev else ListNode(restOf.val % 10) 
            prev = restOf.val + 1 >= 10
            restOf = restOf.next
            current = current.next
        
        if prev:
            current.next = ListNode(1)
        return dummy.next
        


            


         # return head of new list
        