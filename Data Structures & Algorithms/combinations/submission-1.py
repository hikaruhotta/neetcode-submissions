class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        for i in range(1, n + 1):
            self.helper([i], n, k)
        return self.result
    
    def helper(self, path: List[int], n: int, k: int) -> None:
        if len(path) == k:
            self.result.append(path.copy())
            return
        
        for j in range(path[-1] + 1, n + 1):
            path = path + [j]
            self.helper(path, n, k)
            path.pop()
        
    