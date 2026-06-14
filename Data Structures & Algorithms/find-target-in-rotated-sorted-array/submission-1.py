class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        min_index = 0

        while left <= right:
            # window is sorted
            if nums[left] < nums[right]:
                if nums[left] < nums[min_index]:
                    min_index = left
                break
            

            mid = left + (right - left) // 2
            if nums[mid] < nums[min_index]:
                min_index = mid

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        if target >= nums[min_index] and target <= nums[-1]:
            # search right side of min index
            left, right = min_index, len(nums) - 1
        else:
            # search side of min_index
            left, right = 0, min_index - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        

        return -1
    



