class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        L, R = 0, len(intervals) - 1
        while L <= R:
            M = L + (R - L) // 2
            if intervals[M][0] <= newInterval[0]:
                L = M + 1
            else:
                R = M - 1
        intervals.insert(L, newInterval)

        i = 0
        for j in range(len(intervals)):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            else:
                i += 1
                intervals[i] = intervals[j]

        return intervals[:i+1]