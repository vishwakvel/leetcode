class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsdict = {}

        for s in strs:
            sorted_s = tuple(sorted(s)) # cant use list so use tuple

            if sorted_s not in strsdict: # default dict to set key value
                strsdict[sorted_s] = []

            strsdict[sorted_s].append(s) # key = sorted string value = s (from str)

        return list(strsdict.values())
