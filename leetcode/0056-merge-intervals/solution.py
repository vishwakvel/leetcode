class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for start2, end2 in intervals[1:]:
            start1, end1 = ans[-1]

            if start2 <= end1 and start1 <= end2:
                ans[-1] = [start1, max(end1, end2)]
            else:
                ans.append([start2, end2])
        
        return ans
