class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums is unique
        self.nums = sorted(nums)
        self.cache = {}
        return self.helper(target)
    
    def helper(self, target) -> int:
        if target == 0:
            return 1

        if target in self.cache:
            return self.cache[target]
        
        result = 0
        for num in self.nums:
            if num <= target:
                result += self.helper(target - num)
        
        self.cache[target] = result
        return result
        
