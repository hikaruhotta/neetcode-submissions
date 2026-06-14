class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob 0 house, cannot rob n - 1
        dp1 = [0]
        # do not rob 0 house, can rob n - 1
        dp2 = [0]
        for i, num in enumerate(nums):
            if i == 0:
                dp1.append(num)
                dp2.append(0)
            elif i == len(nums) - 1:
                dp1.append(dp1[-1])
                dp2.append(max(dp2[-1], dp2[-2] + num))
            else:
                dp1.append(max(dp1[-1], dp1[-2] + num))
                dp2.append(max(dp2[-1], dp2[-2] + num))
        
        return max(dp1 + dp2)
