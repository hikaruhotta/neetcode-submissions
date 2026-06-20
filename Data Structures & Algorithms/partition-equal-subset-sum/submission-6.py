class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        self.cache = {}
        return self.helper(nums, 0, sum(nums) // 2)

    
    def helper(self, nums: List[int], index: int, target: int) -> bool:
        if index == len(nums):
            return target == 0

        if (index, target) in self.cache:
            return self.cache[(index, target)]
        
        include = self.helper(nums, index + 1, target - nums[index])
        skip = self.helper(nums, index + 1, target)

        result = include or skip
        self.cache[(index, target)] = result

        return include or skip


