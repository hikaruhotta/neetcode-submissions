class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [None for _ in range(len(nums))]
        min_jumps[0] = 0

        for i in range(len(nums)):
            max_jump_length = nums[i]
            for j in range(1, max_jump_length + 1):
                landing_index = min(i + j, len(nums) - 1)
                if min_jumps[landing_index] is None:
                    min_jumps[landing_index] = min_jumps[i] + 1
                else:
                    min_jumps[landing_index] = min(min_jumps[landing_index], min_jumps[i] + 1)
        
        return min_jumps[-1]