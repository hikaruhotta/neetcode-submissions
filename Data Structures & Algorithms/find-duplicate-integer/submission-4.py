class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        intersect = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                intersect = slow
                break
        
        slow = 0
        while True:
            slow = nums[slow]
            intersect = nums[intersect]
            if slow == intersect:
                return slow
        
        return -1
        