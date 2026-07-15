class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for start, end in intervals[1:]:
            prev = ans[-1]

            if start <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                ans.append([start, end])
        
        return ans
