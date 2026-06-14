class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper([], nums)
        return self.result
    
    def helper(self, curr: List[int], nums: List[int]) -> None:
        self.result.append(curr)

        for i, num in enumerate(nums):
            self.helper(curr + [num], nums[i + 1:])
        




