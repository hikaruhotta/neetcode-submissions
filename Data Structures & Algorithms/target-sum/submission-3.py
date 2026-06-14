class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        self.nums = nums
        return self.helper(0, target)
    
    def helper(self, index: int, target: int) -> int:
        if index == len(self.nums):
            if target == 0:
                return 1
            else:
                return 0

        if (index, target) in self.cache:
            return self.cache[(index, target)]


        subtract = self.helper(index + 1, target + self.nums[index])

        add = self.helper(index + 1, target - self.nums[index])

        self.cache[(index, target)] = subtract + add

        return subtract + add