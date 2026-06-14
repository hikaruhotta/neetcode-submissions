class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.cache = {}
        return self.dfs(0, 0, 0)

    def dfs(self, index, a_total, b_total) -> bool:
        if index == len(self.nums):
            return a_total == b_total
        
        if (index, a_total, b_total) in self.cache:
            return self.cache[(index, a_total, b_total)]
        
        result = self.dfs(index + 1, a_total + self.nums[index], b_total) or self.dfs(index + 1, a_total, b_total + self.nums[index])
        self.cache[index, a_total, b_total] = result
        return result
