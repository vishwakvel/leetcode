class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]

        for i in range(n):
            ans = max(ans, expand(i, i), expand(i, i + 1), key=len)
        
        return ans
