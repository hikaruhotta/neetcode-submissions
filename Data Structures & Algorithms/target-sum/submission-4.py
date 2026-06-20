class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.cache = {}
        return self.helper(0, target)
    
    def helper(self, index: int, target: int) -> int:
        if index == len(self.nums):
            return 1 if target == 0 else 0

        if (index, target) in self.cache:
            return self.cache[(index, target)]
        
        add = self.helper(index + 1, target - self.nums[index])
        subtract = self.helper(index + 1, target + self.nums[index])

        result = add + subtract
        self.cache[(index, target)] = result

        return result