class CountSquares:

    def __init__(self):
        self.x_points = {}
        self.y_points = {}
        self.counts = {}
        

    def add(self, point: List[int]) -> None:
        if point[0] not in self.x_points:
            self.x_points[point[0]] = []
        if point[1] not in self.y_points:
            self.y_points[point[1]] = []

        self.x_points[point[0]].append((point[0], point[1]))
        self.y_points[point[1]].append((point[0], point[1]))
        if (point[0], point[1]) not in self.counts:
            self.counts[(point[0], point[1])] = 0
        self.counts[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        result = 0

        x_0, y_0 = point[0], point[1]

        x_matches = self.x_points[x_0] if x_0 in self.x_points else []

        for (x_1, y_1) in x_matches:
            side_len = abs(y_1 - y_0)
            if side_len == 0:
                continue
            
            # plus
            x_2, y_2 = x_0 + side_len, y_0
            x_3, y_3 = x_2, y_1
            if (x_2, y_2) in self.counts and (x_3, y_3) in self.counts:
                result += self.counts[(x_2, y_2)] * self.counts[(x_3, y_3)]

            # minus
            x_2, y_2 = x_0 - side_len, y_0
            x_3, y_3 = x_2, y_1
            if (x_2, y_2) in self.counts and (x_3, y_3) in self.counts:
                result += self.counts[(x_2, y_2)] * self.counts[(x_3, y_3)]

        return result




        
