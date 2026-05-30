class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Create defaultdict called freq that keeps track of each character's freq for each sliding window. So key is char and value is count
        2. Set left = 0, max_freq (which keeps track of freq of most shown up char in all windows we check), and longest (longest length of substring)
        3. Sliding window so move right until end. In the defaultdict, increase count (value) of current char (key) by 1. Then set max_freq as the max of the current max_freq and the the value of the current char in the default dict. Also set window size.
        4. Check if window size - max_freq is greater than k (aka if the number of changes needed to make this the longest repeated substring is greater than the number of replacements we have)
            a) If it is, then decrease the value of the left char by 1, increase left by 1 and also decrease size by 1 (since you are shrinking the window by 1 by moving left)
            b) If it isn't, then continue
        5. Set longest as the max of the current longest and the size of the window
        """
        left = 0
        max_freq = 0
        longest = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            size = right - left + 1

            while size - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                size -= 1
            
            longest = max(longest, size)
        
        return longest
