class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()
        ans = []

        for i in range(len(s) - 9):
            dna = s[i:i+10]

            if dna in seen:
                ans.append(dna)
            else:
                seen.add(dna)

        return list(set(ans))
