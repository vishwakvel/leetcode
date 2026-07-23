class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aindices = []
        bindices = []

        for i in range(len(s)):
            if s[i: i+len(a)] == a:
                aindices.append(i)
            
            if s[i: i+len(b)] == b:
                bindices.append(i)
        
        ans = []
        j = 0

        for i in aindices:
            while j < len(bindices) and bindices[j] < i - k:
                j += 1
            
            if j < len(bindices) and bindices[j] <= i + k:
                ans.append(i)
        
        return ans
