class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(a, b):
            parenta = find(a)
            parentb = find(b)

            if parenta != parentb:
                parent[parentb] = parenta
        
        for a, b in pairs:
            union(a, b)
        
        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        ans = list(s)

        for indices in groups.values():
            chars = []

            for i in indices:
                chars.append(s[i])

            chars.sort()
            indices.sort()

            for i, c in zip(indices, chars):
                ans[i] = c

        return "".join(ans)
