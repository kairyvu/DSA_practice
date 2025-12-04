class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            lastStart, lastEnd = res[-1]
            if start > lastEnd:
                res.append([start, end])
                continue
            res[-1][1] = max(end, lastEnd)
        return res