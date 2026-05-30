class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. Create counter for t to keep track of chars as well as how many of each appear. Also create an empty counter to fill with the window's chars. Formed var is to keep track of how many chars have been fully taken care of.
        2. For each right char, add to window Counter
        3. Check if that char is in need Counter and if need and window values for that char are equal (aka if count for both chars are the same)
            a) If true, then increase formed by 1 since that means 1 more char has been fully taken care of
            b) If not, continue
        4. Then, we need to greedily shorten a valid substring we find and see if we can find a smaller one. For this, we use a while loop and check if the length of this substring is smaller than the global min.
            a) If it is, then replace the min_len and ans with the current ones we just found
            b) If not, continue
        5. Then we prepare to move to the left, so first we remove the char from the window (just 1 of it not the whole char)
        6. Check if left char is in need Counter and if the window's value of left char is less than need's value of left char
            a) If it is, then decrease formed by 1
            b) If it isn't, continue
        7. Finally increase left by 1 so move window to the right
        """
        
        need = Counter(t)
        window = Counter()
        formed = 0
        left = 0
        min_len = float("inf")
        ans = ""

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1
            
            while formed == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                
                left += 1
        
        return ans
