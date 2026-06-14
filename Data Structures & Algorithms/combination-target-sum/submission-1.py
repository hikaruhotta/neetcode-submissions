class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.dfs([], nums, target)
        return self.result
    
    def dfs(self, curr: List[int], nums: List[int], target: int) -> None:
        if target == 0:
            self.result.append(curr)
            return
        
        for i, num in enumerate(nums):
            if num <= target:
                self.dfs(curr + [num], nums[i:], target - num)
        
        

