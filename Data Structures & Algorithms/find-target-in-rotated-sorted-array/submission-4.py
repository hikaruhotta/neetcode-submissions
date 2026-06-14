class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        min_index = 0

        while L <= R:
            if nums[L] <= nums[R]:
                if nums[L] < nums[min_index]:
                    min_index = L
                break
            
            M = L + (R - L) // 2
            if nums[M] < nums[min_index]:
                min_index = M
            
            if nums[L] <= nums[M]:
                L = M + 1
            else:
                R = M - 1

        L, R = 0, len(nums) - 1

        while L <= R:
            M = L + (R - L) // 2

            M_ord = (M + min_index) % len(nums)

            if nums[M_ord] == target:
                return M_ord
            
            elif nums[M_ord] > target:
                R = M - 1
            else:
                L = M + 1
        
        return -1
        
        