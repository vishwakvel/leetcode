from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        vals = sorted(count.keys())
        damage = {}

        def dfs(index):
            if index >= len(vals):
                return 0
            
            if index in damage:
                return damage[index]

            damage[index] = max(dfs(index + 1), vals[index] * count[vals[index]] + dfs(bisect.bisect_left(vals, vals[index] + 3)))

            return damage[index]

        return dfs(0)
