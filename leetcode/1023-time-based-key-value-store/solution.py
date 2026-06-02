class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        left = 0
        right = len(values) - 1
        prev = None

        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                prev = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if prev is None:
            return ""
        else:
            return values[prev][1]
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
