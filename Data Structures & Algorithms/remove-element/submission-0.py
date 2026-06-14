class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = -1

        for i in range(len(nums)):
            if nums[i] != val:
                j += 1
                nums[j] = nums[i]
        
        return j + 1

