class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        self.nums = nums
        self.cache = {}
        return self.dfs(0, sum(nums) // 2)

    def dfs(self, index, target) -> bool:
        if index == len(self.nums):
            return target == 0
        
        if (index, target) in self.cache:
            return self.cache[(index, target)]
        
        result = self.dfs(index + 1, target - self.nums[index]) or self.dfs(index + 1, target)
        self.cache[(index, target)] = result
        return result

