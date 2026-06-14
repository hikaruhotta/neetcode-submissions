class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by asc start position
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars, key=lambda x: -x[0])

        # something about intersections and user a stack to represent that
        stack = [cars[0]]

        for i in range(1, len(cars)):
            front_car, back_car = stack[-1], cars[i]

            front_car_pos, front_car_speed = front_car
            back_car_pos, back_car_speed = back_car

            front_car_arrival = (target - front_car_pos) / front_car_speed
            back_car_arrival = (target - back_car_pos) / back_car_speed

            # no catch up
            if front_car_arrival < back_car_arrival:
                stack.append(back_car)
            else:
                # noop because we are constrained by the front car and the back car caught up to the front car and merged
                continue
                
        
        return len(stack)