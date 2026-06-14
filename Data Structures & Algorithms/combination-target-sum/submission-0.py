class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.curr = []
        self.nums = nums
        self.result = []
        self.dfs(0, target)
        return self.result
        
    def dfs(self, i, target):
        if target == 0:
            self.result.append(self.curr.copy())
            return
        elif i >= len(self.nums):
            return
        
        for j in range(i, len(self.nums)):
            if self.nums[j] <= target:
                self.curr.append(self.nums[j])
                self.dfs(j, target - self.nums[j])
                self.curr.pop()
        

