class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            should_append = True
            while stack and self.willCollide(stack[-1], a):
                if abs(stack[-1]) == abs(a):
                    should_append = False
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(a):
                    should_append = False
                    break
                else:
                    stack.pop()
            
            if should_append:
                stack.append(a)
            
        return stack

    def willCollide(self, asteroid1, asteroid2) -> bool:
        if asteroid1 == 0 or asteroid2 == 0:
            if asteroid1 == 0:
                return asteroid2 < 0
            else:
                return asteroid1 > 0
        
        return asteroid1 > 0 and asteroid2 < 0
