class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastStart, lastEnd = res[-1]
            if start > lastEnd:
                res.append([start, end])
                continue
            res[-1][1] = max(end, lastEnd)
        return res