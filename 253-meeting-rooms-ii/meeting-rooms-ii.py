from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(s for s, e in intervals)
        ends   = sorted(e for s, e in intervals)

        res, i = 0, 0
        for s in starts:
            if s >= ends[i]:
                i += 1
            else:
                res += 1

        return res