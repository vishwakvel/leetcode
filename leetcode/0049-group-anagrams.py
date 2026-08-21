class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            hashmap[sorted_s].append(s)
        
        return list(hashmap.values())
