class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        i = 0

        while i < len(s):
            if i == len(s)-1:
                ans += symbols[s[i]]
                break
            else:
                curr = symbols[s[i]]
                nxt = symbols[s[i+1]]

                if nxt > curr:
                    ans += (nxt - curr)
                    i += 2
                else:
                    ans += (curr)
                    i += 1
        
        return ans
