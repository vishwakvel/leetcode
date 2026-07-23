import bisect

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) # key to value, time

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        array = self.hashmap[key]
        left = 0
        right = len(array) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if array[mid][1] <= timestamp:
                ans = array[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
