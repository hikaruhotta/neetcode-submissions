class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)

        self.results = []
        self.curr = []

        self.dfs(0)

        return self.results

    def dfs(self, index):
        self.results.append(self.curr.copy())

        if index >= len(self.nums):
            return

        
        for i in range(index, len(self.nums)):
            if i == index or (self.nums[i] != self.nums[i - 1]):
                self.curr.append(self.nums[i])
                self.dfs(i + 1)
                self.curr.pop()
