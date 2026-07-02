class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        curr = 0
        result = float('inf')
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target:
                result = min(result, j - i + 1)
                curr -= nums[i]
                i += 1
            
        if result == float('inf'):
            return 0
        
        return result
            
            