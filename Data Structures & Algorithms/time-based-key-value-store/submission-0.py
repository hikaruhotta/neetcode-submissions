class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache or not self.cache[key]:
            return ""
        
        values = self.cache[key]
        left, right = 0, len(values) - 1

        most_recent = None

        while left <= right:
            mid = left + (right - left) // 2
            prev_value, prev_timestamp = values[mid]

            if prev_timestamp > timestamp:
                right = mid - 1
            else:
                if most_recent is None or prev_timestamp > most_recent[1]:
                    most_recent = (prev_value, prev_timestamp)
                left = mid + 1
        
        prev_value, prev_timestamp = values[right]
        if most_recent:
            if most_recent[1] > prev_timestamp:
                prev_value, prev_timestamp = most_recent
        return prev_value if prev_timestamp <= timestamp else ""
        
        

        
