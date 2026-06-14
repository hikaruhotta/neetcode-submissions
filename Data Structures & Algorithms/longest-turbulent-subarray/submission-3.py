class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, max_len, sign = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and sign != ">":
                max_len = max(max_len, r - l + 1)
                sign = ">"
                r += 1
            elif arr[r - 1] > arr[r] and sign != "<":
                max_len = max(max_len, r - l + 1)
                sign = "<"
                r += 1
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                sign = ""
        
        return max_len









            

            
            
            

