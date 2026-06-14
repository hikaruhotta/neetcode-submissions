class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]

        for i in range(1, len(height)):
            max_left.append(max(max_left[-1], height[i - 1]))

        max_right = [0]
        for i in reversed(range(len(height) - 1)):
            max_right.append(max(max_right[-1], height[i + 1]))
        max_right = max_right[::-1]
        
        result = 0
        for i in range(len(height)):
            lower = min(max_left[i], max_right[i])
            if lower > height[i]:
                result += lower - height[i]

        return result

