class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i - 1])

        suffix = [1]

        for i in reversed(range(len(nums) - 1)):
            suffix.append(suffix[-1] * nums[i + 1])
        
        suffix = suffix[::-1]

        result = []

        for i in range(len(prefix)):
            result.append(prefix[i] * suffix[i])
        
        return result
    