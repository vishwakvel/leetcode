class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        parent = list(range(n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
                
            return parent[x]

        def union(a, b):
            parenta = find(a)
            parentb = find(b)

            if parenta != parentb:
                parent[parentb] = parenta

        indices = list(range(n))
        indices.sort(key=lambda i: nums[i])

        for i in range(1, n):
            a = indices[i - 1]
            b = indices[i]

            if nums[b] - nums[a] <= limit:
                union(a, b)

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        ans = list(nums)

        for indices in groups.values():
            chars = []

            for i in indices:
                chars.append(nums[i])

            chars.sort()
            indices.sort()

            for i, c in zip(indices, chars):
                ans[i] = c

        return ans