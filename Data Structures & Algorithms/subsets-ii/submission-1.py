class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(0, sorted(nums), [])
        return self.res
    
    def helper(self, index: int, nums: List[int], currSet: List[int]):
        if index >= len(nums):
            self.res.append(currSet.copy())
            return
        
        # include index
        currSet.append(nums[index])
        self.helper(index + 1, nums, currSet)
        currSet.pop()

        # dont include index
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.helper(index + 1, nums, currSet)
