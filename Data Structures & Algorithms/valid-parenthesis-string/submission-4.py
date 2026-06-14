class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                elif left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            left_i = left.pop()
            star_i = star.pop()

            if left_i >= star_i:
                return False
        
        return not left
