class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        complement = {
            ')' : '(', '}' : '{', ']' : '['
        }

        for ch in s:
            if ch not in ['(', ')', '{', '}', '[', ']']:
                continue
            
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif ch in [')', '}', ']']:
                if not stack or stack[-1] != complement[ch]:
                    return False
                else:
                    stack.pop()
        
        return not stack

            
