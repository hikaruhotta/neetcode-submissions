class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
            
        L, R = 0, len(nums) - 1
        result = 0
        while L <= R:
            M = L + (R - L) // 2
            if nums[M] >= target:
                result = M
                R = M - 1
            else:
                L = M + 1
        return result
            

            