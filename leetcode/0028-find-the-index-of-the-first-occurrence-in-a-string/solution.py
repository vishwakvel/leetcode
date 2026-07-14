class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)

        for i in range(len(haystack) - size + 1):
            if haystack[i:i + size] == needle:
                return i
        
        return -1
