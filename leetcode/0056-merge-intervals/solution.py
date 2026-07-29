class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            pstart, pend = ans[-1]

            if start <= pend:
                ans[-1] = [pstart, max(pend, end)]
            else:
                ans.append([start, end])
        
        return ans
