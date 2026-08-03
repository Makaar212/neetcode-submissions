# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # What is going on here

        # so basically we are creating a dummy node to avoid weird edge cases. 

        # garunteed none empty lists so that's fine

        # First we want to create a carry variable in case there is a carryover from the previous operation. 

        # then we want to grab the values IF THEY EXIST, so use ternarys

        # then if they exist we create the value to add to our new list.

        # edge case covered where the value is greater than 10 

        # Carry // 10 js so we don't hav eto do a conditional. 
        
        # create the next node

        # move everythign if they exist.

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10 
            val %= 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


        