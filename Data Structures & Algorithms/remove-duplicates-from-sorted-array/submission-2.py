class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0

        for R in range(1, len(nums)):
            if nums[L] == nums[R]:
                continue
            else:
                L += 1
                nums[L] = nums[R]
        
        return L + 1
