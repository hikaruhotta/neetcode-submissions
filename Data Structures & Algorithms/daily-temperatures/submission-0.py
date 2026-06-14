class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temperature, i))
                continue
            
            while len(stack) > 0 and temperature > stack[-1][0]:
                top_temp, top_i = stack.pop()
                result[top_i] = i - top_i

            stack.append((temperature, i))

        return result
            
                