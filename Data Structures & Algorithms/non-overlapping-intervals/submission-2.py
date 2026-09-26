class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Duplicated intervals may exist

        not sorted 
        == not overlapping 

        if len intervals is 1 or 0 just return that striaght up
        """

        if len(intervals) <=1:
            return 0
        

        res = []
        intervals.sort()
        res.append(intervals[0])
        for start, end in intervals:
            if start < res[-1][1]:
                if end > res[-1][1]:
                    continue
                else:
                    res[-1] = [start,end]
            else:
                res.append([start, end])
        print(res)
        print(intervals)
        return len(intervals) - len(res)
