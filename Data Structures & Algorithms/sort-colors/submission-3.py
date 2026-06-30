class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, M, R = 0, 0, len(nums) - 1

        while L <= R and M <= R:
            if nums[M] == 0:
                nums[M], nums[L] = nums[L], nums[M]
                L += 1
                M += 1
            elif nums[M] == 1:
                M += 1
            elif nums[M] == 2:
                nums[M], nums[R] = nums[R], nums[M]
                R -= 1
