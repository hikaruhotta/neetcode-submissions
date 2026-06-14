class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        L, R = 0, len(nums) - 1

        while L <= R:
            if nums[L] <= nums[R]:
                result = min(result, nums[L])
                break

            M = L + (R - L) // 2
            result = min(result, nums[M])
            if nums[L] <= nums[M]:
                L = M + 1
            else:
                R = M - 1
        
        return result