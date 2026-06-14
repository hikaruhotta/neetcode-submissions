class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []

        for i, num in enumerate(nums):
            candidates = []
            
            candidates.append(num)
            if i - 1 >= 0:
                candidates.append(dp[i - 1])
            if i - 2 >= 0:
                candidates.append(dp[i - 2] + num)

            dp.append(max(candidates))
        
        return max(dp)
