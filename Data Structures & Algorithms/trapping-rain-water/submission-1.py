class Solution:
    def trap(self, height: List[int]) -> int:
        # for each index we wangt to find the tallest bar to the right and left and take the min of those to get the water

        max_to_left = 0
        prefix = []
        for i in range(len(height)):
            max_to_left = max(max_to_left, height[i])
            prefix.append(max_to_left)
        
        max_to_right = 0
        suffix = []
        for i in reversed(range(len(height))):
            max_to_right = max(max_to_right, height[i])
            suffix.append(max_to_right)
        suffix = suffix[::-1]

        area = 0
        for i in range(len(height)):
            water_height = min(prefix[i], suffix[i])
            area += water_height - height[i]

        return area