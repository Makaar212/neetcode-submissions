class Solution:
    def mySqrt(self, x: int) -> int:
        l, r  = 0, x
        res = 0
        while l <= r :
            m = (l + r) // 2

            squared = m * m 

            if squared > x:
                r = m - 1
            elif squared < x:
                res = m
                l = m + 1
            else:
                return m
        return res