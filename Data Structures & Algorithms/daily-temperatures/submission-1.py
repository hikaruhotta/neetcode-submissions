class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            if i == 0 or temperatures[i] <= temperatures[i - 1]:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    popped_temp, j = stack.pop()
                    result[j] = i - j
                stack.append((temperatures[i], i))
        
        return result
