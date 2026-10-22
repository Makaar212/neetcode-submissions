class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Input is a list of integers
        # output is the first smallest int that is not in the array

        # We can be given negatives in our list
        # What if list is empty? 
        # what if list has one element. 

        # we clearly want something that is as close to one as possible. 

        # O(n) time and space solution is to turn the nums into a set and starting from 1 we count up 
        # until we reach soemthing that is not in the list

        # the next solution is if the array is sorted, we keep going until we reach the next empty spot

        # Something to be cautious of is the fact that 234567 should return 1

        # let's start with the set solution and see if we can improve from there


        seen = set(nums)
        res = 1
        while res in seen:
            res += 1
        return res