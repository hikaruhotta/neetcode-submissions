class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_dp = [1]
        max_dp = [1]

        for i, num in enumerate(nums):
            candidates = [num, min_dp[-1] * num, max_dp[-1] * num]
            min_dp.append(min(candidates))
            max_dp.append(max(candidates))

        print(min_dp)
        print(max_dp)
        
        return max(max_dp[1:] + min_dp[1:])
        