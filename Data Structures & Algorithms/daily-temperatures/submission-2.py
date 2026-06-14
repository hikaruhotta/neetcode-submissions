class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                (t, j) = stack.pop()
                result[j] = i - j
            stack.append((temperatures[i], i))
        
        return result
