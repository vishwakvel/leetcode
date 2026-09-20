class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        ans = 0

        for i, char in enumerate(s):
            ans += (alphabet.index(char) + 1) * (i + 1)

        return ans