class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        
        left = [0] * len(height)
        right = [0] * len(height)

        biggestL = height[0]
        biggestR = height[-1]
        for i, value in enumerate(height):
            left[i] = biggestL
            biggestL = max(value, biggestL)
        
        for i in range(len(height) - 1,-1, -1):
            right[i] = biggestR
            biggestR = max(biggestR, height[i])

        
        totalArea = 0

        for i, value in enumerate(height):
            curr = min(right[i], left[i]) - value
            curr = max(curr, 0)

            totalArea += curr
            


        return totalArea

        
        