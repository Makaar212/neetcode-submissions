class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        biggest = 0

        # [7, 1, 7, 2, 2, 4]
        # stack 

        # Itereate through the array
        for i in range(len(heights)):

            # if i < stack[-1]:
            if stack and stack[-1][0] > heights[i]:
                while stack and stack[-1][0] > heights[i]:
                
                    # pop stack[-1] and calculate height ((len - index)  * height) 
                    iHeight, ind = stack.pop()
                    biggest = max(((i - ind) * iHeight), biggest)
                    # append new value with old index
                stack.append([heights[i], ind])
            # else append stack
            else:
                stack.append([heights[i], i])
        # iterate through stack, calc height, return max Rectangle ((len - index)  * height) 
        while stack:
            iHeight, ind = stack.pop()
            biggest = max((len(heights) - ind) * iHeight, biggest)
        return biggest