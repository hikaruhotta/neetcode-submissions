class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.helper(1, n, k, [])
        return self.combinations
    
    def helper(self, i: int, n: int, k: int, currComb: List[int]):
        if len(currComb) == k:
            self.combinations.append(currComb.copy())
            return
        elif i > n:
            return
        
        for j in range(i, n + 1):
            currComb.append(j)
            self.helper(j + 1, n, k, currComb)
            currComb.pop()
        
