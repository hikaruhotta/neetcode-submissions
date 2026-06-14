class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float('inf')] * len(nums)
        res[0] = 0

        for i, num in enumerate(nums):
            if res[i] == float('inf'):
                continue
            
            for j in range(num + 1):
                if i + j < len(nums):
                    res[i + j] = min(res[i + j], res[i] + 1)
        
        return res[-1]