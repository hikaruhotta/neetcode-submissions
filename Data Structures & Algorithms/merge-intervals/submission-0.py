class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = []

        for interval in intervals:
            if stack:
                top_interval = stack[-1]
                if top_interval[1] >= interval[0]:
                    stack.pop()
                    merged_interval = [min(interval[0], top_interval[0]), max(interval[1], top_interval[1])]
                    stack.append(merged_interval)
                else:
                    stack.append(interval)
            else:
                stack.append(interval)
        
        return stack