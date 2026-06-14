from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        queue = deque()
        queue.append(("(", 1, 0))

        while queue:
            s, num_open, num_close = queue.popleft()
            if num_open > n or num_close > n or num_close > num_open:
                continue
            
            if num_open == n and num_close == n:
                results.append(s)
            else:
                queue.append((s + "(", num_open + 1, num_close))
                queue.append((s + ")", num_open, num_close + 1))
        
        return results


