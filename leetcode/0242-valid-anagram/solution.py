class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if lengths are different then obviously false
            return False
        return sorted(s) == sorted(t) # if sorted lexicographically they should be the same if they are then true else false
