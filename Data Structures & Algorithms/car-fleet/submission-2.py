class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [(start position, arrival time)]
        arr = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        arr = sorted(arr, key=lambda x: -x[0])

        stack = []

        for pos, end_time in arr:
            stack.append(end_time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)
            
                    
