class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for i in range(len(nums))]

        can_reach[0] = True

        for i in range(len(nums)):
            if can_reach[i]:
                for j in range(nums[i]):
                    if i + j + 1 < len(can_reach):
                        can_reach[i + j + 1] = True
        return can_reach[-1]
