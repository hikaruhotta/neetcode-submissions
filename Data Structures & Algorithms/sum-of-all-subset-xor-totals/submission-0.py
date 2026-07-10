class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0
        self.nums = nums
        for i in range(len(self.nums)):
            self.helper(i, 0)
        return self.result
    
    def helper(self, index: int, prev_xor: int) -> None:
        if index == len(self.nums):
            return

        curr_xor = prev_xor ^ self.nums[index]
        self.result += curr_xor

        for i in range(index + 1, len(self.nums)):
            self.helper(i, curr_xor)


