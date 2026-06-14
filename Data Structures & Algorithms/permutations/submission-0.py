class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = set(nums)
        self.curr = []
        self.result = []
        self.dfs()
        return self.result
    
    def dfs(self):
        if len(self.nums) == 0:
            self.result.append(self.curr.copy())
            return
        
        for num in self.nums.copy():
            self.curr.append(num)
            self.nums.remove(num)
            self.dfs()
            self.nums.add(num)
            self.curr.pop()
        
