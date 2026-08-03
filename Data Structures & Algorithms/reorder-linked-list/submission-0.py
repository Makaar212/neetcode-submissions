# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        curr = head
        array = []
        while curr:
            array.append(curr)
            curr = curr.next
        

        l, r = 0, len(array) - 1
        while l < r:
            array[l].next = array[r]
            l += 1
            if l >= r:
                break

            array[r].next = array[l]
            r -= 1
        
        array[l].next = None
        



        

        