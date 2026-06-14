class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        res = [False] * len(nums)
        res[0] = True
        for i, num in enumerate(nums):
            if not res[i]:
                continue
            for j in range(num + 1):
                if i + j < len(nums):
                    res[i + j] = True
        
        return res[-1]
