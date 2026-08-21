class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. Convert s and t into counters which is O(n) complexity
        2. Return true if they're equal and false if they're not
        """
        from collections import Counter
        
        return Counter(s) == Counter(t)
