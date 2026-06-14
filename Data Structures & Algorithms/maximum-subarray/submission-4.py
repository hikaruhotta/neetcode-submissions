class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [nums[0]]

        for i in range(1, len(nums)):
            res.append(max(nums[i] + res[-1], nums[i]))
        
        return max(res)