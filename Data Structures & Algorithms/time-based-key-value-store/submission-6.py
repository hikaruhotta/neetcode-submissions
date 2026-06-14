class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key]

        L, R = 0, len(values) - 1
        result = ""

        while L <= R:
            M = L + (R - L) // 2
            if values[M][0] <= timestamp:
                result = values[M][1]
                L = M + 1
            else:
                R = M - 1
        
        return result
        
