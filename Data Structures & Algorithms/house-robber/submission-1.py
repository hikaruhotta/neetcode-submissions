class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []

        for i, num in enumerate(nums):
            candidates = []
            
            candidates.append(num)
            if i - 2 >= 0:
                candidates.append(dp[i - 2] + num)
            if i - 3 >= 0:
                candidates.append(dp[i - 3] + num)

            dp.append(max(candidates))
        
        return max(dp)
