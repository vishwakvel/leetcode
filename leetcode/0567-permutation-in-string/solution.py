class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        counter_s1 = Counter(s1)
        left = 0

        for right in range(len(s2) - size + 1):
            window_counter = Counter(s2[right:right+size])
            
            if counter_s1 == window_counter:
                return True
        
        return False
