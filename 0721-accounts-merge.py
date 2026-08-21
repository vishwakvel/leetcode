class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        names = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return
            
            if size[px] < size[py]:
                parent[px] = py
                size[py] += size[px]
            else:
                parent[py] = px
                size[px] += size[py]
        
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    size[email] = 1
                
                names[email] = name
            
            first = account[1]

            for email in account[2:]:
                union(first, email)
        
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)
        
        ans = []

        for root, emails in groups.items():
            emails.sort()
            ans.append([names[root]] + emails)
        
        return ans
