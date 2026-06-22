class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        for j in range(len(intervals)):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            else:
                i += 1
                intervals[i] = intervals[j]
        return intervals[:i+1]