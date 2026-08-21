class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        half = ""
        mid = ""
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in freq:
                if freq[char] % 2 == 1:
                    mid = char
                    freq[char] -= 1

                for i in range(freq[char]//2):
                    half += char
        
        return half + mid + half[::-1]
