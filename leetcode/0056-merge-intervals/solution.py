class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # my logic is comparing 2 intervals if start1 < end2 and start2 < end1 then they overlap. sort list first since we want to keep track of earliest first
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            prevstart, prevend = ans[-1]
            currstart, currend = intervals[i]

            if currstart <= prevend and prevstart <= currend:
                ans[-1] = [prevstart, max(prevend, currend)]
            else:
                ans.append([currstart, currend])
        
        return ans
