"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if the input size is 1 or 0 we can return True
        # no == is not an overlap
        # it's given in any order so we will need to sort first
        # strictly less than not equal to

        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda i: i.start)
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < prevEnd:
                return False
            else:
                prevEnd = end
        return True


        """ 

        intervals =  5,8 9,15 1,2 3,5
        1,2 3,5 5,8 9,15

        preEnd = 15
        start = 9 
        end = 15
        

        """