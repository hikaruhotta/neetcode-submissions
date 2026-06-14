class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')

        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                min_len = min(R - L + 1, min_len)
                curr_sum -= nums[L]
                L += 1
                
        
        if min_len == float('inf'):
            return 0
        
        return min_len