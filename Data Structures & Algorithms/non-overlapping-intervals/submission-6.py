class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res