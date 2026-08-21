class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]: # oldend < newstart
                ans.append(interval)
            elif interval[0] > newInterval[1]: # oldstart > newend
                ans.append(newInterval)
                return ans + intervals[index:]
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        ans.append(newInterval)
        return ans
