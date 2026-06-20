class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        dp0 = [0] * len(nums)
        dp0[0], dp0[1] = nums[0], 0

        dp1 = [0] * len(nums)
        dp1[0], dp1[1] = 0, nums[1]

        for i in range(2, len(nums)):
            candidates0 = [0]
            candidates1 = [0]

            if i != len(nums) - 1:
                candidates0.append(dp0[i - 2] + nums[i])
                if i >= 3:
                    candidates0.append(dp0[i - 3] + nums[i])

            if i != len(nums) - 2:
                candidates1.append(dp1[i - 2] + nums[i])
                if i >= 3:
                    candidates1.append(dp1[i - 3] + nums[i])

            dp0[i] = max(candidates0)
            dp1[i] = max(candidates1)
        
        return max(dp0 + dp1)
