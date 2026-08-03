# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle fast slow tech
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the middle, leaving both ends pointing at None
        second = slow.next
        # then reverse second half
        prev = slow.next = None  # split the two linkedlists

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev

        while second:
            ftmp = first.next
            first.next = second
            first = ftmp

            stmp = second.next 
            second.next = first
            second = stmp


        # then merge
        