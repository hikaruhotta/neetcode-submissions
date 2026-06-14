class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.partition_helper(s, [])
        return self.result

    def partition_helper(self, s, curr):
        if len(s) == 0:
            self.result.append(curr.copy())
            return

        for right in range(1, len(s) + 1):
            if self.is_palindrome(s[:right]):
                curr.append(s[:right])
                self.partition_helper(
                    s[right:], curr
                )
                curr.pop()
        return
    
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
