class CountSquares:

    def __init__(self):
        self.x_match = {}
        self.counts = {}


    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]

        if x not in self.x_match:
            self.x_match[x] = []
        self.x_match[x].append((x, y))

        if (x, y) not in self.counts:
            self.counts[(x, y)] = 0
        self.counts[(x, y)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]

        if x not in self.x_match:
            return 0
        res = 0
        for x_i, y_i in set(self.x_match[x]):
            point2 = (x_i, y_i)

            if x_i == x and y_i == y:
                continue

            side_length = abs(y - y_i)
            # neg
            point3 = (x - side_length, y)
            point4 = (x - side_length, y_i)

            if point2 in self.counts and point3 in self.counts and point4 in self.counts:
                res += self.counts[point2] * self.counts[point3] * self.counts[point4]


            # pos
            point3 = (x + side_length, y)
            point4 = (x + side_length, y_i)

            if point2 in self.counts and point3 in self.counts and point4 in self.counts:
                res += self.counts[point2] * self.counts[point3] * self.counts[point4]
            
        return res

        



        




        
