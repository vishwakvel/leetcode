class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        tmap = defaultdict(int)
        formed = 0
        
        if n > m:
            return ""

        for char in t:
            tmap[char] += 1
        
        left = 0
        smap = defaultdict(int)
        ans = (float("inf"), None, None)

        for right in range(m):
            char = s[right]
            smap[char] += 1

            if char in tmap and tmap[char] == smap[char]: # counts match
                formed += 1
            
            while left <= right and formed == len(tmap): # as long as its valid
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                smap[char] -= 1

                if char in tmap and smap[char] < tmap[char]: # if it became invalid
                    formed -= 1 # reduces once then stops since while loop stops
                
                left += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
