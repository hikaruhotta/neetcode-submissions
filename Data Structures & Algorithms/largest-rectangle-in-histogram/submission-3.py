class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, j = stack.pop()
                result = max(result, h * (i - j))
                start = j
            stack.append((height, start))
        
        while stack:
            h, i = stack.pop()
            result = max(result, h * (len(heights) - i))
        
        return result
