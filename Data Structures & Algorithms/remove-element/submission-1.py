class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_length = len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        return j