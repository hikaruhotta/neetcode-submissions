class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        self.nums = nums
        return self.dfs(0, target)

    def dfs(self, index: int, target: int) -> int:
        if index == len(self.nums):
            if target == 0:
                return 1
            else:
                return 0

        if (index, target) in self.cache:
            return self.cache[(index, target)]

        
        neg = self.dfs(index + 1, target - self.nums[index])
        pos = self.dfs(index + 1, target + self.nums[index])

        self.cache[(index, target)] = neg + pos

        return neg + pos
        

