class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        best = r
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)
            if totalTime > h:
                l = k + 1
            elif totalTime <= h:
                best = k
                r = k - 1
        
        return best
        