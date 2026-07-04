class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in reversed(range(m)):
            nums1[i + n] = nums1[i]
        for i in range(n):
            nums1[i] = 0
        i, j = n, 0
        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if i < len(nums1):
            while i < len(nums1):
                nums1[k] = nums1[i]
                k += 1
                i += 1
        elif j < len(nums2):
            while j < len(nums2):
                nums1[k] = nums2[j]
                k += 1
                j += 1
        
        

        