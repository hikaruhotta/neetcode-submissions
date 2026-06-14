class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(0, [], nums)
        return self.result

    def helper(self, index: int, seq: list[int], nums: list[int], ) -> None:
        if index == len(nums) + 1:
            return
        
        self.result.append(seq.copy())

        for i in range(index, len(nums)):
            seq.append(nums[i])
            self.helper(i + 1, seq, nums)
            seq.pop()
