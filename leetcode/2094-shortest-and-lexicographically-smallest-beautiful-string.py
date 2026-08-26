class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] == "1":
                count += 1

            while count > k:
                if s[left] == "1":
                    count -= 1
                left += 1

            if count == k:
                while s[left] == "0":
                    left += 1

                curr = s[left:right + 1]

                if not ans or len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans):
                    ans = min(ans, curr)

        return ans