class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        maxfreq = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            maxfreq = max(maxfreq, freq[s[right]])

            while (right - left + 1 ) - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
