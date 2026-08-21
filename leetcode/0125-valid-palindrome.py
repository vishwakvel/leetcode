class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. Empty string to store phrase. Then convert to lowercase and remove all non-alphanumeric chars
        2. Set left = 0 and right = end of string
        3. Keep checking if left and right are equal
            a) If they are, nothing happens
            b) If they aren't, then return False
        4. Increase left by 1 and decrease right by 1 every time
        """
        clean = ""

        for c in s.lower():
            if c.isalnum():
                clean += c

        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        
        return True
