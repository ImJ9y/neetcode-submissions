"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time = sorted(interval.start for interval in intervals)
        end_time = sorted(interval.end for interval in intervals)

        room = 0
        end_idx = 0
        for start in start_time:
            if start < end_time[end_idx]:
                room += 1
            else:
                end_idx += 1
            
        return room