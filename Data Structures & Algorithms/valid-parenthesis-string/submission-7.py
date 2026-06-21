class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                open_stack.append((ch, i))
            elif ch == '*':
                star_stack.append((ch, i))
            elif ch == ')':
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        print(open_stack, star_stack)
        while open_stack:
            if star_stack and star_stack[-1][1] > open_stack[-1][1]:
                star_stack.pop()
                open_stack.pop()
            else:
                return False
        
        return True
        