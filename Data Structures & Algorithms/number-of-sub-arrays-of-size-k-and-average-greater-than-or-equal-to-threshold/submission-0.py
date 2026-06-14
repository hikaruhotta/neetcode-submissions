class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = k * threshold
        res = 0

        curr_sum = 0

        L = 0

        for R in range(len(arr)):
            curr_sum += arr[R]
            if R - L >= k:
                curr_sum -= arr[L]
                L += 1
            if R - L + 1 == k and curr_sum >= threshold:
                res += 1
        
        return res
