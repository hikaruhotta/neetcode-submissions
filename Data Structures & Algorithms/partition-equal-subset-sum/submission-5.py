class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        final_target = sum(nums) // 2

        dp = [False] * (final_target + 1)

        i = 0
        for target in range(1, final_target + 1):
            if nums[i] == target:
                dp[target] = True
        
        for i in range(1, len(nums)):
            next_dp = [False] * (final_target + 1)
            for target in range(1, final_target + 1):
                skip = dp[target]

                include = False
                if nums[i] <= target:
                    include = dp[target - nums[i]]
                
                next_dp[target] = skip or include

            dp = next_dp
        
        return dp[-1]