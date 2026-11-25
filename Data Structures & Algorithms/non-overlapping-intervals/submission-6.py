class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1.  2
        #.    2.    4
        #.1.        4

        res = []
        intervals.sort()
        # 1 100
        # 1 11
        # 2 12
        # 11 22

        count = 0
        for start, end in intervals:
            if not res or res[-1][1] <= start:
                res.append([start, end])
            else:
                res[-1][1] = min(res[-1][1], end)
                count += 1
        
        return count
