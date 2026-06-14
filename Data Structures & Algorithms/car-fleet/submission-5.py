class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: -x[0])

        stack = [cars[0]]

        for i in range(1, len(cars)):
            front_pos, front_speed = stack[-1]
            curr_pos, curr_speed = cars[i]

            front_arrival = float(target - front_pos) / front_speed
            curr_arrival = float(target - curr_pos) / curr_speed

            if curr_arrival > front_arrival:
                stack.append(cars[i])

        return len(stack)
        
