class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper([], set(nums))
        return self.result

    def helper(self, seq: List[int], nums: Set):
        if len(nums) == 0:
            self.result.append(seq.copy())
            return
        
        for num in nums.copy():
            seq.append(num)
            nums.remove(num)
            self.helper(seq, nums)
            nums.add(num)
            seq.pop()