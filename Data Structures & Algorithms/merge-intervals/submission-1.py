class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """

        Hey thank you so much for having me, do you mind giving me a second to read and 

        array of size 1 or 0 return it back straight up

        array not sorted, == counts as overlapping 

        1 3, 8 10, 1 5, 6 7
        """
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals.sort()

        res.append(intervals[0])

        for i in range(len(intervals)):
            start = intervals[i][0]
            lastIndex = res[-1][1]

            if start <= lastIndex:
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res