class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = self.insertNewIntervalIndex(intervals, newInterval)
        intervals = intervals[:insert_index] + [newInterval] + intervals[insert_index:]
        return self.mergeIntervals(intervals)

    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            
            top_interval = stack[-1]
            if top_interval[1] >= interval[0]:
                stack.pop()
                merged_interval = [min(top_interval[0], interval[0]), max(top_interval[1], interval[1])]
                stack.append(merged_interval)
            else:
                stack.append(interval)
        
        return stack

            


        

    def insertNewIntervalIndex(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, len(intervals) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] == newInterval[0]:
                return mid
            elif intervals[mid][0] > newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

    

