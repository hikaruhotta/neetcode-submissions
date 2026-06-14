class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        stack = []

        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0] > heights[i]:
                h, index = stack.pop()
                result = max(result, (i - index) * h)
            stack.append((heights[i], index))
        
        while stack:
            h, j = stack.pop()
            result = max(result, (len(heights) - j) * h)
        
        return result
