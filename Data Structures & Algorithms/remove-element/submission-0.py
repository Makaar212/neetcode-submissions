class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         # If i'm understanding this problem correctly, 
         # Input is a list of integers and a val which is also an integer, 

         # output is supposed to be an integer? which is the amount of elements that are not equal to val
         # Then we're also supposed to remove all the occurrences in place 


         # so 3 tasks from what I'm seeing


         # First remove all occurrences of val
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
            else:                 
                k+= 1
        nums.sort()
        return k
        

         # Count all occurrences of non val items

         # edit the array in place to be sorted, this means that all of the numbers in the list that aren't 
         # val have to be in the front, the first k values must be 