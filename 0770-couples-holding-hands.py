class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {}

        for i, person in enumerate(row):
            pos[person] = i
        
        swaps = 0

        for i in range(0, len(row), 2):
            partner = row[i] ^ 1

            if row[i+1] != partner:
                swaps += 1

                index = pos[partner]
                row[i+1], row[index] = row[index], row[i+1]

                pos[row[index]] = index
                pos[row[i+1]] = i+1
        
        return swaps
