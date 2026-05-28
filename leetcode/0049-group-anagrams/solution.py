class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Create a defaultdict with empty list set as the base value
        2. Go through each element in strs and sort the str alphabetically
            a) Keys are the sorted string and values are the anagrams in the strs list
        3. Add str to dict using sorted str as the key and appending the str to the respective value
        4. Return list of dict.values() (convert to list because .values() is a diff view type)
        """
        ans = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            ans[sorted_s].append(s)
        
        return list(ans.values())
