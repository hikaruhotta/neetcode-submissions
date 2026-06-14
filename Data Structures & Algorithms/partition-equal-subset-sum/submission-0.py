class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.dfs(nums, 0, 0)

    def dfs(self, nums: List[int], a_total, b_total) -> bool:
        if len(nums) == 0:
            return a_total == b_total
        
        return self.dfs(nums[1:], a_total + nums[0], b_total) or self.dfs(nums[1:], a_total, b_total + nums[0])
