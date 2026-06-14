class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        result = max(self.maxSubarraySum(nums), sum(nums) - self.minSubarraySum(nums))
        if result > 0:
            return result
        return max(nums)

    def maxSubarraySum(self, nums: List[int]) -> int:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(max(nums[i] + res[-1], nums[i]))
        return max(res)

    def minSubarraySum(self, nums: List[int]) -> int:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(min(nums[i] + res[-1], nums[i]))
        return min(res)

            

