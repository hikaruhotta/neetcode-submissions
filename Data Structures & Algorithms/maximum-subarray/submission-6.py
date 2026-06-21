class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            result = max(result, curr_sum)
            curr_sum = max(curr_sum, 0)
        return result