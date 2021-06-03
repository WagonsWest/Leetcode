class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        n = len(intervals)
        sorted_intervals = sorted(intervals, key = lambda x: x[1])
        no_overlap = 1

        end = sorted_intervals[0][-1]
        for i in range(n):
            # > start means there is overlap
            if end <= sorted_intervals[i][0]:
                no_overlap += 1
                end = sorted_intervals[i][-1]

        return n-no_overlap