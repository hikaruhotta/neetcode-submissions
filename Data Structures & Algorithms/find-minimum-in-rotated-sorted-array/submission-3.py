class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = 0

        while left <= right:
            if nums[left] < nums[right]:
                return min(nums[result], nums[left])

            mid = left + (right - left) // 2
            if nums[mid] < nums[result]:
                result = mid
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return nums[result]