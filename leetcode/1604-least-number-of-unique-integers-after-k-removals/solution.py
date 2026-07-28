from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        
        freqs = sorted(count.values())
        
        uniq = len(freqs)

        for freq in freqs:
            if k >= freq:
                k -= freq
                uniq -= 1
            else:
                break
        
        return uniq
