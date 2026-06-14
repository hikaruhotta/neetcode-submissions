class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        
        result = 0
        stack = []

        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            
            top_interval = stack[-1]
            if top_interval[1] > interval[0]:
                result += 1
                if top_interval[1] > interval[1]:
                    stack.pop()
                    stack.append(interval)
                else:
                    continue
            else:
                stack.append(interval)


        return result