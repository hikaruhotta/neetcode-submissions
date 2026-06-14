class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        self.nums = nums
        self.cache = {}
        return self.dfs(0, 0, 0)[0]

    def dfs(self, index, seq_len, seq_max) -> tuple:
        if index == len(self.nums):
            return (seq_len, seq_max)

        if (index, seq_len, seq_max) in self.cache:
            return self.cache[(index, seq_len, seq_max)]

        candidates = []

        # start new sequence from index
        candidates.append(self.dfs(index + 1, 1, self.nums[index]))

        # skip index and continue current sequence
        candidates.append(self.dfs(index + 1, seq_len, seq_max))

        # include index in current sequence (if possible)
        if self.nums[index] > seq_max:
            candidates.append(self.dfs(index + 1, seq_len + 1, self.nums[index]))

        sorted_candidates = sorted(candidates, key=lambda x: (-x[0], x[1]))

        result = sorted_candidates[0]

        self.cache[(index, seq_len, seq_max)] = result

        return result










            

            


