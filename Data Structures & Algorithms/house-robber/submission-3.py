class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            candidates = []
            candidates.append(dp[i - 2])
            if i >= 3:
                candidates.append(dp[i - 3])
            dp[i] = max(candidates) + nums[i]
        
        return max(dp)
