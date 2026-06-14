class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            j = None
            while len(stack) > 0 and height < stack[-1][0]:
                h, j = stack.pop()

                max_area = max(h * (i - j), max_area)

            stack.append((height, j if j is not None else i))

        i = len(heights)

        while stack:
            h, j = stack.pop()
            max_area = max(h * (i - j), max_area)

        return max_area
