class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        
        
        left = self.sortArray(nums[:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2:])

        merged = []
        L, R = 0, 0
        while L < len(left) and R < len(right):
            if left[L] < right[R]:
                merged.append(left[L])
                L += 1
            else:
                merged.append(right[R])
                R += 1
        if L < len(left):
            merged += left[L:]
        elif R < len(right):
            merged += right[R:]
        
        return merged