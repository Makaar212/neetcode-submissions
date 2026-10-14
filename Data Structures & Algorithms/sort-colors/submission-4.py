class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # so we are given a list of ints, each of which being 0s 1s or 2s

        # the task that we are given is ot basically sort it. this is just a sorting funciton
        # however there is something that is very interesting about this problem that allows for O(n) 
        # solution, it's the fact that we are guaranteed 012s only. 

        # so there's an approach that I'm thinkign about which is a counting approach where we just count instances of each thing then replace for that many of that intance

        # What would another approach


        freq = Counter(nums)
        j = 0
        for i in range(3):
            if i in freq:
                while freq[i] != 0:
                    nums[j] = i
                    j += 1
                    freq[i] -= 1
        