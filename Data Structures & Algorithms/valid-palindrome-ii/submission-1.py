class Solution:
    def validPalindrome(self, s: str) -> bool:
        num_delete = 0
        i, j = 0, len(s) - 1
        return self.helper(s, i, j, 0)
    
    def helper(self, s: str, i: int, j: int, num_delete: int) -> bool:
        if num_delete >= 2:
            return False
        
        if j <= i:
            return True
        
        if s[i] == s[j]:
            return self.helper(s, i + 1, j - 1, num_delete)

        candidates = []
        if s[i] == s[j - 1]:
            candidates.append(self.helper(s, i, j - 1, num_delete + 1))
        
        if s[i + 1] == s[j]:
             candidates.append(self.helper(s, i + 1, j, num_delete + 1))
        
        return any(candidates)
                