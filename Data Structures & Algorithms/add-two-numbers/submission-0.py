# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # add all lists to an array
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        # iterate through both lists
        # create numbers add together
        number1 = ""
        number2 = ""
        for num in reversed(num1):
            number1 += str(num)
        for num in reversed(num2):
            number2 += str(num)
        result = int(number2) + int(number1)
        
        dummy = current =  ListNode(0, None)
        for c in reversed(str(result)):
            current.next = ListNode(int(c), None)
            current = current.next
        
        return dummy.next


        # go through the number backwards
        
        