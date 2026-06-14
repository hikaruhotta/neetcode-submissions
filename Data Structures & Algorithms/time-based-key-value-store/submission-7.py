class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        values = self.time_map[key]

        L, R = 0, len(values) - 1

        result_index = None

        while L <= R:
            M = L + (R - L) // 2
            if values[M][1] == timestamp:
                return values[M][0]
            
            elif values[M][1] < timestamp:
                if not result_index or M > result_index:
                    result_index = M
                L = M + 1
            else:
                R = M - 1
        
        if result_index is None:
            return ""
        
        return values[result_index][0]
        
