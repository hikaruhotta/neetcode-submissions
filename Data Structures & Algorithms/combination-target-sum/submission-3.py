class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = sorted(nums)
        self.result = []
        self.helper(0, [], target)
        return self.result

    def helper(self, index: int, seq: List[int], target: int) -> None:
        if target == 0:
            self.result.append(seq.copy())
        if index == len(self.nums):
            return
        
        for i in range(index, len(self.nums)):
            if self.nums[i] <= target:
                seq.append(self.nums[i])
                self.helper(i, seq, target - self.nums[i])
                seq.pop()
            else:
                break
