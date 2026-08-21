class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        seen = [False] * 1440
        recent = None
        earliest = None
        ans = float("inf")

        for time in timePoints: # build seen array if dup then immediately return 0
            index = int(time[:2])*60 + int(time[3:])

            if seen[index]:
                return 0
            else:
                seen[index] = True
        
        for minute in range(1440): # for each min check if in seen
            if seen[minute]:
                if earliest is None: # set what earliest time is (used to do final check since time is circular)
                    earliest = minute
                
                if recent is not None: # some prev min exists find min with dist
                    ans = min(ans, minute - recent)
                
                recent = minute
        
        ans = min(ans, 1440 - recent + earliest)
        return ans
