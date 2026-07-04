class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr) - 1

        closest_index = 0
        while L <= R:
            M = L + (R - L) // 2
            if abs(arr[M] - x) < abs(arr[closest_index] - x):
                closest_index = M
            if arr[M] <= x:
                L = M + 1
            else:
                R = M - 1

        i, j = closest_index, closest_index

        while j - i + 1 < k:
            if i == 0 and j == len(arr) - 1:
                break
            elif i == 0:
                j += 1
            elif j == len(arr) - 1:
                i -= 1
            else:
                if abs(arr[i - 1] - x) <= abs(arr[j + 1] - x):
                    i -= 1
                else:
                    j += 1
            
        return arr[i : j + 1]