class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(text, pattern):
            lps = [0] * len(pattern)
            prev = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[prev]:
                    prev += 1
                    lps[i] = prev
                    i += 1
                elif prev > 0:
                    prev = lps[prev - 1]
                else:
                    lps[i] = 0
                    i += 1
            
            result = []
            t = 0
            p = 0

            while t < len(text):
                if text[t] == pattern[p]:
                    t += 1
                    p += 1

                    if p == len(pattern):
                        result.append(t - p)
                        p = lps[p - 1]
                elif p > 0:
                    p = lps[p - 1]
                else:
                    t += 1
            
            return result
        
        aindices = kmp(s, a)
        bindices = kmp(s, b)
        b = 0
        ans = []

        for a in aindices:
            while b < len(bindices) and bindices[b] < a - k:
                b += 1
            
            if b < len(bindices) and bindices[b] <= a + k:
                ans.append(a)
        
        return ans
