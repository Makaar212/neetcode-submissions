class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        longest = 0
        current = 0
        l = 0 
        r = len(heights) - 1

        while l < r:
            current = (r - l) * min(heights[l], heights[r])
            longest = max(longest, current)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1


        return longest 
        