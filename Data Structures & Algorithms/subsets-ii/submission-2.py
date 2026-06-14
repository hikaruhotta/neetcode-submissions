class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.result = []
        self.helper(0, [])
        return self.result
    
    def helper(self, index: int, seq: List[int]) -> None:
        self.result.append(seq.copy())

        if index == len(self.nums):
            return
        
        for i in range(index, len(self.nums)):
            if i > index and self.nums[i] == self.nums[i - 1]:
                continue
            
            seq.append(self.nums[i])
            self.helper(i + 1, seq)
            seq.pop()
