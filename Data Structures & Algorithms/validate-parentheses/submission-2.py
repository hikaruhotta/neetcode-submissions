class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
           ')': "(",
           '}':'{',
           ']':'[' 
        }

        stack = []
        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
            else:
                open_ch = complement[ch]
                if len(stack) == 0 or stack[-1] != open_ch:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
        