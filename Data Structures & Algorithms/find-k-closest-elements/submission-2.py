import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_index = 0
        L, R = 0, len(arr) - 1
        while L <= R:
            M = L + (R - L) // 2
            if abs(arr[M] - x) < abs(arr[closest_index] - x):
                closest_index = M
            if arr[M] < x:
                L = M + 1
            else:
                R = M - 1
        
        L, R = closest_index, closest_index
        while R - L + 1 < k:
            left, right = None, None
            if L - 1 >= 0:
                left = arr[L - 1]
            if R + 1 < len(arr):
                right = arr[R + 1]
            
            if left is None or right is None:
                if left:
                    L -= 1
                elif right:
                    R += 1
                else:
                    break
            else:
                if abs(x - left) <= abs(x - right):
                    L -= 1
                else:
                    R += 1

        return arr[L : R + 1]
        