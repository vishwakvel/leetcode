class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. Create empty chars set which holds all chars we've looked at. Reference to check if current char we're looking at is repeated or not.
        2. Set left = 0 and use a for loop to move right from start to end
        3. First check if right char is in chars (aka if its repeated)
            a) If it is, then remove it from chars and move left by 1
            b) If it isn't, then continue
        4. Add right char to chars set and set longest as max of current length of substring and previous max
        """
        chars = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            longest = max(longest, right - left + 1)

        return longest
