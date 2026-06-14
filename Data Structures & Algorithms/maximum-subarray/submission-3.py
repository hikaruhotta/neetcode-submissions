class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = []

        for num in nums:
            other = max_sub[-1] if max_sub else 0
            max_sub.append(max(num, num + other))
        
        result = max(max_sub)

        return result
