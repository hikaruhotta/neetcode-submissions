class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.results = []
        self.helper(s, [])
        return self.results
    
    def helper(self, s: str, seq: List[str]) -> None:
        if len(s) == 0:
            self.results.append(seq.copy())
            return

        for i in range(len(s)):
            sub_str = s[0 : i + 1]
            if self.isPalindrome(sub_str):
                seq.append(sub_str)
                self.helper(s[i + 1:], seq)
                seq.pop()
        

    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        return True